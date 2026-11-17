// Tests navigateur du formulaire de demande (Playwright). L'API est simulée ICI SEULEMENT, pour tester l'interface.
// Lancer : (cd public && python3 -m http.server 8765) puis  node tests/form.e2e.cjs
const { chromium } = require("playwright");
const BASE = process.env.BASE || "http://localhost:8765";
const SHOTS = process.env.SHOTS || "/tmp/rqshots";
require("fs").mkdirSync(SHOTS, { recursive: true });
let fails = 0; const ok = (c, m) => { console.log((c ? "  ✓ " : "  ✗ ") + m); if (!c) fails++; };

async function setup(b, { ready = true, post = 200, mobile = false, path = "/" } = {}) {
  const ctx = await b.newContext(mobile ? { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 } : { viewport: { width: 1440, height: 900 } });
  const p = await ctx.newPage(); const errs = []; p.on("pageerror", (e) => errs.push(e.message));
  p.on("console", (m) => { if (m.type() === "error" && !/unsplash|TUNNEL|Failed to load resource/.test(m.text())) errs.push(m.text()); });
  const posts = [];
  await p.route("**/api/demande", async (route) => {
    const r = route.request();
    if (r.method() === "GET") return route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ ready, channels: {} }) });
    posts.push(r.postDataBuffer());
    if (post === 200) return route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ ok: true, id: "ABS-20261117-K7Q2M", receivedAt: new Date().toISOString() }) });
    return route.fulfill({ status: post, contentType: "application/json", body: JSON.stringify({ ok: false, error: "delivery_failed" }) });
  });
  await p.addInitScript(() => { window.__opened = []; window.open = (u) => { window.__opened.push(u); return null; }; });
  await p.goto(BASE + path, { waitUntil: "domcontentloaded" });
  await p.addStyleTag({ content: ".js .reveal{opacity:1!important;transform:none!important}" });
  await p.locator("#diagnostic").scrollIntoViewIfNeeded(); await p.waitForTimeout(400);
  return { ctx, p, errs, posts };
}
const vis = (p, n) => p.locator(`[data-req] [data-p="${n}"]`).isVisible();
const next = async (p) => { await p.locator('[data-req] .rq-p:not([hidden]) [data-next]').click(); await p.waitForTimeout(350); };
async function fillAll(p, { photos = [] } = {}) {
  await p.locator('[data-req] label.rq-card:has(input[value=wc])').click(); await p.waitForTimeout(450);
  await p.locator('[data-req] .rq-chip').first().click();
  await p.locator('[data-req] [name=desc]').fill("Le WC du rez-de-chaussée déborde.");
  await next(p);
  await p.locator('[data-req] [name=cp]').fill("1050");
  await p.locator('[data-req] [name=addr]').fill("Rue de la Paix 12");
  await next(p);
  if (photos.length) { await p.locator('[data-req] [data-file]').setInputFiles(photos); await p.waitForTimeout(1500); }
  await next(p);
  await p.locator('[data-req] [name=name]').fill("Marie Dupont");
  await p.locator('[data-req] [name=tel]').fill("0470 12 34 56");
  await p.locator('[data-req] [name=mail]').fill("marie@exemple.be");
  await p.locator('[data-req] [name=consent]').check();
  await next(p);
}

(async () => {
  const b = await chromium.launch({ executablePath: "/usr/bin/google-chrome", args: ["--no-sandbox"] });

  console.log("1. Validation et navigation (ordinateur)");
  { const { ctx, p, errs } = await setup(b);
    ok(await vis(p, 1), "étape 1 visible au départ");
    await next(p); ok(await p.locator('[data-err=problem].show').isVisible(), "erreur si aucun problème choisi");
    await p.screenshot({ path: SHOTS + "/d1.png", clip: await p.locator("[data-req]").boundingBox() });
    await p.locator('[data-req] label.rq-card:has(input[value=egout])').click(); await p.waitForTimeout(450);
    ok(await vis(p, 2), "clic sur une carte → étape 2 (transition)");
    ok(await p.locator('[data-req] .rq-chip').count() > 0, "situations proposées pour l'égout");
    await next(p); ok(await p.locator('[data-err=urgency].show').isVisible(), "erreur si urgence non choisie");
    await p.locator('[data-req] label.rq-urg:has(input[value=urgent])').click();
    ok(await p.locator('[data-req] [data-urgbox]').isVisible(), "urgence → bouton d'appel et conseils affichés");
    await p.screenshot({ path: SHOTS + "/d2.png", clip: await p.locator("[data-req]").boundingBox() });
    await next(p); ok(await vis(p, 3), "étape 3");
    await p.locator('[data-req] [name=cp]').fill("12"); await next(p);
    ok(await p.locator('[data-err=cp].show').isVisible() && await p.locator('[data-err=city].show').isVisible(), "code postal et ville invalides refusés");
    await p.locator('[data-req] [name=cp]').fill("4000");
    ok((await p.locator('[data-req] [name=city]').inputValue()) === "Liège", "ville préremplie depuis le code postal (4000 → Liège)");
    ok(!(await p.locator('[data-err=cp].show').isVisible()), "l'erreur disparaît dès que c'est corrigé");
    await p.locator('[data-req] .rq-p:not([hidden]) [data-back]').click(); ok(await vis(p, 2), "retour à l'étape 2");
    ok(await p.locator('[data-req] input[name=urgency][value=urgent]').isChecked(), "les choix sont conservés au retour");
    await next(p); await next(p); ok(await vis(p, 4), "étape 4 (photos facultatives)"); await next(p);
    await p.locator('[data-req] [name=tel]').fill("123"); await next(p);
    ok(await p.locator('[data-err=name].show').isVisible() && await p.locator('[data-err=tel].show').isVisible() && await p.locator('[data-err=consent].show').isVisible(), "nom, téléphone et consentement exigés");
    await p.locator('[data-req] [name=mail]').fill("pas-un-mail"); await p.locator('[data-req] [name=mail]').blur(); await p.waitForTimeout(350);
    ok(await p.locator('[data-err=mail].show').isVisible(), "e-mail invalide signalé à la sortie du champ");
    await p.screenshot({ path: SHOTS + "/d5.png", clip: await p.locator("[data-req]").boundingBox() });
    ok(errs.length === 0, "aucune erreur JavaScript (" + errs.join(" | ") + ")");
    await ctx.close(); }

  console.log("2. Photos : ajout, compression, suppression, limites");
  { const { ctx, p } = await setup(b);
    await p.locator('[data-req] label.rq-card:has(input[value=wc])').click(); await p.waitForTimeout(450);
    await p.locator('[data-req] label.rq-urg:has(input[value=soon])').click(); await next(p);
    await p.locator('[data-req] [name=cp]').fill("1050"); await next(p);
    await p.locator('[data-req] [data-file]').setInputFiles(["/tmp/rqimg/p1.jpg", "/tmp/rqimg/p2.jpg"]); await p.waitForTimeout(1500);
    ok(await p.locator('[data-req] [data-thumbs] li').count() === 2, "2 photos ajoutées avec aperçu");
    const sizes = await p.evaluate(() => [...document.querySelectorAll('[data-thumbs] img')].map((i) => [i.naturalWidth, i.naturalHeight]));
    ok(sizes.every(([w]) => w <= 1600), "photos redimensionnées à 1600 px max (" + JSON.stringify(sizes) + ")");
    await p.locator('[data-req] [data-file]').setInputFiles(["/tmp/rqimg/p3.jpg", "/tmp/rqimg/p4.jpg", "/tmp/rqimg/p5.jpg"]); await p.waitForTimeout(1500);
    ok(await p.locator('[data-req] [data-thumbs] li').count() === 4 && await p.locator('[data-err=photos].show').isVisible(), "limite de 4 photos, message affiché");
    ok(await p.locator('[data-req] [data-addbtn]').isHidden(), "bouton d'ajout masqué à 4 photos");
    await p.locator('[data-req] [data-rm="1"]').click();
    ok(await p.locator('[data-req] [data-thumbs] li').count() === 3 && await p.locator('[data-req] [data-addbtn]').isVisible(), "suppression d'une photo");
    await p.locator('[data-req] [data-file]').setInputFiles(["/tmp/rqimg/doc.pdf"]); await p.waitForTimeout(500);
    ok(await p.locator('[data-err=photos].show').isVisible() && await p.locator('[data-req] [data-thumbs] li').count() === 3, "fichier non photo refusé");
    await p.screenshot({ path: SHOTS + "/d4.png", clip: await p.locator("[data-req]").boundingBox() });
    await ctx.close(); }

  console.log("3. Récapitulatif, modification, envoi réussi");
  { const { ctx, p, posts, errs } = await setup(b);
    await fillAll(p, { photos: ["/tmp/rqimg/p1.jpg", "/tmp/rqimg/p2.jpg"] });
    ok(await vis(p, 6), "récapitulatif affiché");
    const rc = await p.locator('[data-req] [data-recap]').innerText();
    ok(/WC bouché/.test(rc) && /Intervention urgente/.test(rc) && /1050 Ixelles \(Bruxelles\)/.test(rc) && /Marie Dupont/.test(rc) && /déborde/.test(rc), "récapitulatif complet (problème, urgence, adresse + région, description, coordonnées)");
    ok(await p.locator('[data-req] .rq-mini img').count() === 2, "les 2 photos figurent dans le récapitulatif");
    ok((await p.locator('[data-req] [data-sendlbl]').innerText()) === "Envoyer ma demande", "bouton d'envoi direct (serveur prêt)");
    await p.screenshot({ path: SHOTS + "/d6.png", clip: await p.locator("[data-req]").boundingBox() });
    await p.locator('[data-req] [data-edit="3"]').click(); ok(await vis(p, 3), "« Modifier » ouvre la bonne étape");
    ok((await p.locator('[data-req] .rq-p:not([hidden]) [data-nextlbl]').innerText()) === "Revenir au récapitulatif", "bouton « Revenir au récapitulatif »");
    await p.locator('[data-req] [name=addr]').fill("Avenue Louise 200"); await next(p);
    ok(await vis(p, 6) && /Avenue Louise 200/.test(await p.locator('[data-req] [data-recap]').innerText()), "modification reportée dans le récapitulatif");
    await p.locator('[data-req] [data-submit]').click(); await p.waitForTimeout(800);
    ok(await vis(p, "ok"), "écran de confirmation après réponse positive du serveur");
    ok((await p.locator('[data-req] [data-okid]').innerText()) === "ABS-20261117-K7Q2M", "numéro de demande affiché");
    ok(await p.locator('[data-req] [data-okurg]').isVisible(), "urgence : bouton d'appel sur la confirmation");
    const body = posts[0] ? posts[0].toString("latin1") : "";
    ok(/name="problem"\r\n\r\nwc/.test(body) && /name="cp"\r\n\r\n1050/.test(body) && (body.match(/name="photos"; filename=/g) || []).length === 2 && /image\/jpeg/.test(body), "données et 2 photos JPEG envoyées au serveur");
    ok(await p.evaluate(() => sessionStorage.getItem("abs-demande-fr")) === null, "brouillon effacé après l'envoi");
    await p.screenshot({ path: SHOTS + "/dok.png", clip: await p.locator("[data-req]").boundingBox() });
    ok(errs.length === 0, "aucune erreur JavaScript");
    await ctx.close(); }

  console.log("4. Erreur d'envoi : rien de simulé, repli WhatsApp/appel");
  { const { ctx, p } = await setup(b, { post: 502 });
    await fillAll(p); await p.locator('[data-req] [data-submit]').click(); await p.waitForTimeout(800);
    ok(await vis(p, "ko") && !(await vis(p, "ok")), "écran d'erreur, pas de confirmation");
    await p.locator('[data-req] [data-kowa]').click();
    const u = await p.evaluate(() => window.__opened[0] || "");
    ok(u.startsWith("https://wa.me/32484724724?text=") && decodeURIComponent(u).includes("Marie Dupont") && decodeURIComponent(u).includes("1050 Ixelles"), "WhatsApp prérempli avec toute la demande");
    await p.locator('[data-req] [data-retry]').click(); ok(await vis(p, 6), "« Réessayer » revient au récapitulatif");
    await p.screenshot({ path: SHOTS + "/dko.png", clip: await p.locator("[data-req]").boundingBox() });
    await ctx.close(); }

  console.log("5. Serveur non configuré : WhatsApp comme aujourd'hui");
  { const { ctx, p, posts } = await setup(b, { ready: false });
    await fillAll(p);
    ok((await p.locator('[data-req] [data-sendlbl]').innerText()) === "Envoyer via WhatsApp" && await p.locator('[data-req] [data-wanote]').isVisible(), "bouton « Envoyer via WhatsApp » + explication");
    await p.locator('[data-req] [data-submit]').click(); await p.waitForTimeout(300);
    ok(posts.length === 0 && (await p.evaluate(() => window.__opened.length)) === 1, "aucun envoi serveur, WhatsApp ouvert");
    ok(!(await vis(p, "ok")), "pas d'écran « Demande envoyée »");
    await ctx.close(); }

  console.log("6. Sauvegarde temporaire et page service");
  { const { ctx, p } = await setup(b);
    await p.locator('[data-req] label.rq-card:has(input[value=douche])').click(); await p.waitForTimeout(450);
    await p.locator('[data-req] label.rq-urg:has(input[value=quote])').click(); await next(p);
    await p.locator('[data-req] [name=cp]').fill("9000");
    await p.reload({ waitUntil: "domcontentloaded" }); await p.waitForTimeout(500);
    ok(await p.locator('[data-req] input[value=douche]').isChecked() && (await p.locator('[data-req] [name=cp]').inputValue()) === "9000" && (await p.locator('[data-req] [name=city]').inputValue()) === "Gand", "réponses retrouvées après rechargement (même onglet)");
    ok(await vis(p, 3), "reprise à la bonne étape");
    await ctx.close();
    const s = await setup(b, { path: "/debouchage-sanibroyeur.html" });
    ok(await s.p.locator('[data-req] input[value=wc]').isChecked(), "page sanibroyeur : « WC bouché » présélectionné");
    await s.ctx.close();
    const n = await setup(b, { path: "/nl/" });
    ok(/Wat is het probleem/.test(await n.p.locator("[data-req]").innerText()), "version néerlandaise");
    await n.ctx.close(); }

  console.log("7. Mobile (390 px)");
  { const { ctx, p, errs } = await setup(b, { mobile: true });
    await p.screenshot({ path: SHOTS + "/m1.png", clip: await p.locator("[data-req]").boundingBox() });
    const ov = await p.evaluate(() => document.documentElement.scrollWidth > innerWidth); ok(!ov, "pas de défilement horizontal");
    await fillAll(p, { photos: ["/tmp/rqimg/p1.jpg"] });
    ok(await vis(p, 6), "parcours complet au doigt");
    await p.screenshot({ path: SHOTS + "/m6.png", clip: await p.locator("[data-req]").boundingBox() });
    const small = await p.evaluate(() => [...document.querySelectorAll("[data-req] button:not([hidden]), [data-req] .rq-card, [data-req] .rq-urg")].filter((e) => e.offsetParent && e.getBoundingClientRect().height < 40).map((e) => e.className + ":" + Math.round(e.getBoundingClientRect().height)));
    ok(small.length === 0 || small.every((s) => /rq-edit/.test(s)), "cibles tactiles ≥ 40 px (" + small.join(",") + ")");
    await p.locator('[data-req] [data-submit]').click(); await p.waitForTimeout(800);
    ok(await vis(p, "ok"), "envoi réussi sur mobile");
    await p.screenshot({ path: SHOTS + "/mok.png", clip: await p.locator("[data-req]").boundingBox() });
    ok(errs.length === 0, "aucune erreur JavaScript");
    await ctx.close(); }

  console.log("8. Le reste du site fonctionne toujours");
  { const { ctx, p, errs } = await setup(b);
    ok(await p.locator(".hp-quick a").count() === 5, "barre « Qu'est-ce qui bouche ? »");
    ok(await p.locator(".tl-5 .tl").count() === 5, "5 catégories");
    await p.locator("#faq-4 summary").click(); ok(/locataire/i.test(await p.locator(".fq-panel").innerText()), "FAQ : réponse affichée à côté");
    await p.locator(".zn-ask input").fill("1050"); await p.locator(".zn-ask button[type=submit], .zn-ask button").first().click(); await p.waitForTimeout(400);
    ok(await p.locator(".zn-card").innerText().then((t) => /Ixelles|1050/.test(t)), "vérification de commune sur la carte");
    ok(await p.locator('a[href^="tel:"]').count() > 5, "boutons d'appel présents");
    ok(await p.locator('a[href="#diagnostic"]').count() >= 2, "les liens « Diagnostic express » mènent au formulaire");
    ok(errs.length === 0, "aucune erreur JavaScript sur l'accueil");
    await ctx.close(); }

  await b.close();
  console.log(fails ? `\n${fails} échec(s)` : "\nTout est vert.");
  process.exit(fails ? 1 : 0);
})();
