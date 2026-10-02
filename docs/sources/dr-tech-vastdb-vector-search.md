

## FILE: vastdb-adbc-driver/README.md
Source: https://github.com/vast-data/vastdb-adbc-driver/blob/main/README.md

```
# VastDB Query Engine ADBC Driver

## Overview

The VastDB ADBC Driver provides access to the VastDB Query Engine.

For more details about the VAST Query Engine, see [this whitepaper](https://kb.vastdata.com/documentation/docs/vast-query-engine).

For more details about the VAST Database, see [this whitepaper](https://vastdata.com/whitepaper/#TheVASTDataBase).

## Requirements

- Linux / Mac client with network access to the VAST Cluster
- [Virtual IP pool configured with DNS service](https://support.vastdata.com/s/topic/0TOV40000000FThOAM/configuring-network-access-v50)
- [S3 access & secret keys on the VAST cluster](https://support.vastdata.com/s/article/UUID-4d2e7e23-b2fb-7900-d98f-96c31a499626)
- [Tabular identity policy with the proper permissions](https://support.vastdata.com/s/article/UUID-14322b60-d6a2-89ac-3df0-3dfbb6974182)


## Installation

The VastDB ADBC Driver is shipped as a standalone library.

## Usage

Example of using the VastDB ADBC Driver with the Python `adbc-driver-manager`.

```python
import adbc_driver_manager

with adbc_driver_manager.dbapi.connect(
    driver="<path/to/driver>",
    db_kwargs={
        "vast.db.endpoint": "<vast_cluster_endpoint>",
        "vast.db.access_key": "<aws_access_key>",
        "vast.db.secret_key": "<aws_secret_key>",
    }
) as conn:
    # Use the database connection
    pass
```

See [Options](#options) for the full list of database, connection, and statement options.

## Options

### Database options

Set these on `AdbcDatabase` before creating a connection. All three are required.

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `vast.db.endpoint` | URL string | — | VAST cluster endpoint URL. Required. |
| `vast.db.access_key` | string | — | AWS access key. Required. |
| `vast.db.secret_key` | string | — | AWS secret key. Required. |

Standard ADBC database options are not supported.

### Connection options

#### Standard ADBC options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `adbc.connection.autocommit` | `"true"` or `"false"` | `"true"` | Controls transaction autocommit mode. Can be set at connection creation or via `AdbcConnectionSetOption` before the connection is used (before creating statements, calling `get_objects`, or `get_table_schema`). Cannot be changed after the connection is used. |

#### Custom options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `vast.db.end_user` | string | — | End-user impersonation. Set at connection creation. For more details see [User Impersonation](https://kb.vastdata.com/documentation/docs/user-impersonation). |
| `vast.db.variable.<name>` | string, integer, or double | — | Define a user variable accessible in queries, e.g. `SELECT getVariable('x')`. Any valid DuckDB user variable name is valid. Set after connection init. |
| `vast.db.setting.<name>` | string, integer, or double | — | Set a VAST session setting that influences query execution (see supported settings below). Set after connection init. |

User variables and session settings cannot be passed at connection creation; set them with `AdbcConnectionSetOption` after the connection is initialized.

#### Supported VAST session settings

- `vector_search_skip_recent_non_indexed`
- `vector_search_min_prob`
- `vector_search_max_prob`
- `vector_search_pruning_distance_ratio`
- `vector_search_min_full_clusters_after_filtering`
- `vector_search_defer_projection`

### Statement options

#### Standard ADBC options

Used with `AdbcStatementExecuteUpdate` for bulk data ingest (see [Data ingestion](#data-ingestion)).

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `adbc.ingest.mode` | `adbc.ingest.mode.append` | — | Ingest mode. Only append is supported. Required for ingest. |
| `adbc.ingest.target_catalog` | `vastdb` | — | Target catalog. Only `vastdb` is accepted when set. |
| `adbc.ingest.target_db_schema` | schema path | — | Fully qualified schema path (e.g. `"bucket/schema"`). Required for ingest. |
| `adbc.ingest.target_table` | table name | — | Target table name. Required for ingest. |

Other standard ingest options are not supported.

## Data ingestion

The driver supports ADBC bulk ingest via `AdbcStatementExecuteUpdate`, following the standard ADBC ingest option keys listed above.

**Supported data binding**

- `AdbcStatementBind` — bind a single Arrow `RecordBatch`. This is the supported way to provide ingest data.
- `AdbcStatementBindStream` — **not supported**.

**Requirements**

1. Set all required ingest options (`adbc.ingest.mode`, `adbc.ingest.target_db_schema`, `adbc.ingest.target_table`).
2. Bind a `RecordBatch` with `AdbcStatementBind`.
3. An SQL statement must **not** be set on the statement.
4. Call `AdbcStatementExecuteUpdate`.

Ingest respects the connection's transaction mode: use `commit` / `rollback` when autocommit is disabled.

Example using the Python `adbc-driver-manager`:

```python
import adbc_driver_manager
import pyarrow as pa

bucket = "my-bucket"
schema_name = "s"
table_name = "t"

schema = pa.schema([("a", pa.int32())])
batch = pa.record_batch([pa.array([42], type=pa.int32())], schema=schema)

with adbc_driver_manager.dbapi.connect(
    driver="<path/to/driver>",
    db_kwargs={
        "vast.db.endpoint": "<vast_cluster_endpoint>",
        "vast.db.access_key": "<aws_access_key>",
        "vast.db.secret_key": "<aws_secret_key>",
    },
) as conn:
    with adbc_driver_manager.AdbcStatement(conn.adbc_connection) as stmt:
        stmt.set_options(
            **{
                "adbc.ingest.mode": "adbc.ingest.mode.append",
                "adbc.ingest.target_catalog": "vastdb",
                "adbc.ingest.target_db_schema": f"{bucket}/{schema_name}",
                "adbc.ingest.target_table": table_name,
            }
        )
        stmt.bind(batch)
        rows_affected = stmt.execute_update()
```

## Logging

- **Default logging level**: `INFO`.
- To increase verbosity, set the environment variable `RUST_LOG` to values like `DEBUG` or `TRACE`.

### Log Location

Logs are written to the following directory on Linux systems:

`~/.local/share/VastDbDriver/vastdb_driver.log`

Or, on Mac to:

`~/Library/Logs/VastDbDruver/vastdb_driver.log`

- Home directory can be changed by setting `VAST_ADBC_LOG_DIR`
- Console logs can be enabled by settings `VAST_ADBC_STDOUT=1`
- Logs are rotated daily or when the file reaches 100 MB.
- The system keeps up to 10 log files at a time.

## Known Limitations

- **AdbcConnectionGetObjects**: Supports only the `vastdb` catalog and exact filter for `db_schema`
- **ExecutePartitions** Not supported.
- **AdbcStatementPrepare**: Prepare should be done using SQL prepare statements through execute.
- **StatementExecuteSchema**, **AdbcStatementGetParameterSchema** and **AdbcStatementSetSubstraitPlan**: Not supported.
- **AdbcStatementBindStream**: Not supported. Ingest accepts data only via `AdbcStatementBind` with a single `RecordBatch`.
- **Ingest modes**: Only `adbc.ingest.mode.append` is supported (`create`, `create_append`, and `replace` are not).

## Support

For detailed documentation, FAQs, and troubleshooting guides, refer to the official resources or contact the VastDB support team.

--- 

*This driver is compatible with the ADBC interface, and thus integrates seamlessly into existing ADBC workflows, with noted exceptions.*

```


## FILE: vss-blueprint video-backend vastdb_service.py (excerpt 1)
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/retrieval/video-backend/src/services/vastdb_service.py

```
    """Service for VastDB vector operations with permission filtering"""
    
    def __init__(self):
        self.settings = settings
        self.client = None
        self._adbc_connection = None
        self._connect()
        self._setup_adbc()
    
    def _connect(self):
        """Initialize VastDB connection"""
        try:
            self.client = vastdb.connect(
                endpoint=self.settings.vdb_endpoint,
                access=self.settings.vdb_access_key,
                secret=self.settings.vdb_secret_key,
                ssl_verify=False
            )
            logger.info("VastDB connection established")
        except Exception as e:
            logger.error(f"Failed to connect to VastDB: {e}")
            raise
    
    def _setup_adbc(self):
        """Set up ADBC connection for native VastDB vector search"""
        if not ADBC_AVAILABLE:
            logger.error("ADBC driver manager not available")
            return
        
        try:
            logger.info(f"Setting up ADBC connection to VastDB at {self.settings.vdb_endpoint}")
            
            # Check for driver in embedded location (from Docker image), then fallback to /tmp
            driver_paths = [
                "/opt/adbc-driver/libadbc_driver_vastdb.so",  # Embedded in Docker image
                "/tmp/libadbc_driver_vastdb.so"  # Fallback location
            ]
            
            driver_path = None
            for path in driver_paths:
                if os.path.exists(path):
                    driver_path = path
                    logger.info(f"Found VastDB ADBC driver at {driver_path}")
                    break
            
            # If not found, try to download from artifactory (fallback)
            if not driver_path:
                driver_path = "/tmp/libadbc_driver_vastdb.so"
                driver_url = "https://artifactory.vastdata.com/files/vastdb-native-client/1955131/libadbc_driver_vastdb.so"
                logger.warning(f"Driver not found in image, downloading from {driver_url}")
                urllib.request.urlretrieve(driver_url, driver_path)
                # Make executable
                os.chmod(driver_path, 0o755)
                logger.info(f"VastDB ADBC driver downloaded to {driver_path}")
            
            # Store connection parameters for ADBC
            self._adbc_connection = {
                "driver_path": driver_path,
                "endpoint": self.settings.vdb_endpoint,
                "access_key": self.settings.vdb_access_key,
                "secret_key": self.settings.vdb_secret_key,
                "bucket": self.settings.vdb_bucket,
                "schema": self.settings.vdb_schema
            }
            logger.info("ADBC connection parameters configured")
            
        except Exception as e:
            logger.error(f"Failed to setup ADBC: {e}")
            self._adbc_connection = None
    
    def similarity_search(
        self,
        query_embedding: List[float],
        top_k: int,
        user: User,
        tags: List[str] = None,

```


## FILE: vss-blueprint video-backend vastdb_service.py (excerpt 2)
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/retrieval/video-backend/src/services/vastdb_service.py

```
            return merged, text_ms + visual_ms, max(text_perm, visual_perm), formatted_sql

        if mode == "visual":
            if query_visual_embedding is not None:
                query_embedding = query_visual_embedding
            elif not query_embedding:
                raise ValueError("query_embedding is required for visual search")
            vector_column = "vectors_visual"
        else:
            vector_column = "vectors"
        
        try:
            # Build SQL query with vector similarity
            # Fetch more results than needed to account for permission filtering
            fetch_count = min(top_k * 3, 100)  # Fetch 3x to ensure enough after filtering
            
            # Use ADBC for vector similarity search
            if not self._adbc_connection:
                raise RuntimeError("ADBC not configured - cannot perform vector similarity search")
            
            # Build SQL query using array_cosine_distance function (better for normalized embeddings)
            table_path = f'"{self._adbc_connection["bucket"]}/{self._adbc_connection["schema"]}"."{self.settings.vdb_collection}"'
            dimension = len(query_embedding)
            
            sql_query = f"""
                SELECT 
                    filename,
                    source,
                    reasoning_content,
                    allowed_users,
                    is_public,
                    upload_timestamp,
                    duration,
                    segment_number,
                    total_segments,
                    segment_start_sec,
                    segment_end_sec,
                    original_video,
                    tags,
                    cosmos_model,
                    tokens_used,
                    cached_prompt_tokens,
                    camera_id,
                    capture_type,
                    location,
                    perception_json,
                    object_classes,
                    object_counts,
                    max_detection_conf,
                    perception_ok,
                    array_cosine_distance({vector_column}::FLOAT[{dimension}], ARRAY{query_embedding}::FLOAT[{dimension}]) as distance
                FROM {table_path}
            """
            
            # Build WHERE clause conditions
            where_conditions = []
            
            # Add tag filter if provided
            if tags:
                tags_str = ", ".join([f"'{tag}'" for tag in tags])
                where_conditions.append(f"tags && ARRAY[{tags_str}]")

```


## FILE: vss-blueprint video-backend vastdb_service.py (excerpt 3)
Source: https://github.com/vast-data/vss-blueprint/blob/main/source-code/retrieval/video-backend/src/services/vastdb_service.py

```
            formatted_sql = self._format_sql_for_display(formatted_sql)
            
            # Execute query using ADBC
            with adbc_driver_manager.dbapi.connect(
                driver=self._adbc_connection["driver_path"],
                db_kwargs={
                    "vast.db.endpoint": self._adbc_connection["endpoint"],
                    "vast.db.access_key": self._adbc_connection["access_key"],
                    "vast.db.secret_key": self._adbc_connection["secret_key"]
                }
            ) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql_query)
                    arrow_table = cursor.fetch_arrow_table()
            
            df = arrow_table.to_pandas()
            
            search_time_ms = (time.time() - start_time) * 1000
            
            if df.empty:
                return [], search_time_ms, 0, formatted_sql

```


## FILE: vastdb_sdk/vastdb/_adbc.py
Source: https://github.com/vast-data/vastdb_sdk/blob/main/vastdb/_adbc.py

```
import logging
from typing import Optional

import pyarrow as pa
import sqlglot
from adbc_driver_manager.dbapi import Connection, Cursor, connect
from sqlglot import exp

from vastdb._internal import VectorIndex
from vastdb._table_interface import IbisPredicate
from vastdb.table_metadata import TableRef

log = logging.getLogger(__name__)


TXID_OVERRIDE_PROPERTY: str = "vast.db.external_txid"
END_USER_PROPERTY: str = "vast.db.end_user"
VAST_DIST_ALIAS = "vast_pysdk_vector_dist"
DEFAULT_ADBC_DRIVER_CACHE_DIR: str = "~/.vast/adbc_drivers_cache"
DEFAULT_ADBC_DRIVER_CACHE_BY_URL_DIR: str = f"{DEFAULT_ADBC_DRIVER_CACHE_DIR}/by_url"


def _get_adbc_connection(
    adbc_driver_path: str,
    endpoint: str,
    access_key: str,
    secret_key: str,
    txid: int,
    end_user: Optional[str],
) -> Connection:
    """Get an adbc connection in transaction."""
    conn_kwargs = {TXID_OVERRIDE_PROPERTY: str(txid)}
    if end_user is not None:
        conn_kwargs[END_USER_PROPERTY] = end_user

    return connect(
        driver=adbc_driver_path,
        db_kwargs={
            "vast.db.endpoint": endpoint,
            "vast.db.access_key": access_key,
            "vast.db.secret_key": secret_key,
        },
        conn_kwargs=conn_kwargs,
    )


def _remove_table_qualification_from_columns(expression: exp.Expression):
    """Goes over all columns which are fully qualified with "t0" table reference (ibis default table qualification for unbound tables.

    Note: use only if one table is involved - if two tables exist in the expression columns might become ambiguous.
    """
    for col in expression.find_all(exp.Column):
        col.set("table", None)
    return expression


def _ibis_to_qe_predicates(predicate: IbisPredicate) -> str:
    ibis_sql = predicate.to_sql()
    parsed = sqlglot.parse_one(ibis_sql)

    # currently there is a single table
    # removing the
    without_table_qualification = _remove_table_qualification_from_columns(
        parsed.expressions[0].this
    )

    return without_table_qualification.sql()


def _vector_search_sql(
    query_vector: list[float],
    vector_index: VectorIndex,
    table_ref: TableRef,
    columns: list[str],
    limit: int,
    predicate: Optional[IbisPredicate] = None,
) -> str:
    query_vector_dim = len(query_vector)

    query_vector_literal = f"{query_vector}::FLOAT[{query_vector_dim}]"
    dist_func = f"{vector_index.sql_distance_function}({vector_index.column}::FLOAT[{query_vector_dim}], {query_vector_literal})"
    dist_alias = f"{dist_func} as {VAST_DIST_ALIAS}"

    projection_str = ",".join(columns + [dist_alias])

    if predicate is not None:
        where = f"WHERE {_ibis_to_qe_predicates(predicate)}"
    else:
        where = ""

    return f"""
            SELECT {projection_str}
            FROM {table_ref.query_engine_full_path}
            {where}
            ORDER BY {VAST_DIST_ALIAS}
            LIMIT {limit}"""


class AdbcDriverVastdbNotInstalledException(Exception):
    pass


class AdbcConnection:
    def __init__(
        self,
        endpoint: str,
        access_key: str,
        secret_key: str,
        txid: int,
        end_user: Optional[str] = None,
        adbc_driver_path: Optional[str] = None
    ):
        if adbc_driver_path is None:
            try:
                import adbc_driver_vastdb
            except ImportError as e:
                raise AdbcDriverVastdbNotInstalledException(
                    "The ADBC driver is required for this feature. "
                    "Please install it using: pip install 'vastdb[adbc]' or supply a path explicitly."
                ) from e

            adbc_driver_path = adbc_driver_vastdb.get_driver_path()

        assert isinstance(adbc_driver_path, str)
        self._adbc_conn = _get_adbc_connection(adbc_driver_path, endpoint, access_key, secret_key, txid, end_user)

        self._cursor = self._adbc_conn.cursor()

    @property
    def cursor(self) -> Cursor:
        return self._cursor

    def close(self):
        self._cursor.close()

    def vector_search(
        self,
        query_vector: list[float],
        vector_index: VectorIndex,
        table_ref: TableRef,
        columns: list[str],
        limit: int,
        predicate: Optional[IbisPredicate] = None,
    ) -> pa.RecordBatchReader:
        """Top-n on vector-column."""
        sql = _vector_search_sql(
            query_vector=query_vector,
            vector_index=vector_index,
            table_ref=table_ref,
            columns=columns,
            limit=limit,
            predicate=predicate,
        )

        self._cursor.execute(sql)
        return self._cursor.fetch_record_batch()

```


## FILE: vastdb_sdk/vastdb/tests/test_vector_search.py
Source: https://github.com/vast-data/vastdb_sdk/blob/main/vastdb/tests/test_vector_search.py

```
from collections import defaultdict

import numpy as np
import pyarrow as pa
import pytest

from vastdb import errors
from vastdb._adbc import _ibis_to_qe_predicates
from vastdb._internal import VectorIndex, VectorIndexSpec
from vastdb._table_interface import IbisPredicate
from vastdb.table_metadata import TableMetadata, TableRef, TableType

DIM = 8
TEST_DISTANCE_FUNC = 'array_distance'
TEST_DISTANCE_METRIC = 'l2sq'

VectorColumnArrowType = pa.list_(
    pa.field(name='item', type=pa.float32(), nullable=False), DIM)

query_vector: np.ndarray = np.ones(DIM)
first_closest_vector = (query_vector * 1.1).tolist()
second_closest_vector = (query_vector * 1.2).tolist()
third_closest_vector = (query_vector * 1.3).tolist()
fourth_closest_vector = (query_vector * 1.4).tolist()
fifth_closest_vector = (query_vector * 1.5).tolist()
furthest_vector = (np.ones(DIM) * 5).tolist()

vector_column_name = 'vector_col'

data = [
    {
        "id": 0,
        "n1": 1,
        "n2": 100,
        vector_column_name: first_closest_vector,
    },
    {
        "id": 1,
        "n1": 2,
        "n2": 100,
        vector_column_name: second_closest_vector,
    },
    {
        "id": 2,
        "n1": 3,
        "n2": 200,
        vector_column_name: third_closest_vector,
    },
    {
        "id": 3,
        "n1": 4,
        "n2": 200,
        vector_column_name: fourth_closest_vector,
    },
    {
        "id": 4,
        "n1": 5,
        "n2": 200,
        vector_column_name: fifth_closest_vector,
    },
    {
        "id": 5,
        "n1": 6,
        "n2": 200,
        vector_column_name: furthest_vector,
    },

]


def into_arrow_arrays(data: list[dict]) -> list[list]:
    agg = defaultdict(list)
    for d in data:
        for k, v in d.items():
            agg[k].append(v)

    return [v for v in agg.values()]


def test_sanity(session, clean_bucket_name: str):
    arrow_schema = pa.schema([('id', pa.int32()), ('n1', pa.int32(
    )), ('n2', pa.int32()), (vector_column_name, VectorColumnArrowType),])

    limit = 3

    ref = TableRef(clean_bucket_name, 's', 't')
    table_md = TableMetadata(ref,
                             arrow_schema,
                             TableType.Regular,
                             vector_index=VectorIndex(vector_column_name,
                                                      TEST_DISTANCE_METRIC,
                                                      TEST_DISTANCE_FUNC))
    data_table = pa.table(schema=arrow_schema, data=into_arrow_arrays(data))

    with session.transaction() as tx:
        table = tx.bucket(clean_bucket_name).create_schema(
            's').create_table('t', arrow_schema)
        table.insert(data_table)

    # TODO merge in same tx
    with session.transaction() as tx:
        table = tx.table_from_metadata(table_md)

        reader = table.vector_search(vec=query_vector.tolist(),
                                     columns=['id', 'n1', 'n2'],
                                     limit=limit)

        result_table = reader.read_all()

        assert set([v.as_py() for v in result_table['n1']]) == {1, 2, 3}


def test_with_predicates(session, clean_bucket_name: str):
    vector_column_name = 'vector_column'
    arrow_schema = pa.schema([('id', pa.int32()), ('n1', pa.int32(
    )), ('n2', pa.int32()), (vector_column_name, VectorColumnArrowType),])
    limit = 3

    ref = TableRef(clean_bucket_name, 's', 't')
    table_md = TableMetadata(ref, arrow_schema, TableType.Regular,
                             vector_index=VectorIndex(vector_column_name,
                                                      TEST_DISTANCE_METRIC,
                                                      TEST_DISTANCE_FUNC))
    data_table = pa.table(schema=arrow_schema, data=into_arrow_arrays(data))

    with session.transaction() as tx:
        table = tx.bucket(clean_bucket_name).create_schema(
            's').create_table('t', arrow_schema)
        table.insert(data_table)

    with session.transaction() as tx:
        table = tx.table_from_metadata(table_md)

        pred = table_md.ibis_table['n2'] == 200
        reader = table.vector_search(vec=query_vector.tolist(),
                                     columns=['id', 'n1', 'n2'],
                                     limit=limit,
                                     predicate=pred)

        result_table = reader.read_all()

        assert set([v.as_py() for v in result_table['n1']]) == {3, 4, 5}


arrow_schema = pa.schema([('id', pa.int32()), ('n1', pa.int32(
)), ('n2', pa.int32()), (vector_column_name, VectorColumnArrowType),])

ref = TableRef('b', 's', 't')
table_md = TableMetadata(ref, arrow_schema, TableType.Regular)


@pytest.mark.parametrize('ibis_predicate, expected', [
    ((table_md.ibis_table['n1'] == 1) & (table_md.ibis_table['n2'] == 2),
     '("n1" = 1) AND ("n2" = 2)'),
    ((table_md.ibis_table['n1'] == 1),
     '"n1" = 1')
])
def test_ibis_to_query_engine_predicates(ibis_predicate: IbisPredicate, expected: str):
    assert _ibis_to_qe_predicates(ibis_predicate) == expected


def test_with_predicates_get_vector_index_properties_from_server(session,
                                                                 clean_bucket_name: str):
    try:
        session.features.check_vector()
    except errors.NotSupportedVersion:
        pytest.skip("Vector index is not supported on this vast server version")

    vector_column_name = 'vector_column'
    vector_index_distance_metric = 'l2sq'
    vector_index_sql_distance_function = "array_distance"

    arrow_schema = pa.schema([('id', pa.int32()), ('n1', pa.int32(
    )), ('n2', pa.int32()), (vector_column_name, VectorColumnArrowType),])
    limit = 3

    ref = TableRef(clean_bucket_name, 's', 't')
    table_md = TableMetadata(ref, arrow_schema, TableType.Regular)
    data_table = pa.table(schema=arrow_schema, data=into_arrow_arrays(data))

    with session.transaction() as tx:
        table = (tx.bucket(clean_bucket_name)
                 .create_schema('s')
                 .create_table('t',
                               arrow_schema,
                               vector_index=VectorIndexSpec(vector_column_name,
                                                            vector_index_distance_metric)))
        table.insert(data_table)

    with session.transaction() as tx:
        table = tx.table_from_metadata(table_md)

        table.reload_stats()
        assert table.vector_index == VectorIndex(
            column=vector_column_name,
            distance_metric=vector_index_distance_metric,
            sql_distance_function=vector_index_sql_distance_function)

        pred = table_md.ibis_table['n2'] == 200
        reader = table.vector_search(vec=query_vector.tolist(),
                                     columns=['id', 'n1', 'n2'],
                                     limit=limit,
                                     predicate=pred)

        result_table = reader.read_all()

        assert set([v.as_py() for v in result_table['n1']]) == {3, 4, 5}

```


## FILE: vastdb_sdk/vastdb/tests/test_vector_index.py
Source: https://github.com/vast-data/vastdb_sdk/blob/main/vastdb/tests/test_vector_index.py

```
"""Tests for vector index functionality."""

import logging
from typing import Optional

import pyarrow as pa
import pytest

from vastdb import errors
from vastdb._internal import VectorIndexSpec
from vastdb.session import Session

log = logging.getLogger(__name__)


@pytest.mark.parametrize("table_name,vector_index", [
    # Test 1: Table without vector index
    ("table_without_index", None),
    # Test 2: Table with L2 vector index
    ("table_with_l2_index", VectorIndexSpec("embedding", "l2sq")),
    # Test 3: Table with inner product vector index
    ("table_with_ip_index", VectorIndexSpec("embedding", "ip")),
])
def test_create_table_with_vector_index_metadata(session: Session,
                                                 clean_bucket_name: str,
                                                 table_name: str,
                                                 vector_index: Optional[VectorIndexSpec]):
    if vector_index is not None:
        try:
            session.features.check_vector()
        except errors.NotSupportedVersion:
            pytest.skip("Vector index is not supported on this vast server version")
    """Test that table creation and stats retrieval work correctly with vector index metadata."""
    schema_name = "schema1"

    with session.transaction() as tx:
        log.info(f"Testing table '{table_name}' with {vector_index}")

        # Create schema
        bucket = tx.bucket(clean_bucket_name)
        schema = bucket.create_schema(schema_name)

        # Create the appropriate schema based on whether vector index is needed
        if vector_index is None:
            # Simple table without vector index
            arrow_schema = pa.schema([
                ('id', pa.int64()),
                ('data', pa.string())
            ])
        else:
            # Table with vector column
            vector_dimension = 128  # Fixed-size vector dimension
            vec_type = pa.list_(pa.field('', pa.float32(), False), vector_dimension)
            arrow_schema = pa.schema([
                ('id', pa.int64()),
                ('embedding', vec_type)  # Fixed-size vector column
            ])

        # Create table with or without vector index
        log.info(f"Creating table: {table_name}")
        table = schema.create_table(
            table_name=table_name,
            columns=arrow_schema,
            vector_index=vector_index
        )

        # Reload stats to ensure we get the vector index metadata
        table.reload_stats()

        # Get vector index metadata
        result_vector_index = table._metadata._vector_index

        log.info(f"Vector index metadata: {result_vector_index}")

        # Assert expected values (should match input parameters)
        result_vector_index_spec = (
            None
            if result_vector_index is None
            else result_vector_index.to_vector_index_spec()
        )
        assert result_vector_index_spec == vector_index

        log.info(f"✓ Test passed for table '{table_name}'")


@pytest.mark.parametrize("table_name,vector_index,expected_error", [
    # Test 1: Invalid column name (column doesn't exist in schema)
    ("table_invalid_column", VectorIndexSpec("nonexistent_column", "l2sq"), "invalid vector indexed column name nonexistent_column"),
    # Test 2: Invalid distance metric
    ("table_invalid_metric", VectorIndexSpec("embedding", "invalid_metric"), "invalid vector index distance metric invalid_metric, supported metrics: 'l2sq', 'ip'"),
])
def test_create_table_with_invalid_vector_index(session: Session,
                                                clean_bucket_name: str,
                                                table_name: str,
                                                vector_index: VectorIndexSpec,
                                                expected_error: str):
    """Test that table creation fails with appropriate error messages for invalid vector index parameters."""
    if vector_index is not None:
        try:
            session.features.check_vector()
        except errors.NotSupportedVersion:
            pytest.skip("Vector index is not supported on this vast server version")
    schema_name = "schema1"

    with session.transaction() as tx:
        log.info(f"Testing invalid table '{table_name}' with vector_index={vector_index}, expected_error={expected_error}")

        # Create schema
        bucket = tx.bucket(clean_bucket_name)
        schema = bucket.create_schema(schema_name)

        # Table with vector column
        vector_dimension = 128  # Fixed-size vector dimension
        vec_type = pa.list_(pa.field('', pa.float32(), False), vector_dimension)
        arrow_schema = pa.schema([
            ('id', pa.int64()),
            ('embedding', vec_type)  # Fixed-size vector column
        ])

        # Attempt to create table with invalid parameters - should raise an error
        log.info(f"Attempting to create invalid table: {table_name}")
        with pytest.raises((errors.BadRequest)) as exc_info:
            schema.create_table(
                table_name=table_name,
                columns=arrow_schema,
                vector_index=vector_index
            )

        # Verify the error message contains the expected error text
        assert expected_error in str(exc_info.value), \
            f"Expected error message to contain '{expected_error}', got '{str(exc_info.value)}'"

        log.info(f"✓ Test passed for invalid table '{table_name}'")


def test_vector_index_metadata_from_stats(session: Session, clean_bucket_name: str):
    """Test that vector index metadata is correctly retrieved from table stats."""
    try:
        session.features.check_vector()
    except errors.NotSupportedVersion:
        pytest.skip("Vector index is not supported on this vast server version")

    schema_name = "schema1"
    table_name = "vector_table"

    with session.transaction() as tx:
        # Create schema
        bucket = tx.bucket(clean_bucket_name)
        schema = bucket.create_schema(schema_name)

        # Create table with vector index
        vector_dimension = 128
        vec_type = pa.list_(pa.field('', pa.float32(), False), vector_dimension)
        arrow_schema = pa.schema([
            ('id', pa.int64()),
            ('embedding', vec_type)
        ])

        table = schema.create_table(
            table_name=table_name,
            columns=arrow_schema,
            vector_index=VectorIndexSpec("embedding", "l2sq")
        )

        # Check stats object directly
        stats = table.stats
        assert stats is not None
        assert stats.vector_index is not None
        assert stats.vector_index.column == "embedding"
        assert stats.vector_index.distance_metric == "l2sq"

        # Check via the table methods
        assert table._metadata._vector_index is not None
        assert table._metadata._vector_index.column == "embedding"
        assert table._metadata._vector_index.distance_metric == "l2sq"

        log.info("✓ Vector index metadata correctly retrieved from stats")

```


## FILE: vast-vector-store/README.md
Source: https://github.com/vast-data/vast-vector-store/blob/main/README.md

```
# langchain-vastdb

LangChain VectorStore integration for [VAST Database](https://vastdata.com/).

`langchain-vastdb` provides a `VastDBVectorStore` class that implements the
LangChain `VectorStore` interface, enabling similarity search, document storage,
and retrieval-augmented generation (RAG) workflows backed by VAST Database's
native vector indexing.

**Compatibility:** Python 3.10 - 3.13 | langchain-core >= 1.0, < 2 | vastdb >= 2.0.3 | Query Engine paths require VAST 5.4+

**Status:** Alpha (v0.0.1). API may change between minor releases.

**License:** Apache-2.0

## Requirements

- Python 3.10+
- A running VAST Database cluster. The store reads the cluster version from
  the SDK session and picks paths per operation:

  | VAST | search | `get_by_ids` | delete | notes |
  |---|---|---|---|---|
  | 5.3 | SDK in-memory scan (`VASTDB_ALLOW_FALLBACK=1` required) | SDK | SDK | no Query Engine |
  | 5.4 | Query Engine, brute force | Query Engine | SDK | not live-tested; Query Engine DML unverified |
  | 5.5 | Query Engine, vector index when built | Query Engine | Query Engine | verified on 5.5.1 |

  Configuring ADBC on a 5.3 cluster is harmless: lookup and delete stay on the SDK.
- `vastdb` SDK >= 2.0.3
- `langchain-core` >= 1.0, < 2
- An `Embeddings` model (e.g., OpenAI, HuggingFace, or any LangChain-compatible embeddings)

## Installation

```bash
pip install langchain-vastdb
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add langchain-vastdb
```

## Quickstart

### Option 1: Pass a pre-built session

```python
import vastdb
from langchain_vastdb import VastDBVectorStore

session = vastdb.connect(
    endpoint="http://vast-cluster:8070",
    access="YOUR_ACCESS_KEY",
    secret="YOUR_SECRET_KEY",
)

store = VastDBVectorStore(
    embedding=my_embeddings,
    session=session,
    bucket="my-bucket",
    schema="my-schema",
    table_name="my-table",
)

# Add documents and search
ids = store.add_texts(["Paris is the capital of France."])
results = store.similarity_search("capital city", k=1)
print(results[0].page_content)
```

### Option 2: Use the convenience factory

```python
from langchain_vastdb import VastDBVectorStore

store = VastDBVectorStore.from_connection_params(
    embedding=my_embeddings,
    endpoint="http://vast-cluster:8070",
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
    bucket="my-bucket",
    schema="my-schema",
    table_name="my-table",
)
```

Credentials are passed to `vastdb.connect()` for the SDK session. They are also
kept on the instance as private attributes (`_access_key`, `_secret_key`) so the
ADBC Query Engine connection can reuse them; they are never exposed publicly.

### Option 3: Create a store and add texts in one call

```python
import vastdb
from langchain_vastdb import VastDBVectorStore

session = vastdb.connect(
    endpoint="http://vast-cluster:8070",
    access="YOUR_ACCESS_KEY",
    secret="YOUR_SECRET_KEY",
)

store = VastDBVectorStore.from_texts(
    texts=["Paris is the capital of France.", "Berlin is the capital of Germany."],
    embedding=my_embeddings,
    session=session,
    bucket="my-bucket",
    schema="my-schema",
    table_name="my-table",
)
```

## CRUD Operations

```python
# Add documents with metadata
ids = store.add_texts(
    ["Some text", "More text"],
    metadatas=[{"source": "wiki"}, {"source": "blog"}],
)

# Similarity search by text query
docs = store.similarity_search("capital city", k=2)

# Similarity search with distance scores
scored = store.similarity_search_with_score("capital city", k=2)
for doc, score in scored:
    print(f"{doc.page_content} (distance: {score})")

# Search with a pre-computed vector
docs = store.similarity_search_by_vector([0.1, 0.2, ...], k=2)

# Retrieve documents by ID
docs = store.get_by_ids(ids)

# Delete by ID
store.delete(ids=ids)
```

### Using as a retriever

`VastDBVectorStore` integrates directly with LangChain's retriever interface:

```python
retriever = store.as_retriever(search_kwargs={"k": 3})
docs = retriever.invoke("What is the capital of France?")
```

This works seamlessly in LCEL RAG chains:

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

retriever = store.as_retriever(search_kwargs={"k": 3})
prompt = ChatPromptTemplate.from_template(
    "Answer based on context:\n{context}\n\nQuestion: {question}"
)

def format_docs(docs):
    return "\n".join(d.page_content for d in docs)

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm  # any LangChain-compatible LLM
    | StrOutputParser()
)
answer = chain.invoke("What is the capital of France?")
```

### Cache management

`VastDBVectorStore` caches table metadata after the first access to avoid
repeated bucket/schema/table round trips. If you alter the table structure
externally, invalidate the cache:

```python
store.invalidate_table_cache()
```

## Configuration Reference

### Constructor: `VastDBVectorStore(...)`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `embedding` | `Embeddings` | *required* | The embeddings model used to generate vectors. |
| `session` | `vastdb.Session` | *required* | A pre-built session connected to the VAST cluster. |
| `bucket` | `str` | *required* | The VAST bucket name containing the target table. |
| `schema` | `str` | *required* | The schema name within the bucket. |
| `table_name` | `str` | *required* | The table name for vector operations. |
| `id_column` | `str` | `"id"` | Column name for document IDs. |
| `text_column` | `str` | `"text"` | Column name for document text. |
| `vector_column` | `str` | `"vector"` | Column name for embedding vectors. |
| `metadata_column` | `str` | `"metadata"` | Column name for document metadata (stored as JSON). |
| `adbc_driver_path` | `str \| None` | `None` | Path to `libadbc_driver_vastdb.so`. Enables Query Engine search, lookup and delete. |
| `adbc_endpoint` | `str \| None` | `None` | Full Query Engine URL (e.g. `http://host:80`), separate from the SDK endpoint. |
| `access_key` | `str \| None` | `None` | Access key for ADBC connection. |
| `secret_key` | `str \| None` | `None` | Secret key for ADBC connection. |

### Custom column names

Column names default to `id`, `text`, `vector`, and `metadata`. Override them at
construction time:

```python
store = VastDBVectorStore(
    embedding=my_embeddings,
    session=session,
    bucket="my-bucket",
    schema="my-schema",
    table_name="my-table",
    id_column="doc_id",
    text_column="content",
    vector_column="emb",
    metadata_column="meta",
)
```

### Factory classmethod: `from_connection_params(...)`

Creates a `VastDBVectorStore` by building a `vastdb.Session` internally from
connection parameters.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `embedding` | `Embeddings` | *required* | The embeddings model. |
| `endpoint` | `str` | *required* | The VAST cluster HTTP endpoint URL. |
| `access_key` | `str` | *required* | Access key for authentication. |
| `secret_key` | `str` | *required* | Secret key for authentication. |
| `bucket` | `str` | *required* | The VAST bucket name. |
| `schema` | `str` | *required* | The schema name within the bucket. |
| `table_name` | `str` | *required* | The table name for vector operations. |
| `adbc_driver_path` | `str \| None` | `None` | Path to ADBC driver shared library. |
| `adbc_endpoint` | `str \| None` | `None` | ADBC/QueryEngine endpoint. |
| `**kwargs` | | | Additional keyword arguments forwarded to the constructor (e.g., custom column names). |

### ADBC Query Engine operations

With the ADBC driver, endpoint and credentials configured, vector search fetches
ranked documents in one Query Engine SQL query. `get_by_ids` and delete also
use the Query Engine; upsert joins the SQL delete and SDK Arrow insert in one
transaction. Insertion remains SDK Arrow. A vector index is optional: without
one (or on VAST 5.4) the Query Engine brute-forces the distance; with one, the
distance function comes from the index metadata (`array_distance` for l2sq,
`array_inner_product` for ip). A freshly created indexed table may brute-force
until the index is built. See the version table under Requirements for which
operations use the Query Engine on 5.3, 5.4 and 5.5. Without ADBC, lookup and
delete retain their SDK paths. With `VASTDB_ALLOW_FALLBACK=1`, search, lookup
and delete all fall back to the SDK on ADBC errors; otherwise errors propagate.

Unfiltered `count()` uses cached table stats, which may lag recent writes or
over-count while a table settles. Use `count(predicate)` for an exact count;
it scans matching IDs rather than using Query Engine `COUNT(*)`.

```python
store = VastDBVectorStore(
    embedding=my_embeddings,
    session=session,
    bucket="my-bucket",
    schema="my-schema",
    table_name="my-table",
    adbc_driver_path="/usr/lib/libadbc_driver_vastdb.so",
    adbc_endpoint="http://query-engine.example.com:80",
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
)
```

## Subclassing Guide

`VastDBVectorStore` uses the **Template Method** pattern. Public methods like
`add_texts` and `similarity_search` handle embedding, filter conversion, and
result formatting, then delegate storage operations to five protected hook
methods. Override these hooks to customize behavior without reimplementing the
full LangChain interface.

### Hook methods

| Hook | Purpose | Returns |
|------|---------|---------|
| `_insert_vectors` | Customize record insertion | `list[str]` (IDs) |
| `_build_metadata_columns` | Customize column layout for metadata | `dict[str, list]` |
| `_select_columns` / `_typed_metadata_columns` | Customize document columns projected during search and lookup | `list[str]` / mapping |
| `_vector_search` | Customize similarity search | `list[tuple[dict, float]]` |
| `_delete_by_ids` | Customize document deletion | `bool` |
| `_get_by_ids` | Customize ID lookup (not used by ADBC search) | `list[dict]` |
| `_row_to_document` | Customize row-to-Document conversion | `Document` |

### Hook signatures

```python
def _insert_vectors(
    self,
    texts: list[str],
    embeddings: list[list[float]],
    metadatas: list[dict],
    ids: list[str],
    *,
    tx: Transaction | None = None,
) -> list[str]: ...

def _vector_search(
    self,
    query_vector: list[float],
    k: int,
    predicate: ibis.Expr | None = None,
    *,
    tx: Transaction | None = None,
    **kwargs: Any,
) -> list[tuple[dict, float]]: ...

def _delete_by_ids(
    self,
    ids: list[str],
    *,
    tx: Transaction | None = None,
) -> bool: ...

def _get_by_ids(
    self,
    ids: list[str],
    *,
    tx: Transaction | None = None,
) -> list[dict]: ...

def _row_to_document(
    self,
    row: dict,
    score: float | None = None,
) -> Document: ...
```

Override `_open_adbc_connection(self, **kwargs)` with `**kwargs` even if your
subclass currently ignores them: joined operations pass
`adbc_conn_kwargs_overrides={"vast.db.external_txid": str(tx.txid)}`.

### Transaction reuse

Write hooks open a transaction by default. The optional `tx` parameter lets
subclasses pass in an existing transaction for multi-step atomic operations
(ADBC delete joins it):

```python
with self._session.transaction() as tx:
    self._insert_vectors(texts, embeddings, metadatas, ids, tx=tx)
    # additional operations in the same transaction
```

### Example: typed metadata columns

The base class stores metadata as a single JSON string column. If you need typed
columns for performance-critical filtering, set `_typed_metadata_columns`:

```python
from langchain_vastdb import TypedColumn, VastDBVectorStore


class TypedMetadataStore(VastDBVectorStore):
    """Store with typed 'category' and 'priority' metadata columns."""

    _typed_metadata_columns = {
        "category": TypedColumn(),
        "priority": TypedColumn(),
    }
```

This automatically extracts `category` and `priority` into separate typed columns
on insert, preserves any extra metadata in the JSON column, and merges everything
back together on read. The public LangChain interface (`add_texts`,
`similarity_search`, etc.) stays unchanged.

Use `TypedColumn` fields for custom defaults, PyArrow type coercion, or
controlling which columns are backfilled on read
(see the [Migration Guide](docs/migration-guide.md) for details).

## Examples

See the [`examples/`](examples/) directory for runnable scripts:

- `basic_usage.py` -- add texts, search, retrieve
- `rag_pipeline.py` -- `as_retriever()` + LCEL RAG chain
- `subclassing.py` -- declarative typed metadata columns
- `filtered_search.py` -- metadata filtering patterns

## Migration Guide

Migrating an existing `VectorStore` subclass to `VastDBVectorStore`? See the
[Migration Guide](docs/migration-guide.md) for step-by-step instructions,
a hook mapping table, and a before/after code comparison.

## Development

Clone the repository and install dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Run the linter:

```bash
uv run ruff check .
```

Run unit tests:

```bash
uv run pytest tests/unit_tests/
```

Run integration tests (requires a VAST cluster):

```bash
uv run pytest tests/integration_tests/
```

## License

Apache-2.0 -- see [LICENSE](LICENSE) for details.
test sync

```
