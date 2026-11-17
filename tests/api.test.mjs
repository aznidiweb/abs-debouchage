// Tests de la fonction /api/demande avec un environnement Cloudflare simulé (D1, R2, Resend, WhatsApp).
// Lancer : node --test tests/api.test.mjs
import test from "node:test";
import assert from "node:assert/strict";
import { onRequestGet, onRequestPost, validate, newId, region, emailContent } from "../functions/api/demande.js";

function fakeDB({ fail = false } = {}) {
  const rows = [];
  return { rows, prepare(sql) { return { bind(...a) { return { async run() { if (fail) throw new Error("db down"); rows.push({ sql, a }); return { success: true }; } }; } }; } };
}
function fakeR2() { const objs = {}; return { objs, async put(k, v, o) { objs[k] = { size: v.byteLength, o }; } }; }
function form(over = {}, photos = []) {
  const fd = new FormData();
  const base = { problem: "wc", urgency: "urgent", desc: "Le WC déborde", cp: "1050", city: "Ixelles", addr: "Rue X 1", name: "Marie Dupont",
    tel: "0470 12 34 56", mail: "marie@exemple.be", consent: "1", lang: "fr", page: "/", website: "", situation: "L'eau monte" };
  for (const [k, v] of Object.entries({ ...base, ...over })) if (v !== undefined) fd.append(k, v);
  photos.forEach((p, i) => fd.append("photos", p, `photo-${i + 1}.jpg`));
  return fd;
}
const req = (fd) => new Request("https://absdebouchage.be/api/demande", { method: "POST", body: fd });
const jpeg = (n = 2000) => new Blob([new Uint8Array(n).fill(7)], { type: "image/jpeg" });

let fetchCalls = [];
function mockFetch(status = 200) {
  fetchCalls = [];
  globalThis.fetch = async (url, init) => { fetchCalls.push({ url, body: JSON.parse(init.body) }); return new Response(status === 200 ? "{\"id\":\"x\"}" : "boom", { status }); };
}
const EMAIL = { RESEND_API_KEY: "k", LEAD_EMAIL_TO: "a@b.be, c@d.be", LEAD_EMAIL_FROM: "ABS <demandes@absdebouchage.be>" };
const WA = { WA_TOKEN: "t", WA_PHONE_ID: "123", WA_TO: "32484724724", WA_TEMPLATE: "nouvelle_demande" };

test("GET : pas configuré → ready=false", async () => {
  const r = await onRequestGet({ env: {} }); const j = await r.json();
  assert.equal(j.ready, false); assert.deepEqual(j.channels, { database: false, photos: false, email: false, whatsapp: false });
});
test("GET : D1 seule suffit → ready=true", async () => {
  const j = await (await onRequestGet({ env: { DB: fakeDB() } })).json(); assert.equal(j.ready, true);
});
test("POST sans configuration → 503, jamais de faux succès", async () => {
  const r = await onRequestPost({ request: req(form()), env: {} }); const j = await r.json();
  assert.equal(r.status, 503); assert.equal(j.ok, false); assert.equal(j.error, "not_configured");
});
test("POST complet : base + photos + e-mail + WhatsApp", async () => {
  mockFetch(200); const DB = fakeDB(), PHOTOS = fakeR2();
  const r = await onRequestPost({ request: req(form({}, [jpeg(), jpeg(3000)])), env: { DB, PHOTOS, ...EMAIL, ...WA } }); const j = await r.json();
  assert.equal(r.status, 200); assert.equal(j.ok, true); assert.match(j.id, /^ABS-\d{8}-[2-9A-Z]{5}$/);
  assert.ok(!Number.isNaN(Date.parse(j.receivedAt)));
  assert.deepEqual(j.delivered, { database: true, photos: true, email: true, whatsapp: true });
  assert.equal(Object.keys(PHOTOS.objs).length, 2); assert.ok(Object.keys(PHOTOS.objs)[0].includes(j.id));
  const ins = DB.rows[0].a; assert.equal(ins[0], j.id); assert.equal(ins[9], "Bruxelles"); assert.equal(ins[14], 2);
  const mail = fetchCalls.find((c) => c.url.includes("resend")); assert.ok(mail);
  assert.deepEqual(mail.body.to, ["a@b.be", "c@d.be"]); assert.equal(mail.body.reply_to, "marie@exemple.be"); assert.equal(mail.body.attachments.length, 2);
  assert.match(mail.body.subject, /URGENT.*WC bouché.*1050 Ixelles/);
  const wa = fetchCalls.find((c) => c.url.includes("graph.facebook.com/v21.0/123/messages")); assert.ok(wa);
  assert.equal(wa.body.template.name, "nouvelle_demande"); assert.equal(wa.body.template.components[0].parameters[0].text, j.id);
});
test("E-mail en panne mais base OK → succès (la demande est conservée)", async () => {
  mockFetch(500); const DB = fakeDB();
  const j = await (await onRequestPost({ request: req(form()), env: { DB, ...EMAIL } })).json();
  assert.equal(j.ok, true); assert.equal(j.delivered.email, false); assert.equal(j.delivered.database, true);
});
test("Base et e-mail en panne → 502, pas de succès", async () => {
  mockFetch(500);
  const r = await onRequestPost({ request: req(form()), env: { DB: fakeDB({ fail: true }), ...EMAIL } }); const j = await r.json();
  assert.equal(r.status, 502); assert.equal(j.ok, false); assert.equal(j.error, "delivery_failed");
});
test("Champs obligatoires et formats refusés (422)", async () => {
  const bad = form({ problem: "x", urgency: "", cp: "105", city: "", name: "", tel: "12", mail: "pas-un-mail", consent: "0" });
  const r = await onRequestPost({ request: req(bad), env: { DB: fakeDB() } }); const j = await r.json();
  assert.equal(r.status, 422); assert.deepEqual(j.fields.sort(), ["city", "consent", "cp", "mail", "name", "problem", "tel", "urgency"]);
});
test("Photos : 5 refusées, mauvais type refusé, trop lourde refusée", () => {
  assert.ok(validate(form({}, [jpeg(), jpeg(), jpeg(), jpeg(), jpeg()])).errors.includes("photos"));
  const fd = form(); fd.append("photos", new Blob(["x"], { type: "application/pdf" }), "a.pdf"); assert.ok(validate(fd).errors.includes("photos"));
  assert.ok(validate(form({}, [jpeg(3 * 1024 * 1024)])).errors.includes("photos"));
  assert.deepEqual(validate(form({}, [jpeg()])).errors, []);
});
test("Champ piège rempli (robot) → refusé", async () => {
  const r = await onRequestPost({ request: req(form({ website: "http://spam" })), env: { DB: fakeDB() } }); assert.equal(r.status, 400);
});
test("Téléphones belges et internationaux acceptés, e-mail facultatif", () => {
  for (const t of ["0470 12 34 56", "02/123.45.67", "+32 470 12 34 56", "0032470123456", "+33 6 12 34 56 78"]) assert.deepEqual(validate(form({ tel: t })).errors, [], t);
  assert.deepEqual(validate(form({ mail: "" })).errors, []);
});
test("Région déduite du code postal", () => {
  assert.equal(region("1000"), "Bruxelles"); assert.equal(region("1300"), "Wallonie"); assert.equal(region("4000"), "Wallonie");
  assert.equal(region("2000"), "Flandre"); assert.equal(region("9000"), "Flandre"); assert.equal(region("1500"), "Flandre");
});
test("Identifiants uniques", () => { const s = new Set(Array.from({ length: 500 }, () => newId())); assert.equal(s.size, 500); });
test("E-mail : texte échappé (pas d'injection HTML)", () => {
  const { html } = emailContent("ABS-1", new Date(), { ...validate(form({ desc: "<script>alert(1)</script>" })).f }, []);
  assert.ok(!html.includes("<script>")); assert.ok(html.includes("&lt;script&gt;"));
});
