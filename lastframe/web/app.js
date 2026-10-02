"use strict";
const $ = id => document.getElementById(id);
const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const fmt = n => `${String(Math.floor(n / 60)).padStart(2,"0")}:${String(Math.floor(n % 60)).padStart(2,"0")}`;
let catalog = [], round = null, selected = null, confidence = 70, result = null, filter = "All", phase = "before";
let progress = 0, playing = false, animation = null, lastTick = null, status = {}, segments = [];
let history = [];
try { const stored = JSON.parse(localStorage.getItem("lastframe-history") || "[]"); if (Array.isArray(stored)) history = stored.filter(r => r && typeof r.title === "string" && typeof r.correct === "boolean" && typeof r.brier === "number").slice(-200); } catch {}

async function api(path, body) {
  const response = await fetch(path, {method:body === undefined ? "GET" : "POST", headers:body === undefined ? {} : {"Content-Type":"application/json"}, body:body === undefined ? undefined : JSON.stringify(body)});
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `Request failed (${response.status}).`);
  return data;
}
let toastTimer;
function toast(message) { $("toast").textContent = message; $("toast").hidden = false; clearTimeout(toastTimer); toastTimer = setTimeout(() => $("toast").hidden = true, 6000); }

// Schematics are deliberately abstract and labeled. No downloaded or generated
// imagery is represented as footage. Animation is just an interactive diagram.
function car(x,y,color="#dbe4bd",angle=0,width=35,height=64) {
  return `<g transform="translate(${x} ${y}) rotate(${angle})"><rect x="${-width/2-3}" y="${-height/2+8}" width="6" height="12" rx="2" fill="#182b25"/><rect x="${width/2-3}" y="${-height/2+8}" width="6" height="12" rx="2" fill="#182b25"/><rect x="${-width/2-3}" y="${height/2-20}" width="6" height="12" rx="2" fill="#182b25"/><rect x="${width/2-3}" y="${height/2-20}" width="6" height="12" rx="2" fill="#182b25"/><rect x="${-width/2}" y="${-height/2}" width="${width}" height="${height}" rx="7" fill="${color}" stroke="#203b30" stroke-width="2"/><rect x="${-width/2+5}" y="${-height/2+13}" width="${width-10}" height="13" rx="3" fill="#507167"/><rect x="${-width/2+5}" y="${height/2-23}" width="${width-10}" height="10" rx="2" fill="#507167"/><path d="M${-width/2+5} ${-height/2+4}h8 M${width/2-13} ${-height/2+4}h8" stroke="#eef6c5" stroke-width="3"/></g>`;
}
function person(x,y,carrying=false) {
  return `<g transform="translate(${x} ${y})"><ellipse cy="10" rx="10" ry="5" fill="#162e25" opacity=".3"/><path d="M-5 3l-3 12 M5 3l3 12" stroke="#1c3830" stroke-width="5"/><ellipse cy="0" rx="9" ry="7" fill="#e0bd70" stroke="#253d2f" stroke-width="2"/><circle cy="-8" r="5" fill="#ecd1a0"/>${carrying?'<rect x="9" y="-5" width="15" height="14" fill="#bb9462" stroke="#443e2d"/>':''}</g>`;
}
function sceneSVG(kind, p=0, continuation=false) {
  const t = Math.max(0,Math.min(1,p));
  let draw = "";
  if (kind === "warehouse") {
    draw = '<rect width="800" height="450" fill="#bec6b0"/><path d="M0 310H800 M410 0V450" stroke="#9dab94" stroke-width="105"/><path d="M0 310H800 M410 0V450" stroke="#d5ca77" stroke-width="2" stroke-dasharray="10 9"/>';
    for (const x of [35,170,520,655]) for (const y of [65,165]) draw += `<rect x="${x}" y="${y}" width="100" height="65" fill="#7b8d72" stroke="#4f6653" stroke-width="3"/><path d="M${x+8} ${y+32}h84" stroke="#b2b99a" stroke-width="2"/>`;
    draw += '<text x="570" y="410" fill="#708066" font-size="11" font-family="monospace">AISLE JUNCTION</text>' + car(continuation ? 335+t*150 : 210+t*125,310,"#e2c968",90,48,72) + person(410,continuation ? 265 : 180+t*70);
  } else if (kind === "highway") {
    draw = '<rect width="800" height="450" fill="#7d8f77"/><rect x="0" y="70" width="800" height="310" fill="#485b51"/><path d="M0 170H800 M0 275H800" stroke="#d0d6b8" stroke-width="3" stroke-dasharray="35 30"/><path d="M0 80H800 M0 365H800" stroke="#ddcf8b" stroke-width="3"/>';
    for (const y of [120,320]) for (const x of [100,245,390,535,700]) draw += car(x,y,"#bdcab1",90,35,65);
    for (const x of [75,360,515,670]) draw += car(x,225,"#9bb3a5",90,35,65);
    draw += car(continuation ? 205+Math.min(t*2,1)*65 : 200+t*5,225,"#e1bd68",90,35,65);
    draw += '<text x="24" y="415" fill="#e0e6ca" font-size="11" font-family="monospace">FIXED HIGHWAY VIEW / SCHEMATIC</text>';
  } else if (kind === "doorway") {
    draw = '<rect width="800" height="450" fill="#c0c7b3"/><rect x="0" y="205" width="800" height="85" fill="#dae0cc"/><path d="M410 0V205 M410 290V450" stroke="#68826f" stroke-width="17"/><path d="M410 204l70-45" stroke="#8a9e83" stroke-width="5"/><text x="480" y="160" fill="#6b7e66" font-size="11" font-family="monospace">SHARED DOORWAY</text>';
    draw += person(continuation ? 350+t*170 : 230+t*115,248,true) + person(continuation ? 450 : 590-t*120,256);
  } else if (kind === "neighborhood") {
    draw = '<rect width="800" height="450" fill="#94a589"/><rect y="100" width="800" height="250" fill="#53695b"/><path d="M0 225H800" stroke="#c6d2b2" stroke-width="3" stroke-dasharray="28 24"/><rect y="55" width="800" height="45" fill="#bdc9ab"/>';
    for (const x of [60,220,565,710]) draw += `<circle cx="${x}" cy="35" r="30" fill="#607d56"/><circle cx="${x+8}" cy="30" r="17" fill="#749364"/>`;
    draw += car(continuation ? 360+t*180 : 360,continuation ? 118+t*53 : 118,"#e2c46d",90,35,65) + car(100+t*380,285,"#a4bcb0",90,35,65);
    draw += '<text x="24" y="410" fill="#e0e6ca" font-size="11" font-family="monospace">FIXED NEIGHBORHOOD VIEW / SCHEMATIC</text>';
  } else {
    draw = '<rect width="800" height="450" fill="#91a28c"/><rect x="0" y="90" width="800" height="280" fill="#4b6155"/><rect x="0" y="38" width="800" height="52" fill="#c5ceb4"/><rect x="0" y="370" width="800" height="45" fill="#c5ceb4"/><path d="M0 230H800" stroke="#cbd4b6" stroke-width="3" stroke-dasharray="32 24"/><path d="M0 98H800 M0 363H800" stroke="#dae0c5" stroke-width="2"/>';
    for (let y=110;y<360;y+=34) draw += `<rect x="460" y="${y}" width="62" height="16" fill="#d3dbc1" opacity=".85"/>`;
    draw += car(310,122,"#96afa3",90,44,86);
    if (kind === "bus") {
      draw += '<rect x="580" y="46" width="34" height="22" fill="#e3e7d4" stroke="#5b7761"/><text x="584" y="61" fill="#52684f" font-size="10" font-family="monospace">BUS</text>';
      draw += car(continuation ? 380+t*185 : 160+t*220,160,"#d1c582",90,48,126)+person(560,70);
    } else {
      draw += person(continuation ? 490 : 480+t*10,continuation ? 78+t*205 : 65+t*13);
      draw += car(continuation ? 345 : 170+t*175,295,"#e2c46d",90,35,65);
    }
    draw += '<text x="24" y="402" fill="#60765c" font-size="11" font-family="monospace">URBAN APPROACH / SCHEMATIC</text>';
  }
  return `<svg viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${esc(kind)} schematic practice scene"><defs><pattern id="grid" width="25" height="25" patternUnits="userSpaceOnUse"><path d="M25 0H0V25" fill="none" stroke="#fff" stroke-width=".4" opacity=".1"/></pattern></defs>${draw}<rect width="800" height="450" fill="url(#grid)"/><path d="M17 37V17H37 M763 17H783V37 M17 413V433H37 M763 433H783V413" fill="none" stroke="#e0e6c9" stroke-width="1" opacity=".6"/></svg>`;
}
const kinds = {"Urban driving":"crossing", "Warehouse":"warehouse", "Highway":"highway", "Indoor spaces":"doorway", "Neighborhood":"neighborhood"};
function cardKind(s) { return s.id === "bus-stop" ? "bus" : kinds[s.pack] || "crossing"; }
function renderLibrary() {
  $("library-count").textContent = String(catalog.length).padStart(2,"0");
  $("library").innerHTML = catalog.filter(s => filter === "All" || s.pack === filter).map(s => {
    const done = history.some(r => r.scenario_id === s.id);
    return `<button class="scenario-card ${round?.scenario.id === s.id ? "active" : ""}" data-id="${esc(s.id)}"><div class="card-visual">${sceneSVG(cardKind(s),.6)}<span>${s.provenance === "storyboard" ? "STORYBOARD" : "REVIEWED VSS"}</span></div><div class="card-body"><span>${esc(s.pack)}</span><h3>${esc(s.title)}</h3><div><span>${esc(s.difficulty || "Practice")}</span><b>${done ? "✓ PRACTICED" : "↗ OPEN DRILL"}</b></div></div></button>`;
  }).join("");
  $("library").querySelectorAll("button[data-id]").forEach(button => button.onclick = () => startRound(button.dataset.id));
}
let startSerial = 0;
async function startRound(id) {
  const serial = ++startSerial;
  stop();
  try {
    const next = await api("/api/rounds", {scenario_id:id});
    if (serial !== startSerial) return;
    round = next; selected = null; confidence = 70; result = null; phase = "before"; progress = 0;
    $("reveal-panel").hidden = true; $("commit-button").disabled = true;
    $("commit-button").innerHTML = 'Commit & reveal <span>↗</span>';
    $("question").textContent = round.scenario.question; $("context-text").textContent = round.scenario.context;
    $("pack-label").textContent = round.scenario.pack.toUpperCase(); $("skill-label").textContent = round.scenario.skill;
    $("difficulty-label").textContent = round.scenario.difficulty || "Practice";
    $("scene-label").textContent = round.scenario.title;
    $("screen-source").textContent = round.scenario.provenance === "storyboard" ? "SCHEMATIC / DEMO" : "VSS / REVIEWED FOOTAGE";
    $("demo-notice").hidden = round.scenario.provenance !== "storyboard";
    renderOptions(); renderConfidence(); loadPhase("before"); renderLibrary(); showView("train");
  } catch(e) { toast(e.message); }
}
function renderOptions() {
  $("options").innerHTML = round.scenario.options.map(o => `<button class="option ${selected === o.id ? "selected" : ""} ${result && result.answer === o.id ? "correct" : ""} ${result && selected === o.id && !result.correct ? "incorrect" : ""}" data-option="${esc(o.id)}" ${result ? "disabled" : ""}><span>${esc(o.id.toUpperCase())}</span>${esc(o.text)}</button>`).join("");
  $("options").querySelectorAll("button").forEach(b => b.onclick = () => { if(result) return; selected = b.dataset.option; renderOptions(); $("commit-button").disabled = false; });
}
function renderConfidence() {
  $("confidence-label").textContent = {50:"Could go either way",70:"Fairly sure",90:"Very sure"}[confidence];
  document.querySelectorAll("[data-confidence]").forEach(b => { b.classList.toggle("selected",Number(b.dataset.confidence)===confidence); b.disabled = Boolean(result); });
}
function clip() { return phase === "before" ? round.scenario.clip : result.clip; }
function loadPhase(next, seek=null) {
  stop(); phase = next; progress = 0;
  const c = clip(); $("freeze").classList.remove("shown");
  $("phase-label").textContent = next === "before" ? "OBSERVE" : "CONTINUATION";
  $("clip-range").textContent = `${fmt(c.start)} — ${fmt(c.end)}`;
  $("video").hidden = !c.url; $("scene").hidden = Boolean(c.url);
  if(c.url) {
    $("video").src = c.url;
    $("video").onloadedmetadata = () => { if(seek !== null) $("video").currentTime = Math.max(0,seek-c.start); };
    $("video").load();
  } else {
    if(seek !== null) progress = Math.max(0,Math.min(1,(seek-c.start)/(c.end-c.start)));
    paint();
  }
  updateTransport();
}
function paint() { if(!round || clip().url) return; $("scene").innerHTML = sceneSVG(clip().scene,progress,phase === "after"); }
function updateTransport() {
  if(!round) return;
  $("play-button").textContent = playing ? "Ⅱ" : "▶";
  $("play-button").setAttribute("aria-label",playing ? "Pause playback" : "Play current window");
  $("timeline-progress").style.width = `${progress*100}%`;
  $("screen-time").textContent = `${fmt(clip().start+progress*(clip().end-clip().start))}.${Math.floor((clip().start+progress*(clip().end-clip().start))%1*10)}`;
}
function stop() { playing = false; if(animation) cancelAnimationFrame(animation); animation = null; lastTick = null; $("video").pause(); updateTransport(); }
function finish() { stop(); if(phase === "before" && !result) $("freeze").classList.add("shown"); }
function tick(now) {
  if(!playing) return;
  if(lastTick !== null) progress = Math.min(1,progress + (now-lastTick)/1000/(clip().end-clip().start));
  lastTick = now; paint(); updateTransport();
  if(progress>=1) { finish(); return; }
  animation = requestAnimationFrame(tick);
}
async function play() {
  if(!round) return;
  if(playing) { stop(); return; }
  if(progress >= 1) { progress=0; if(clip().url) $("video").currentTime=0; }
  playing=true; $("freeze").classList.remove("shown"); updateTransport();
  if(clip().url) { try { await $("video").play(); } catch { stop(); toast("Video playback failed. Check the VSS connection."); } }
  else { lastTick=null; animation=requestAnimationFrame(tick); }
}
$("video").ontimeupdate = () => { if(!round || !clip().url) return; progress=Math.min(1,$("video").currentTime/(clip().end-clip().start)); updateTransport(); if(progress>=1) finish(); };
$("video").onended = finish;
$("video").onerror = () => { if(round && clip().url) toast("The source video could not be played. Check the workshop stream."); };
$("play-button").onclick = play;
$("restart-button").onclick = () => { loadPhase(phase); play(); };
document.querySelectorAll("[data-confidence]").forEach(b => b.onclick = () => { if(result) return; confidence=Number(b.dataset.confidence); renderConfidence(); });
$("commit-button").onclick = async () => {
  if(!selected || result) return;
  const token = round.round_id, submittedOption=selected, submittedConfidence=confidence;
  $("commit-button").disabled=true; $("commit-button").textContent="Unlocking continuation…";
  try {
    const response = await api(`/api/rounds/${token}/answer`, {option_id:submittedOption,confidence:submittedConfidence});
    if(round.round_id !== token) return;
    result=response; renderOptions(); renderConfidence();
    $("commit-button").textContent="Decision committed ✓";
    history.push({round_id:token,scenario_id:round.scenario.id,title:round.scenario.title,skill:round.scenario.skill,
      provenance:result.provenance,correct:result.correct,confidence:result.confidence,brier:result.brier,
      outcome:result.outcome,evidence:result.evidence,at:new Date().toISOString()});
    history=history.slice(-200);
    try { localStorage.setItem("lastframe-history",JSON.stringify(history)); } catch { toast("Session notes could not be saved in this browser."); }
    $("attempt-count").textContent=String(history.length).padStart(2,"0");
    renderReveal(); renderLibrary(); loadPhase("after"); play();
  } catch(e) { if(round.round_id !== token) return; toast(e.message); $("commit-button").disabled=false; $("commit-button").innerHTML='Commit & reveal <span>↗</span>'; }
};
function renderReveal() {
  const source = result.provenance === "storyboard" ? "ILLUSTRATIVE STORYBOARD — NOT SOURCE FOOTAGE" : "HUMAN-REVIEWED VSS FOOTAGE";
  $("reveal-panel").innerHTML=`<div class="result-top"><div><div class="eyebrow">THE CONTINUATION</div><h2>${esc(result.outcome)}</h2></div><span class="result-tag">${result.correct ? "MATCHED THE CLIP ✓" : "A DIFFERENT CONTINUATION"}</span></div><p>${esc(result.explanation)}</p><div class="evidence-list">${result.evidence.map((e,i)=>`<button class="evidence-item" data-evidence="${i}"><span>${fmt(e.at)} ↗ REPLAY EVIDENCE</span><p>${esc(e.text)}</p></button>`).join("")}</div><div class="reveal-footer"><span>${source}<br>CONFIDENCE ${result.confidence}% · BRIER ${result.brier.toFixed(2)} / LOWER IS BETTER</span><button class="button" id="next-button">Next perspective ↗</button></div>`;
  $("reveal-panel").hidden=false;
  $("reveal-panel").querySelectorAll("[data-evidence]").forEach(b=>b.onclick=()=>{ const at=result.evidence[Number(b.dataset.evidence)].at; loadPhase(at<round.scenario.clip.end ? "before" : "after",at); if(!clip().url) paint(); $("screen").scrollIntoView({behavior:"smooth",block:"center"}); });
  $("next-button").onclick=()=>{ const index=catalog.findIndex(s=>s.id===round.scenario.id); startRound(catalog[(index+1)%catalog.length].id); };
}
function showView(view) {
  $("train-view").hidden=view!=="train"; $("review-view").hidden=view!=="review";
  $("nav-train").classList.toggle("active",view==="train"); $("nav-review").classList.toggle("active",view==="review");
  $("page-label").textContent=view==="train" ? "PRACTICE" : "SESSION REVIEW";
  if(view==="review") { stop(); renderReview(); }
}
function renderReview() {
  if(!history.length) { $("review-content").innerHTML='<p class="empty">Your field notes start with your first decision.</p><button class="button" id="begin-button">Open decision room ↗</button>'; $("begin-button").onclick=()=>showView("train"); return; }
  const matches=history.filter(h=>h.correct).length, brier=history.reduce((a,h)=>a+h.brier,0)/history.length;
  const grouped={}; for(const h of history) { grouped[h.skill] ??= {n:0,m:0}; grouped[h.skill].n++; grouped[h.skill].m+=Number(h.correct); }
  const weakest=Object.entries(grouped).sort((a,b)=>a[1].m/a[1].n-b[1].m/b[1].n)[0];
  $("review-content").innerHTML=`<div class="review-stats"><div class="review-stat"><div class="eyebrow">MATCHED CONTINUATIONS</div><strong>${matches}/${history.length}</strong><span>Prediction matches; not a safety qualification.</span></div><div class="review-stat"><div class="eyebrow">CONFIDENCE CALIBRATION</div><strong>${brier.toFixed(2)}</strong><span>Mean binary Brier score. Lower is better.</span></div><div class="review-stat"><div class="eyebrow">PRACTICE AGAIN</div><strong style="font:22px Georgia,serif">${esc(weakest[0])}</strong><span>${weakest[1].m}/${weakest[1].n} matched. A small practice sample.</span></div></div><p class="muted">Repeated drills are included. Storyboard and VSS results retain their provenance in the export. Confidence scores apply to whether your chosen outcome matched.</p>${[...history].reverse().map(h=>`<div class="review-row"><div><b>${esc(h.title)}</b><p>${esc(h.skill)} · ${h.provenance === "storyboard" ? "Storyboard" : "Reviewed footage"}</p></div><span>${h.correct ? "✓ MATCHED" : "↗ REVIEW"}</span><span>${h.confidence}% CONFIDENCE</span><span>BRIER ${h.brier.toFixed(2)}</span></div>`).join("")}<div class="review-actions"><button id="download-review" class="button">Export field notes ↓</button><button id="clear-review" class="button secondary">Clear session notes</button></div>`;
  $("download-review").onclick=exportNotes;
  $("clear-review").onclick=()=>{ history=[]; try { localStorage.removeItem("lastframe-history"); } catch {} $("attempt-count").textContent="00"; renderReview(); renderLibrary(); };
}
function exportNotes() {
  let text="# LAST FRAME — Session notes\n\nPrediction matches to recorded continuations; not a safety assessment.\n\n";
  for(const h of history) { text+=`## ${h.title}\n\nSource: ${h.provenance}\nSkill: ${h.skill}\nMatch: ${h.correct ? "yes" : "no"}; confidence: ${h.confidence}%; Brier: ${h.brier}\n\n${h.outcome}\n\n`; for(const e of h.evidence || []) text+=`- ${fmt(e.at)}: ${e.text}\n`; text+="\n"; }
  const url=URL.createObjectURL(new Blob([text],{type:"text/markdown"})); const a=document.createElement("a"); a.href=url; a.download="lastframe-session.md"; a.click(); setTimeout(()=>URL.revokeObjectURL(url),1000);
}
$("nav-train").onclick=()=>showView("train"); $("nav-review").onclick=()=>showView("review");
$("export-button").onclick=exportNotes;
$("filters").querySelectorAll("button").forEach(b=>b.onclick=()=>{ filter=b.dataset.filter; $("filters").querySelectorAll("button").forEach(x=>x.classList.toggle("selected",x===b)); renderLibrary(); });
document.querySelectorAll(".close-dialog").forEach(b=>b.onclick=()=>b.closest("dialog").close());
$("connection-button").onclick=()=>$("connection-dialog").showModal();
$("nav-studio").onclick=()=>{ stop(); $("studio-dialog").showModal(); $("studio-connection").innerHTML=status.vss_configured ? '<p class="muted">Workshop credentials configured. Search to verify connectivity.</p>' : '<div class="connection-warning"><p>VSS is not connected. Run LAST FRAME on the workshop VM with your assigned team config to search ingested footage.</p></div>'; $("search-form").querySelector("button").disabled=!status.vss_configured; $("draft-button").disabled=!status.drafting_configured; };
$("search-form").onsubmit=async event=>{
  event.preventDefault(); const button=$("search-form").querySelector("button"); button.disabled=true; $("studio-message").textContent="Searching the video index…"; $("studio-editor").hidden=true;
  try { const results=await api("/api/studio/search",{query:$("search-query").value}); $("studio-message").textContent=results.length ? "Select a result to inspect its neighboring segments." : "No matches. Try another query or inspect the ingestion prompt.";
    $("search-results").innerHTML=results.map((r,i)=>`<button class="search-hit" data-hit="${i}"><span>${esc(r.camera_id)} / ${esc(r.location)} / ${r.start === null ? "TIMING UNAVAILABLE" : fmt(r.start)}</span><p>${esc(typeof r.caption === "string" ? r.caption : JSON.stringify(r.caption))}</p></button>`).join("");
    $("search-results").querySelectorAll("button").forEach(b=>b.onclick=()=>loadSegments(results[Number(b.dataset.hit)]));
  } catch(e) { $("studio-message").textContent=e.message; } finally { button.disabled=false; }
};
async function loadSegments(row) {
  $("studio-message").textContent="Loading the parent video's timeline…";
  try {
    segments=await api("/api/studio/segments",{original_video:row.original_video});
    const pairs=segments.map((s,i)=>({s,i})).filter(({s,i})=>segments[i+1] && Math.abs(s.end-segments[i+1].start)<=.1);
    if(!pairs.length) throw new Error("No adjacent timed segments were returned. Check the VSS response shape or select a longer video.");
    $("before-select").innerHTML=pairs.map(({s,i})=>`<option value="${i}">${fmt(s.start)}–${fmt(s.end)} observation / ${fmt(segments[i+1].start)}–${fmt(segments[i+1].end)} continuation</option>`).join("");
    $("studio-editor").hidden=false; selectPair(); $("studio-message").textContent="Watch both clips, then write or draft a drill. Drafts require human review.";
  } catch(e) { $("studio-message").textContent=e.message; }
}
function currentPair() { const i=Number($("before-select").value); return [segments[i],segments[i+1]]; }
function selectPair() {
  const [before,after]=currentPair();
  $("before-preview").src=`/api/studio/media?source=${encodeURIComponent(before.source)}`;
  $("after-preview").src=`/api/studio/media?source=${encodeURIComponent(after.source)}`;
  $("before-caption").textContent=typeof before.caption === "string" ? before.caption : JSON.stringify(before.caption);
  $("after-caption").textContent=typeof after.caption === "string" ? after.caption : JSON.stringify(after.caption);
  for(const id of ["draft-context","draft-outcome","draft-explanation","draft-evidence","option-a","option-b","option-c"]) $(id).value="";
  $("draft-evidence-at").value=after.start; $("draft-evidence-at").min=before.start; $("draft-evidence-at").max=after.end;
  $("reviewed-check").checked=false;
}
$("before-select").onchange=selectPair;
$("draft-button").onclick=async()=>{
  const [before,after]=currentPair(); $("draft-button").disabled=true; $("studio-message").textContent="Drafting the setup from the observation, then checking the continuation separately…";
  try {
    const draft=await api("/api/studio/draft",{before_source:before.source,after_source:after.source});
    for(const key of ["title","skill","question","context","answer","outcome","explanation"]) $("draft-"+key).value=draft[key] || "";
    for(const o of draft.options || []) if(["a","b","c"].includes(o.id)) $("option-"+o.id).value=o.text;
    $("draft-evidence").value=draft.evidence?.[0]?.text || ""; $("draft-evidence-at").value=draft.evidence?.[0]?.at ?? after.start;
    $("reviewed-check").checked=false; $("studio-message").textContent="Draft ready. Check every claim against the footage, especially the answer and evidence timestamp.";
  } catch(e) { $("studio-message").textContent=e.message; } finally { $("draft-button").disabled=!status.drafting_configured; }
};
$("publish-button").onclick=async()=>{
  const [before,after]=currentPair();
  if(!$("reviewed-check").checked) { $("studio-message").textContent="Watch both clips and confirm the review checkbox before publishing."; return; }
  const scenario={id:"vss-"+crypto.randomUUID(),pack:$("draft-pack").value,provenance:"human-reviewed-vss",reviewed:true,difficulty:"Reviewed drill",original_video:before.original_video,
    before:{start:before.start,end:before.end,source:before.source,original_video:before.original_video},after:{start:after.start,end:after.end,source:after.source,original_video:after.original_video},
    options:["a","b","c"].map(id=>({id,text:$("option-"+id).value})),evidence:[{at:Number($("draft-evidence-at").value),text:$("draft-evidence").value}]};
  for(const key of ["title","skill","question","context","answer","outcome","explanation"]) scenario[key]=$("draft-"+key).value;
  $("publish-button").disabled=true;
  try { await api("/api/studio/publish",scenario); catalog=await api("/api/scenarios"); $("studio-dialog").close(); filter="All"; $("filters").querySelectorAll("button").forEach(b=>b.classList.toggle("selected",b.dataset.filter==="All")); await startRound(scenario.id); toast("Reviewed drill published. The continuation is now hidden until an answer is committed."); }
  catch(e) { $("studio-message").textContent=e.message; } finally { $("publish-button").disabled=false; }
};
async function init() {
  try {
    [catalog,status]=await Promise.all([api("/api/scenarios"),api("/api/status")]);
    $("mode-badge").textContent=status.vss_configured ? "WORKSHOP CONFIGURED" : "STORYBOARD DEMO";
    $("connection-label").textContent=status.vss_configured ? "VSS configured" : "Local practice mode";
    $("connection-copy").textContent=status.vss_configured ? "Search the archive to check connectivity." : "Storyboards today. Your video archive when connected.";
    $("attempt-count").textContent=String(history.length).padStart(2,"0");
    renderLibrary(); if(catalog.length) await startRound(catalog[0].id);
  } catch(e) { toast("Could not load LAST FRAME: "+e.message); }
}
init();
