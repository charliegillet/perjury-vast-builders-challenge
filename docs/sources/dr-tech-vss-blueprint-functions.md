

## FILE: vss-blueprint/source-code/ingest/vastdb-writer/main.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/vastdb-writer/main.py

```
from opentelemetry import trace
from vast_runtime.vast_event import VastEvent  # type: ignore

from common.models import Settings, EmbeddingEvent
from common.vastdb_client import VastDBClient
from common.handler_utils import parse_embedding_event, validate_embedding


def init(ctx):
    """Initialize the serverless function"""
    with ctx.tracer.start_as_current_span("VastDB Writer Initialization"):
        settings = Settings.from_ctx_secrets(ctx.secrets)
        ctx.vastdb_client = VastDBClient(settings)


def handler(ctx, event: VastEvent):
    """Main handler function for vast serverless runtime"""
    
    with ctx.tracer.start_as_current_span("VastDB Writer Handler") as handler_span:
        try:
            data = event.get_data()
            event_type = getattr(event, 'get_type', lambda: 'element_trigger')()
            handler_span.set_attribute("event_type", event_type)

            if data.get("status") == "error":
                ctx.logger.warning(f"[SKIP] upstream error: {data.get('error')}")
                return {"status": "skipped", "reason": data.get("error", "upstream error")}

            if data.get("status") == "skipped":
                ctx.logger.info(f"[SKIP] upstream skipped: {data.get('reason')}")
                return {"status": "skipped", "reason": data.get("reason", "upstream skipped")}
            
            with ctx.tracer.start_as_current_span("Embedding Event Parsing") as parse_span:
                embedding_event = parse_embedding_event(data)
                
                source = embedding_event.get("source", "")
                filename = embedding_event.get("filename", "")
                reasoning_content = embedding_event.get("reasoning_content", "")
                embedding = embedding_event.get("embedding", [])
                embedding_model = embedding_event.get("embedding_model", "")
                embedding_dimensions = embedding_event.get("embedding_dimensions", 0)
                status = embedding_event.get("status", "success")
                
                is_public = embedding_event.get("is_public")
                allowed_users = embedding_event.get("allowed_users")
                segment_number = embedding_event.get("segment_number")
                total_segments = embedding_event.get("total_segments")
                tags = embedding_event.get("tags", "")
                original_video = embedding_event.get("original_video", filename)
                
                camera_id = embedding_event.get("camera_id", "")
                capture_type = embedding_event.get("capture_type", "")
                location = embedding_event.get("location", "")
                
                allowed_users_count = len(allowed_users.split(",")) if allowed_users else 0
                
                ctx.logger.info(f"[INPUT] {filename} | segment {segment_number}/{total_segments} | {len(embedding)} dims | reasoning={len(reasoning_content)} chars")
                
                parse_span.set_attributes({
                    "source": source,
                    "filename": filename,
                    "embedding_model": embedding_model,
                    "embedding_dimensions": embedding_dimensions,
                    "status": status,
                    "reasoning_content_length": len(reasoning_content),
                    "is_public": str(is_public),
                    "allowed_users_count": allowed_users_count,
                    "segment_number": segment_number,
                    "total_segments": total_segments,
                    "tags": tags,
                    "original_video": original_video,
                    "camera_id": camera_id,
                    "capture_type": capture_type,
                    "location": location
                })

            with ctx.tracer.start_as_current_span("Embedding Validation") as validation_span:
                if not validate_embedding(embedding):
                    validation_span.set_attributes({"valid": False})
                    ctx.logger.info(f"[SKIP] {filename} | no valid embedding (dims={len(embedding) if embedding else 0})")
                    return {"status": "skipped", "reason": "No valid embedding"}
                
                validation_span.set_attributes({"valid": True})

            with ctx.tracer.start_as_current_span("VastDB Storage") as storage_span:
                table_full_name = f"{ctx.vastdb_client.bucket}.{ctx.vastdb_client.schema_name}.{ctx.vastdb_client.table_name}"
                ctx.logger.info(f"[VASTDB] Writing to {table_full_name}")
                
                store_result = ctx.vastdb_client.store_vector(embedding_event)
                success = store_result != "error"
                
                storage_span.set_attributes({
                    "storage_result": store_result,
                    "storage_success": success,
                    "filename": filename,
                    "vector_dimensions": len(embedding),
                    "table_name": table_full_name,
                    "segment_number": segment_number,
                    "total_segments": total_segments
                })
                
                if not success:
                    ctx.logger.error(f"[VASTDB] FAILED to store {filename} segment {segment_number}/{total_segments} | table={table_full_name}")

            result = {
                "source": source,
                "filename": filename,
                "embedding_dimensions": len(embedding),
                "embedding_model": embedding_model,
                "storage_result": store_result,
                "storage_success": success,
                "status": "error" if store_result == "error" else "success"
            }
            
            ctx.logger.info(f"[COMPLETE] {filename} | segment {segment_number}/{total_segments} → {table_full_name} | {store_result} | public={is_public} | camera={camera_id or 'none'}")
            return result
            
        except ValueError as e:
            msg = str(e)
            if msg.startswith("Upstream"):
                ctx.logger.warning(f"[SKIP] {msg}")
                return {"status": "skipped", "reason": msg}
            handler_span.set_attribute("error", True)
            handler_span.set_attribute("error.message", msg)
            ctx.logger.error(f"VastDB write failed: {msg}")
            return {"status": "error", "error": msg}
        except Exception as e:
            handler_span.set_attribute("error", True)
            handler_span.set_attribute("error.message", str(e))
            handler_span.record_exception(e)
            ctx.logger.error(f"VastDB write failed: {e}")
            return {"status": "error", "error": str(e)}


```


## FILE: vss-blueprint/source-code/ingest/vastdb-writer/common/vastdb_client.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/vastdb-writer/common/vastdb_client.py

```
import logging
import json
import vastdb
import pyarrow as pa
from typing import Dict, Any, Tuple
from datetime import datetime

from common import vastdb_patch  # noqa: F401 — apply SDK patch before select/insert
from common.segment_index import pk_for_source


def _resolve_segment_times(
    embedding_event: Dict[str, Any],
    segment_number: int,
    segment_duration: float,
) -> Tuple[float, float]:
    """Resolve timeline position in parent video from pipeline metadata or derive."""
    start_raw = embedding_event.get("segment_start_sec")
    end_raw = embedding_event.get("segment_end_sec")
    if start_raw is not None and end_raw is not None:
        try:
            return float(start_raw), float(end_raw)
        except (TypeError, ValueError):
            pass

    step = embedding_event.get("segment_step_sec")
    try:
        step_sec = float(step) if step is not None else 5.0
    except (TypeError, ValueError):
        step_sec = 5.0

    sn = segment_number if segment_number > 0 else 1
    start = (sn - 1) * step_sec
    end = start + segment_duration
    return start, end


class VastDBClient:
    """VastDB client for storing video reasoning vectors"""

    def __init__(self, settings):
        self.settings = settings
        self.table_name = settings.vdbcollection
        self.bucket = settings.vdbbucket
        self.schema_name = settings.vdbschema
        self.visual_dim = (
            settings.visual_embedding_dimensions
            if getattr(settings, "visual_embedding_dimensions", 0) > 0
            else settings.embeddingdimensions
        )

        self.schema_columns = pa.schema([
            ("pk", pa.utf8()),
            ("source", pa.utf8()),
            ("filename", pa.utf8()),
            ("segment_number", pa.uint32()),
            ("segment_start_sec", pa.float64()),
            ("segment_end_sec", pa.float64()),
            ("reasoning_content", pa.utf8()),
            ("perception_json", pa.string()),
            ("object_classes", pa.utf8()),
            ("object_counts", pa.utf8()),
            ("max_detection_conf", pa.float32()),
            ("perception_ok", pa.bool_()),
            ("perception_source", pa.utf8()),
            ("detection_sidecar_uri", pa.utf8()),
            ("detection_frame_count", pa.uint32()),
            ("detection_count", pa.uint32()),
            ("vectors", pa.list_(pa.field(name="item", type=pa.float32(), nullable=False), self.settings.embeddingdimensions)),
            ("vectors_visual", pa.list_(pa.field(name="item", type=pa.float32(), nullable=False), self.visual_dim)),
            ("cosmos_model", pa.utf8()),
            ("embedding_model", pa.utf8()),
            ("visual_embedding_model", pa.utf8()),
            ("tokens_used", pa.int32()),
            ("cached_prompt_tokens", pa.int32()),
            ("processing_time", pa.float64()),
            ("timestamp", pa.utf8()),
            ("allowed_users", pa.list_(pa.utf8())),
            ("is_public", pa.bool_()),
            ("upload_timestamp", pa.timestamp('ns')),
            ("duration", pa.float64()),
            ("total_segments", pa.uint32()),
            ("original_video", pa.utf8()),
            ("tags", pa.list_(pa.utf8())),
            ("camera_id", pa.utf8()),
            ("capture_type", pa.utf8()),
            ("location", pa.utf8()),
            ("extra_metadata", pa.string())
        ])

        self._initialize_connection()

    def _initialize_connection(self):
        endpoint = self.settings.vdbendpoint
        if not endpoint.startswith(("http://", "https://")):
            endpoint = f"http://{endpoint}"

        self.session = vastdb.connect(
            endpoint=endpoint,
            access=self.settings.vdbaccesskey,
            secret=self.settings.vdbsecretkey,
            ssl_verify=False,
        )

    def _prepare_table(self, tx):
        """Create schema/table inline in the current write transaction (no pre-check session)."""
        bucket = tx.bucket(self.bucket)
        schema = bucket.schema(self.schema_name, fail_if_missing=False)
        if schema is None:
            logging.info("[VASTDB] Creating schema %s", self.schema_name)
            schema = bucket.create_schema(self.schema_name, fail_if_exists=False)

        table = schema.table(self.table_name, fail_if_missing=False)
        if table is None:
            try:
                logging.info(
                    "[VASTDB] Creating table %s with %d columns",
                    self.table_name,
                    len(self.schema_columns),
                )
                schema.create_table(self.table_name, columns=self.schema_columns)
            except Exception as exc:
                if "409" not in str(exc) and "Conflict" not in str(exc) and "already exists" not in str(exc).lower():
                    raise
            table = schema.table(self.table_name, fail_if_missing=False)

        if table is None:
            raise vastdb.errors.MissingTable(self.bucket, self.schema_name, self.table_name)
        return table

    def store_vector(self, embedding_event: Dict[str, Any]) -> bool:
        """Store video reasoning with vector in VastDB. Skips duplicate source."""
        try:
            source = embedding_event.get("source", "")
            filename = embedding_event.get("filename", "")
            reasoning_content = (embedding_event.get("reasoning_content") or "").strip()
            embedding = embedding_event.get("embedding", [])
            visual_embedding = embedding_event.get("visual_embedding") or []
            visual_embedding_ok = bool(embedding_event.get("visual_embedding_ok", False))
            visual_embedding_model = embedding_event.get("visual_embedding_model", "") or ""

            if not reasoning_content:
                return True

            if not embedding:
                logging.warning("No embedding vector to store")
                return False

            pk = pk_for_source(source)
            timestamp = datetime.utcnow().isoformat() + "Z"

            is_public = embedding_event.get("is_public", True)
            allowed_users_str = embedding_event.get("allowed_users", "")
            tags_str = embedding_event.get("tags", "")
            original_video = embedding_event.get("original_video", filename)
            upload_timestamp_str = embedding_event.get("upload_timestamp", "")
            segment_duration_event = embedding_event.get("segment_duration", 5.0)
            segment_number_event = embedding_event.get("segment_number")
            total_segments_event = embedding_event.get("total_segments")

            camera_id = embedding_event.get("camera_id", "")
            capture_type = embedding_event.get("capture_type", "")
            location = embedding_event.get("location", "")

            allowed_users = [u.strip() for u in allowed_users_str.split(",") if u.strip()] if allowed_users_str else []
            tags = [t.strip() for t in tags_str.split(",") if t.strip()] if tags_str else []

            if segment_number_event is not None:
                segment_number = int(segment_number_event) if segment_number_event else 0
            else:
                segment_number = 0
                if "_segment_" in filename:
                    try:
                        parts = filename.split("_segment_")[1].split("_of_")
                        segment_number = int(parts[0])
                    except Exception:
                        pass

            if total_segments_event is not None:
                total_segments = int(total_segments_event) if total_segments_event else 1
            else:
                total_segments = 1
                if "_segment_" in filename and "_of_" in filename:
                    try:
                        parts = filename.split("_of_")[1].split(".")[0]
                        total_segments = int(parts)
                    except Exception:
                        pass

            segment_duration = float(segment_duration_event) if segment_duration_event else 5.0
            segment_start_sec, segment_end_sec = _resolve_segment_times(
                embedding_event, segment_number, segment_duration
            )

            if upload_timestamp_str:
                try:
                    upload_timestamp = datetime.fromisoformat(upload_timestamp_str.replace('Z', '+00:00'))
                except Exception:
                    upload_timestamp = datetime.utcnow()
            else:
                upload_timestamp = datetime.utcnow()

            if not visual_embedding or len(visual_embedding) != self.visual_dim:
                visual_embedding = [0.0] * self.visual_dim

            extra_metadata = {
                "status": embedding_event.get("status", "success"),
                "embedding_dimensions": embedding_event.get("embedding_dimensions", 0),
                "visual_embedding_dimensions": len(visual_embedding),
                "visual_embedding_ok": visual_embedding_ok,
            }
            stream_id = str(embedding_event.get("stream_id") or "").strip()
            if stream_id:
                extra_metadata["stream_id"] = stream_id
            if embedding_event.get("chunk_index") is not None:
                extra_metadata["chunk_index"] = embedding_event.get("chunk_index")
            chunk_start = embedding_event.get("chunk_start_sec")
            if chunk_start is not None:
                try:
                    chunk_start_f = float(chunk_start)
                    extra_metadata["chunk_start_sec"] = chunk_start_f
                    extra_metadata["stream_position_sec"] = round(chunk_start_f + float(segment_start_sec), 3)
                except (TypeError, ValueError):
                    pass
            ingest_kind = str(embedding_event.get("ingest_kind") or "").strip()
            if ingest_kind:
                extra_metadata["ingest_kind"] = ingest_kind

            record = {
                "pk": pk,
                "source": source,
                "filename": filename,
                "segment_number": segment_number,
                "segment_start_sec": segment_start_sec,
                "segment_end_sec": segment_end_sec,
                "reasoning_content": reasoning_content,
                "perception_json": embedding_event.get("perception_json", "") or "",
                "object_classes": embedding_event.get("object_classes", "") or "",
                "object_counts": embedding_event.get("object_counts", "{}") or "{}",
                "max_detection_conf": float(embedding_event.get("max_detection_conf") or 0.0),
                "perception_ok": bool(embedding_event.get("perception_ok", False)),
                "perception_source": embedding_event.get("perception_source", "") or "",
                "detection_sidecar_uri": embedding_event.get("detection_sidecar_uri", "") or "",
                "detection_frame_count": int(embedding_event.get("detection_frame_count") or 0),
                "detection_count": int(embedding_event.get("detection_count") or 0),
                "vectors": embedding,
                "vectors_visual": visual_embedding,
                "cosmos_model": embedding_event.get("cosmos_model", ""),
                "embedding_model": embedding_event.get("embedding_model", ""),
                "visual_embedding_model": visual_embedding_model,
                "tokens_used": embedding_event.get("tokens_used", 0),
                "cached_prompt_tokens": int(embedding_event.get("cached_prompt_tokens") or 0),
                "processing_time": embedding_event.get("processing_time", 0.0),
                "timestamp": timestamp,
                "allowed_users": allowed_users,
                "is_public": is_public,
                "upload_timestamp": upload_timestamp,
                "duration": segment_duration,
                "total_segments": total_segments,
                "original_video": original_video,
                "tags": tags,
                "camera_id": camera_id,
                "capture_type": capture_type,
                "location": location,
                "extra_metadata": json.dumps(extra_metadata, ensure_ascii=False),
            }

            arrow_table = pa.Table.from_pylist([record], schema=self.schema_columns)

            with self.session.transaction() as tx:
                table = self._prepare_table(tx)
                if self._skip_or_dedupe_existing_segment(table, source):
                    return True
                table.insert(arrow_table)

            return True

        except Exception as e:
            logging.error(f"Error storing vector: {e}")
            return False

    def _skip_or_dedupe_existing_segment(self, table, source: str) -> bool:
        """Return True when insert should be skipped. Runs inside the write transaction."""
        existing = table.select(
            predicate=(table["source"] == source),
            columns=["source"],
            internal_row_id=False,
        ).read_all()
        if existing.num_rows == 0:
            return False
        logging.info("[VASTDB] Skip duplicate index: %s", source)
        return True

    def close(self):
        if hasattr(self, 'session') and hasattr(self.session, 'close'):
            self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

```


## FILE: vss-blueprint/source-code/ingest/vastdb-writer/common/vastdb_patch.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/vastdb-writer/common/vastdb_patch.py

```
"""Monkey-patch VastDB SDK so predicate selects work on tables with vector columns."""
from __future__ import annotations

import logging

import pyarrow as pa
import vastdb._internal as _internal

logger = logging.getLogger(__name__)

_original_build_query_data_request = _internal.build_query_data_request


def _unsupported_vector_field(field: pa.Field) -> bool:
    field_type = str(field.type)
    if "fixed_size_list" in field_type:
        return True
    return "list<" in field_type and "float" in field_type


def _patched_build_query_data_request(schema, predicate, field_names):
    supported_fields = []
    unsupported = set()
    for field in schema:
        if _unsupported_vector_field(field):
            unsupported.add(field.name)
        else:
            supported_fields.append(field)
    if unsupported:
        logger.debug("[VastDB] Excluding unsupported columns from predicate query: %s", unsupported)
    filtered_names = [name for name in field_names if name not in unsupported]
    return _original_build_query_data_request(pa.schema(supported_fields), predicate, filtered_names)


_internal.build_query_data_request = _patched_build_query_data_request

```


## FILE: vss-blueprint/source-code/ingest/vastdb-writer/common/models.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/vastdb-writer/common/models.py

```
import os
import json
from typing import Any, Optional, Dict, List
from pydantic import BaseModel


class Settings(BaseModel):
    """Configuration settings for VastDB writer"""
    # VastDB settings
    vdbendpoint: str
    vdbbucket: str
    vdbschema: str
    vdbaccesskey: str
    vdbsecretkey: str
    vdbcollection: str
    
    # For schema definition
    embeddingdimensions: int
    embeddingmodel: str
    visual_embedding_dimensions: int = 0
    
    @classmethod
    def from_ctx_secrets(cls, secrets: Dict[str, str]) -> 'Settings':
        """Load settings from runtime context secrets (uses defaults for missing keys)."""
        raw = secrets["vss2-secret"]
        config = {field: raw[field] for field in cls.__annotations__.keys() if field in raw}
        return cls(**config)


class EmbeddingEvent(BaseModel):
    """Event data from reasoning-embedder"""
    source: str
    filename: str
    reasoning_content: str
    embedding: List[float]
    embedding_model: str
    embedding_dimensions: int
    visual_embedding: List[float] = []
    visual_embedding_model: str = ""
    visual_embedding_dimensions: int = 0
    visual_embedding_ok: bool = False
    cosmos_model: str
    tokens_used: int
    cached_prompt_tokens: int = 0
    processing_time: float
    status: str = "success"
    
    # Metadata fields (from pipeline)
    is_public: bool = True  # Default to public (CLI uploads)
    allowed_users: str | None = None  # Empty for CLI uploads
    tags: str | None = None
    upload_timestamp: str | None = None
    segment_number: int | None = None
    total_segments: int | None = None
    segment_duration: float | None = None
    segment_start_sec: float | None = None
    segment_end_sec: float | None = None
    original_video: str | None = None

    perception_json: str | None = None
    object_classes: str | None = None
    object_counts: str | None = None
    max_detection_conf: float | None = None
    perception_ok: bool = False

    # Stream capture metadata (from video-streaming service)
    camera_id: str | None = None
    capture_type: str | None = None
    location: str | None = None


```


## FILE: vss-blueprint/source-code/ingest/video-embedder/common/cosmos_embed_client.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/video-embedder/common/cosmos_embed_client.py

```
"""
NVIDIA Cosmos-Embed1 NIM client (/v1/embeddings).

API differs from OpenAI-style embed models:
  - request_type: query | bulk_text | bulk_video
  - model: nvidia/cosmos-embed1
  - output: 256-dim vectors (no dimensions parameter)
"""
import base64
import logging
from typing import List, Optional

import requests

COSMOS_EMBED1_MODEL = "nvidia/cosmos-embed1"

_CONN_EXC = (
    requests.exceptions.ConnectionError,
    requests.exceptions.Timeout,
    requests.exceptions.ChunkedEncodingError,
)
# 401/403 included: GPU/proxy auth blips and intermittent Forbidden must not soft-ack.
_TRANSIENT_STATUS = (401, 403, 408, 429, 500, 502, 503, 504)


class TransientError(Exception):
    """Retryable failure — hand the retry off to the VastPipeline."""


class CosmosEmbed1Client:
    def __init__(self, settings):
        self.model = getattr(settings, "embeddingmodel", COSMOS_EMBED1_MODEL) or COSMOS_EMBED1_MODEL
        if "cosmos-embed" not in self.model.lower():
            self.model = COSMOS_EMBED1_MODEL
        self.nvidia_api_key = getattr(settings, "nvidia_api_key", None) or ""
        self.embedding_authorization = getattr(settings, "embedding_authorization", "") or ""
        self.is_cloud = not getattr(settings, "embedding_local_nim", False)
        scheme = (getattr(settings, "embeddinghttpscheme", "http") or "http").rstrip(":/")
        host = (getattr(settings, "embeddinghost", "localhost") or "localhost").strip().strip("/")
        port = int(getattr(settings, "embeddingport", 8002) or 8002)
        default_port = 443 if scheme == "https" else 80
        if "/" in host:  # host carries a path prefix, e.g. gateway/tenant/model
            hostname, _, path = host.partition("/")
            netloc = hostname if port == default_port else f"{hostname}:{port}"
            self.base_url = f"{scheme}://{netloc}/{path}/v1"
        elif port == default_port:
            self.base_url = f"{scheme}://{host}/v1"
        else:
            self.base_url = f"{scheme}://{host}:{port}/v1"
        self.expected_dim = int(getattr(settings, "embeddingdimensions", 256) or 256)

    def _headers(self) -> dict:
        headers = {"Content-Type": "application/json"}
        token = (self.embedding_authorization or "").strip()
        if token:  # explicit token wins (works for local gateways too, not just cloud)
            headers["Authorization"] = token if token.lower().startswith("bearer ") else f"Bearer {token}"
        elif self.is_cloud and self.nvidia_api_key:
            headers["Authorization"] = f"Bearer {self.nvidia_api_key}"
        return headers

    def _post(self, payload: dict, timeout: int = 120) -> List[List[float]]:
        url = f"{self.base_url}/embeddings"
        # One in-process retry on connection errors; transient HTTP -> TransientError
        # so the handler raises and VastPipeline redelivers (no soft-ack).
        try:
            response = requests.post(url, json=payload, headers=self._headers(), timeout=timeout)
        except _CONN_EXC as exc:
            logging.warning("[RETRY] connection error to %s; retrying once: %s", url, exc)
            try:
                response = requests.post(url, json=payload, headers=self._headers(), timeout=timeout)
            except _CONN_EXC as exc2:
                raise TransientError(f"connection failed after 1 retry: {exc2}") from exc2
        if response.status_code in _TRANSIENT_STATUS:
            raise TransientError(f"transient HTTP {response.status_code}: {response.text[:300]}")
        if response.status_code == 200:
            items = response.json().get("data", [])
            vectors = [item.get("embedding", []) for item in items if item.get("embedding")]
            if not vectors:
                raise RuntimeError("Cosmos-Embed1 returned no embeddings")
            return vectors
        # Prefer redelivery over silent drop for unexpected HTTP errors.
        raise TransientError(f"Cosmos-Embed1 failed: {response.status_code}: {response.text[:500]}")

    def embed_texts(self, texts: List[str], *, for_query: bool = False) -> List[List[float]]:
        if not texts:
            return []
        if len(texts) == 1:
            for_query = True
        if for_query and len(texts) == 1:
            payload = {
                "input": texts[0],
                "model": self.model,
                "request_type": "query",
                "encoding_format": "float",
            }
        else:
            payload = {
                "input": texts,
                "model": self.model,
                "request_type": "bulk_text",
                "encoding_format": "float",
            }
        logging.info(
            f"[COSMOS_EMBED] Text embed | n={len(texts)} | "
            f"request_type={payload['request_type']}"
        )
        return self._post(payload)

    def embed_video_mp4(self, video_bytes: bytes) -> List[float]:
        """Embed a short segment MP4 (query mode, base64 video)."""
        if not video_bytes:
            raise ValueError("Empty video bytes")
        b64 = base64.b64encode(video_bytes).decode("ascii")
        payload = {
            "input": f"data:video/mp4;base64,{b64}",
            "model": self.model,
            "request_type": "query",
            "encoding_format": "float",
        }
        logging.info(f"[COSMOS_EMBED] Video embed | {len(video_bytes)} bytes")
        vectors = self._post(payload, timeout=180)
        return vectors[0]

    def embed_query_text(self, text: str) -> List[float]:
        return self.embed_texts([text], for_query=True)[0]

```


## FILE: vss-blueprint/source-code/ingest/video-reasoner/common/clients.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/video-reasoner/common/clients.py

```
import logging
import time
import base64
from typing import Dict, Any, Optional
import requests
import boto3
from opentelemetry import trace

from .prompts import get_prompt_for_scenario
from .reasoning_prompt import build_reasoning_prompt, normalize_reasoning_content

_CONN_EXC = (
    requests.exceptions.ConnectionError,
    requests.exceptions.Timeout,
    requests.exceptions.ChunkedEncodingError,
)
# 401/403 included: GPU/proxy auth blips and intermittent Forbidden must not soft-ack.
_TRANSIENT_STATUS = (401, 403, 408, 429, 500, 502, 503, 504)


class TransientError(Exception):
    """Retryable failure — hand the retry off to the VastPipeline."""


def _safe_non_negative_int(value: Any) -> int:
    """
    Best-effort int coercion for usage fields.
    Returns 0 for missing, invalid, NaN/inf, or negative values.
    """
    try:
        parsed = int(float(value))
    except (TypeError, ValueError, OverflowError):
        return 0
    return parsed if parsed > 0 else 0


def extract_usage_token_metrics(usage: Optional[Dict[str, Any]]) -> Dict[str, int]:
    """
    OpenAI-compatible usage: total_tokens and input-side tokens served from prefix/KV cache.
    Reported as usage.prompt_tokens_details.cached_tokens — "prompt" here means full model
    input (instructions plus multimodal/video context), not text-only.
    """
    if not usage:
        return {"total_tokens": 0, "cached_prompt_tokens": 0}
    pt = usage.get("prompt_tokens")
    ct = usage.get("completion_tokens")
    total = usage.get("total_tokens")
    if total is None and (pt is not None or ct is not None):
        total = _safe_non_negative_int(pt) + _safe_non_negative_int(ct)
    total_i = _safe_non_negative_int(total)
    cached = 0
    details = usage.get("prompt_tokens_details")
    if isinstance(details, dict):
        cached = _safe_non_negative_int(details.get("cached_tokens"))
    if cached == 0:
        cached = _safe_non_negative_int(usage.get("cached_tokens"))
    return {"total_tokens": total_i, "cached_prompt_tokens": cached}


class S3Client:
    """S3 client for downloading videos"""
    
    def __init__(self, settings):
        self.settings = settings
        self.client = boto3.client(
            "s3",
            endpoint_url=settings.s3endpoint,
            aws_access_key_id=settings.s3accesskey,
            aws_secret_access_key=settings.s3secretkey,
            verify=False
        )
    
    def download_file(self, bucket: str, key: str) -> bytes:
        """Download file from S3"""
        logging.info(f"[S3_CLIENT] Downloading s3://{bucket}/{key}")
        response = self.client.get_object(Bucket=bucket, Key=key)
        content = response["Body"].read()
        logging.info(f"[S3_CLIENT] Downloaded {len(content)} bytes")
        return content
    
    def head_object(self, bucket: str, key: str) -> Dict[str, Any]:
        """Get object metadata from S3"""
        logging.info(f"[S3_CLIENT] Fetching metadata for s3://{bucket}/{key}")
        response = self.client.head_object(Bucket=bucket, Key=key)
        logging.info(f"[S3_CLIENT] Retrieved metadata: {response.get('Metadata', {})}")
        return response


class CosmosReasoningClient:
    """Cosmos reasoning client for video analysis using hosted Reason2 API"""

    def __init__(self, settings):
        """Initialize Cosmos reasoning client"""
        self.settings = settings
        self.cosmos_url = settings.cosmos_url
        self.session = requests.Session()
        
        # Initialize tracer
        self.tracer = trace.get_tracer(__name__)

    def get_cosmos_reasoning(
        self,
        video_content: bytes,
        prompt: str = "Describe the main events in this clip.",
        max_tokens: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get reasoning content from Cosmos API using base64-encoded video"""
        with self.tracer.start_as_current_span("Cosmos Reasoning API Call") as span:
            span.set_attributes({
                "cosmos_url": self.cosmos_url,
                "model": self.settings.cosmos_model,
                "video_size_bytes": len(video_content)
            })
            
            # Encode video to base64
            start_encode = time.time()
            video_base64 = base64.b64encode(video_content).decode()
            encode_time = time.time() - start_encode
            video_size_mb = len(video_content) / (1024 * 1024)
            base64_size_kb = len(video_base64) / 1024
            
            span.set_attributes({
                "video_size_mb": video_size_mb,
                "base64_size_kb": base64_size_kb,
                "encode_time_seconds": encode_time
            })
            
            logging.info(f"[COSMOS] Encoding video ({video_size_mb:.2f} MB) to base64 ({base64_size_kb:.1f} KB)...")
            
            # Prepare content with base64-encoded video
            content = [
                {"type": "text", "text": prompt},
                {
                    "type": "video_url",
                    "video_url": {
                        "url": f"data:video/mp4;base64,{video_base64}"
                    }
                }
            ]
            
            payload = {
                "model": self.settings.cosmos_model,
                "messages": [{
                    "role": "user",
                    "content": content
                }],
                "max_tokens": max_tokens if max_tokens is not None else self.settings.cosmos_max_tokens,
                "temperature": self.settings.cosmos_temperature
            }
            
            headers = {"Content-Type": "application/json"}
            token = (self.settings.cosmos_authorization or "").strip()
            if token:
                headers["Authorization"] = (
                    token if token.lower().startswith("bearer ") else f"Bearer {token}"
                )
            
            # One in-process retry on connection errors; transient HTTP -> TransientError
            # so the handler raises and VastPipeline redelivers (no soft-ack).
            start_time = time.time()
            try:
                response = self.session.post(
                    self.cosmos_url, headers=headers, json=payload, timeout=600
                )
            except _CONN_EXC as exc:
                logging.warning("[RETRY] connection error to %s; retrying once: %s", self.cosmos_url, exc)
                try:
                    response = self.session.post(
                        self.cosmos_url, headers=headers, json=payload, timeout=600
                    )
                except _CONN_EXC as exc2:
                    raise TransientError(f"connection failed after 1 retry: {exc2}") from exc2
            if response.status_code in _TRANSIENT_STATUS:
                raise TransientError(f"transient HTTP {response.status_code}: {response.text[:300]}")

            reasoning_time = time.time() - start_time
            span.set_attributes({
                "reasoning_time_seconds": reasoning_time,
                "http_status_code": response.status_code
            })

            if response.status_code != 200:
                error_text = response.text[:1000] if hasattr(response, "text") else str(response.status_code)
                # Prefer redelivery over silent drop for unexpected HTTP errors.
                raise TransientError(f"Cosmos API error ({response.status_code}): {error_text}")

            response_data = response.json()
            
            choices = response_data.get("choices", [])
            if not choices:
                raise RuntimeError("No choices in Cosmos API response")
            
            reasoning_content = choices[0].get("message", {}).get("content", "")
            usage = response_data.get("usage") or {}
            metrics = extract_usage_token_metrics(usage)
            tokens_used = metrics["total_tokens"]
            cached_prompt_tokens = metrics["cached_prompt_tokens"]

            span.set_attributes({
                "reasoning_content_length": len(reasoning_content),
                "tokens_used": tokens_used,
                "cached_prompt_tokens": cached_prompt_tokens,
            })

            cache_note = f", {cached_prompt_tokens} cached input (API prompt_tokens_details)" if cached_prompt_tokens else ""
            logging.info(
                f"[COSMOS] {self.settings.cosmos_model} | {len(reasoning_content)} chars, "
                f"{tokens_used} tokens{cache_note} | {reasoning_time:.2f}s"
            )

            return {
                "reasoning_content": reasoning_content,
                "tokens_used": tokens_used,
                "cached_prompt_tokens": cached_prompt_tokens,
                "processing_time": reasoning_time,
                "cosmos_model": self.settings.cosmos_model,
                "raw_response": response_data
            }

    def analyze_video(
        self,
        video_content: bytes,
        filename: str,
        prompt: Optional[str] = None,
        scenario: Optional[str] = None,
        object_classes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Complete video analysis pipeline using Cosmos reasoning.
        
        Args:
            video_content: Video file content as bytes
            filename: Name of the video file
            prompt: Optional custom prompt (overrides scenario)
            scenario: Optional scenario name (overrides settings default, ignored if prompt is provided)
            object_classes: Optional comma-separated YOLO class names injected into the prompt
        """
        if prompt is None:
            scenario_to_use = scenario if scenario else self.settings.scenario
            scene_prompt = get_prompt_for_scenario(scenario_to_use)
        else:
            scene_prompt = prompt
        prompt = build_reasoning_prompt(scene_prompt, object_classes or "")
        
        with self.tracer.start_as_current_span("Complete Video Analysis (Cosmos)") as span:
            scenario_used = scenario if scenario else self.settings.scenario
            span.set_attributes({
                "filename": filename,
                "file_size_bytes": len(video_content),
                "scenario": scenario_used
            })
            
            # Check video size limit
            max_size_bytes = self.settings.max_video_size_mb * 1024 * 1024
            if len(video_content) > max_size_bytes:
                raise ValueError(f"Video too large: {len(video_content)} > {max_size_bytes} bytes")
            
            # Send base64-encoded video directly to API (no SFTP upload)
            reasoning_result = self.get_cosmos_reasoning(video_content, prompt)
            reasoning_content = normalize_reasoning_content(
                reasoning_result["reasoning_content"]
            )

            result = {
                "filename": filename,
                "reasoning_content": reasoning_content,
                "cosmos_model": reasoning_result["cosmos_model"],
                "tokens_used": reasoning_result["tokens_used"],
                "cached_prompt_tokens": reasoning_result.get("cached_prompt_tokens", 0),
                "processing_time": reasoning_result["processing_time"],
            }

            span.set_attributes({
                "reasoning_content_length": len(result["reasoning_content"]),
                "total_tokens": result["tokens_used"],
                "cached_prompt_tokens": result["cached_prompt_tokens"],
                "total_processing_time": result["processing_time"]
            })
            
            return result

    def close(self):
        """Close HTTP session"""
        if hasattr(self, 'session'):
            self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


```


## FILE: vss-blueprint/source-code/ingest/video-reasoner/common/prompts.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/video-reasoner/common/prompts.py

```
"""
Preconfigured prompts for different video analysis scenarios.
Set the 'scenario' key in your secret to switch between them.

GUI labels & capture types: source-code/shared/ingest_metadata.py (exposed via GET /api/v1/metadata/ingest-config)
"""

SCENARIO_PROMPTS = {
    "surveillance": """Analyze this surveillance footage. Focus on people, unusual behavior, safety hazards, abandoned objects, vehicles, crowds, and security concerns. Be specific about locations within the frame.""",

    "traffic": """Analyze this traffic camera footage. Focus on vehicles, traffic flow, violations, pedestrians, congestion, accidents or near-misses, and road conditions.""",

    "live_driving": """Analyze this ~5 second dashcam or mobile road camera clip. Describe road type, traffic controls, vehicles (especially trucks and buses), pedestrians or cyclists, lane-blocking vehicles, readable signage, and any visible violations or hazards. Describe only what is clearly visible.""",

    "nhl": """Analyze this NHL hockey game footage. Focus on key plays, player actions, penalties, goaltending, special teams, face-offs, and team formations. Note jersey numbers and team colors when visible.""",

    "sports": """Analyze this sports footage. Focus on key plays, player movement, scoring chances, defense, fouls, momentum shifts, and notable performances.""",

    "retail": """Analyze this retail store footage. Focus on customer flow, product interactions, checkout queues, staff activity, suspicious behavior, and store layout usage.""",

    "warehouse": """Analyze this warehouse footage. Focus on forklifts, workers, inventory handling, PPE compliance, hazards, spills, and dock activity.""",

    "egocentric": """Analyze this first-person (egocentric) footage. Focus on hand actions, object manipulation, tools, task steps, and workspace context from the wearer's viewpoint.""",

    "general": """Analyze this video footage. Focus on people, objects, environment, notable activities, and interactions. Be factual and specific.""",

    "nyc_control": """Analyze this NYC urban footage for command and control. Focus on location cues, readable signage or plates, traffic or public-safety anomalies, vehicles of interest, and whether the scene appears controlled or needs monitoring.""",

    "nyc_safety_surveillance": """Analyze this ~5 second NYC street surveillance clip. Describe pedestrians, vehicles, readable signs and vehicle brands, street furniture, crowd activity, and any visible safety concerns. Describe only what is clearly visible.""",
}


DEFAULT_SCENARIO = "general"


def get_prompt_for_scenario(scenario: str) -> str:
    """
    Get the plain scenario prompt.
    Falls back to 'general' if scenario is not found.
    """
    scenario_lower = scenario.lower().strip()

    if scenario_lower in SCENARIO_PROMPTS:
        return SCENARIO_PROMPTS[scenario_lower]

    import logging
    logging.warning(f"[PROMPTS] Unknown scenario '{scenario}', falling back to 'general'")
    return SCENARIO_PROMPTS["general"]


def get_available_scenarios() -> list[str]:
    """Return list of all available scenario keys"""
    return list(SCENARIO_PROMPTS.keys())


```


## FILE: vss-blueprint/source-code/ingest/video-reasoner/common/reasoning_prompt.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/video-reasoner/common/reasoning_prompt.py

```
"""Plain-text reasoning prompt builder and response normalizer."""
import json
import re
from typing import Any, Dict

REASONING_CONTENT_MAX_CHARS = 1024

_PLAIN_TEXT_INSTRUCTION = (
    "Respond in plain prose only (no JSON, no markdown, no bullet lists). "
    f"Keep your answer under {REASONING_CONTENT_MAX_CHARS} characters.\n"
    "Write a dense, searchable description of what is clearly visible. "
    "Prefer concrete searchable atoms when you can see them: "
    "colors; brand or logo names; vehicle type (and color if clear); "
    "readable street, shop, or sign text; exact counts only when obvious; "
    "the main action underway; the most likely next move if strongly implied. "
    "Mention only what the clip shows — do not invent brands, streets, counts, "
    "or futures that are not evident. Skip filler (weather, 'urban setting', "
    "'no hazards') unless it is the main point of the clip."
)

_SCENE_SUMMARY_RE = re.compile(
    r'"scene_summary"\s*:\s*"((?:\\.|[^"\\])*)"',
    re.DOTALL | re.IGNORECASE,
)
_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*([\s\S]*?)\s*```", re.IGNORECASE)


def build_reasoning_prompt(scene_prompt: str, object_classes: str = "") -> str:
    """Combine scenario prompt with YOLO object hints and plain-text instructions."""
    parts = [scene_prompt.strip()]
    classes = _normalize_class_list(object_classes)
    if classes:
        parts.append(f"Detected objects in this clip: {classes}.")
    parts.append(_PLAIN_TEXT_INSTRUCTION)
    return "\n\n".join(parts)


def normalize_reasoning_content(raw: str) -> str:
    """Return plain text only: strip JSON/markdown fences and truncate."""
    text = (raw or "").strip()
    if not text:
        return ""

    fence_match = _JSON_FENCE_RE.search(text)
    if fence_match:
        text = fence_match.group(1).strip()

    if text.startswith("{"):
        text = _plain_from_json(text) or text

    summary_match = _SCENE_SUMMARY_RE.search(text)
    if summary_match:
        try:
            text = str(json.loads(f'"{summary_match.group(1)}"')).strip()
        except json.JSONDecodeError:
            text = summary_match.group(1).replace('\\"', '"').strip()

    text = _JSON_FENCE_RE.sub("", text)
    text = text.replace("```", "").strip()
    text = re.sub(r"\s+", " ", text).strip()

    return _truncate(text)


def _normalize_class_list(object_classes: str) -> str:
    classes: list[str] = []
    for part in str(object_classes or "").split(","):
        name = part.strip().lower()
        if name and name not in classes:
            classes.append(name)
    return ", ".join(classes)


def _plain_from_json(text: str) -> str:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return ""
    if not isinstance(data, dict):
        return ""
    summary = str(data.get("scene_summary") or "").strip()
    if summary:
        return summary
    return _flatten_structured_dict(data)


def _flatten_structured_dict(data: Dict[str, Any]) -> str:
    parts: list[str] = []
    for key in ("scene_summary", "summary", "description"):
        value = str(data.get(key) or "").strip()
        if value:
            parts.append(value)
            break
    actions = data.get("actions") or []
    if isinstance(actions, list) and actions:
        parts.append("; ".join(str(a).strip() for a in actions if str(a).strip()))
    return ". ".join(p for p in parts if p).strip()


def _truncate(text: str) -> str:
    if len(text) <= REASONING_CONTENT_MAX_CHARS:
        return text
    cut = text[:REASONING_CONTENT_MAX_CHARS]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "..."

```


## FILE: vss-blueprint/source-code/ingest/video-segmenter/common/handler_utils.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/video-segmenter/common/handler_utils.py

```
import logging
import re
from typing import Dict, Any, List, Tuple
from urllib.parse import unquote


def parse_s3_event(event_data: Dict[str, Any]) -> Dict[str, str]:
    """Parse S3 event data to extract bucket and key."""
    sequencer = None
    etag = None
    
    if "Records" in event_data:
        record = event_data["Records"][0]
        s3_info = record.get("s3", {})
        bucket = s3_info.get("bucket", {}).get("name", "")
        key = s3_info.get("object", {}).get("key", "")
        sequencer = s3_info.get("object", {}).get("sequencer", "")
        etag = s3_info.get("object", {}).get("eTag", "")
        event_name = record.get("eventName", "unknown")
    elif "bucket" in event_data and "key" in event_data:
        bucket = event_data["bucket"]
        key = event_data["key"]
        event_name = event_data.get("eventName", "unknown")
    else:
        raise ValueError(f"Unsupported event format: {event_data}")
    
    key = unquote(key)
    
    return {
        "bucket": bucket,
        "key": key,
        "event_name": event_name,
        "sequencer": sequencer,
        "etag": etag
    }


def should_process_event(key: str, event_name: str) -> Tuple[bool, str]:
    """Check if the event should be processed. Returns (should_process, skip_reason)."""
    if "Delete" in event_name:
        return False, "Delete event"
    
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']
    key_lower = key.lower()
    
    if not any(key_lower.endswith(ext) for ext in video_extensions):
        return False, f"Not a video file: {key}"
    
    if "_segment_" in key_lower or "-segment-" in key_lower:
        return False, "Already a segment"
    
    return True, ""


def get_output_bucket_name(input_bucket: str, suffix: str = "-segments") -> str:
    """Get output bucket name for segments."""
    return f"{input_bucket}{suffix}"


def get_segment_list_prefix(original_filename: str) -> str:
    """S3 prefix for listing segment objects of a source video."""
    base_name = original_filename.rsplit(".", 1)[0]
    return f"segments/{base_name}_segment_"


def segments_already_complete(segment_keys: List[str], original_filename: str) -> Tuple[bool, str]:
    """True when every segment 1..N exists for some consistent total N."""
    base_name = original_filename.rsplit(".", 1)[0]
    pattern = re.compile(
        rf"^segments/{re.escape(base_name)}_segment_(\d{{3}})_of_(\d{{3}})\."
    )
    by_total: dict[int, set[int]] = {}
    for key in segment_keys:
        match = pattern.match(key)
        if not match:
            continue
        seg_num, total = int(match.group(1)), int(match.group(2))
        by_total.setdefault(total, set()).add(seg_num)

    for total, found in by_total.items():
        if found == set(range(1, total + 1)):
            return True, f"All {total} segments already exist in S3"
    return False, ""


def get_segment_key(original_filename: str, segment_number: int, total_segments: int) -> str:
    """Generate S3 key for a segment."""
    name_parts = original_filename.rsplit('.', 1)
    base_name = name_parts[0]
    extension = name_parts[1] if len(name_parts) > 1 else 'mp4'
    return f"segments/{base_name}_segment_{segment_number:03d}_of_{total_segments:03d}.{extension}"


def prepare_metadata(
    original_metadata: Dict[str, str],
    segment_number: int,
    total_segments: int,
    duration: float,
    parent_video_source: str,
    segment_start_sec: float,
    segment_end_sec: float,
    segment_step_sec: float,
) -> Dict[str, str]:
    """Prepare metadata for a video segment, preserving original S3 metadata."""
    metadata = {}
    if "Metadata" in original_metadata:
        metadata = dict(original_metadata["Metadata"])
    
    # Add segment-specific metadata
    metadata["segment_number"] = str(segment_number)
    metadata["total_segments"] = str(total_segments)
    metadata["segment_duration"] = f"{duration:.2f}"
    # Canonical parent video key for grouping (full S3 URI of source upload)
    metadata["original_video"] = parent_video_source
    metadata["segment_start_sec"] = f"{segment_start_sec:.3f}"
    metadata["segment_end_sec"] = f"{segment_end_sec:.3f}"
    metadata["segment_step_sec"] = f"{segment_step_sec:.3f}"
    metadata["segment_type"] = "video_segment"

    for key in ("stream_id", "chunk_index", "chunk_start_sec", "chunk_duration_sec", "capture_interval", "ingest_kind", "capture_timestamp"):
        val = metadata.get(key) or original_metadata.get("Metadata", {}).get(key)
        if val is not None and str(val).strip() != "":
            metadata[key] = str(val).strip()
    
    return metadata


```


## FILE: vss-blueprint/source-code/ingest/video-segmenter/common/models.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/video-segmenter/common/models.py

```
import os
import json
from typing import Any, Optional, Dict
from pydantic import BaseModel, computed_field, Field


class Settings(BaseModel):
    """Configuration settings for video segmenter"""
    # S3 settings
    s3accesskey: str
    s3secretkey: str
    s3endpoint: str
    
    # Video processing settings
    segment_duration: int = 5  # seconds
    output_codec: str = "libx264"
    output_format: str = "mp4"
    output_bucket_suffix: str = "-segments"  # e.g., videos -> videos-segments
    # Higher quality re-encode (lower CRF = larger files, better fidelity; 18 is near-visually lossless for many sources)
    video_crf: int = 18
    # Use medium (or faster) for multi-segment jobs: "slow" risks serverless timeouts so only segment 001 completes.
    ffmpeg_preset: str = "medium"
    audio_bitrate: str = "192k"
    
    @classmethod
    def from_ctx_secrets(cls, secrets: Dict[str, Any]) -> "Settings":
        """Load settings from runtime context secrets; optional keys use model defaults."""
        src = secrets["vss2-secret"]
        config = {name: src[name] for name in cls.model_fields if name in src}
        return cls(**config)


class S3ObjectMetadataModel(BaseModel):
    """Pydantic model for parsing S3 metadata from video uploads"""
    
    # Metadata fields from frontend upload
    is_public: str | None = Field(None, alias="is-public")  # "true" or "false"
    allowed_users: str | None = Field(None, alias="allowed-users")  # Comma-separated usernames
    tags: str | None = None  # Comma-separated tags
    original_filename: str | None = Field(None, alias="original-filename")
    upload_timestamp: str | None = Field(None, alias="upload-timestamp")
    
    # Metadata fields from video-streaming service
    camera_id: str | None = Field(None, alias="camera-id")  # Camera identifier
    capture_type: str | None = Field(None, alias="capture-type")  # traffic, streets, crowds, malls
    location: str | None = Field(None, alias="location")  # Geographic area
    capture_timestamp: str | None = Field(None, alias="capture-timestamp")  # When captured
    
    # Analysis scenario metadata
    scenario: str | None = None  # Analysis prompt scenario (egocentric, surveillance, etc.)
    
    class Config:
        extra = "allow"
        populate_by_name = True
    
    def get_is_public_bool(self) -> bool:
        """Convert is_public string to boolean"""
        if self.is_public:
            return self.is_public.lower() == "true"
        return False
    
    def get_allowed_users_list(self) -> list[str]:
        """Parse allowed_users from comma-separated string"""
        if not self.allowed_users:
            return []
        return [u.strip() for u in self.allowed_users.split(",") if u.strip()]
    
    def get_tags_list(self) -> list[str]:
        """Parse tags from comma-separated string"""
        if not self.tags:
            return []
        return [t.strip() for t in self.tags.split(",") if t.strip()]


class VideoSegmentInfo(BaseModel):
    """Information about a video segment"""
    segment_number: int
    total_segments: int
    duration: float
    start_time: float
    end_time: float
    segment_key: str
    segment_size: int


```


## FILE: vss-blueprint/source-code/ingest/video-detector/README.md
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/ingest/video-detector/README.md

```
# Video detector (YOLO11)

Runs object detection on each segment MP4 before the VLM reasoner.

## Flow

1. Receive S3 segment land event (same shape as reasoner).
2. Download segment MP4 from S3 and call `POST <yolo_infer>/v1/infer` with `video_base64`, `filename`, and `include_frames`.
3. Write gzipped sidecar JSON to `detections/{segment_stem}.json.gz` on the segments bucket.
4. Normalize `object_counts` to **max concurrent per class** (peak boxes in any frame); fallback ≈ raw_sum / frame_count when frames are not stored. `detection_count` remains total raw boxes.
5. Emit summary fields (`object_classes`, `object_counts`, `perception_ok`, …) plus metadata pass-through to **video-reasoner**.

## Pipeline link

`video-segment-land-trigger → video-detector → video-reasoner → video-embedder → video-vastdb-writer`

## Secret keys (`vss2-secret`)

| Key | Description |
|-----|-------------|
| `yolo_infer_host` | GPU host or hosted API path for infer service |
| `yolo_infer_port` | Default `8022` (use `443` for HTTPS APIs) |
| `detector_authorization` | (optional) Bearer token sent as `Authorization` when set |
| `yolo_conf` | Confidence threshold (passed to infer service if supported) |
| `yolo_model` | Model id label (logging) |
| `yolo_presign_ttl` | Presigned GET TTL seconds |
| `detection_sidecar_prefix` | S3 key prefix, default `detections/` |
| `detection_store_frames` | `true` to write frame bboxes sidecar |

Also requires S3 keys (`s3accesskey`, `s3secretkey`, `s3endpoint`) and optional VastDB keys for idempotency skip.

## Build

```bash
cd source-code/ingest/video-detector
vastde functions build vss-video-detector
```

Or `./source-code/scripts/build-vastde-functions.sh`.

```


## FILE: vss-blueprint/source-code/enrichment/prompt-suggester/main.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/enrichment/prompt-suggester/main.py

```
from datetime import datetime, timezone

from vast_runtime.vast_event import VastEvent  # type: ignore

from common.llm_suggester import generate_suggestions
from common.models import Settings
from common.vastdb_client import VastDBClient


def init(ctx):
    """Initialize the serverless function."""
    with ctx.tracer.start_as_current_span("Prompt Suggester Initialization"):
        settings = Settings.from_ctx_secrets(ctx.secrets)
        ctx.settings = settings
        ctx.vastdb_client = VastDBClient(settings)
        ctx.logger.info(
            f"[INIT] segments={settings.vdbcollection} prompts={settings.vdbpromptscollection} "
            f"cosmos={settings.cosmos_model} @ {settings.cosmos_host}:{settings.cosmos_port}"
        )


def handler(ctx, event: VastEvent):
    """Main handler for vast serverless runtime (scheduled trigger)."""

    with ctx.tracer.start_as_current_span("Prompt Suggester Handler") as handler_span:
        try:
            data = event.get_data()
            event_type = getattr(event, "get_type", lambda: "scheduled_trigger")()
            handler_span.set_attribute("event_type", event_type)
            if data:
                handler_span.set_attribute("trigger_payload_keys", ",".join(sorted(data.keys())))

            ctx.logger.info("[SUGGEST] Starting scheduled prompt/event generation")

            with ctx.tracer.start_as_current_span("Fetch Corpus") as fetch_span:
                segments = ctx.vastdb_client.fetch_corpus()
                processed_videos = ctx.vastdb_client.list_processed_videos()
                existing_prompts = ctx.vastdb_client.list_existing_search_prompts()
                segments = ctx.vastdb_client.filter_unprocessed_corpus(segments, processed_videos)
                videos = ctx.vastdb_client.list_distinct_videos(segments)
                fetch_span.set_attributes({
                    "segments_sampled": len(segments),
                    "unique_videos": len(videos),
                    "videos_already_processed": len(processed_videos),
                    "lookback_hours": ctx.settings.suggestions_lookback_hours,
                })
                ctx.logger.info(
                    f"[SUGGEST] Corpus: {len(segments)} sample segments, {len(videos)} new videos "
                    f"({len(processed_videos)} already processed, skipped)"
                )

            if not segments:
                ctx.logger.info(
                    "[SUGGEST] No new videos in lookback window "
                    "(all already have suggestions or no segments)"
                )
                return {
                    "status": "success",
                    "skipped": True,
                    "reason": "no_new_videos",
                    "videos_already_processed": len(processed_videos),
                    "segments_scanned": 0,
                    "search_prompts": 0,
                    "key_events": 0,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }

            with ctx.tracer.start_as_current_span("LLM Suggestions") as llm_span:
                search_prompts, key_events, batch_id = generate_suggestions(ctx.settings, segments)
                llm_span.set_attributes({
                    "batch_id": batch_id,
                    "search_prompts": len(search_prompts),
                    "key_events": len(key_events),
                })

            with ctx.tracer.start_as_current_span("VastDB Storage") as storage_span:
                table_full = (
                    f"{ctx.vastdb_client.bucket}.{ctx.vastdb_client.schema_name}."
                    f"{ctx.vastdb_client.prompts_table_name}"
                )
                ctx.logger.info(f"[VASTDB] Writing suggestions to {table_full}")
                rows_written = ctx.vastdb_client.store_suggestions(
                    batch_id,
                    search_prompts,
                    key_events,
                    skip_prompt_texts=existing_prompts,
                    skip_videos=processed_videos,
                )
                storage_span.set_attributes({
                    "table_name": table_full,
                    "rows_written": rows_written,
                    "batch_id": batch_id,
                })

            result = {
                "status": "success",
                "batch_id": batch_id,
                "segments_scanned": len(segments),
                "unique_videos": len(videos),
                "search_prompts": len(search_prompts),
                "key_events": len(key_events),
                "rows_written": rows_written,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
            ctx.logger.info(
                f"[COMPLETE] batch={batch_id} prompts={len(search_prompts)} "
                f"events={len(key_events)} rows={rows_written}"
            )
            return result

        except Exception as exc:
            handler_span.set_attribute("error", True)
            handler_span.set_attribute("error.message", str(exc))
            handler_span.record_exception(exc)
            ctx.logger.error(f"[SUGGEST] Failed: {exc}")
            return {"status": "error", "error": str(exc)}

```


## FILE: vss-blueprint/scripts/vss-blueprint-models/yolo-infer/main.py
Source: https://github.com/vast-data/vss-blueprint/blob/main/scripts/vss-blueprint-models/yolo-infer/main.py

```
"""
YOLO11 bbox JSON (one-shot segment).

Accepts either:
  - presigned HTTP(S) URL to MP4, or
  - base64-encoded MP4 in the JSON body

Run on the RTX GPU host:
  CUDA_VISIBLE_DEVICES=2 ./run.sh
"""

from __future__ import annotations

import asyncio
import base64
import binascii
import os
import re
import tempfile
import uuid
from collections import Counter
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, HttpUrl, model_validator

YOLO_MODEL = os.environ.get("YOLO_MODEL", "yolo11s.pt")
YOLO_CONF = float(os.environ.get("YOLO_CONF", "0.4"))
YOLO_DEVICE = os.environ.get("YOLO_DEVICE", "0")
PERCEPTION_SOURCE = os.environ.get("PERCEPTION_SOURCE", "yolo11_coco")
DOWNLOAD_TIMEOUT_S = float(os.environ.get("DOWNLOAD_TIMEOUT_S", "120"))
MAX_DOWNLOAD_BYTES = int(os.environ.get("MAX_DOWNLOAD_BYTES", str(200 * 1024 * 1024)))
MAX_BASE64_CHARS = int(os.environ.get("MAX_BASE64_CHARS", str(280 * 1024 * 1024)))

_model = None
_DATA_URI_RE = re.compile(r"^data:video/[^;]+;base64,", re.IGNORECASE)


def _get_model():
    global _model
    if _model is None:
        from ultralytics import YOLO

        _model = YOLO(YOLO_MODEL)
    return _model


def _infer_video_sync(video_path: Path) -> list[dict[str, Any]]:
    import cv2

    model = _get_model()
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video: {video_path}")
    vid_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    vid_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap.release()

    frames_out: list[dict[str, Any]] = []
    for i, result in enumerate(
        model.predict(
            source=str(video_path),
            stream=True,
            conf=YOLO_CONF,
            device=YOLO_DEVICE,
            verbose=False,
        )
    ):
        dets: list[dict[str, Any]] = []
        if result.boxes is not None:
            names = result.names or {}
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                cls_id = int(box.cls[0])
                dets.append(
                    {
                        "label": names.get(cls_id, str(cls_id)),
                        "confidence": round(float(box.conf[0]), 4),
                        "bbox": [int(x1), int(y1), int(x2), int(y2)],
                    }
                )
        frames_out.append(
            {
                "frame_index": i,
                "shape": [vid_h, vid_w],
                "detections": dets,
            }
        )
    return frames_out


def _aggregate_frames(frames: list[dict[str, Any]]) -> dict[str, Any]:
    class_counts: Counter[str] = Counter()
    max_conf = 0.0
    all_classes: set[str] = set()

    for frame in frames:
        for det in frame.get("detections", []):
            label = det.get("label") or "unknown"
            class_counts[label] += 1
            all_classes.add(label)
            conf = float(det.get("confidence") or 0.0)
            if conf > max_conf:
                max_conf = conf

    return {
        "object_classes": sorted(all_classes),
        "object_counts": dict(class_counts),
        "max_detection_conf": round(max_conf, 4),
        "frame_count": len(frames),
        "detection_count": sum(class_counts.values()),
    }


def _build_response(frames: list[dict[str, Any]], include_frames: bool) -> dict[str, Any]:
    summary = _aggregate_frames(frames)
    perception = {
        "source": PERCEPTION_SOURCE,
        "frames": frames if include_frames else None,
        **summary,
    }
    return {
        "ok": True,
        "perception_ok": len(frames) > 0,
        "perception_json": perception,
        "object_classes": summary["object_classes"],
        "object_counts": summary["object_counts"],
        "max_detection_conf": summary["max_detection_conf"],
        "frames": frames if include_frames else None,
    }


async def _download_video(url: str, dest: Path) -> None:
    async with httpx.AsyncClient(follow_redirects=True, timeout=DOWNLOAD_TIMEOUT_S) as client:
        async with client.stream("GET", url) as resp:
            if resp.status_code >= 400:
                body = await resp.aread()
                raise HTTPException(
                    502,
                    f"Presigned URL fetch failed: HTTP {resp.status_code} — {body[:200]!r}",
                )
            size = 0
            with dest.open("wb") as fh:
                async for chunk in resp.aiter_bytes(chunk_size=1024 * 1024):
                    size += len(chunk)
                    if size > MAX_DOWNLOAD_BYTES:
                        raise HTTPException(413, f"Download exceeds {MAX_DOWNLOAD_BYTES} bytes")
                    fh.write(chunk)


def _decode_video_base64(video_base64: str) -> bytes:
    raw = video_base64.strip()
    if len(raw) > MAX_BASE64_CHARS:
        raise HTTPException(413, f"video_base64 exceeds {MAX_BASE64_CHARS} characters")
    raw = _DATA_URI_RE.sub("", raw)
    try:
        data = base64.b64decode(raw, validate=True)
    except binascii.Error as exc:
        raise HTTPException(400, f"Invalid base64 in video_base64: {exc}") from exc
    if len(data) > MAX_DOWNLOAD_BYTES:
        raise HTTPException(413, f"Decoded video exceeds {MAX_DOWNLOAD_BYTES} bytes")
    if len(data) < 12:
        raise HTTPException(400, "Decoded video is too small to be a valid MP4")
    return data


def _tmp_video_path(tmp_dir: Path, filename: str | None) -> Path:
    suffix = Path(filename or "segment.mp4").suffix or ".mp4"
    if suffix.lower() not in (".mp4", ".mov", ".mkv", ".avi", ".webm"):
        suffix = ".mp4"
    return tmp_dir / f"{uuid.uuid4().hex}{suffix}"


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await asyncio.to_thread(_get_model)
    yield


app = FastAPI(title="VSS YOLO11 Infer", version="1.1.0", lifespan=lifespan)


class InferRequest(BaseModel):
    url: HttpUrl | None = Field(
        None,
        description="Presigned HTTP/HTTPS URL to a segment MP4",
    )
    video_base64: str | None = Field(
        None,
        description="Base64-encoded MP4 bytes (optional data:video/mp4;base64, prefix)",
    )
    filename: str | None = Field(
        None,
        description="Optional hint when using video_base64 (e.g. segment.mp4)",
    )
    include_frames: bool = Field(
        False,
        description="If true, include per-frame bboxes in response (can be large)",
    )

    @model_validator(mode="after")
    def _exactly_one_input(self) -> InferRequest:
        has_url = self.url is not None
        has_b64 = bool(self.video_base64 and self.video_base64.strip())
        if has_url == has_b64:
            raise ValueError("Provide exactly one of: url, video_base64")
        return self


@app.get("/healthz")
async def healthz() -> dict[str, Any]:
    cuda_ok = False
    try:
        import torch

        cuda_ok = torch.cuda.is_available()
    except ImportError:
        pass
    return {
        "ok": True,
        "model": YOLO_MODEL,
        "device": YOLO_DEVICE,
        "cuda_available": cuda_ok,
        "model_loaded": _model is not None,
        "inputs": ["url", "video_base64"],
    }


async def _run_infer_on_path(video_path: Path, include_frames: bool) -> dict[str, Any]:
    try:
        frames = await asyncio.to_thread(_infer_video_sync, video_path)
    except Exception as exc:
        raise HTTPException(502, f"Inference failed: {exc}") from exc
    return _build_response(frames, include_frames)


@app.post("/v1/infer")
async def infer(req: InferRequest) -> dict[str, Any]:
    tmp_dir = Path(tempfile.gettempdir()) / "vss-yolo-infer"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    video_path = _tmp_video_path(tmp_dir, req.filename)

    try:
        if req.url is not None:
            url = str(req.url)
            scheme = urlparse(url).scheme.lower()
            if scheme not in ("http", "https"):
                raise HTTPException(400, f"Unsupported URL scheme: {scheme}")
            await _download_video(url, video_path)
        else:
            data = _decode_video_base64(req.video_base64 or "")
            video_path.write_bytes(data)

        return await _run_infer_on_path(video_path, req.include_frames)
    except HTTPException:
        raise
    finally:
        video_path.unlink(missing_ok=True)


@app.post("/v1/infer-base64")
async def infer_base64(req: InferRequest) -> dict[str, Any]:
    """Alias when clients always send base64 (url must be omitted)."""
    if not req.video_base64:
        raise HTTPException(400, "video_base64 is required for /v1/infer-base64")
    if req.url is not None:
        raise HTTPException(400, "Use /v1/infer with url only, not both")
    return await infer(req)

```
