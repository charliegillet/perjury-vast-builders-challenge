/* Progressive truck inventory. Its scope is independent of the current video playhead. */
(() => {
  const panel = document.createElement('details');
  panel.className = 'truck-inventory';
  panel.innerHTML = '<summary>Truck evidence <span class="truck-summary">Detect trucks and inspect colour evidence</span></summary><div class="truck-toolbar"><button type="button" class="ghost truck-start">Scan all selected-camera footage</button><span class="truck-status" role="status" aria-live="polite">Select a VAST location and assessment camera.</span></div><p class="truck-scope">Colours require agreement across multiple clear frames. Tracks stay local to each segment; this is not a count of unique vehicles across the whole archive. Braking is assessed separately.</p><div class="truck-results"></div>';
  document.querySelector('.wall-wrap')?.append(panel);
  const style = document.createElement('style');
  style.textContent = '.truck-inventory{margin-top:12px;border-top:1px solid #e8e8e8;padding-top:10px;font:inherit;font-size:12px}.truck-inventory summary{cursor:pointer;font-weight:600}.truck-summary,.truck-status,.truck-scope{color:#777;font-weight:400}.truck-summary{margin-left:8px;font-size:11px}.truck-toolbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:12px}.truck-toolbar button{padding:7px 10px;border:1px solid #ddd;border-radius:6px;background:white;cursor:pointer}.truck-scope{font-size:11px;line-height:1.5}.truck-results{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;max-height:340px;overflow:auto}.truck-card{border:1px solid #e5e5e5;border-radius:6px;padding:8px;min-width:0}.truck-card img{width:100%;aspect-ratio:16/9;object-fit:contain;background:#fafafa}.truck-card p{margin:5px 0;overflow-wrap:anywhere}.truck-card small{color:#777}.truck-card a{color:inherit}.truck-colour{font-weight:600}';
  document.head.append(style);
  const status = panel.querySelector('.truck-status');
  const summary = panel.querySelector('.truck-summary');
  const results = panel.querySelector('.truck-results');
  const startButton = panel.querySelector('.truck-start');
  let currentKey = '', generation = 0, timer = null;
  const escape = value => String(value ?? '').replace(/[&<>"']/g, x => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]));
  const selection = () => typeof S !== 'undefined' && S.scope && S.assessmentCamera ? `${S.scope.id}:${S.assessmentCamera}` : '';
  const render = data => {
    status.textContent = `${data.state} · ${data.sources_scanned}/${data.sources_total} segments scanned · ${data.tracks_processed}/${data.tracks_detected} tracks processed${data.failed_sources ? ` · ${data.failed_sources} segments unavailable` : ''}`;
    const known = data.tracks.filter(t => t.state === 'classified');
    summary.textContent = `${known.length} tracks with colour evidence · ${data.tracks_detected} detected`;
    results.innerHTML = [...data.tracks].sort((a,b)=>Number(b.colour==='white')-Number(a.colour==='white')).slice(0,100).map(t => `<article class="truck-card"><p class="truck-colour">${escape(t.colour ? `${t.colour} truck` : 'Colour uncertain')}</p>${t.evidence?.length ? `<a href="api/trucks/evidence/${encodeURIComponent(data.id)}/${encodeURIComponent(t.id)}" target="_blank" rel="noopener"><img loading="lazy" src="api/trucks/evidence/${encodeURIComponent(data.id)}/${encodeURIComponent(t.id)}" alt="Timestamped truck evidence"/></a>` : ''}<p><small>${escape(t.camera)} · ${t.first_seen.toFixed(2)}–${t.last_seen.toFixed(2)}s in segment</small></p><small>${escape(t.reason || 'Awaiting colour assessment')}</small></article>`).join('');
  };
  const poll = async (id, g) => {
    try {
      const response = await fetch(`api/trucks/inventory/${encodeURIComponent(id)}`);
      if (!response.ok) throw new Error('Inventory status unavailable');
      const data = await response.json();
      if (g !== generation) return;
      render(data);
      if (['scanning','classifying'].includes(data.state)) timer=setTimeout(()=>poll(id,g),2000);
      else startButton.disabled=false;
    } catch (error) { if(g===generation) {status.textContent=error.message;startButton.disabled=false;} }
  };
  startButton.onclick = async () => {
    if (!selection()) {status.textContent='Choose a VAST location and assessment camera first.';return;}
    if (S.busy) {status.textContent='Wait for the current assessment before starting a full scan.';return;}
    const g=++generation; currentKey=selection();clearTimeout(timer);startButton.disabled=true;
    status.textContent='Loading real VAST detection evidence…';
    try {
      const response=await fetch('api/trucks/inventory',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({scope_id:S.scope.id,camera:S.assessmentCamera})});
      const data=await response.json();
      if(g!==generation)return;
      if(!response.ok)throw new Error(typeof data.detail==='string'?data.detail:'Could not start inventory');
      render(data);poll(data.id,g);
    } catch(error) {if(g===generation){status.textContent=error.message;startButton.disabled=false;}}
  };
  setInterval(()=>{
    const key=selection();
    if(currentKey && key!==currentKey) {generation++;clearTimeout(timer);currentKey='';results.innerHTML='';summary.textContent='Detect trucks and inspect colour evidence';status.textContent='Selection changed. Scan this camera to load its evidence.';startButton.disabled=false;}
  },500);
})();
