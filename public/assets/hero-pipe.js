/* ==========================================================================
   ABS Débouchage — animation du héros (en continu)
   Canalisation en verre vue en coupe : l'eau est bloquée par un bouchon,
   le furet + la haute pression le cassent, l'eau s'écoule, tombe dans la
   grille, descend dans le regard puis part dans l'égout. Le cycle reprend
   sans interruption (le bouchon se reforme doucement).
   Canvas 2D, 3 calques. Bouton pause (WCAG 2.2.2), veille hors écran.
   ========================================================================== */
(function () {
  var box = document.querySelector("[data-pipe]");
  if (!box) return;
  var cBack = box.querySelector(".pc-back"), cWater = box.querySelector(".pc-water"), cFront = box.querySelector(".pc-front");
  var chip = box.querySelector(".pipe-chip"), chipTxt = chip.querySelector("span:last-child"), btn = box.querySelector(".pipe-replay");
  var L = JSON.parse(box.getAttribute("data-pipe"));

  /* ---- géométrie (unités logiques 640 x 480) ---- */
  var W = 640, H = 480, CY = 176, RO = 72, RI = 58, XM = 466, XC = 270, C1 = 128, C2 = 366;
  var GY = 360;            // niveau du sol
  var DX = 516;            // axe de la grille / du regard
  var DW = 15;             // demi-largeur du regard
  var SY = 432, SR = 22;   // égout horizontal
  var ctxB = cBack.getContext("2d"), ctxW = cWater.getContext("2d"), ctxF = cFront.getContext("2d");
  var scale = 1, dpr = 1;

  function resize() {
    var w = box.clientWidth; if (!w) return;
    dpr = Math.min(window.devicePixelRatio || 1, 2); scale = w / W;
    [cBack, cWater, cFront].forEach(function (c) { c.width = Math.round(w * dpr); c.height = Math.round(w * H / W * dpr); });
    [ctxB, ctxW, ctxF].forEach(function (c) { c.setTransform(scale * dpr, 0, 0, scale * dpr, 0, 0); });
    drawBack(); render(state.t);
  }

  /* ---- forme du bouchon ---- */
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

  /* ---- calque arrière ---- */
  var stones = [];
  for (var s = 0; s < 46; s++) stones.push([Math.random() * W, GY + 14 + Math.random() * (H - GY - 14), 1.5 + Math.random() * 3.5]);
  function drawBack() {
    var c = ctxB; c.clearRect(0, 0, W, H);
    var g = c.createRadialGradient(W * 0.5, CY, 20, W * 0.5, CY, 380);
    g.addColorStop(0, "rgba(56,130,246,.20)"); g.addColorStop(1, "rgba(56,130,246,0)");
    c.fillStyle = g; c.fillRect(0, 0, W, GY);
    // sol en coupe
    var sg = c.createLinearGradient(0, GY, 0, H);
    sg.addColorStop(0, "#1b2737"); sg.addColorStop(1, "#0c141f");
    c.fillStyle = sg; c.fillRect(0, GY, W, H - GY);
    c.fillStyle = "rgba(255,255,255,.05)";
    stones.forEach(function (st) { c.beginPath(); c.ellipse(st[0], st[1], st[2] * 1.4, st[2], 0, 0, Math.PI * 2); c.fill(); });
    c.fillStyle = "#2c3b4e"; c.fillRect(0, GY - 2, W, 4);
    // regard + égout (intérieur sombre)
    c.fillStyle = "#050d18";
    c.fillRect(DX - DW, GY, DW * 2, SY - GY);
    c.fillRect(DX - DW, SY - SR, W - DX + DW + 10, SR * 2);
    // halo de la grille
    c.save(); c.translate(DX, GY); c.scale(1, 0.3);
    var gg = c.createRadialGradient(0, 0, 4, 0, 0, 72); gg.addColorStop(0, "rgba(47,127,209,.5)"); gg.addColorStop(1, "rgba(47,127,209,0)");
    c.fillStyle = gg; c.beginPath(); c.arc(0, 0, 72, 0, Math.PI * 2); c.fill(); c.restore();
    // intérieur de la canalisation
    var ig = c.createLinearGradient(0, CY - RI, 0, CY + RI);
    ig.addColorStop(0, "#0c2238"); ig.addColorStop(0.5, "#14365a"); ig.addColorStop(1, "#0a1d31");
    c.fillStyle = ig; c.fillRect(-10, CY - RI, XM + 10, RI * 2);
    c.save(); c.translate(XM, CY); c.scale(0.24, 1);
    c.fillStyle = "#06121f"; c.beginPath(); c.arc(0, 0, RI, 0, Math.PI * 2); c.fill(); c.restore();
  }

  /* ---- simulation ---- */
  var T = { fill: 1.4, tool: [1.6, 3.3], drill: [3.3, 4.6], burst: 4.6, back: [5.3, 7.0], stopFlow: 7.4, end: 10.6 };
  var state = { t: 0 }, running = false, last = 0, raf = 0;
  var water = [], chunks = [], drops = [];
  function resetSim() { water = []; chunks = []; drops = []; state.t = 0; }
  function ease(t) { return t < 0 ? 0 : t > 1 ? 1 : 1 - Math.pow(1 - t, 3); }
  function seg(t, a, b) { return t <= a ? 0 : t >= b ? 1 : (t - a) / (b - a); }
  function clogScale(t) {
    if (t < 0.7) return ease(t / 0.7);                 // le bouchon se reforme
    if (t < T.drill[0]) return 1;
    if (t < T.burst) return 1 - 0.35 * seg(t, T.drill[0], T.burst);
    return 0;
  }
  function newDrop(x, y, vx, vy, r, flow) { return { x: x, y: y, vx: vx, vy: vy, r: r, flow: flow, zone: 0, hi: Math.random() < 0.25 }; }
  function splash(x, y) { for (var k = 0; k < 3; k++) drops.push({ x: x, y: y, vx: (Math.random() - 0.5) * 3, vy: -2 - Math.random() * 2.5, life: 1 }); }
  function emitChunks(n, spread) {
    for (var k = 0; k < n; k++) {
      var a = (Math.random() - 0.5) * spread;
      chunks.push({ x: XC + (Math.random() - 0.5) * 30, y: CY + (Math.random() - 0.5) * RI, vx: 3 + Math.random() * 6, vy: Math.sin(a) * 5 - 1, r: 3 + Math.random() * 6, a: Math.random() * 6, va: (Math.random() - 0.5) * 0.4, col: Math.random() < 0.5 ? "#6b4423" : "#8a5a2e", zone: 0 });
    }
  }

  // zones : 0 = canalisation, 1 = chute libre, 2 = regard, 3 = égout
  function routeFree(p, dt, isChunk) {
    p.vy += 0.42 * dt; p.vx *= 0.995; p.x += p.vx * dt; p.y += p.vy * dt;
    if (p.y >= GY - 2) {
      if (Math.abs(p.x - DX) < DW + 12) { p.zone = 2; p.vx = 0; p.vy = Math.max(p.vy, 4); if (!isChunk) p.r = Math.min(p.r, 10); }
      else { if (!isChunk) splash(p.x, GY - 2); return false; }
    }
    return true;
  }
  function routeDown(p, dt) {
    p.vy = Math.min(p.vy + 0.3 * dt, 7); p.y += p.vy * dt; p.x += (DX - p.x) * 0.25;
    if (p.y >= SY - 2) { p.zone = 3; p.vx = 3.4 + Math.random() * 1.4; p.vy = 0; }
    return true;
  }
  function routeSewer(p, dt) {
    p.vy += 0.2 * dt; p.x += p.vx * dt; p.y += p.vy * dt;
    var bot = SY + SR - p.r * 0.55, top = SY - SR + p.r * 0.55;
    if (p.y > bot) { p.y = bot; p.vy = -Math.abs(p.vy) * 0.2; }
    if (p.y < top) { p.y = top; p.vy = Math.abs(p.vy) * 0.2; }
    return p.x < W + 24;
  }

  function stepSim(dt) {
    var t = state.t, burst = t >= T.burst;
    var clogLeft = XC - RI * 0.72 * Math.max(clogScale(t), 0.2) - 4;
    // l'eau arrive et s'accumule derrière le bouchon
    if (!burst && t < T.fill + 1.2 && water.length < 118) {
      for (var a = 0; a < 3; a++) water.push(newDrop(-12, CY - RI + 14 + Math.random() * (RI * 2 - 28), 5, 0, 12 + Math.random() * 5, false));
    }
    // flux continu après l'explosion
    if (burst && t < T.stopFlow) {
      for (var n = 0; n < 2; n++) water.push(newDrop(-10, CY + RI - 18 - Math.random() * 40, 4 + Math.random() * 2, 0, 10 + Math.random() * 5, true));
    }
    for (var k = water.length - 1; k >= 0; k--) {
      var p = water[k], keep = true;
      if (p.zone === 0) {
        if (!burst && !p.flow) {
          p.vx += (Math.random() - 0.42) * 0.6; p.vy += (Math.random() - 0.5) * 0.6;
          p.vx *= 0.92; p.vy *= 0.9; p.x += p.vx * dt; p.y += p.vy * dt;
          if (p.x > clogLeft - p.r * 0.4) { p.x = clogLeft - p.r * 0.4; p.vx = -Math.abs(p.vx) * 0.5; }
        } else {
          if (!p.flow) { p.flow = true; p.vx = 3 + Math.random() * 3; }
          p.vx = Math.min(p.vx + 0.12 * dt, 7); p.vy += 0.25 * dt;
          p.x += p.vx * dt; p.y += p.vy * dt;
          if (p.x > XM - 4) { p.zone = 1; p.vx = Math.min(p.vx, 2.2 + Math.random() * 0.8); p.vy = Math.max(p.vy, 0.5); }
        }
        if (p.zone === 0) {
          var top = CY - RI + p.r * 0.7, bot = CY + RI - p.r * 0.7;
          if (p.y < top) { p.y = top; p.vy = Math.abs(p.vy) * 0.3; }
          if (p.y > bot) { p.y = bot; p.vy = -Math.abs(p.vy) * 0.25; }
        }
      } else if (p.zone === 1) keep = routeFree(p, dt, false);
      else if (p.zone === 2) keep = routeDown(p, dt);
      else keep = routeSewer(p, dt);
      if (!keep) water.splice(k, 1);
    }
    for (var d = drops.length - 1; d >= 0; d--) { var q = drops[d]; q.vy += 0.3 * dt; q.x += q.vx * dt; q.y += q.vy * dt; q.life -= 0.035 * dt; if (q.life <= 0) drops.splice(d, 1); }
    for (var j = chunks.length - 1; j >= 0; j--) {
      var c = chunks[j], ok = true;
      if (c.zone === 0) {
        c.vy += 0.3 * dt; c.x += c.vx * dt; c.y += c.vy * dt;
        if (c.y > CY + RI - c.r) { c.y = CY + RI - c.r; c.vy *= -0.3; c.vx = c.vx * 0.96 + 0.25 * dt; }
        if (c.y < CY - RI + c.r) { c.y = CY - RI + c.r; c.vy = Math.abs(c.vy); }
        if (c.x > XM - 4) { c.zone = 1; c.vx = Math.min(c.vx, 2.6); }
      } else if (c.zone === 1) ok = routeFree(c, dt, true);
      else if (c.zone === 2) ok = routeDown(c, dt);
      else ok = routeSewer(c, dt);
      c.a += c.va * dt;
      if (!ok) chunks.splice(j, 1);
    }
  }

  /* ---- étiquette ---- */
  var phase = -1;
  function setPhase(n) { if (n === phase) return; phase = n; chip.className = "pipe-chip s" + n; chipTxt.textContent = L.states[n]; }

  /* ---- rendu ---- */
  function render(t) {
    ctxW.clearRect(0, 0, W, H);
    for (var k = 0; k < water.length; k++) {
      var p = water[k];
      ctxW.fillStyle = p.hi ? "#7cc0ff" : (p.zone ? "#4aa3ff" : "#2f86ef");
      ctxW.beginPath(); ctxW.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctxW.fill();
    }
    for (var d = 0; d < drops.length; d++) { var q = drops[d]; ctxW.fillStyle = "rgba(124,192,255," + q.life + ")"; ctxW.beginPath(); ctxW.arc(q.x, q.y, 5, 0, Math.PI * 2); ctxW.fill(); }

    var c = ctxF; c.clearRect(0, 0, W, H);
    // bouchon
    var sc = clogScale(t);
    if (sc > 0.02) {
      var shake = t > T.drill[0] && t < T.burst ? (Math.random() - 0.5) * 4 : 0, wob = t * 2.2;
      c.save(); c.translate(shake, shake * 0.6); c.globalAlpha = Math.min(1, sc * 1.4);
      var cg = c.createRadialGradient(XC - 12, CY - 20, 6, XC, CY, RI);
      cg.addColorStop(0, "#9a6a3c"); cg.addColorStop(0.55, "#5e3b1f"); cg.addColorStop(1, "#33200f");
      clogPath(c, XC, CY, RI * sc, wob); c.fillStyle = cg; c.fill();
      c.strokeStyle = "rgba(205,170,120,.55)"; c.lineWidth = 1.6;
      for (var h = 0; h < 7; h++) {
        var hy = CY - RI * 0.7 * sc + h * RI * 0.22 * sc;
        c.beginPath(); c.moveTo(XC - RI * 0.5 * sc, hy); c.quadraticCurveTo(XC + Math.sin(h + wob) * 10, hy + 8, XC + RI * 0.5 * sc, hy - 4); c.stroke();
      }
      c.fillStyle = "rgba(30,18,8,.55)";
      [[-14, -18, 6], [10, 8, 8], [-6, 26, 5], [14, -30, 4]].forEach(function (dd) { c.beginPath(); c.arc(XC + dd[0] * sc, CY + dd[1] * sc, dd[2] * sc, 0, Math.PI * 2); c.fill(); });
      c.restore();
    }
    // morceaux
    for (var j = 0; j < chunks.length; j++) {
      var ch = chunks[j]; c.save(); c.translate(ch.x, ch.y); c.rotate(ch.a); c.fillStyle = ch.col;
      var r = ch.zone >= 2 ? ch.r * 0.8 : ch.r;
      c.beginPath(); c.moveTo(-r, -r * 0.4); c.lineTo(r * 0.6, -r); c.lineTo(r, r * 0.5); c.lineTo(-r * 0.3, r); c.closePath(); c.fill(); c.restore();
    }
    // furet
    var tin = ease(seg(t, T.tool[0], T.tool[1])), tout = ease(seg(t, T.back[0], T.back[1]));
    var tx = -60 + (XC - RI * 0.62 - 14 + 60) * tin - (XC + 40) * tout;
    if (t > T.tool[0] && tx > -40) {
      var spin = t * (t > T.drill[0] && t < T.burst + 0.4 ? 40 : 14);
      c.strokeStyle = "#c9d2dc"; c.lineWidth = 6; c.lineCap = "round";
      c.beginPath(); c.moveTo(-20, CY - 4); c.lineTo(tx - 10, CY - 4); c.stroke();
      c.strokeStyle = "rgba(60,72,88,.9)"; c.lineWidth = 2;
      for (var s2 = -20 + ((spin * 3) % 12); s2 < tx - 12; s2 += 12) { c.beginPath(); c.moveTo(s2, CY - 8); c.lineTo(s2 + 5, CY); c.stroke(); }
      c.save(); c.translate(tx, CY - 4);
      var hg = c.createLinearGradient(0, -16, 0, 16); hg.addColorStop(0, "#f1f4f7"); hg.addColorStop(0.5, "#9aa6b3"); hg.addColorStop(1, "#5c6876");
      c.fillStyle = hg; c.beginPath(); c.moveTo(-14, -12); c.lineTo(10, -8); c.lineTo(20, 0); c.lineTo(10, 8); c.lineTo(-14, 12); c.closePath(); c.fill();
      c.strokeStyle = "#c2410c"; c.lineWidth = 2.4;
      for (var b = 0; b < 3; b++) { var aa = spin + b * 2.09; c.beginPath(); c.moveTo(-8 + b * 7, Math.sin(aa) * 11); c.lineTo(-4 + b * 7, -Math.sin(aa) * 11); c.stroke(); }
      c.restore();
      if (t > T.drill[0] + 0.4 && t < T.burst + 0.5) {
        c.strokeStyle = "rgba(200,232,255,.85)"; c.lineWidth = 2;
        for (var qq = 0; qq < 6; qq++) { var off = (Math.random() - 0.5) * 34; c.beginPath(); c.moveTo(tx + 20, CY - 4 + off * 0.3); c.lineTo(tx + 40 + Math.random() * 20, CY - 4 + off); c.stroke(); }
      }
    }
    drawGlass(c);
    drawUnderground(c);
  }

  function drawGlass(c) {
    var wg = c.createLinearGradient(0, CY - RO, 0, CY - RI);
    wg.addColorStop(0, "rgba(190,215,240,.55)"); wg.addColorStop(1, "rgba(120,160,200,.18)");
    c.fillStyle = wg; c.fillRect(-10, CY - RO, XM + 10, RO - RI);
    var bg = c.createLinearGradient(0, CY + RI, 0, CY + RO);
    bg.addColorStop(0, "rgba(120,160,200,.18)"); bg.addColorStop(1, "rgba(190,215,240,.45)");
    c.fillStyle = bg; c.fillRect(-10, CY + RI, XM + 10, RO - RI);
    c.fillStyle = "rgba(255,255,255,.28)"; c.fillRect(-10, CY - RI + 6, XM + 10, 5);
    c.fillStyle = "rgba(255,255,255,.12)"; c.fillRect(-10, CY - RI + 16, XM + 10, 10);
    c.fillStyle = "rgba(255,255,255,.10)"; c.fillRect(-10, CY + RI - 14, XM + 10, 4);
    c.strokeStyle = "rgba(220,235,250,.6)"; c.lineWidth = 1.5;
    c.beginPath(); c.moveTo(-10, CY - RO); c.lineTo(XM, CY - RO); c.moveTo(-10, CY + RO); c.lineTo(XM, CY + RO); c.stroke();
    [C1, C2].forEach(function (x) {
      var mg = c.createLinearGradient(0, CY - RO - 8, 0, CY + RO + 8);
      mg.addColorStop(0, "#e9eef3"); mg.addColorStop(0.18, "#aeb9c5"); mg.addColorStop(0.5, "#6f7c8b"); mg.addColorStop(0.82, "#b7c2cd"); mg.addColorStop(1, "#59636f");
      c.fillStyle = mg; c.fillRect(x - 13, CY - RO - 8, 26, RO * 2 + 16);
      c.fillStyle = "rgba(0,0,0,.25)"; c.fillRect(x + 11, CY - RO - 8, 2, RO * 2 + 16);
      c.fillStyle = "#3e4955"; [CY - RO + 4, CY + RO - 4].forEach(function (y) { c.beginPath(); c.arc(x, y, 3.2, 0, Math.PI * 2); c.fill(); });
    });
    c.save(); c.translate(XM, CY); c.scale(0.24, 1); c.lineWidth = 6; c.strokeStyle = "rgba(230,240,250,.9)"; c.beginPath(); c.arc(0, 0, RO, -Math.PI / 2, Math.PI / 2); c.stroke();
    c.lineWidth = 3; c.strokeStyle = "rgba(160,180,200,.8)"; c.beginPath(); c.arc(0, 0, RI, -Math.PI / 2, Math.PI / 2); c.stroke(); c.restore();
  }

  /* grille, regard et égout (parois en béton au premier plan) */
  function drawUnderground(c) {
    var wall = "#566475", wallHi = "#7d8b9b";
    c.lineWidth = 4; c.lineCap = "butt";
    // parois du regard
    c.strokeStyle = wall;
    c.beginPath(); c.moveTo(DX - DW - 2, GY); c.lineTo(DX - DW - 2, SY + SR + 2); c.lineTo(W + 10, SY + SR + 2); c.stroke();
    c.beginPath(); c.moveTo(DX + DW + 2, GY); c.lineTo(DX + DW + 2, SY - SR - 2); c.lineTo(W + 10, SY - SR - 2); c.stroke();
    c.strokeStyle = wallHi; c.lineWidth = 1.5;
    c.beginPath(); c.moveTo(DX + DW + 4, SY - SR - 4); c.lineTo(W + 10, SY - SR - 4); c.stroke();
    // grille
    c.save(); c.translate(DX, GY); c.scale(1, 0.3);
    c.strokeStyle = "#7c8a99"; c.lineWidth = 5; c.beginPath(); c.arc(0, 0, 32, 0, Math.PI * 2); c.stroke();
    c.strokeStyle = "rgba(124,138,153,.85)"; c.lineWidth = 3.4;
    for (var k = -2; k <= 2; k++) { c.beginPath(); c.moveTo(k * 11, -29); c.lineTo(k * 11, 29); c.stroke(); }
    c.restore();
    // libellé
    c.font = "700 12px 'Plus Jakarta Sans', system-ui, sans-serif"; c.fillStyle = "rgba(255,255,255,.55)";
    c.textAlign = "right"; c.fillText(L.sewer, W - 14, GY + 26);
    c.textAlign = "left";
  }

  /* ---- boucle continue ---- */
  function frame(now) {
    var real = Math.min(0.25, Math.max(0, (now - last) / 1000)); last = now;
    var prev = state.t; state.t += real;
    var t = state.t, steps = Math.max(1, Math.ceil(real * 60 / 2)), dt = real * 60 / steps;
    if (prev < T.drill[0] + 0.3 && t >= T.drill[0] + 0.3) emitChunks(6, 1.2);
    if (prev < T.drill[0] + 0.8 && t >= T.drill[0] + 0.8) emitChunks(6, 1.2);
    if (prev < T.burst && t >= T.burst) emitChunks(34, 2.4);
    setPhase(t < T.tool[0] ? 0 : t < T.drill[0] + 0.4 ? 1 : t < T.burst ? 2 : 3);
    for (var st = 0; st < steps; st++) stepSim(dt);
    render(t);
    if (t >= T.end) { state.t = 0; phase = -1; chunks = []; }   // on enchaîne sans coupure
    raf = requestAnimationFrame(frame);
  }
  function start() {
    if (running) return;
    running = true; box.classList.add("is-playing");
    last = performance.now(); raf = requestAnimationFrame(frame);
  }
  function halt() { if (!running) return; cancelAnimationFrame(raf); running = false; box.classList.remove("is-playing"); }

  /* ---- pause, veille hors écran / onglet caché ---- */
  var userPaused = false, inView = false;
  var ICON_PAUSE = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5v14M15 5v14"/></svg>';
  var ICON_PLAY = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="m7 4 13 8-13 8z"/></svg>';
  function setBtn() {
    btn.innerHTML = userPaused ? ICON_PLAY : ICON_PAUSE;
    btn.setAttribute("aria-label", userPaused ? L.play : L.pause);
    btn.setAttribute("aria-pressed", userPaused ? "true" : "false");
  }
  function update() { if (!userPaused && inView && !document.hidden) start(); else halt(); }
  btn.addEventListener("click", function () { userPaused = !userPaused; setBtn(); update(); });
  document.addEventListener("visibilitychange", update);
  window.addEventListener("resize", resize);

  resetSim(); setPhase(0); resize(); setBtn();
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(function (en) { inView = en[0].isIntersecting; update(); }, { threshold: 0.15 }).observe(box);
  } else { inView = true; update(); }
})();
