// Browser-side audio → 16 kHz mono 16-bit PCM WAV for Canary-1B (FINAL-IDEA-v3 §10).
// MediaRecorder webm/opus, or an uploaded m4a/mp3/wav: decodeAudioData → OfflineAudioContext resample
// (downmixes to mono) → Int16 PCM → 44-byte RIFF header. The server needs no ffmpeg for audio.
(function (g) {
  async function toWav16k(blob, rate) {
    rate = rate || 16000;
    const AC = g.AudioContext || g.webkitAudioContext;
    const ac = new AC();
    let audio;
    try {
      audio = await ac.decodeAudioData(await blob.arrayBuffer());
    } finally {
      if (ac.close) ac.close();
    }
    const n = Math.max(1, Math.ceil(audio.duration * rate));
    const off = new OfflineAudioContext(1, n, rate);
    const src = off.createBufferSource();
    src.buffer = audio;
    src.connect(off.destination);
    src.start();
    const pcm = (await off.startRendering()).getChannelData(0);
    const view = new DataView(new ArrayBuffer(44 + pcm.length * 2));
    const tag = (o, s) => { for (let i = 0; i < s.length; i++) view.setUint8(o + i, s.charCodeAt(i)); };
    tag(0, "RIFF"); view.setUint32(4, 36 + pcm.length * 2, true); tag(8, "WAVE");
    tag(12, "fmt "); view.setUint32(16, 16, true); view.setUint16(20, 1, true); view.setUint16(22, 1, true);
    view.setUint32(24, rate, true); view.setUint32(28, rate * 2, true); view.setUint16(32, 2, true);
    view.setUint16(34, 16, true); tag(36, "data"); view.setUint32(40, pcm.length * 2, true);
    for (let i = 0; i < pcm.length; i++) {
      const s = Math.max(-1, Math.min(1, pcm[i]));
      view.setInt16(44 + i * 2, s < 0 ? s * 0x8000 : s * 0x7fff, true);
    }
    return new Blob([view], { type: "audio/wav" });
  }
  g.PerjuryWav = { toWav16k };
})(window);
