/* ==========================================================================
   ABS Débouchage — animation du héros : une canalisation se débouche
   Canvas 2D, 3 calques : arrière (tuyau), eau (filtre « goo »), avant (verre,
   bouchon, furet, morceaux). Se joue une fois quand le héros est visible,
   s'arrête sur l'état « débouché », bouton Rejouer. Respecte reduced-motion.
   ========================================================================== */
(function () {
  var box = document.querySelector("[data-pipe]");
  if (!box) return;
  var cBack = box.querySelector(".pc-back"), cWater = box.querySelector(".pc-water"), cFront = box.querySelector(".pc-front");
  var chip = box.querySelector(".pipe-chip"), chipTxt = chip.querySelector("span:last-child"), replay = box.querySelector(".pipe-replay");
  var L = JSON.parse(box.getAttribute("data-pipe"));
  var mq = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---- géométrie (unités logiques 640 x 420) ---- */
  var W = 640, H = 420, CY = 196, RO = 76, RI = 62, XM = 520, XC = 300, C1 = 150, C2 = 404;
  var ctxB = cBack.getContext("2d"), ctxW = cWater.getContext("2d"), ctxF = cFront.getContext("2d");
  var scale = 1, dpr = 1;

  function resize() {
    var w = box.clientWidth; dpr = Math.min(window.devicePixelRatio || 1, 2); scale = w / W;
    [cBack, cWater, cFront].forEach(function (c) { c.width = Math.round(w * dpr); c.height = Math.round(w * H / W * dpr); });
    [ctxB, ctxW, ctxF].forEach(function (c) { c.setTransform(scale * dpr, 0, 0, scale * dpr, 0, 0); });
    drawBack();
    if (!running) render(state.t);
  }

  /* ---- bruit simple pour la forme du bouchon ---- */
  var seed = [];
  for (var i = 0; i < 22; i++) seed.push(Math.random());
  function clogPath(ctx, x, y, r, wob) {
    ctx.beginPath();
    for (var k = 0; k <= 22; k++) {
      var a = k / 22 * Math.PI * 2, n = seed[k % 22];
      var rr = r * (0.86 + 0.2 * n + 0.04 * Math.sin(a * 3 + wob));
      var px = x + Math.cos(a) * rr * 0.72, py = y + Math.sin(a) * rr;
      if (k === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.closePath();
  }

  /* ---- calque arrière : fond, intérieur du tuyau, sortie, grille d'évacuation ---- */
  function drawBack() {
    var c = ctxB; c.clearRect(0, 0, W, H);
    // halo
    var g = c.createRadialGradient(W * 0.55, CY, 20, W * 0.55, CY, 360);
    g.addColorStop(0, "rgba(56,130,246,.20)"); g.addColorStop(1, "rgba(56,130,246,0)");
    c.fillStyle = g; c.fillRect(0, 0, W, H);
    // grille d'évacuation au sol
    var gx = XM + 52, gy = 372;
    c.save(); c.translate(gx, gy); c.scale(1, 0.32);
    var gg = c.createRadialGradient(0, 0, 4, 0, 0, 70); gg.addColorStop(0, "rgba(47,127,209,.55)"); gg.addColorStop(1, "rgba(47,127,209,0)");
    c.fillStyle = gg; c.beginPath(); c.arc(0, 0, 70, 0, Math.PI * 2); c.fill();
    c.fillStyle = "#0a1626"; c.strokeStyle = "#5d6b7c"; c.lineWidth = 4; c.beginPath(); c.arc(0, 0, 42, 0, Math.PI * 2); c.fill(); c.stroke();
    c.strokeStyle = "#3a4757"; c.lineWidth = 4;
    for (var k = -2; k <= 2; k++) { c.beginPath(); c.moveTo(k * 14, -38); c.lineTo(k * 14, 38); c.stroke(); }
    c.restore();
    // paroi arrière du tuyau (intérieur)
    var ig = c.createLinearGradient(0, CY - RI, 0, CY + RI);
    ig.addColorStop(0, "#0c2238"); ig.addColorStop(0.5, "#14365a"); ig.addColorStop(1, "#0a1d31");
    c.fillStyle = ig; c.fillRect(-10, CY - RI, XM + 10, RI * 2);
    // fond de la sortie
    c.save(); c.translate(XM, CY); c.scale(0.24, 1);
    c.fillStyle = "#06121f"; c.beginPath(); c.arc(0, 0, RI, 0, Math.PI * 2); c.fill(); c.restore();
  }

  /* ---- état de l'animation ---- */
  var state = { t: 0 }, running = false, last = 0, raf = 0, played = false;
  var water = [], chunks = [];
  function resetSim() {
    water = []; chunks = []; state.t = 0;
    for (var k = 0; k < 120; k++) water.push(backedParticle());
  }
  function backedParticle() {
    return { x: 10 + Math.random() * (XC - RI * 0.7 - 20), y: CY - RI + 12 + Math.random() * (RI * 2 - 24), vx: 0, vy: 0, r: 12 + Math.random() * 5, out: false, flow: false, hi: Math.random() < 0.25 };
  }
  function ease(t) { return t < 0 ? 0 : t > 1 ? 1 : 1 - Math.pow(1 - t, 3); }
  function seg(t, a, b) { return t <= a ? 0 : t >= b ? 1 : (t - a) / (b - a); }

  var T = { tool: [1.6, 3.4], drill: [3.4, 4.7], burst: 4.7, back: [5.4, 7.2], end: 9.8 };

  function stepSim(dt) {
    var t = state.t, burst = t >= T.burst;
    var clogLeft = XC - RI * 0.62 * clogScale(t) - 4;
    // flux continu après l'explosion
    if (burst && t < 7.6 && Math.random() < 0.9) {
      for (var n = 0; n < 2; n++) water.push({ x: -10, y: CY + RI - 18 - Math.random() * 40, vx: 4 + Math.random() * 2, vy: 0, r: 10 + Math.random() * 5, out: false, flow: true, hi: Math.random() < 0.25 });
    }
    for (var k = water.length - 1; k >= 0; k--) {
      var p = water[k];
      if (!burst && !p.flow) {
        // eau bloquée : elle s'agite et pousse contre le bouchon
        p.vx += (Math.random() - 0.45) * 0.6; p.vy += (Math.random() - 0.5) * 0.6;
        p.vx *= 0.9; p.vy *= 0.9;
        p.x += p.vx * dt; p.y += p.vy * dt;
        if (p.x > clogLeft - p.r * 0.4) { p.x = clogLeft - p.r * 0.4; p.vx *= -0.5; }
      } else {
        if (!p.flow) { p.flow = true; p.vx = 3 + Math.random() * 3; }
        if (!p.out) {
          p.vx += 0.12 * dt; if (p.vx > 7) p.vx = 7;
          p.vy += 0.25 * dt; // l'eau retombe au fond du tuyau
          p.x += p.vx * dt; p.y += p.vy * dt;
          if (p.x > XM - 4) { p.out = true; p.vx = Math.min(p.vx, 2.6 + Math.random() * 0.8); p.vy = Math.max(p.vy, 0.5); }
        } else {
          p.vy += 0.42 * dt; p.vx *= 0.995;
          p.x += p.vx * dt; p.y += p.vy * dt;
          if (p.y > 362) { if (Math.random() < 0.35) splash(p.x); water.splice(k, 1); continue; }
          if (p.y > H + 30 || p.x > W + 30) { water.splice(k, 1); continue; }
        }
      }
      if (!p.out) {
        var top = CY - RI + p.r * 0.7, bot = CY + RI - p.r * 0.7;
        if (p.y < top) { p.y = top; p.vy = Math.abs(p.vy) * 0.3; }
        if (p.y > bot) { p.y = bot; p.vy = -Math.abs(p.vy) * 0.25; }
        if (p.x < 0 && !burst) { p.x = 0; p.vx = Math.abs(p.vx); }
      }
    }
    for (var d = drops.length - 1; d >= 0; d--) { var q = drops[d]; q.vy += 0.3 * dt; q.x += q.vx * dt; q.y += q.vy * dt; q.life -= 0.03 * dt; if (q.life <= 0) drops.splice(d, 1); }
    // morceaux du bouchon
    for (var j = chunks.length - 1; j >= 0; j--) {
      var c = chunks[j];
      c.vy += 0.3 * dt; c.x += c.vx * dt; c.y += c.vy * dt; c.a += c.va * dt;
      if (c.x < XM) { if (c.y > CY + RI - c.r) { c.y = CY + RI - c.r; c.vy *= -0.3; c.vx *= 0.96; c.vx += 0.25 * dt; } if (c.y < CY - RI + c.r) { c.y = CY - RI + c.r; c.vy = Math.abs(c.vy); } }
      if (c.y > H + 30 || c.x > W + 30) chunks.splice(j, 1);
    }
  }
  var drops = [];
  function splash(x) { for (var k = 0; k < 3; k++) drops.push({ x: x, y: 362, vx: (Math.random() - 0.5) * 3, vy: -2 - Math.random() * 2.5, life: 1 }); }
  function clogScale(t) {
    if (t < T.drill[0]) return 1;
    if (t < T.burst) return 1 - 0.35 * seg(t, T.drill[0], T.burst);
    return 0;
  }
  function emitChunks(n, spread) {
    for (var k = 0; k < n; k++) {
      var a = (Math.random() - 0.5) * spread;
      chunks.push({ x: XC + (Math.random() - 0.5) * 30, y: CY + (Math.random() - 0.5) * RI, vx: 3 + Math.random() * 6, vy: Math.sin(a) * 5 - 1, r: 3 + Math.random() * 6, a: Math.random() * 6, va: (Math.random() - 0.5) * 0.4, col: Math.random() < 0.5 ? "#6b4423" : "#8a5a2e" });
    }
  }

  /* ---- étiquette d'état ---- */
  var phase = -1;
  function setPhase(n) {
    if (n === phase) return; phase = n;
    chip.className = "pipe-chip s" + n;
    chipTxt.textContent = L.states[n];
  }

  /* ---- rendu ---- */
  function render(t) {
    // eau
    ctxW.clearRect(0, 0, W, H);
    for (var k = 0; k < water.length; k++) {
      var p = water[k];
      ctxW.fillStyle = p.hi ? "#7cc0ff" : (p.out ? "#4aa3ff" : "#2f86ef");
      ctxW.beginPath(); ctxW.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctxW.fill();
    }
    for (var d = 0; d < drops.length; d++) { var q = drops[d]; ctxW.fillStyle = "rgba(124,192,255," + q.life + ")"; ctxW.beginPath(); ctxW.arc(q.x, q.y, 5, 0, Math.PI * 2); ctxW.fill(); }
    var c = ctxF; c.clearRect(0, 0, W, H);
    // bouchon
    var sc = clogScale(t);
    if (sc > 0.02) {
      var shake = t > T.drill[0] && t < T.burst ? (Math.random() - 0.5) * 4 : 0;
      var wob = t * 2.2;
      c.save(); c.translate(shake, shake * 0.6);
      var cg = c.createRadialGradient(XC - 12, CY - 20, 6, XC, CY, RI);
      cg.addColorStop(0, "#9a6a3c"); cg.addColorStop(0.55, "#5e3b1f"); cg.addColorStop(1, "#33200f");
      clogPath(c, XC, CY, RI * sc, wob); c.fillStyle = cg; c.fill();
      // cheveux / filasse
      c.strokeStyle = "rgba(205,170,120,.55)"; c.lineWidth = 1.6;
      for (var h = 0; h < 7; h++) {
        var hy = CY - RI * 0.7 * sc + h * RI * 0.22 * sc;
        c.beginPath(); c.moveTo(XC - RI * 0.5 * sc, hy); c.quadraticCurveTo(XC + Math.sin(h + wob) * 10, hy + 8, XC + RI * 0.5 * sc, hy - 4); c.stroke();
      }
      c.fillStyle = "rgba(30,18,8,.55)";
      [[-14, -18, 6], [10, 8, 8], [-6, 26, 5], [14, -30, 4]].forEach(function (d) { c.beginPath(); c.arc(XC + d[0] * sc, CY + d[1] * sc, d[2] * sc, 0, Math.PI * 2); c.fill(); });
      c.restore();
    }
    // morceaux
    for (var j = 0; j < chunks.length; j++) {
      var ch = chunks[j]; c.save(); c.translate(ch.x, ch.y); c.rotate(ch.a); c.fillStyle = ch.col;
      c.beginPath(); c.moveTo(-ch.r, -ch.r * 0.4); c.lineTo(ch.r * 0.6, -ch.r); c.lineTo(ch.r, ch.r * 0.5); c.lineTo(-ch.r * 0.3, ch.r); c.closePath(); c.fill(); c.restore();
    }
    // furet électrique
    var tin = ease(seg(t, T.tool[0], T.tool[1])), tout = ease(seg(t, T.back[0], T.back[1]));
    var tx = -60 + (XC - RI * 0.62 - 14 + 60) * tin - (XC + 40) * tout;
    if (t > T.tool[0] && tx > -40) {
      var spin = t * (t > T.drill[0] && t < T.burst + 0.4 ? 40 : 14);
      c.strokeStyle = "#c9d2dc"; c.lineWidth = 6; c.lineCap = "round";
      c.beginPath(); c.moveTo(-20, CY - 4); c.lineTo(tx - 10, CY - 4); c.stroke();
      c.strokeStyle = "rgba(60,72,88,.9)"; c.lineWidth = 2;
      for (var s2 = -20 + ((spin * 3) % 12); s2 < tx - 12; s2 += 12) { c.beginPath(); c.moveTo(s2, CY - 8); c.lineTo(s2 + 5, CY); c.stroke(); }
      // tête
      c.save(); c.translate(tx, CY - 4);
      var hg = c.createLinearGradient(0, -16, 0, 16); hg.addColorStop(0, "#f1f4f7"); hg.addColorStop(0.5, "#9aa6b3"); hg.addColorStop(1, "#5c6876");
      c.fillStyle = hg; c.beginPath(); c.moveTo(-14, -12); c.lineTo(10, -8); c.lineTo(20, 0); c.lineTo(10, 8); c.lineTo(-14, 12); c.closePath(); c.fill();
      c.strokeStyle = "#c2410c"; c.lineWidth = 2.4;
      for (var b = 0; b < 3; b++) { var aa = spin + b * 2.09; c.beginPath(); c.moveTo(-8 + b * 7, Math.sin(aa) * 11); c.lineTo(-4 + b * 7, -Math.sin(aa) * 11); c.stroke(); }
      c.restore();
      // jet haute pression
      if (t > T.drill[0] + 0.4 && t < T.burst + 0.5) {
        c.strokeStyle = "rgba(200,232,255,.85)"; c.lineWidth = 2;
        for (var q = 0; q < 6; q++) { var off = (Math.random() - 0.5) * 34; c.beginPath(); c.moveTo(tx + 20, CY - 4 + off * 0.3); c.lineTo(tx + 40 + Math.random() * 20, CY - 4 + off); c.stroke(); }
      }
    }
    drawGlass(c);
  }

  /* ---- verre, colliers et bord de sortie (au premier plan) ---- */
  function drawGlass(c) {
    // épaisseur du tuyau (haut et bas)
    var wg = c.createLinearGradient(0, CY - RO, 0, CY - RI);
    wg.addColorStop(0, "rgba(190,215,240,.55)"); wg.addColorStop(1, "rgba(120,160,200,.18)");
    c.fillStyle = wg; c.fillRect(-10, CY - RO, XM + 10, RO - RI);
    var bg = c.createLinearGradient(0, CY + RI, 0, CY + RO);
    bg.addColorStop(0, "rgba(120,160,200,.18)"); bg.addColorStop(1, "rgba(190,215,240,.45)");
    c.fillStyle = bg; c.fillRect(-10, CY + RI, XM + 10, RO - RI);
    // reflets
    c.fillStyle = "rgba(255,255,255,.28)"; c.fillRect(-10, CY - RI + 6, XM + 10, 5);
    c.fillStyle = "rgba(255,255,255,.12)"; c.fillRect(-10, CY - RI + 16, XM + 10, 10);
    c.fillStyle = "rgba(255,255,255,.10)"; c.fillRect(-10, CY + RI - 14, XM + 10, 4);
    c.strokeStyle = "rgba(220,235,250,.6)"; c.lineWidth = 1.5;
    c.beginPath(); c.moveTo(-10, CY - RO); c.lineTo(XM, CY - RO); c.moveTo(-10, CY + RO); c.lineTo(XM, CY + RO); c.stroke();
    // colliers métalliques
    [C1, C2].forEach(function (x) {
      var mg = c.createLinearGradient(0, CY - RO - 8, 0, CY + RO + 8);
      mg.addColorStop(0, "#e9eef3"); mg.addColorStop(0.18, "#aeb9c5"); mg.addColorStop(0.5, "#6f7c8b"); mg.addColorStop(0.82, "#b7c2cd"); mg.addColorStop(1, "#59636f");
      c.fillStyle = mg; c.fillRect(x - 13, CY - RO - 8, 26, RO * 2 + 16);
      c.fillStyle = "rgba(0,0,0,.25)"; c.fillRect(x + 11, CY - RO - 8, 2, RO * 2 + 16);
      c.fillStyle = "#3e4955"; [CY - RO + 4, CY + RO - 4].forEach(function (y) { c.beginPath(); c.arc(x, y, 3.2, 0, Math.PI * 2); c.fill(); });
    });
    // bord de sortie (ellipse en perspective)
    c.save(); c.translate(XM, CY);
    var rg = c.createLinearGradient(0, -RO, 0, RO); rg.addColorStop(0, "#f1f5f9"); rg.addColorStop(0.5, "#8d9aa8"); rg.addColorStop(1, "#c9d3dd");
    c.scale(0.24, 1); c.strokeStyle = rg; c.lineWidth = 14 / 0.24 * 0.24 * 4; c.beginPath(); c.arc(0, 0, (RO + RI) / 2, 0, Math.PI * 2);
    c.restore(); c.save(); c.translate(XM, CY); c.scale(0.24, 1); c.lineWidth = 6; c.strokeStyle = "rgba(230,240,250,.9)"; c.beginPath(); c.arc(0, 0, RO, -Math.PI / 2, Math.PI / 2); c.stroke();
    c.lineWidth = 3; c.strokeStyle = "rgba(160,180,200,.8)"; c.beginPath(); c.arc(0, 0, RI, -Math.PI / 2, Math.PI / 2); c.stroke(); c.restore();
  }

  /* ---- boucle ---- */
  function frame(now) {
    var real = Math.min(0.25, Math.max(0, (now - last) / 1000)); last = now;
    var prev = state.t; state.t += real;
    var t = state.t;
    var steps = Math.max(1, Math.ceil(real * 60 / 2)), dt = real * 60 / steps;
    if (prev < T.drill[0] + 0.3 && t >= T.drill[0] + 0.3) emitChunks(6, 1.2);
    if (prev < T.drill[0] + 0.8 && t >= T.drill[0] + 0.8) emitChunks(6, 1.2);
    if (prev < T.burst && t >= T.burst) emitChunks(34, 2.4);
    setPhase(t < T.tool[0] ? 0 : t < T.drill[0] + 0.4 ? 1 : t < T.burst ? 2 : 3);
    for (var st = 0; st < steps; st++) stepSim(dt);
    render(t);
    if (t < T.end || water.length || chunks.length) raf = requestAnimationFrame(frame);
    else stopRun();
  }
  function play() {
    cancelAnimationFrame(raf); resetSim(); phase = -1; running = true; played = true;
    box.classList.add("is-playing"); box.classList.remove("is-done");
    last = performance.now(); raf = requestAnimationFrame(frame);
  }
  function stopRun() { running = false; scheduleLoop(); box.classList.remove("is-playing"); box.classList.add("is-done"); drawStill(true); }

  /* état final fixe (pour reduced-motion et avant lecture) */
  function drawStill(final) {
    resetSim();
    if (final) {
      water = []; state.t = 6.2; setPhase(3);
      water = []; drops = []; chunks = [];
      for (var k = 0; k < 40; k++) water.push({ x: -6 + k * 13.5, y: CY + RI - 13 - Math.random() * 5, r: 12 + Math.random() * 3, out: false, hi: k % 4 === 0 });
      for (var m = 0; m < 16; m++) { var u = m / 15; water.push({ x: XM + 2 + u * 50, y: CY + RI - 8 + u * u * 150 + u * 8, r: 11 - u * 3, out: true, hi: m % 4 === 0 }); }
      for (var n2 = 0; n2 < 5; n2++) drops.push({ x: XM + 46 + (n2 - 2) * 9, y: 352 - (n2 % 2) * 8, vx: 0, vy: 0, life: 0.8 });
      state.t = 99;
    } else { setPhase(0); }
    render(state.t);
  }

  /* ---- lecture en boucle, pause manuelle, veille hors écran ---- */
  var userPaused = false, inView = false, loopTimer = 0;
  var ICON_PAUSE = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5v14M15 5v14"/></svg>';
  var ICON_PLAY = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="m7 4 13 8-13 8z"/></svg>';
  function setBtn() {
    replay.innerHTML = userPaused ? ICON_PLAY : ICON_PAUSE;
    replay.setAttribute("aria-label", userPaused ? L.play : L.pause);
    replay.setAttribute("aria-pressed", userPaused ? "true" : "false");
  }
  function scheduleLoop() {
    clearTimeout(loopTimer);
    if (userPaused || !inView || document.hidden || mq.matches) return;
    loopTimer = setTimeout(function () { if (!userPaused && inView && !document.hidden) play(); }, 2600);
  }
  function halt() { clearTimeout(loopTimer); if (running) { cancelAnimationFrame(raf); running = false; box.classList.remove("is-playing"); } }
  function resume() {
    if (userPaused || mq.matches) return;
    if (running) return;
    if (state.t > 0 && state.t < T.end) { running = true; box.classList.add("is-playing"); last = performance.now(); raf = requestAnimationFrame(frame); }
    else play();
  }
  replay.addEventListener("click", function () {
    userPaused = !userPaused; setBtn();
    if (userPaused) { halt(); } else { resume(); }
  });
  window.addEventListener("resize", function () { resize(); });
  resize();

  function init() {
    setBtn();
    if (mq.matches) { drawStill(true); box.classList.add("is-done"); return; }
    drawStill(false);
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (en) {
        inView = en[0].isIntersecting;
        if (inView) { if (!played) setTimeout(resume, 400); else resume(); } else halt();
      }, { threshold: 0.3 }).observe(box);
    } else { inView = true; play(); }
  }
  if (mq.addEventListener) mq.addEventListener("change", function () { if (mq.matches && running) { cancelAnimationFrame(raf); stopRun(); drawStill(true); } });
  document.addEventListener("visibilitychange", function () { if (document.hidden) halt(); else if (inView) resume(); });
  init();
})();
