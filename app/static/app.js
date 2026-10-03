// PERJURY courtroom UI (FINAL-IDEA-v3 §9). Vanilla JS, no build step.
// Every URL is relative (api/testify, with no leading slash): the Ingress serves this page at /app/ and strips /app.
"use strict";

// ------------------------------------------------------------------ constants
const LANES = [
  ["DATA", [["s3", "S3"], ["dataengine", "DataEngine"], ["vastdb", "VastDB"], ["vss", "VSS"]]],
  ["MODELS", [["cosmos3", "Cosmos3"], ["embed1", "Embed1"], ["yolo", "YOLO"], ["canary", "Canary"]]],
  ["AGENT", [["wandb_inference", "W&B Inference"], ["weave", "Weave"]]],
  ["PLATFORM", [["coreweave", "CoreWeave"], ["cursor", "Cursor"], ["k8s", "K8s"]]],
];
const SVC = {};
LANES.forEach(([lane, items]) => items.forEach(([id, name]) => { SVC[id] = { lane, name }; }));
const BADGES = new Set(["coreweave", "cursor"]);
const GPU_SVCS = new Set(["cosmos3", "embed1", "yolo", "canary"]);
const TIER_BADGE = { JURY: "COSMOS", RECORDS: "YOLO", CAPTIONS: "CAP" };
const SLOT_ROWS = [1, 2, 3, 4, 5, 6];
const POLES = [1, 2, 3];
const COND = {
  road: { A: "dry", B: "wet", C: "snow", D: "?" },
  traffic: { A: "free-flow", B: "slow", C: "stop-and-go", D: "?" },
  light: { A: "day", B: "dusk", C: "night", D: "?" },
};

// ------------------------------------------------------------------ helpers
const $ = (s, root) => (root || document).querySelector(s);
const $$ = (s, root) => Array.from((root || document).querySelectorAll(s));
const esc = (v) => String(v == null ? "" : v).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const fmtMs = (ms) => (ms == null ? "" : ms >= 1000 ? (ms / 1000).toFixed(ms >= 10000 ? 0 : 1) + " s" : Math.round(ms) + " ms");
const pct = (x) => (x == null || isNaN(x) ? "–" : Math.round(x * 100) + "%");
const hhmm = (iso) => { try { const d = new Date(iso); return isNaN(d) ? "--:--" : d.toTimeString().slice(0, 5); } catch (e) { return "--:--"; } };
const qs = (o) => Object.entries(o).map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`).join("&");
const json = (v) => esc(JSON.stringify(v, null, 2));

let toastTimer = null;
function toast(msg, kind) {
  const t = $("#toast");
  t.textContent = msg;
  t.className = "toast" + (kind ? " " + kind : "");
  t.hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { t.hidden = true; }, kind === "info" ? 3500 : 7000);
}

async function getJSON(url, opts) {
  const res = await fetch(url, opts);
  let body = null;
  try { body = await res.json(); } catch (e) { body = null; }
  if (!res.ok) {
    const d = body && body.detail;
    throw new Error(Array.isArray(d) ? d.map((x) => x.msg).join("; ") : d || `${res.status} ${res.statusText}`);
  }
  return body;
}

// ------------------------------------------------------------------ state
const S = {
  health: {},
  scene: 2,
  scenes: {},
  run: null,
  ctrl: null,
  busy: false,
  replay: null,       // {name, recorded_at} while showing a replay
  chips: {},
  rec: null,
  micStream: null,
  tab: "courtroom",
  live: null,
  editing: false,
  catalog: null, scope: null, catalogLoading: false, catalogRequest: 0, assessmentCamera: null, catalogPlayers: [],
};

function newRun(opts) {
  return {
    id: null, text: opts.text || "", scene: opts.scene || S.scene, source: "typed", heardMs: null,
    atoms: [], A: {}, activeAtom: null, pinned: false, parser: null,
    verdict: null, receipt: null, stock: null, events: [], services: [],
    clientT0: null, done: false, replay: !!opts.replay, mode: S.health.mode,
  };
}

// ------------------------------------------------------------------ boot
document.addEventListener("DOMContentLoaded", boot);

async function boot() {
  buildRibbon();
  bindUI();
  $$(".detail-close").forEach((b) => b.addEventListener("click", () => { b.closest("details").open = false; }));
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") $$(".workspace-detail[open]").forEach((d) => { d.open = false; }); });
  setupMic();
  try {
    S.health = await getJSON("health");
  } catch (e) {
    toast("Server unreachable: " + e.message);
  }
  applyHealth();
  await loadScenes();
  await loadCatalog();
  loadReplays();
  setInterval(tick, 100);
  setInterval(refreshHealth, 15000);
}

async function refreshHealth() {
  try { S.health = await getJSON("health"); applyHealth(); } catch (e) { /* keep last */ }
}

function applyHealth() {
  const h = S.health || {};
  const fixture = h.mode === "fixture";
  const coverage = S.scope ? null : h.coverage;
  const banner = $("#banner-coverage");
  banner.hidden = !coverage || coverage.complete !== false || fixture;
  if (!banner.hidden) {
    const actual = coverage.actual || {};
    const cameras = Object.values(actual.cameras_per_scene || {}).reduce((a, n) => a + Number(n), 0);
    banner.textContent = `RECORDED FOOTAGE · ${(actual.scenes || []).length} scene(s) · ${cameras} cameras · ${actual.segments || 0} segments. Coverage is incomplete; claims requiring a larger jury may return UNPROVEN.`;
  }
  $("#banner-fixture").hidden = !fixture;
  if (fixture) {
    $("#banner-fixture-note").textContent = h.dev_stub ? "DEV STUB (scripted run, pipeline not loaded)" : "no live services were called";
  }
  if (h.pipeline_error && !h.pipeline && !h.dev_stub) {
    $("#wall-foot").textContent = "Pipeline not loaded: " + h.pipeline_error;
  }
  renderChip("k8s");
}

async function loadScenes() {
  const nav = $("#scenes");
  const results = await Promise.all([1, 2, 3].map((n) => getJSON(`api/scene/${n}`).catch((e) => ({ scene: n, error: e.message }))));
  results.forEach((r) => { S.scenes[r.scene] = r; });
  nav.innerHTML = results.map((r) => {
    const available = !r.error && r.cameras?.length > 0;
    const label = available ? `${r.cameras.length} cameras` : "Unavailable";
    return `<button type="button" class="scene-btn" data-scene="${r.scene}" ${available ? "" : "disabled"}><b>Scene ${r.scene}</b> · ${label}</button>`;
  }).join("");
  $$(".scene-btn", nav).forEach((b) => b.addEventListener("click", () => {
    if (S.busy) return toast("A run is in progress; wait for the verdict.", "info");
    selectScene(+b.dataset.scene, { clear: true });
  }));
  const available = results.filter((r) => !r.error && r.cameras?.length > 0);
  const initial = available.find((r) => r.scene === S.scene) || available[0];
  if (initial) selectScene(initial.scene, { clear: true });
}

function selectScene(n, opts) {
  S.scope = null;
  S.scene = n;
  $$(".scene-btn").forEach((b) => b.classList.toggle("on", +b.dataset.scene === n));
  const meta = S.scenes[n] || {};
  $("#scene-context").textContent = [meta.location, "Recorded footage"].filter(Boolean).join(" · ");
  buildWall();
  if (opts && opts.clear) {
    S.run = null;
    resetBoard();
  }
  paintWall();
}

async function loadReplays() {
  const sel = $("#replay");
  try {
    const data = await getJSON("api/replays");
    const list = data.replays || [];
    sel.innerHTML = `<option value="">Replay ▾ ${list.length ? "(" + list.length + ")" : ""}</option>` + list.map((r) => {
      const v = r.verdict ? ` → ${r.verdict}` : "";
      const label = `${r.curated ? "★ " : ""}${hhmm(r.recorded_at)} · S${r.scene || "?"} · ${(r.text || r.name).slice(0, 48)}${v}`;
      return `<option value="${esc(r.name)}" data-at="${esc(r.recorded_at)}">${esc(label)}</option>`;
    }).join("");
  } catch (e) {
    sel.innerHTML = `<option value="">Replay ▾ (none)</option>`;
  }
}

function bindUI() {
  $("#edit-claim").addEventListener("click", () => { S.editing = true; document.body.classList.remove("submitted"); $("#claim").focus(); });
  $("#claim-form").addEventListener("submit", (e) => {
    e.preventDefault();
    testify($("#claim").value, { source: "typed" });
  });
  $("#upload-btn").addEventListener("click", () => $("#upload").click());
  $("#upload").addEventListener("change", async (e) => {
    const f = e.target.files && e.target.files[0];
    e.target.value = "";
    if (f) await handleAudio(f, "upload");
  });
  $("#replay").addEventListener("change", (e) => {
    const opt = e.target.selectedOptions[0];
    const name = e.target.value;
    e.target.value = "";
    if (name) startReplay(name, opt && opt.dataset.at);
  });
  $("#replay").addEventListener("focus", loadReplays);
  $("#replay-exit").addEventListener("click", () => { exitReplay(); S.run = null; resetBoard(); paintWall(); });
  $$(".tab").forEach((b) => b.addEventListener("click", () => showTab(b.dataset.tab)));
  $("#drawer-close").addEventListener("click", closeDrawer);
  $("#drawer").addEventListener("click", (e) => { if (e.target.id === "drawer") closeDrawer(); });
  $("#chip-close").addEventListener("click", () => { $("#chip-modal").hidden = true; });
  $("#chip-modal").addEventListener("click", (e) => { if (e.target.id === "chip-modal") $("#chip-modal").hidden = true; });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") { closeDrawer(); $("#chip-modal").hidden = true; }
  });
  $("#witness-run").addEventListener("click", async () => {
    try { await getJSON("api/witness/run", { method: "POST" }); toast("Witness stand started.", "info"); setTimeout(loadWitness, 1500); }
    catch (e) { toast("Witness run failed: " + e.message); }
  });
}

function showTab(tab) {
  S.tab = tab;
  $$(".tab").forEach((b) => b.classList.toggle("on", b.dataset.tab === tab));
  ["courtroom", "witness", "bench", "log"].forEach((t) => { $("#tab-" + t).hidden = t !== tab; });
  if (tab === "bench") loadBench();
  if (tab === "witness") loadWitness();
  if (tab === "log") renderLog();
}

// ------------------------------------------------------------------ runs + SSE
async function streamSSE(url, opts, onEvent) {
  const res = await fetch(url, opts);
  if (!res.ok) {
    let d = `${res.status}`;
    try { const b = await res.json(); d = Array.isArray(b.detail) ? b.detail.map((x) => x.msg).join("; ") : b.detail || d; } catch (e) { /* not json */ }
    throw new Error(d);
  }
  const reader = res.body.getReader();
  const dec = new TextDecoder();
  let buf = "";
  for (;;) {
    const { value, done } = await reader.read();
    if (done) break;
    buf += dec.decode(value, { stream: true });
    let i;
    while ((i = buf.indexOf("\n\n")) >= 0) {
      const frame = buf.slice(0, i);
      buf = buf.slice(i + 2);
      let name = "message";
      const data = [];
      frame.split("\n").forEach((line) => {
        if (line.startsWith("event:")) name = line.slice(6).trim();
        else if (line.startsWith("data:")) data.push(line.slice(5).trimStart());
      });
      if (!data.length) continue;
      let payload = {};
      try { payload = JSON.parse(data.join("\n")); } catch (e) { continue; }
      onEvent(name, payload);
    }
  }
}

async function runStream(url, opts) {
  if (S.ctrl) S.ctrl.abort();
  const ctrl = new AbortController();
  S.ctrl = ctrl;
  setBusy(true);
  try {
    await streamSSE(url, { ...opts, signal: ctrl.signal }, (name, data) => {
      if (S.ctrl === ctrl) handleEvent(name, data);
    });
  } catch (e) {
    if (e.name !== "AbortError") {
      toast(e.message);
      if (S.run && !S.run.verdict) setStamp("idle", "NO VERDICT");
    }
  } finally {
    if (S.ctrl === ctrl) {
      S.ctrl = null;
      setBusy(false);
      if (S.run) { S.run.done = true; settleDeliberating(); paintWall(); renderTrace(); }
    }
  }
}

function setBusy(b) {
  S.busy = b;
  $("#go").disabled = b;
  $("#go").textContent = b ? "…" : "Testify";
}

async function testify(text, opts) {
  text = (text || "").replace(/\s+/g, " ").trim();
  if (!text) return toast("Type or say a claim first.", "info");
  if (text.length > 500) return toast("Keep testimony under 500 characters.");
  if (S.busy) return toast("Wait for the current assessment to finish.", "info");
  if (S.catalogLoading) return toast("Wait for the selected footage to load.", "info");
  if (S.scope && !S.assessmentCamera) return toast("Choose an assessment camera first.", "info");
  if (S.live && (!S.live.lastReceived || Date.now() - S.live.lastReceived > 30000)) return toast("Live evidence is unavailable or stale. Reconnect the source.");
  S.editing = false;
  exitReplay();
  $("#claim").value = text;
  S.run = newRun({ text, scene: S.scene });
  resetBoard();
  S.run.source = opts.source || "typed";
  renderTestimony();
  setStamp("out", "THE JURY IS OUT");
  if ($("#stock-ab").checked) showStockPending();
  const body = { text, scene: S.scene, stock_ab: $("#stock-ab").checked, transcript_source: opts.source || "typed" };
  if (S.scope) { body.scope_id = S.scope.id; body.camera = S.assessmentCamera; body.scene = 1; body.stock_ab = false; }
  if (opts.transcript_id) body.transcript_id = opts.transcript_id;
  if (S.tab !== "courtroom") showTab("courtroom");
  const endpoint = S.live ? `api/live/${encodeURIComponent(S.live.id)}/testify` : "api/testify";
  await runStream(endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
}

function startReplay(name, at) {
  S.scope = null;
  $("#legacy-scenes").hidden = false;
  buildWall();
  S.replay = { name, recorded_at: at };
  $("#banner-replay").hidden = false;
  $("#replay-when").textContent = hhmm(at);
  $("#replay-name").textContent = name;
  S.run = newRun({ replay: true });
  resetBoard();
  setStamp("out", "THE JURY IS OUT");
  if (S.tab !== "courtroom") showTab("courtroom");
  runStream(`api/replay/${encodeURIComponent(name)}?speed=1`, { method: "GET" });
}

function exitReplay() {
  if (!S.replay) return;
  S.replay = null;
  $("#banner-replay").hidden = true;
}

// ------------------------------------------------------------------ event handling
function handleEvent(name, d) {
  const run = S.run;
  if (!run) return;
  const t = d._t_ms || 0;
  if (run.clientT0 == null) run.clientT0 = performance.now() - t;
  run.events.push({ event: name, t_ms: t, data: d });
  if (d.replay && S.replay && d.recorded_at) $("#replay-when").textContent = hhmm(d.recorded_at);
  const fn = HANDLERS[name];
  if (fn) fn(d, t);
  scheduleTrace();
}

function atomState(id) {
  const r = S.run;
  if (!r.A[id]) r.A[id] = { atom: null, t0: null, t1: null, summon: null, tiles: {}, verdict: null };
  return r.A[id];
}

const HANDLERS = {
  scope_start(d) { S.run.id = d.run_id; $("#catalog-progress").textContent = "Loading real detection evidence…"; },
  scope_ready(d) {
    S.run.coverage = d.coverage;
    $("#catalog-progress").textContent = `${d.segments} indexed segments · ${d.coverage.analysis_camera} · Detections ${d.coverage.detection_evidence}`;
  },
  run(d) {
    const r = S.run;
    r.id = d.run_id;
    if (d.text) r.text = d.text;
    if (d.mode) r.mode = d.mode;
    if (d.scene && +d.scene !== S.scene) {
      S.scene = +d.scene;
      $$(".scene-btn").forEach((b) => b.classList.toggle("on", +b.dataset.scene === S.scene));
      buildWall();
    }
    r.scene = d.scene || r.scene;
    renderTestimony();
    paintWall();
  },
  transcript(d) {
    const r = S.run;
    r.text = d.text || r.text;
    r.source = d.source || r.source;
    if (d.latency_ms) r.heardMs = d.latency_ms;
    renderTestimony();
  },
  atoms(d) {
    const r = S.run;
    r.atoms = d.atoms || [];
    r.parser = d.parser;
    r.atoms.forEach((a) => { atomState(a.id).atom = a; });
    $("#parser").textContent = d.parser === "rules" ? "(rules parser)" : d.parser ? `(${d.parser} atomizer)` : "";
    renderTestimony();
    renderPills(true);
  },
  t0(d) {
    const st = atomState(d.atom_id);
    st.t0 = d;
    const per = d.data && (d.data.per_camera || d.data.cameras);
    if (per && typeof per === "object") {
      Object.entries(per).forEach(([cam, v]) => {
        const n = typeof v === "object" && v !== null ? (v.segments ?? v.count ?? v.peak ?? v.n ?? 0) : +v || 0;
        const cur = st.tiles[cam];
        if (!cur || cur.tier === "YOLO") st.tiles[cam] = { state: n > 0 ? "yes" : "no", tier: "YOLO", info: n > 0 ? `${n}` : "0" };
      });
      chooseActive(d.atom_id, true);
    }
    renderPills();
    paintWall();
  },
  t1(d) {
    atomState(d.atom_id).t1 = d;
    renderPills();
  },
  summon(d) {
    const st = atomState(d.atom_id);
    st.summon = d;
    (d.jurors || []).forEach((j) => {
      const cur = st.tiles[j.camera];
      st.tiles[j.camera] = { ...(cur && cur.tier === "YOLO" ? {} : cur || {}), state: "summoned", tier: "COSMOS", juror: j };
    });
    chooseActive(d.atom_id, false);
    paintWall();
    setTimeout(() => {
      Object.values(st.tiles).forEach((tl) => { if (tl.state === "summoned") tl.state = "deliberating"; });
      if (S.run && S.run.activeAtom === d.atom_id) paintWall();
    }, 180);
  },
  juror(d) {
    const st = atomState(d.atom_id);
    applyVote(st, d.vote);
    renderPills();
    if (S.run.activeAtom === d.atom_id) { paintWall(); renderExhibits(); }
    else maybeAdvanceActive();
  },
  ground(d) {
    const st = atomState(d.atom_id);
    const tl = st.tiles[d.camera] || (st.tiles[d.camera] = { state: "yes", tier: "COSMOS" });
    tl.ground = d;
    if (S.run.activeAtom === d.atom_id) paintWall();
  },
  zoom(d) {
    const st = atomState(d.atom_id);
    const tl = st.tiles[d.camera] || (st.tiles[d.camera] = { state: "yes", tier: "COSMOS" });
    tl.zoom = d;
    if (S.run.activeAtom === d.atom_id) paintWall();
  },
  atom_verdict(d) {
    const av = d.atom_verdict || {};
    const st = atomState(av.atom_id);
    st.verdict = av;
    (av.votes || []).forEach((v) => applyVote(st, v, true));
    renderTestimony();
    renderPills();
    maybeAdvanceActive();
    paintWall();
    renderExhibits();
  },
  verdict(d) {
    S.run.verdict = d;
    $("#verdict-headline").textContent = {TRUE:"The claim is supported", FALSE:"The claim is contradicted", UNPROVEN:"The full claim cannot be established"}[d.verdict] || "Assessment complete";
    if (!S.run.pinned) chooseDecisive();
    settleDeliberating();
    setStamp(d.verdict, d.verdict);
    $("#why").innerHTML = `<span class="lbl">WHY</span>${esc(d.explanation || "")}`;
    renderPills();
    renderVerdictSummary();
    renderSelectedClaim();
    paintWall();
    renderExhibits();
  },
  stock(d) {
    S.run.stock = d;
    renderStock(d);
  },
  service(d, t) {
    S.run.services.push({ t_ms: t, ...d });
    onService(d);
    if (S.tab === "log") renderLog();
  },
  receipt(d) {
    S.run.receipt = d;
    if (d.weave_url) { S.chips.weave.live = true; if (S.chips.weave.state === "idle") S.chips.weave.state = "done"; renderChip("weave"); }
    renderChip("coreweave");
    renderReceipt();
  },
  error(d) {
    toast(d.message || "error");
    if (!S.run.verdict) {
      setStamp("idle", "NO VERDICT");
      $("#why").innerHTML = `<span class="lbl">ERROR</span>${esc(d.message || "")}`;
    }
  },
  done() {
    S.run.done = true;
    settleDeliberating();
    paintWall();
    if (!S.replay) loadReplays();
  },
};

function applyVote(st, v, final) {
  if (!v || !v.camera) return;
  const prev = st.tiles[v.camera] || {};
  const state = v.vote === "yes" ? "yes" : v.vote === "no" ? "no" : "abstain";
  st.tiles[v.camera] = {
    ...prev, state, vote: v, tier: TIER_BADGE[v.tier] || "COSMOS", cached: !!v.cached, cachedAt: v.cached_at,
    juror: v.juror || prev.juror, flip: !final && prev.state !== state,
  };
}

function settleDeliberating() {
  if (!S.run) return;
  Object.values(S.run.A).forEach((st) => Object.values(st.tiles).forEach((tl) => {
    if (tl.state === "summoned" || tl.state === "deliberating") { tl.state = "abstain"; tl.timedOut = true; }
  }));
}

function pendingTiles(id) {
  const st = S.run && S.run.A[id];
  return st ? Object.values(st.tiles).filter((t) => t.state === "summoned" || t.state === "deliberating").length : 0;
}

function chooseActive(id, weak) {
  const r = S.run;
  if (r.pinned) return;
  const cur = r.activeAtom;
  if (!cur || (!weak && pendingTiles(cur) === 0) || (weak && Object.keys(r.A[cur] ? r.A[cur].tiles : {}).length === 0)) setActive(id, false);
}

function maybeAdvanceActive() {
  const r = S.run;
  if (r.pinned || (r.activeAtom && pendingTiles(r.activeAtom) > 0)) return;
  const next = r.atoms.find((a) => pendingTiles(a.id) > 0);
  if (next) setActive(next.id, false);
}

function chooseDecisive() {
  const r = S.run;
  const withTiles = r.atoms.filter((a) => Object.keys(atomState(a.id).tiles).length);
  if (!withTiles.length) return;
  const score = (a) => {
    const st = atomState(a.id);
    const v = st.verdict ? st.verdict.verdict : "";
    const jury = Object.values(st.tiles).filter((t) => t.tier === "COSMOS").length;
    return (v === "CONTRADICTED" ? 1000 : v === "SUPPORTED" ? 500 : 0) + (st.summon && st.summon.probe === "P-TOW" ? 200 : 0) + jury;
  };
  withTiles.sort((a, b) => score(b) - score(a));
  setActive(withTiles[0].id, false);
}

function setActive(id, pinned) {
  const r = S.run;
  if (!r) return;
  r.activeAtom = id;
  if (pinned) r.pinned = true;
  $$(".pill").forEach((p) => p.classList.toggle("on", p.dataset.atom === id));
  $$(".sp").forEach((p) => p.classList.toggle("focus", (p.dataset.atoms || "").split(",").includes(id)));
  if (!S.live) { paintWall(); renderExhibits(); }
  renderSelectedClaim();
}

function renderSelectedClaim() {
  const r = S.run;
  const st = r && r.activeAtom ? atomState(r.activeAtom) : null;
  $("#selected-claim").innerHTML = st && st.atom ? `<strong>${esc(st.atom.span)}</strong><p>${esc((st.verdict || {}).reason || "Assessment in progress")}</p>` : "Select a claim to inspect its evidence.";
}

// ------------------------------------------------------------------ board reset
function resetBoard() {
  $("#testimony").innerHTML = S.run && S.run.text ? "" : `<span class="placeholder">Say anything about this footage. We'll tell you if it's true — and when we can't.</span>`;
  $("#heard-by").textContent = "";
  $("#parser").textContent = "";
  $("#atoms").innerHTML = `<span class="muted">Atomic claims appear here, each sent to the cheapest witness that can settle it.</span>`;
  $("#why").innerHTML = "";
  document.body.classList.remove("submitted");
  $("#edit-claim").hidden = true;
  $("#verdict-headline").textContent = "Awaiting a claim";
  $("#verdict-summary").textContent = "";
  $("#selected-claim").textContent = "Select a claim to inspect its evidence.";
  $("#verdict-breakdown").innerHTML = "";
  $("#wall-atom").textContent = "";
  $("#stock-panel").hidden = true;
  $("#exhibits").innerHTML = `<span class="muted">Juror keyframes land here.</span>`;
  $("#exhibits-note").textContent = "";
  $("#trace").innerHTML = `<span class="muted">Each call appears as a bar, in ms from the moment you finished speaking.</span>`;
  $("#trace-total").textContent = "";
  $("#trace-weave").hidden = true;
  $("#receipt").innerHTML = `<span class="muted">Service receipt · Real service usage appears after verification</span>`;
  setStamp("idle", "AWAITING TESTIMONY");
  Object.keys(SVC).forEach((id) => {
    const c = S.chips[id];
    Object.assign(c, { state: "idle", inflight: 0, n: 0, ms: 0, since: 0, live: false, pipeline: false, calls: [], note: "" });
    renderChip(id);
  });
  if (S.tab === "log") renderLog();
}

// ------------------------------------------------------------------ testimony
function spanStateOf(id) {
  const st = S.run && S.run.A[id];
  const v = st && st.verdict && st.verdict.verdict;
  return { SUPPORTED: "supported", CONTRADICTED: "contradicted", MOOT: "moot", UNVERIFIABLE: "unverifiable" }[v] || "pending";
}

function spansHTML(text, atoms, stateOf, reasonOf) {
  const ranges = [];
  const claimed = [];
  atoms.forEach((a) => {
    if (!a.span) return;
    let from = 0;
    let at = -1;
    for (;;) {
      at = text.indexOf(a.span, from);
      if (at < 0) break;
      if (!claimed.some((c) => c.s === at && c.e === at + a.span.length && c.span === a.span)) break;
      from = at + 1;
    }
    if (at < 0) at = text.toLowerCase().indexOf(a.span.toLowerCase());
    if (at < 0) return;
    const r = { s: at, e: at + a.span.length, id: a.id, span: a.span };
    claimed.push(r);
    ranges.push(r);
  });
  const cuts = Array.from(new Set([0, text.length, ...ranges.flatMap((r) => [r.s, r.e])])).sort((a, b) => a - b);
  const lastSeg = {};
  const segs = [];
  for (let i = 0; i < cuts.length - 1; i++) {
    const a = cuts[i];
    const b = cuts[i + 1];
    const cover = ranges.filter((r) => r.s <= a && r.e >= b).sort((x, y) => (x.e - x.s) - (y.e - y.s));
    segs.push({ a, b, cover });
    if (cover.length) lastSeg[cover[0].id] = segs.length - 1;
  }
  return segs.map((sg, i) => {
    const piece = esc(text.slice(sg.a, sg.b));
    if (!sg.cover.length) return piece;
    const top = sg.cover[0];
    const state = stateOf(top.id);
    const q = state === "unverifiable" && lastSeg[top.id] === i ? `<sup class="qm">?</sup>` : "";
    return `<span class="sp ${state}" data-atoms="${esc(sg.cover.map((c) => c.id).join(","))}" title="${esc(reasonOf(top.id))}">${piece}${q}</span>`;
  }).join("");
}

function renderTestimony() {
  const r = S.run;
  document.body.classList.toggle("submitted", !!r && !!r.text && !S.editing);
  $("#edit-claim").hidden = !r || !r.text;
  if (!r) return;
  const reason = (id) => { const st = r.A[id]; return st && st.verdict ? `${st.verdict.verdict}: ${st.verdict.reason}` : "pending"; };
  $("#testimony").innerHTML = `<span class="q">“</span>${spansHTML(r.text, r.atoms, spanStateOf, reason)}<span class="q">”</span>`;
  const by = (r.source === "canary" ? `(as heard by Canary${r.heardMs ? " · " + fmtMs(r.heardMs) : ""}` : `(${r.source || "typed"}`) + (r.replay ? " · replay)" : ")");
  $("#heard-by").textContent = by;
  $$("#testimony .sp").forEach((sp) => sp.addEventListener("click", () => {
    const id = (sp.dataset.atoms || "").split(",")[0];
    if (id) setActive(id, true);
  }));
}

// ------------------------------------------------------------------ atom pills
function frac(st) {
  const out = {};
  const v = st.verdict && st.verdict.verdict;
  if (st.t0) {
    const d = st.t0.data || {};
    let k = d.hits ?? d.k;
    let n = d.total ?? d.n;
    const m = k == null && /(\d+) of (\d+)/.exec(st.t0.summary || "");
    if (m) { k = m[1]; n = m[2]; }
    out.RECORDS = k != null && n != null ? `${k}/${n}` : "";
  }
  if (st.t1) {
    const s = st.t1.supports || 0;
    const c = st.t1.contradicts || 0;
    const n = st.t1.total ?? s + c + (st.t1.silent || 0);
    out.CAPTIONS = c > s ? `${c}✗/${n}` : `${s}/${n}`;
  }
  const votes = Object.values(st.tiles).filter((t) => t.vote && t.tier !== "YOLO");
  const stats = (st.verdict && st.verdict.stats) || {};
  if (votes.length || stats.k) {
    const Y = stats.Y ?? stats.match ?? votes.filter((t) => t.state === "yes").length;
    const N = stats.N ?? stats.other ?? votes.filter((t) => t.state === "no").length;
    const k = stats.Y == null && stats.k_valid != null ? stats.k_valid : stats.k ?? (st.summon ? (st.summon.jurors || []).length : votes.length);
    out.JURY = `${v === "CONTRADICTED" ? N : Y}/${k}`;
  } else if (st.summon) {
    out.JURY = `0/${(st.summon.jurors || []).length}`;
  }
  return out;
}

function typeLabel(a) {
  if (!a) return "";
  if (a.type === "coco_presence") return (a.negated ? "no " : "") + (a.cls || "object");
  if (a.type === "count") return `count ${a.count ?? ""}`;
  if (a.type === "towing") return `towing${a.towing_vehicle && a.towing_vehicle !== "any" ? " · " + a.towing_vehicle : ""}`;
  return (a.type || "").replace(/_/g, " ") + (a.value ? ` · ${a.value}` : "");
}

function renderPills(fresh) {
  const r = S.run;
  const box = $("#atoms");
  if (fresh) {
    box.innerHTML = r.atoms.length ? "" : `<span class="muted">No atoms.</span>`;
    r.atoms.forEach((a, i) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "pill pending";
      b.dataset.atom = a.id;
      b.style.animationDelay = `${i * 70}ms`;
      b.addEventListener("click", () => setActive(a.id, true));
      box.appendChild(b);
    });
  }
  r.atoms.forEach((a) => {
    const b = box.querySelector(`.pill[data-atom="${CSS.escape(a.id)}"]`);
    if (!b) return;
    const st = atomState(a.id);
    const state = spanStateOf(a.id);
    const fr = frac(st);
    const decided = st.verdict && st.verdict.tiers && st.verdict.tiers.length ? st.verdict.tiers : null;
    let tiers = Object.keys(fr).filter((t) => fr[t] !== undefined);
    if (decided) tiers = tiers.filter((t) => decided.includes(t)).concat(decided.filter((t) => !(t in fr)));
    const tb = tiers.map((t) => `<span class="tb ${t}">${t}${fr[t] ? " " + esc(fr[t]) : ""}</span>`).join("");
    const label = state === "moot" ? "moot" : typeLabel(a);
    b.className = `pill ${state}${r.activeAtom === a.id ? " on" : ""}`;
    const pillTxt = st.verdict && st.verdict.stats && st.verdict.stats.pill ? ` · ${st.verdict.stats.pill}` : "";
    b.title = st.verdict ? `${st.verdict.verdict}: ${st.verdict.reason}${pillTxt}` : (st.t0 && st.t0.summary) || "pending";
    const note = st.verdict ? `<span class="note">${esc(st.verdict.reason)}</span>` : "";
    const status = {supported:"Supported", contradicted:"Contradicted", unverifiable:"Unverifiable", moot:"Moot", pending:"Checking"}[state] || "Uncertain";
    b.innerHTML = `<span class="ic"></span><span class="atom-copy"><span class="span">${esc(a.span)}</span>${note}<span class="atom-meta"><span class="ty">${esc(label)}</span>${tb}</span></span><span class="atom-status">${status}</span>`;
  });
}

// ------------------------------------------------------------------ jury wall
function buildWall() {
  const wall = $("#wall");
  if (S.live) return;
  if (S.scope) return buildCatalogWall();
  S.catalogPlayers.forEach(dispose => dispose());
  S.catalogPlayers = [];
  const meta = S.scenes[S.scene] || {};
  // Full 18-slot wall: 3 poles x 6 cameras; cameras with no indexed footage render as NO FEED.
  const present = meta.cameras || [];
  wall.classList.remove("available-only");
  let html = `<div></div>` + POLES.map((p) => `<div class="colh">POLE ${p}</div>`).join("");
  SLOT_ROWS.forEach((c) => {
    html += `<div class="rowh">CAM ${c}</div>`;
    POLES.forEach((p) => {
      const cam = `p${p}c${c}`;
      const cameraIndex = present.indexOf(cam);
      if (cameraIndex < 0) {
        html += `<div class="tile outage" data-cam="${cam}"><span class="cam">${cam}</span><span class="nofeed">NO FEED</span></div>`;
        return;
      }
      const t0 = ((meta.t0 || {}).cameras || {})[cam] || {};
      const pr = t0.probes || {};
      const cond = pr.cond ? [COND.road[pr.cond.road], COND.traffic[pr.cond.traffic]].filter(Boolean).join(" · ") : "";
      const cls = Object.entries(t0.segments_with || {}).map(([k, v]) => `${k} ${v}`).join(", ");
      const title = `${cam} · ${t0.segments || 0} segments${cls ? " · YOLO segments with: " + cls : ""}${cond ? " · P-COND: " + cond : ""}`;
      html += `<article class="tile idle" aria-label="Camera ${cameraIndex + 1}" data-cam="${cam}" data-cond="${esc(cond)}" title="${esc(title)}">
        <video src="api/camera-stream?${qs({ scene: S.scene, camera: cam })}" aria-label="Recorded video camera ${cameraIndex + 1}" muted autoplay loop controls playsinline preload="metadata"></video>
        <span class="cam">Camera ${cameraIndex + 1} <small>${esc(cam)}</small></span><span class="mark"></span><div class="gb"></div>
        <div class="badges"></div><span class="video-error" hidden>Video playback unavailable</span></article>`;
    });
  });
  wall.innerHTML = html;
  $$("video", wall).forEach((video) => video.addEventListener("error", () => { $(".video-error", video.closest(".tile")).hidden = false; }));
  $$(".tile:not(.outage)", wall).forEach((t) => t.addEventListener("click", (event) => {
    if (event.target.closest("video")) return;
    const r = S.run;
    const cam = t.dataset.cam;
    if (!r || !r.activeAtom) return;
    const tl = atomState(r.activeAtom).tiles[cam];
    if (tl && (tl.vote || tl.juror) && r.id) openExhibit(r.activeAtom, cam);
  }));
  const tot = meta.t0 && meta.t0.totals;
  if (tot && !(S.health.pipeline_error && !S.health.pipeline && !S.health.dev_stub)) {
    $("#wall-foot").textContent = `Scene ${S.scene} · ${meta.label || ""} · ${meta.cameras.length} cameras · ${tot.segments} segments in VastDB records` +
      (meta.location ? ` · ${meta.location}` : "");
  }
}

function paintWall() {
  if (S.live) return;
  const r = S.run;
  const id = r && r.activeAtom;
  const st = id ? atomState(id) : null;
  const a = st && st.atom;
  if (a) {
    const sm = st.summon;
    $("#wall-atom").textContent = `“${a.span}”${sm ? ` · ${sm.probe_version || sm.probe}` : st.t0 ? " · YOLO records" : ""}${r.pinned ? " · pinned" : ""}`;
  } else {
    $("#wall-atom").textContent = "";
  }
  $$("#wall .tile:not(.outage)").forEach((el) => {
    const cam = el.dataset.cam;
    const tl = st ? st.tiles[cam] : null;
    const state = tl ? tl.state : "idle";
    const prev = el.dataset.state;
    el.className = `tile ${state}`;
    if (tl && tl.flip && prev !== state && (state === "yes" || state === "no" || state === "abstain")) {
      el.classList.add("flip");
      tl.flip = false;
    }
    el.dataset.state = state;
    $(".mark", el).textContent = {yes:"✓ Supports", no:"✕ Contradicts", abstain:"− Abstained", summoned:"Queued", deliberating:"Assessing", idle:"Not assessed"}[state] || state;
    $(".gb", el).innerHTML = tl && tl.ground && tl.ground.bbox_2d ? boxDiv(tl.ground.bbox_2d, "gbox") : "";
    const bits = [];
    if (tl && tl.tier) bits.push(`<span class="tierb ${tl.tier}">${tl.tier}${tl.tier === "YOLO" && tl.info != null ? " " + esc(tl.info) : ""}</span>`);
    if (tl && tl.zoom) bits.push(`<span class="zoomb ${tl.zoom.ok ? "" : "bad"}">ZOOM ${tl.zoom.ok ? "✓" : "✗"}${tl.zoom.conf != null ? " " + (+tl.zoom.conf).toFixed(2) : ""}</span>`);
    if (tl && tl.cached) bits.push(`<span class="clock">Cached · ${esc(hhmm(tl.cachedAt))}</span>`);
    if (tl && tl.timedOut) bits.push(`<span class="clock">timeout</span>`);
    if (!tl && el.dataset.cond) bits.push(`<span class="info">${esc(el.dataset.cond)}</span>`);
    $(".badges", el).innerHTML = bits.join("");
  });
}

function boxDiv(b, cls, label, frame) {
  // bbox_2d is 0-1000 normalized; zoom.crop_box is pixels of the 4K frame (frame = [w, h])
  if (!b || b.length < 4) return "";
  const [x1, y1, x2, y2] = b.map(Number);
  const [scaleX, scaleY] = frame || [1000, 1000];
  const css = `left:${(x1 / scaleX) * 100}%;top:${(y1 / scaleY) * 100}%;width:${((x2 - x1) / scaleX) * 100}%;height:${((y2 - y1) / scaleY) * 100}%`;
  return `<div class="${cls}" style="${css}">${label ? `<span>${esc(label)}</span>` : ""}</div>`;
}

// ------------------------------------------------------------------ verdict, stock, exhibits
function renderVerdictSummary() {
  const r = S.run;
  if (!r || !r.verdict) return;
  const supported = r.atoms.filter((a) => spanStateOf(a.id) === "supported");
  $("#verdict-summary").textContent = `${supported.length} of ${r.atoms.length} claims supported`;
  const contradicted = r.atoms.filter((a) => spanStateOf(a.id) === "contradicted");
  const groups = [["Supported", supported], ...(contradicted.length ? [["Contradicted", contradicted]] : []), ["Needs evidence", r.atoms.filter((a) => !["supported", "contradicted"].includes(spanStateOf(a.id)))]];
  $("#verdict-breakdown").innerHTML = groups.map(([label, atoms]) => `<section><strong>${label} (${atoms.length})</strong>${atoms.map((a) => `<div class="verdict-item ${spanStateOf(a.id)}"><span>${spanStateOf(a.id) === "supported" ? "✓" : spanStateOf(a.id) === "contradicted" ? "✕" : "!"}</span><span>${esc(a.span)}<small>${esc((atomState(a.id).verdict || {}).reason || "Awaiting evidence")}</small></span></div>`).join("")}</section>`).join("");
}

function setStamp(kind, text) {
  const s = $("#stamp");
  s.className = "stamp " + kind;
  s.textContent = text;
  if (["TRUE", "FALSE", "UNPROVEN"].includes(kind)) {
    void s.offsetWidth;
    s.classList.add("land");
    const box = $("#verdict-box");
    box.classList.remove("thud");
    void box.offsetWidth;
    box.classList.add("thud");
  }
}

function showStockPending() {
  $("#stock-panel").hidden = false;
  $("#stock-body").innerHTML = `<span class="muted">Asking the stock VSS agent the same sentence…</span>`;
}

function renderStock(d) {
  $("#stock-panel").hidden = false;
  const cls = String(d.classification || "OTHER").toUpperCase().replace(/\s+/g, "_");
  if (cls === "ERROR") { $("#stock-body").innerHTML = `<p class="stock-error">VSS comparison unavailable: ${esc(d.error || "upstream service error")}</p>`; return; }
  $("#stock-body").innerHTML = `<blockquote>${esc(d.answer || "(no answer)")}</blockquote>
    <span class="cls ${esc(cls)}">${esc(d.classification || "unclassified")}</span>
    <span class="muted"> · search returned ${esc(d.hits ?? "?")} clips for this sentence · ${fmtMs(d.latency_ms)}</span>`;
}

function renderExhibits() {
  if (S.live) { $("#exhibits").innerHTML = `<span class="muted">Live assessment applies to the recently received frames, not archived camera evidence.</span>`; return; }
  const r = S.run;
  const box = $("#exhibits");
  if (!r || !r.activeAtom) return;
  const st = atomState(r.activeAtom);
  const items = Object.entries(st.tiles).filter(([, t]) => t.vote);
  if (!items.length) {
    $("#exhibits-note").textContent = st.atom ? `“${st.atom.span}”` : "";
    box.innerHTML = `<span class="muted">No frame assessments are associated with this claim.</span>`;
    return;
  }
  items.sort((a, b) => (a[1].state === "yes" ? 0 : 1) - (b[1].state === "yes" ? 0 : 1) || a[0].localeCompare(b[0]));
  $("#exhibits-note").textContent = `“${st.atom ? st.atom.span : ""}” · ${items.length} jurors · click for the keyframe`;
  box.innerHTML = items.slice(0, 12).map(([cam, t]) => `
    <button type="button" class="ex-thumb ${t.state}" data-cam="${cam}" title="${esc(t.vote.probe_version || "")}">
      <img src="api/exhibit.jpg?${qs({ run_id: r.id, atom_id: r.activeAtom, camera: cam, panel: 1 })}" alt="Assessment frame for ${esc(cam)}" loading="lazy" />
      <span><strong>${esc(cam)} · Evidence frame</strong><small>${t.state === "yes" ? "Supporting vote" : t.state === "no" ? "Contradicting vote" : "Abstained · not supporting evidence"}</small><em>Open frame →</em></span>
    </button>`).join("");
  $$(".ex-thumb", box).forEach((b) => b.addEventListener("click", () => openExhibit(r.activeAtom, b.dataset.cam)));
}

async function openExhibit(atomId, cam) {
  const r = S.run;
  if (!r || !r.id) return;
  let ex;
  try {
    ex = await getJSON(`api/exhibit?${qs({ run_id: r.id, atom_id: atomId, camera: cam })}`);
  } catch (e) {
    return toast("Exhibit unavailable: " + e.message);
  }
  if (S.run !== r || r.activeAtom !== atomId) return;
  const a = ex.atom || {};
  const v = ex.vote || {};
  const j = ex.juror || {};
  $("#drawer-title").textContent = `EXHIBIT · ${cam} · “${a.span || atomId}” · ${ex.probe_version || ex.probe || ""} · panel ${ex.panel}`;
  const img = $("#exhibit-img");
  img.src = ex.image;
  const vid = $("#exhibit-video");
  vid.pause();
  vid.removeAttribute("src");
  vid.hidden = true;
  const play = $("#drawer-play");
  play.hidden = !ex.stream;
  play.onclick = () => {
    vid.hidden = false;
    vid.src = ex.stream;
    vid.muted = true;
    const p = vid.play();
    if (p && p.catch) p.catch(() => toast("Stream did not play (VSS videos/stream)."));
  };
  let ov = "";
  if (ex.ground && ex.ground.bbox_2d) ov += boxDiv(ex.ground.bbox_2d, "cbox", "Cosmos3 P-GROUND");
  if (ex.zoom && ex.zoom.crop_box) {
    const z = ex.zoom;
    ov += boxDiv(z.crop_box, "ybox", `YOLO zoom ${z.ok ? "✓" : "✗"} ${z.label || ""} ${z.conf != null ? (+z.conf).toFixed(2) : ""}`, [3840, 2160]);
  }
  $("#ex-overlay").innerHTML = ov;
  const kv = [
    ["vote", `${v.vote || "?"}${v.abstain_reason ? " (" + v.abstain_reason + ")" : ""}`],
    ["tier", v.tier],
    ["probe", ex.probe_version || ex.probe],
    ["latency", fmtMs(ex.latency_ms)],
    ["cached", ex.cached ? `yes · ${hhmm(ex.cached_at)}` : "no (live call)"],
    ["yes panels", (v.yes_panels || []).join(", ") || "–"],
    ["visibility", v.visibility],
    ["zoom-check", ex.zoom ? `${ex.zoom.ok ? "pass" : "fail"} · ${ex.zoom.label || ""} ${ex.zoom.conf ?? ""}` : v.zoom_ok == null ? "not run" : String(v.zoom_ok)],
    ["segment", j.source ? `${j.source.split("/").slice(-2).join("/")}${j.seg != null ? ` (seg ${j.seg})` : " (scene-wide pre-run grid)"}` : "scene-wide pre-run grid"],
    ["panel times", (j.times || []).map((x) => (+x).toFixed(1) + " s").join(" · ")],
    ["retrieval", j.rank != null ? `rank ${j.rank}${j.retrieval_score != null ? " · score " + (+j.retrieval_score).toFixed(3) : ""}` : ""],
    ["image sha", v.image_sha],
  ].filter(([, x]) => x != null && x !== "");
  $("#exhibit-meta").innerHTML = `
    <dl class="kv">${kv.map(([k, x]) => `<dt>${esc(k)}</dt><dd>${esc(x)}</dd>`).join("")}</dl>
    <div class="row-label">JUROR RAW JSON <span class="heard">${ex.replay ? "from recording" : "as returned"}</span></div>
    <pre class="json">${json(v.raw ?? null)}</pre>
    <p class="muted" style="margin:0;font-size:12px">The juror never saw the testimony: probes are claim-agnostic and written in advance.</p>`;
  $("#drawer").hidden = false;
}

function closeDrawer() {
  const vid = $("#exhibit-video");
  vid.pause();
  vid.removeAttribute("src");
  $("#drawer").hidden = true;
}

// ------------------------------------------------------------------ ribbon
function buildRibbon() {
  $("#ribbon").innerHTML = LANES.map(([lane, items]) => `
    <div class="lane ${lane}"><div class="lane-name">${lane}</div>
      ${items.map(([id, name]) => `<button type="button" class="chip" data-svc="${id}"><span class="nm">${esc(name)}</span><span class="st">—</span></button>`).join("")}
    </div>`).join("");
  Object.keys(SVC).forEach((id) => {
    S.chips[id] = { state: "idle", inflight: 0, n: 0, ms: 0, since: 0, live: false, pipeline: false, calls: [], note: "" };
    $(`.chip[data-svc="${id}"]`).addEventListener("click", () => openChip(id));
    renderChip(id);
  });
}

function onService(d) {
  const c = S.chips[d.service];
  if (!c) return;
  const now = performance.now();
  const pipeline = /^pipeline/i.test(d.note || "");
  c.note = d.note || c.note;
  if (d.state === "firing") {
    if (c.inflight === 0) c.since = now;
    c.inflight++;
    c.state = "firing";
  } else if (d.state === "done") {
    c.inflight = Math.max(0, c.inflight - 1);
    c.n = Math.max(c.n + 1, d.n || 0);
    c.ms += d.ms || 0;
    if (pipeline) c.pipeline = true; else c.live = true;
    c.state = c.inflight ? "firing" : "done";
    c.calls.push(d);
  } else if (d.state === "pipeline") {
    c.pipeline = true;
    if (!c.inflight && !c.live) c.state = "done";
    c.calls.push(d);
  } else if (d.state === "fallback") {
    c.state = c.inflight ? "firing" : "fallback";
    c.calls.push(d);
  } else if (d.state === "error") {
    c.inflight = Math.max(0, c.inflight - 1);
    c.state = c.inflight ? "firing" : "error";
    c.calls.push(d);
  }
  renderChip(d.service);
  if (GPU_SVCS.has(d.service)) renderChip("coreweave");
}

function gpuSeconds() {
  const r = S.run;
  if (r && r.receipt && r.receipt.gpu_s != null) return +r.receipt.gpu_s;
  let ms = 0;
  ((r && r.services) || []).forEach((e) => { if (e.state === "done" && GPU_SVCS.has(e.service) && !/^pipeline/i.test(e.note || "")) ms += e.ms || 0; });
  return ms / 1000;
}

function renderChip(id) {
  const el = $(`.chip[data-svc="${id}"]`);
  if (!el) return;
  const c = S.chips[id];
  const st = $(".st", el);
  if (id === "coreweave") {
    el.className = "chip badge";
    st.textContent = `${gpuSeconds().toFixed(1)} GPU-s`;
    return;
  }
  if (id === "cursor") {
    el.className = "chip badge";
    st.textContent = "badge";
    return;
  }
  if (id === "k8s") {
    const pod = S.health && S.health.pod;
    el.className = "chip " + (pod ? "k8s-live" : "k8s-off");
    st.textContent = pod ? `pod ${pod.slice(-14)} · /health ✓` : "served from localhost";
    return;
  }
  const cls = ["chip", c.state];
  if (c.state === "done" && c.pipeline && !c.live) cls.push("outlined");
  el.className = cls.join(" ");
  if (c.state === "idle") st.textContent = "—";
  else if (c.state === "firing") st.textContent = `${Math.round(performance.now() - c.since)} ms…${c.n ? " ×" + c.n : ""}`;
  else if (c.state === "done") st.textContent = c.pipeline && !c.live ? "pipeline output" : `${fmtMs(c.ms)} ×${c.n}`;
  else st.textContent = c.state;
  el.title = c.note || "";
}

function openChip(id) {
  const c = S.chips[id];
  const meta = SVC[id];
  $("#chip-title").textContent = `${meta.name} · ${meta.lane}${BADGES.has(id) ? " · badge (never counted)" : ""}`;
  let html = "";
  if (id === "k8s") {
    html = `<p class="muted">Lit when this page was served by the team pod; greyed when served from VM localhost.</p><pre class="json">${json(S.health)}</pre>`;
  } else if (id === "coreweave") {
    html = `<p class="muted">Every model runs on the shared CoreWeave GPU host. The meter sums the measured latency of GPU-host calls in this run. It is a badge and never counts toward "fired".</p><p style="font:600 22px var(--mono)">${gpuSeconds().toFixed(1)} GPU-s</p>`;
  } else if (id === "cursor") {
    html = `<p class="muted">Built in Cursor with the starter skills. The repo ships <code>.cursor/rules</code> and a <code>perjury-verify</code> skill so a Cursor agent can call this API. Badge only; it never counts toward "fired".</p>`;
  } else if (!c.calls.length) {
    html = `<p class="muted">No calls in this run.</p>`;
  } else {
    html = c.calls.slice(-8).reverse().map((d) => `
      <div class="chip-call"><h4>${esc(d.state.toUpperCase())} · ${fmtMs(d.ms)} · ${esc(d.note || "")}</h4>
        <div class="two"><div><div class="row-label">REQUEST</div><pre class="json">${json(d.request ?? null)}</pre></div>
        <div><div class="row-label">RESPONSE</div><pre class="json">${json(d.response ?? null)}</pre></div></div></div>`).join("");
  }
  $("#chip-body").innerHTML = html;
  $("#chip-modal").hidden = false;
}

function renderReceipt() {
  const r = S.run;
  const d = r.receipt;
  if (!d) return;
  const sep = `<span class="sep">·</span>`;
  const bits = [
    `<span class="rv ${esc(d.verdict)}">${esc(d.verdict)}</span>`,
    `${d.atoms ?? r.atoms.length} claims`,
    `Services used: ${(d.fired || []).map((id) => SVC[id] ? SVC[id].name : id).join(", ") || "none reported"}`,
    `${d.calls ?? 0} calls`,
    fmtMs(d.elapsed_ms),

  ];
  const weave = $("#trace-weave");
  weave.hidden = !d.weave_url || !/^https:\/\//.test(d.weave_url);
  if (!weave.hidden) weave.href = d.weave_url;
  if (d.weave_url) bits.push(`<a href="${esc(d.weave_url)}" target="_blank" rel="noopener">Weave trace ↗</a>`);
  bits.push(`<button type="button" class="thumb" data-t="up" title="Correct">👍</button><button type="button" class="thumb" data-t="down" title="Wrong: goes into the bench">👎</button>`);
  const mode = r.replay || S.replay ? `replay of ${hhmm(S.replay && S.replay.recorded_at)}` : d.mode === "fixture" ? "fixture" : "";
  $("#receipt").innerHTML = bits.join(` ${sep} `) + ` <span class="small">Run ${esc(r.id || "unknown")}${mode ? " · " + esc(mode) : ""}</span>`;
  $$("#receipt .thumb").forEach((b) => b.addEventListener("click", () => sendFeedback(b)));
}

async function sendFeedback(btn) {
  const r = S.run;
  if (!r || !r.id) return;
  try {
    const res = await getJSON("api/feedback", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ run_id: r.id, thumbs: btn.dataset.t, note: "" }) });
    $$("#receipt .thumb").forEach((b) => b.classList.toggle("sent", b === btn));
    toast(res.weave ? "Recorded as Weave feedback." : "Recorded to cache/feedback.jsonl.", "info");
  } catch (e) {
    toast("Feedback failed: " + e.message);
  }
}

// ------------------------------------------------------------------ trace waterfall
let traceQueued = false;
function scheduleTrace() {
  if (traceQueued) return;
  traceQueued = true;
  requestAnimationFrame(() => { traceQueued = false; renderTrace(); });
}

function traceRows() {
  const r = S.run;
  const rows = [];
  const open = {};
  r.events.forEach((e) => {
    const d = e.data;
    if (e.event === "service" && SVC[d.service]) {
      const lane = SVC[d.service].lane;
      const purpose = {atomize:"Claim parsing",t1:"Camera assessment",live_capture_compare:"Live evidence comparison"}[d.note] || d.note;
      const label = `${SVC[d.service].name}${purpose ? " · " + purpose : ""}`;
      if (d.state === "firing") {
        const row = { label, lane, start: e.t_ms, end: null, state: "firing", svc: d.service, data: d };
        (open[d.service] = open[d.service] || []).push(row);
        rows.push(row);
      } else {
        const q = open[d.service] || [];
        const row = q.shift();
        const pipeline = d.state === "pipeline" || /^pipeline/i.test(d.note || "");
        if (row) { Object.assign(row, { end: e.t_ms, state: d.state, label, pipeline, data: d }); }
        else rows.push({ label, lane, start: Math.max(0, e.t_ms - (d.ms || 0)), end: e.t_ms, state: d.state, pipeline, data: d });
      }
    } else if (e.event === "scope_start") {
      rows.push({lane:"STEP", label:"VAST evidence preparation", start:e.t_ms, end:null, state:"firing", duration:true, data:d});
    } else if (e.event === "scope_ready") {
      const prep = rows.find(x => x.label === "VAST evidence preparation" && x.end == null);
      if (prep) { prep.end = e.t_ms; prep.state = "done"; prep.data = d; }
    } else if (["transcript", "atoms", "verdict"].includes(e.event)) {
      const label = e.event === "atoms" ? `atomize → ${(d.atoms || []).length} atoms (${d.parser || "?"})` : e.event === "verdict" ? `quorum → ${d.verdict}` : `transcript (${d.source || "?"})`;
      rows.push({ label, lane: "STEP", start: e.t_ms, end: e.t_ms, state: "done", data: d });
    }
  });
  return rows;
}

function renderTrace() {
  const r = S.run;
  if (!r || !r.events.length) return;
  const nowT = r.done || r.clientT0 == null ? 0 : performance.now() - r.clientT0;
  const rows = traceRows();
  const last = r.events[r.events.length - 1].t_ms;
  const total = Math.max(1000, last, nowT) * 1.04;
  $("#trace-total").textContent = `${fmtMs(Math.max(last, r.done ? 0 : nowT))} wall time · ${rows.filter((x) => x.lane !== "STEP").length} service spans · ${rows.filter((x) => x.lane === "STEP").length} processing events`;
  const axis = `<span></span><div class="trace-axis">${[0, 1, 2, 3, 4].map((i) => `<span>${(total * i / 4000).toFixed(1)}s</span>`).join("")}</div><span></span>`;
  $("#trace").innerHTML = axis + rows.slice(0, 60).map((row, i) => {
    const end = row.end == null ? Math.max(row.start, nowT) : row.end;
    const left = (row.start / total) * 100;
    const width = Math.max(0.3, ((end - row.start) / total) * 100);
    const cls = ["bar", row.lane, row.state === "firing" ? "firing" : "", row.state === "error" ? "error" : "", row.pipeline ? "outlined" : ""].join(" ");
    const ms = row.lane === "STEP" && !row.duration ? `@${fmtMs(row.start)}` : row.end == null ? "…" : fmtMs(end - row.start);
    return `<button type="button" class="tl trace-select" data-trace="${i}" title="Inspect ${esc(row.label)}">${esc(row.label)}</button><div class="tr"><div class="${cls}" style="left:${left}%;width:${width}%"></div></div><div class="tms">${ms}</div>`;
  }).join("");
  $$(".trace-select").forEach((button) => button.addEventListener("click", () => {
    const row = rows[Number(button.dataset.trace)];
    $("#chip-title").textContent = row.label;
    $("#chip-body").innerHTML = `<p>Recorded ${esc(row.lane === "STEP" ? "processing event" : "service span")} · start ${esc(fmtMs(row.start))}${row.end == null ? " · Running" : " · end " + esc(fmtMs(row.end))}</p><pre>${json(row.data || {})}</pre>`;
    $("#chip-modal").hidden = false;
    $("#chip-close").focus();
  }));
}

function tick() {
  Object.entries(S.chips).forEach(([id, c]) => { if (c.state === "firing") renderChip(id); });
  if (S.run && !S.run.done && S.busy) renderTrace();
  if (S.rec && S.rec.started) {
    $("#mic-label").textContent = `● ${((performance.now() - S.rec.started) / 1000).toFixed(1)} s · release to submit`;
  }
}

// ------------------------------------------------------------------ ribbon log tab
function renderLog() {
  const r = S.run;
  const box = $("#log-body");
  if (!r || !r.services.length) { box.innerHTML = `<div class="empty-note">No service events yet. Run a testimony.</div>`; return; }
  box.innerHTML = `<table><thead><tr><th>t</th><th>service</th><th>state</th><th>ms</th><th>×n</th><th>note</th></tr></thead><tbody>` +
    r.services.map((e, i) => `<tr class="clk" data-i="${i}"><td>${fmtMs(e.t_ms)}</td><td>${esc((SVC[e.service] || {}).name || e.service)}</td>
      <td class="st-${esc(e.state)}">${esc(e.state)}</td><td>${e.ms ? fmtMs(e.ms) : ""}</td><td>${e.n || ""}</td><td>${esc(e.note || "")}</td></tr>`).join("") +
    `</tbody></table>`;
  $$("tr.clk", box).forEach((tr) => tr.addEventListener("click", () => {
    const e = r.services[+tr.dataset.i];
    $("#chip-title").textContent = `${(SVC[e.service] || {}).name || e.service} · ${e.state} · ${fmtMs(e.t_ms)}`;
    $("#chip-body").innerHTML = `<div class="two"><div><div class="row-label">REQUEST</div><pre class="json">${json(e.request ?? null)}</pre></div><div><div class="row-label">RESPONSE</div><pre class="json">${json(e.response ?? null)}</pre></div></div>`;
    $("#chip-modal").hidden = false;
  }));
}

// ------------------------------------------------------------------ voice: hold to testify, upload
function setupMic() {
  const mic = $("#mic");
  const ok = window.isSecureContext && navigator.mediaDevices && navigator.mediaDevices.getUserMedia && window.MediaRecorder;
  if (!ok) {
    mic.classList.add("insecure");
    $("#mic-label").textContent = "MIC NEEDS HTTPS · HOW?";
    mic.addEventListener("click", () => { const h = $("#mic-hint"); h.hidden = !h.hidden; });
    const origin = location.origin;
    $("#mic-hint").innerHTML = `<b>The browser blocks the microphone on plain HTTP.</b> This page is <code>${esc(origin)}</code>, which is not a secure context.
      <p>Open this app using its <b>HTTPS</b> address, or use a local SSH tunnel at <code>http://localhost</code>, then allow microphone access when prompted.</p>
      Meanwhile: <b>⤒ recording</b> uploads a Voice Memos / QuickTime clip (works over HTTP), or type the claim.`;
    return;
  }
  mic.addEventListener("pointerdown", (e) => { e.preventDefault(); mic.setPointerCapture && mic.setPointerCapture(e.pointerId); startRec(); });
  mic.addEventListener("pointerup", stopRec);
  mic.addEventListener("pointercancel", stopRec);
  mic.addEventListener("contextmenu", (e) => e.preventDefault());
  document.addEventListener("keydown", (e) => {
    if (e.code !== "Space" || e.repeat || isTyping(e.target)) return;
    e.preventDefault();
    startRec();
  });
  document.addEventListener("keyup", (e) => {
    if (e.code !== "Space" || isTyping(e.target)) return;
    e.preventDefault();
    stopRec();
  });
}

function isTyping(t) {
  return t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.tagName === "SELECT" || t.isContentEditable);
}

async function startRec() {
  if (S.rec || S.busy || $("#mic").classList.contains("busy")) return;
  const rec = { stop: false, chunks: [], started: 0 };
  S.rec = rec;
  const mic = $("#mic");
  try {
    if (!S.micStream) S.micStream = await navigator.mediaDevices.getUserMedia({ audio: { channelCount: 1, echoCancellation: true, noiseSuppression: true } });
  } catch (e) {
    S.rec = null;
    return toast("Microphone unavailable: " + e.message + ". Upload a recording or type.");
  }
  if (rec.stop) { S.rec = null; return toast("Hold the button while you speak.", "info"); }
  let mr;
  try { mr = new MediaRecorder(S.micStream); }
  catch (e) {
    S.rec = null;
    return toast("Audio recording unavailable: " + e.message + ". Upload a recording or type.");
  }
  rec.mr = mr;
  mr.ondataavailable = (ev) => { if (ev.data && ev.data.size) rec.chunks.push(ev.data); };
  mr.onstop = async () => {
    const dur = performance.now() - rec.started;
    stopMeter();
    S.rec = null;
    mic.classList.remove("rec");
    $("#mic-label").textContent = "HOLD TO TESTIFY";
    if (dur < 500) return toast("Hold the button while you speak.", "info");
    await handleAudio(new Blob(rec.chunks, { type: mr.mimeType || "audio/webm" }), "mic");
  };
  mr.start(100);
  rec.started = performance.now();
  mic.classList.add("rec");
  startMeter();
}

function stopRec() {
  const rec = S.rec;
  if (!rec) return;
  rec.stop = true;
  if (rec.mr && rec.mr.state !== "inactive") rec.mr.stop();
}

let meter = null;
function startMeter() {
  try {
    const AC = window.AudioContext || window.webkitAudioContext;
    const ac = new AC();
    const an = ac.createAnalyser();
    an.fftSize = 512;
    ac.createMediaStreamSource(S.micStream).connect(an);
    const buf = new Uint8Array(an.fftSize);
    meter = { ac, raf: 0 };
    const loop = () => {
      an.getByteTimeDomainData(buf);
      let peak = 0;
      for (let i = 0; i < buf.length; i++) peak = Math.max(peak, Math.abs(buf[i] - 128));
      $("#mic-level").style.width = Math.min(100, (peak / 128) * 160) + "%";
      meter.raf = requestAnimationFrame(loop);
    };
    loop();
  } catch (e) { meter = null; }
}

function stopMeter() {
  if (!meter) return;
  cancelAnimationFrame(meter.raf);
  meter.ac.close();
  meter = null;
  $("#mic-level").style.width = "0";
}

async function handleAudio(blob, how) {
  const mic = $("#mic");
  mic.classList.add("busy");
  $("#mic-label").textContent = "ENCODING…";
  try {
    const wav = await window.PerjuryWav.toWav16k(blob);
    $("#mic-label").textContent = "CANARY IS LISTENING…";
    const fd = new FormData();
    fd.append("file", wav, "claim.wav");
    const out = await getJSON("api/transcribe", { method: "POST", body: fd });
    if (!out.text) throw new Error("Canary heard nothing; speak again or type.");
    $("#claim").value = out.text;
    mic.classList.remove("busy");
    $("#mic-label").textContent = "HOLD TO TESTIFY";
    S.lastHeardMs = out.latency_ms;
    await testify(out.text, { source: "canary", transcript_id: out.transcript_id });
    if (S.run && !S.run.heardMs) { S.run.heardMs = out.latency_ms; renderTestimony(); }
  } catch (e) {
    toast(`${how === "upload" ? "Recording" : "Voice"} failed: ${e.message}`);
  } finally {
    mic.classList.remove("busy");
    if (!S.rec) $("#mic-label").textContent = mic.classList.contains("insecure") ? "MIC NEEDS HTTPS · HOW?" : "HOLD TO TESTIFY";
  }
}

// ------------------------------------------------------------------ witness stand tab
const WHO = { "videos/synthesize": "videos/synthesize", synthesize: "videos/synthesize", "agent/ask": "agent/ask", ask: "agent/ask", suggestions: "prompt-suggester", "prompt-suggester": "prompt-suggester" };

async function loadWitness() {
  const box = $("#witness-body");
  let data;
  try { data = await getJSON("api/witness"); } catch (e) { box.innerHTML = `<div class="empty-note">${esc(e.message)}</div>`; return; }
  const job = data.job || {};
  const jobNote = job.state === "running" ? `<p class="muted">Witness stand is running… this page refreshes.</p>` : job.state === "error" ? `<p class="muted">Last run failed: ${esc(job.error)}</p>` : "";
  if (job.state === "running") setTimeout(() => { if (S.tab === "witness") loadWitness(); }, 3000);
  const items = Array.isArray(data) ? data : data.parents || data.items || data.witnesses || data.results || [];
  if (data.status === "not_run" || !items.length) {
    box.innerHTML = jobNote + `<div class="empty-note">The witness stand hasn't run yet. VSS summaries (<code>videos/synthesize</code>), <code>agent/ask</code> answers and prompt-suggester key events will be cross-examined here.</div>`;
    return;
  }
  box.innerHTML = jobNote + items.map((it, i) => {
    const who = WHO[it.who] || it.who || it.source_api || (it.question ? "videos/synthesize" : "VSS");
    const sents = it.sentences || it.claims || it.verdicts || [];
    const counts = {};
    sents.forEach((s) => { const v = sentVerdict(s); if (v) counts[v] = (counts[v] || 0) + 1; });
    const where = [it.scene ? `Scene ${it.scene}` : "", it.camera || "", it.original_video ? it.original_video.split("/").pop() : ""].filter(Boolean).join(" · ");
    const body = it.error ? `<div class="witness-sent"><span class="txt muted">${esc(it.error)}</span></div>` : sents.length ? sents.map((s, k) => witnessSentence(s, it, i, k)).join("") : `<div class="witness-sent"><span class="txt">${esc(it.answer || it.text || "")}</span></div>`;
    return `<div class="card witness-item"><div class="head"><span class="who">WHO TESTIFIED · ${esc(who)}</span><span class="muted">${esc(where)}</span>
      <span class="muted">${Object.entries(counts).map(([k, v]) => `${v} ${k}`).join(" · ")}</span></div>${body}</div>`;
  }).join("") + `<details><summary class="muted">raw witness.json</summary><pre class="json">${json(data)}</pre></details>`;
  $$(".w-retry").forEach((b) => b.addEventListener("click", () => {
    const n = +b.dataset.scene;
    if (n && n !== S.scene) selectScene(n, { clear: true });
    showTab("courtroom");
    testify(b.dataset.text, { source: "typed" });
  }));
}

function sentVerdict(s) {
  return s.verdict && typeof s.verdict === "object" ? s.verdict.verdict : s.verdict || (s.claim_verdict && s.claim_verdict.verdict) || "";
}

function witnessSentence(s, it, i, k) {
  const cv = s.claim_verdict || (s.verdict && typeof s.verdict === "object" ? s.verdict : s);
  const text = s.text || s.sentence || cv.text || "";
  const atoms = s.atoms || cv.atoms || [];
  const avs = s.atom_verdicts || cv.atom_verdicts || [];
  const byId = {};
  avs.forEach((a) => { byId[a.atom_id] = a; });
  const stateOf = (id) => ({ SUPPORTED: "supported", CONTRADICTED: "contradicted", MOOT: "moot", UNVERIFIABLE: "unverifiable" }[(byId[id] || {}).verdict] || "pending");
  const reason = (id) => (byId[id] ? `${byId[id].verdict}: ${byId[id].reason}` : "");
  const v = sentVerdict(s);
  const pills = atoms.map((a) => {
    const st = stateOf(a.id);
    const tiers = ((byId[a.id] || {}).tiers || []).map((t) => `<span class="tb ${t}">${t}</span>`).join("");
    return `<span class="pill ${st}" title="${esc(reason(a.id))}"><span class="ic"></span><span class="span">${esc(a.span)}</span>${tiers}</span>`;
  }).join("");
  const scene = it.scene || s.scene || "";
  return `<div class="witness-sent"><div class="txt">${atoms.length ? spansHTML(text, atoms, stateOf, reason) : esc(text)}
      <div class="mini-pills">${pills}</div></div>
      <span class="vd ${esc(v)}">${esc(v || "–")}</span>
      <button type="button" class="ghost w-retry" data-text="${esc(text)}" data-scene="${esc(scene)}" title="Re-run live in the courtroom">▶</button></div>`;
}

// ------------------------------------------------------------------ bench tab
const METRICS = [
  ["catch", "Catch rate", "planted lies → FALSE"],
  ["false_accusation", "False accusation", "truths → FALSE (lower is better)"],
  ["support", "Support rate", "truths → TRUE (the anti-hover number)"],
  ["decline", "Decline", "UNPROVEN ÷ all claims"],
  ["correct_decline", "Correct decline", "unverifiable-by-design → UNPROVEN"],
  ["overreach", "Overreach", "unverifiable-by-design → hard verdict"],
];

function metricOf(v) {
  if (v == null) return null;
  if (typeof v === "number") return { rate: v };
  if (typeof v !== "object") return null;
  const k = v.k ?? v.num ?? v.x ?? v.hits ?? v.count;
  const n = v.n ?? v.den ?? v.total;
  const rate = v.rate ?? v.value ?? v.p ?? (k != null && n ? k / n : null);
  const ci = Array.isArray(v.ci) ? v.ci : Array.isArray(v.wilson) ? v.wilson : [v.lo ?? v.ci_low ?? v.low, v.hi ?? v.ci_high ?? v.high];
  return { k, n, rate, ci: ci && ci[0] != null ? ci : null };
}

function metricCell(m, dev) {
  if (!m) return `<td class="${dev ? "dev" : ""}">–</td>`;
  const frac = m.k != null && m.n != null ? `${m.k}/${m.n} · ` : "";
  const ci = m.ci ? `<span class="ci">95% CI ${pct(m.ci[0])}–${pct(m.ci[1])}</span>` : "";
  const bar = m.rate != null ? `<div class="bar">${m.ci ? `<b style="left:${m.ci[0] * 100}%;width:${(m.ci[1] - m.ci[0]) * 100}%"></b>` : ""}<i style="width:${m.rate * 100}%;${dev ? "background:#5d6a8a" : ""}"></i></div>` : "";
  return `<td class="${dev ? "dev" : ""}">${frac}${pct(m.rate)}${ci}${dev ? "" : bar}</td>`;
}

function splitOf(rep, name) {
  return rep[name] || (rep.splits || {})[name] || (rep.metrics || {})[name] || null;
}

function lineChart(points, series) {
  const W = 420, H = 190, P = 34;
  const ks = points.map((p) => +p.k);
  const xmin = Math.min(...ks), xmax = Math.max(...ks);
  const xs = (k) => P + ((Math.log(k) - Math.log(xmin || 1)) / ((Math.log(xmax) - Math.log(xmin || 1)) || 1)) * (W - 2 * P);
  const ys = (v) => H - P + 8 - v * (H - P - 14);
  let svg = `<svg class="svgchart" viewBox="0 0 ${W} ${H}" width="100%" role="img">`;
  [0, 0.5, 1].forEach((v) => { svg += `<line x1="${P}" x2="${W - P}" y1="${ys(v)}" y2="${ys(v)}" stroke="#243049"/><text x="${P - 6}" y="${ys(v) + 3}" text-anchor="end">${v * 100}%</text>`; });
  points.forEach((p) => { svg += `<text x="${xs(+p.k)}" y="${H - 6}" text-anchor="middle">k=${p.k}</text>`; });
  series.forEach(([key, color, label], si) => {
    const pts = points.map((p) => [xs(+p.k), metricOf(p[key])]).filter(([, m]) => m && m.rate != null);
    if (!pts.length) return;
    svg += `<polyline fill="none" stroke="${color}" stroke-width="2.5" points="${pts.map(([x, m]) => `${x},${ys(m.rate)}`).join(" ")}"/>`;
    pts.forEach(([x, m]) => { svg += `<circle cx="${x}" cy="${ys(m.rate)}" r="3.5" fill="${color}"/>`; });
    svg += `<text x="${W - P}" y="${14 + si * 13}" text-anchor="end" style="fill:${color}">${label}</text>`;
  });
  return svg + `</svg>`;
}

function sycoBars(sy) {
  const rows = Object.entries(sy).filter(([, v]) => v && typeof v === "object").map(([k, v]) => {
    const m = metricOf({ k: v.yes ?? v.k, n: v.n ?? v.total, rate: v.rate });
    return [k, m];
  }).filter(([, m]) => m && m.rate != null);
  if (!rows.length) return `<p class="muted">no sycophancy numbers in the report</p>`;
  return rows.map(([k, m]) => `<div style="margin:8px 0"><div style="display:flex;justify-content:space-between;font:500 12px var(--mono)"><span>${esc(k)} prompt</span><span>${m.k != null ? `${m.k}/${m.n} · ` : ""}${pct(m.rate)} say yes to an absent trailer</span></div>
    <div style="height:10px;background:#1a2238;border-radius:3px;margin-top:4px"><div style="height:100%;width:${m.rate * 100}%;background:${/lead/i.test(k) ? "var(--con)" : "var(--accent)"};border-radius:3px"></div></div></div>`).join("");
}

async function loadBench() {
  const box = $("#bench-body");
  let rep;
  try { rep = await getJSON("api/bench"); } catch (e) { box.innerHTML = `<div class="empty-note">${esc(e.message)}</div>`; return; }
  if (!rep || rep.status === "not_run" || rep.mode === "empty") {
    box.innerHTML = `<div class="empty-note">Bench not run yet. <code>python -m bench.run_bench</code> writes <code>cache/bench_report.json</code>; nothing is shown here until code has measured it.</div>`;
    return;
  }
  if (rep.status === "unreadable") { box.innerHTML = `<div class="empty-note">bench_report.json is unreadable: ${esc(rep.error)}</div>`; return; }
  const weave = rep.weave_url || rep.leaderboard_url || (rep.weave || {}).url;
  const wl = $("#bench-weave");
  wl.hidden = !weave;
  if (weave) wl.href = weave;
  const test = splitOf(rep, "test");
  const dev = splitOf(rep, "dev");
  const stock = rep.stock || rep.stock_ab || splitOf(rep, "stock");
  const stockTest = stock && ((stock.splits || {}).test || stock.test || (stock.catch ? stock : null));
  let html = rep.fixture || rep.mode === "fixture"
    ? `<div class="empty-note" style="margin-bottom:14px;color:var(--warn);border-color:#6b4f0c">FIXTURE bench: these numbers come from offline fakes, not the live models. Never put them on a slide.</div>` : "";
  const evaluationRun = rep.run || (dev && dev.run) || rep;
  if (evaluationRun.evaluation_scope) {
    html += `<div class="empty-note" role="status" style="margin-bottom:14px;color:var(--warn)">${esc(evaluationRun.evaluation_scope)}${evaluationRun.held_out_test_run === false ? " No held-out test has been run." : ""} ${(evaluationRun.exclusions || []).length} claims excluded because footage or independently reviewed ground truth is missing.</div>`;
  }
  if (test || dev) {
    html += `<div class="card"><h3>VERDICT METRICS · claims ${test && test.n_claims ? "· test n=" + test.n_claims : ""}</h3><table class="metrics"><thead><tr><th>metric</th><th>PERJURY · test</th><th>dev</th>${stockTest ? "<th>stock VSS agent · test</th>" : ""}</tr></thead><tbody>` +
      METRICS.map(([key, name, hint]) => {
        const t = test && metricOf(test[key]);
        const d = dev && metricOf(dev[key]);
        const s = stockTest && metricOf(stockTest[key]);
        if (!t && !d && !s) return "";
        return `<tr><td>${esc(name)}<span class="ci">${esc(hint)}</span></td>${metricCell(t)}${metricCell(d, true)}${stockTest ? metricCell(s, true) : ""}</tr>`;
      }).join("") + `</tbody></table></div>`;
  }
  const curveRaw = rep.jury_curve || rep.jury_size_curve || rep.jury || null;
  const curve = Array.isArray(curveRaw) ? curveRaw : curveRaw && typeof curveRaw === "object" ? Object.entries(curveRaw).map(([k, v]) => ({ k: +k, ...v })) : null;
  const sy = rep.sycophancy || rep.sycophancy_bars || null;
  if (curve || sy) {
    html += `<div class="bench-grid">`;
    html += `<div class="card"><h3>JURY-SIZE CURVE · does more cameras help?</h3>${curve && curve.length ? lineChart(curve.filter((p) => p.k), [["catch", "#5eead4", "catch"], ["false_accusation", "#fb5a6e", "false accusation"]]) : `<p class="muted">not measured</p>`}
      <p class="muted" style="font-size:12px;margin:6px 0 0">Flat means juror errors are correlated: quorum cuts variance, not bias.</p></div>`;
    html += `<div class="card"><h3>SYCOPHANCY · neutral vs leading probe</h3>${sy ? sycoBars(sy) : `<p class="muted">not measured</p>`}
      <p class="muted" style="font-size:12px;margin:6px 0 0">Why jurors never hear the testimony.</p></div>`;
    html += `</div>`;
  }
  const prom = (rep.promotion && (rep.promotion.types || rep.promotion)) || rep.promotion_state || rep.router || null;
  if (prom && typeof prom === "object") {
    const entries = Object.entries(prom).filter(([, v]) => v && typeof v === "object" && "promoted" in v);
    if (entries.length) {
      html += `<div class="card"><h3>ROUTER PROMOTION STATE${rep.promotion && rep.promotion.frozen_at ? " · frozen " + esc(hhmm(rep.promotion.frozen_at)) : ""}</h3>` +
        entries.map(([k, v]) => `<span class="prom ${v.promoted ? "yes" : "no"}" title="catch ${pct(v.catch)} · false accusation ${pct(v.false_accusation)} · n=${v.n ?? "?"}">${v.promoted ? "✓" : "–"} ${esc(k)}${v.n != null ? ` <span class="muted">n=${v.n}</span>` : ""}</span>`).join("") +
        `<p class="muted" style="font-size:12px;margin:6px 0 0">A type issues hard verdicts only if dev catch ≥ 80% and false accusation ≤ 10% with n ≥ 5; otherwise "demoted by bench".</p></div>`;
    }
  }
  const per = rep.atom_accuracy || rep.per_type || (test && test.atoms) || null;
  if (per && typeof per === "object") {
    html += `<div class="card"><h3>ATOM ACCURACY PER TYPE · test</h3><table class="metrics"><thead><tr><th>type</th><th>accuracy</th><th>catch</th><th>false accusation</th><th>support</th></tr></thead><tbody>` +
      Object.entries(per).map(([k, v]) => {
        const acc = metricOf(v && v.accuracy ? v.accuracy : v);
        return `<tr><td>${esc(k.replace(/_/g, " "))}<span class="ci">n=${esc((v && v.n) ?? "?")}</span></td>${metricCell(acc)}${metricCell(metricOf(v && v.catch), true)}${metricCell(metricOf(v && v.false_accusation), true)}${metricCell(metricOf(v && v.support), true)}</tr>`;
      }).join("") + `</tbody></table></div>`;
  }
  const claims = test && Array.isArray(test.claims) ? test.claims : null;
  if (claims) {
    html += `<details class="card"><summary class="muted">per-claim results · test (${claims.length})</summary><table class="metrics"><thead><tr><th>id</th><th>scene</th><th>claim</th><th>kind</th><th>expected</th><th>got</th></tr></thead><tbody>` +
      claims.map((c) => `<tr><td>${esc(c.id)}</td><td>${esc(c.scene)}</td><td style="font-family:var(--serif);font-size:14px">${esc(c.text)}</td><td>${esc(c.kind)}</td><td>${esc(c.expected)}</td><td class="vd ${esc(c.verdict)}">${esc(c.verdict)} ${c.correct ? "✓" : "✗"}</td></tr>`).join("") +
      `</tbody></table></details>`;
  }
  html += `<details><summary class="muted">raw bench_report.json</summary><pre class="json">${json(rep)}</pre></details>`;
  box.innerHTML = html;
}


// VAST catalog: metadata loads once; recorded video bytes load only for visible players.
async function loadCatalog(refresh = false) {
  if (S.busy) return toast("Wait for this assessment to finish before changing footage.", "info");
  const generation = ++S.catalogRequest;
  S.catalogLoading = true;
  $("#catalog-progress").textContent = "Fetching indexed footage from VAST…";
  try {
    const data = await getJSON(`api/catalog${refresh ? "?refresh=true" : ""}`);
    if (generation !== S.catalogRequest) return;
    S.catalog = data;
    const select = $("#location-select");
    select.innerHTML = data.locations.map(l => `<option value="${esc(l.key)}">${esc(l.label)} · ${l.count} clips</option>`).join("");
    select.onchange = () => loadLocation(select.value);
    $("#catalog-refresh").onclick = () => loadCatalog(true);
    select.value = data.locations.some(l => l.key === S.scope?.location) ? S.scope.location : "all";
    await loadLocation(select.value);
  } catch (error) {
    if (generation !== S.catalogRequest) return;
    S.catalogLoading = false;
    $("#catalog-progress").textContent = `VAST catalog unavailable: ${error.message}`;
  }
}
async function loadLocation(location) {
  if (S.busy) { $("#location-select").value = S.scope?.location || "all"; return toast("Wait for the current assessment to finish.", "info"); }
  const generation = ++S.catalogRequest;
  S.catalogLoading = true;
  $("#go").disabled = true;
  $("#catalog-progress").textContent = "Loading indexed clips…";
  try {
    const scope = await getJSON(`api/catalog/scope?${qs({location})}`);
    if (generation !== S.catalogRequest) return;
    S.scope = scope; S.scene = 1; S.run = null; S.replay = null;
    $("#legacy-scenes").hidden = true;
    $("#banner-replay").hidden = true;
    S.assessmentCamera = scope.cameras[0]?.key || null;
    const cameras = $("#assessment-camera");
    cameras.disabled = !scope.cameras.length;
    cameras.innerHTML = scope.cameras.map(c => `<option value="${esc(c.key)}">${esc(c.label)} · ${c.clips.length} clips</option>`).join("");
    cameras.onchange = () => {
      if (S.busy) { cameras.value = S.assessmentCamera; return toast("Wait for the current assessment to finish.", "info"); }
      S.assessmentCamera = cameras.value; S.run = null; resetBoard(); buildCatalogWall();
    };
    $("#catalog-progress").textContent = `${scope.coverage.catalog_chunks} clips · ${scope.cameras.length} cameras · Recorded uploads`;
    $("#source-status").textContent = `VAST · ${scope.label} · Latest uploads ${scope.cameras[0]?.clips[0]?.upload_timestamp?.slice(0,10) || "date unavailable"}`;
    resetBoard(); buildCatalogWall(); applyHealth();
  } catch (error) {
    if (generation !== S.catalogRequest) return;
    $("#catalog-progress").textContent = `Could not load footage: ${error.message}`;
    $("#location-select").value = S.scope?.location || "all";
    toast(error.message);
  } finally {
    if (generation === S.catalogRequest) { S.catalogLoading = false; $("#go").disabled = false; }
  }
}
function buildCatalogWall() {
  const scope = S.scope;
  if (!scope) return;
  S.catalogPlayers.forEach(dispose => dispose());
  S.catalogPlayers = [];
  const buckets = new Map();
  scope.cameras.forEach(camera => {
    const location = camera.clips[0]?.location || scope.location;
    if (!buckets.has(location)) buckets.set(location, []);
    buckets.get(location).push(camera);
  });
  const ordered = [];
  while ([...buckets.values()].some(cameras => cameras.length)) {
    buckets.forEach(cameras => { if (cameras.length) ordered.push(cameras.shift()); });
  }
  const selected = ordered.findIndex(camera => camera.key === S.assessmentCamera);
  if (selected > 0) ordered.unshift(ordered.splice(selected,1)[0]);
  const visible = ordered;
  const wall = $("#wall"); wall.classList.add("available-only");
  wall.innerHTML = visible.map(c => `<section class="catalog-slot"><article class="tile idle" data-cam="${esc(c.key)}"><video muted autoplay controls playsinline preload="metadata" aria-label="Recorded footage ${esc(c.label)}"></video><span class="cam">${esc(c.label)}${c.key === S.assessmentCamera ? " <small>Assessment camera</small>" : ""}</span><span class="mark"></span><div class="gb"></div><div class="badges"></div><span class="video-error" hidden><span class="video-error-message">Video unavailable</span><button type="button" class="video-retry">Retry video</button></span></article><label class="clip-control">Recorded clip<select aria-label="Clip for ${esc(c.label)}">${c.clips.map((clip,i) => `<option value="${i}">${i + 1} · ${esc(clip.label || c.label)}</option>`).join("")}</select></label><p class="clip-caption"></p></section>`).join("");
  visible.forEach((camera,i) => {
    const slot = wall.children[i];
    const expand = document.createElement("button");
    expand.type = "button"; expand.className = "camera-expand";
    expand.textContent = "⤢"; expand.setAttribute("aria-label", `Expand ${camera.label}`);
    expand.onclick = () => { const player = $("video",slot); if (player.requestFullscreen) player.requestFullscreen().catch(() => {}); else toast("Use the video fullscreen control.", "info"); };
    $(".tile",slot).append(expand);
    S.catalogPlayers.push(initCatalogPlayer(wall.children[i], camera, scope));
  });
  $("#gallery-count").textContent = `${visible.length} real cameras · Scroll for more`;
  const layout = $("#gallery-layout");
  const resize = () => {
    const trace = $(".trace-block");
    const bottom = (trace?.getBoundingClientRect().height || 100) + 80;
    const available = Math.max(window.innerHeight * .28, window.innerHeight - wall.getBoundingClientRect().top - bottom);
    wall.dataset.layout = layout.value;
    const cardHeight = wall.firstElementChild?.getBoundingClientRect().height || available;
    const rows = layout.value === "6" ? 2 : layout.value === "all" ? Infinity : 1;
    wall.style.setProperty("--gallery-height", `${Math.min(available, cardHeight * rows + (rows === 2 ? 12 : 0))}px`);
  };
  layout.onchange = resize;
  const observer = new ResizeObserver(resize); observer.observe($(".testify-bar"));
  window.addEventListener("resize", resize); resize();
  S.catalogPlayers.push(() => { observer.disconnect(); window.removeEventListener("resize",resize); });
  $("#wall-foot").textContent = `${scope.coverage.catalog_chunks} real clips indexed · Claims assess all indexed footage of ${S.assessmentCamera}, independently of playback position.`;
  paintWall();
}


function initCatalogPlayer(slot, camera, scope) {
  const video = $("video", slot), select = $("select", slot);
  const warning = $(".video-error", slot), message = $(".video-error-message", slot);
  let generation = 0, attempts = 0, retryTimer = null, loadingTimer = null, disposed = false, active = false, loaded = false;
  const clearTimers = () => { clearTimeout(retryTimer); clearTimeout(loadingTimer); retryTimer = null; loadingTimer = null; };
  const attemptPlayback = () => video.play().catch(error => {
    // Chrome may cancel play() when the previous MP4 request is replaced.
    // Autoplay permission and expected cancellation are not source failures.
    if (error.name !== "AbortError" && error.name !== "NotAllowedError" && video.error) retry();
  });
  const load = (retrying = false) => {
    if (disposed || !slot.isConnected || !active) return;
    loaded = true;
    clearTimers();
    const current = ++generation;
    if (!retrying) attempts = 0;
    const clip = camera.clips[Number(select.value)];
    if (!clip) return;
    warning.hidden = true;
    video.pause();
    video.src = `api/catalog/stream?${qs({scope_id:scope.id, source_id:clip.source_id, attempt:attempts})}`;
    video.load();
    $(".clip-caption",slot).textContent = clip.caption || "Recorded VAST clip; indexed captions are used for assessment.";
    attemptPlayback();
    // A stalled clip can fail without firing a media error. Bound recovery.
    loadingTimer = setTimeout(() => {
      if (generation === current && !disposed && !document.hidden && slot.isConnected && video.readyState < 2) retry();
    }, 12000);
  };
  const retry = () => {
    if (disposed || !slot.isConnected || !active || retryTimer) return;
    clearTimeout(loadingTimer);
    if (attempts >= 2) {
      message.textContent = `Clip ${Number(select.value)+1} could not load. Retry or choose another recorded clip.`;
      warning.hidden = false;
      return;
    }
    const current = generation;
    attempts++;
    retryTimer = setTimeout(() => {
      retryTimer = null;
      if (current === generation) load(true);
    }, attempts * 600);
  };
  const recovered = () => {
    clearTimers(); retryTimer = null; loadingTimer = null;
    warning.hidden = true;
  };
  video.addEventListener("loadeddata", recovered);
  video.addEventListener("playing", recovered);
  const visibility = () => { if (document.hidden) video.pause(); else if (active && !disposed) { if (video.readyState < 2) load(true); else attemptPlayback(); } };
  document.addEventListener("visibilitychange", visibility);
  video.addEventListener("error", () => { if (video.error) retry(); });
  video.addEventListener("ended", () => {
    const next = Number(select.value) + 1;
    if (next < camera.clips.length) { select.value = String(next); load(); }
  });
  select.onchange = () => { loaded = false; load(); };
  $(".video-retry", slot).onclick = () => load();
  const viewport = new IntersectionObserver(entries => {
    active = entries[0].isIntersecting;
    if (active && !document.hidden) { if (!loaded || video.readyState < 2) load(); else attemptPlayback(); }
    else { clearTimers(); video.pause(); }
  }, {root:$("#wall"), threshold:.15});
  viewport.observe(slot);
  return () => { disposed = true; generation++; viewport.disconnect(); clearTimers(); document.removeEventListener("visibilitychange", visibility); video.pause(); video.removeAttribute("src"); video.load(); };
}
