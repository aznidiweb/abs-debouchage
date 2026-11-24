/**
 * ABS Débouchage — réception des demandes d'intervention.
 * Cloudflare Pages Function : https://absdebouchage.be/api/demande
 *
 *   GET  → { ready, channels }  : le formulaire sait s'il peut envoyer directement (sinon il passe par WhatsApp).
 *   POST → multipart/form-data   : valide, numérote, enregistre, prévient l'entreprise.
 *
 * Aucun envoi n'est simulé : la réponse { ok: true } n'est renvoyée que si la demande a été
 * réellement enregistrée en base (D1) ou réellement envoyée par e-mail.
 *
 * Réglages (Cloudflare → Pages → abs-debouchage → Settings), voir CONFIGURATION-DEMANDES.md :
 *   Bindings   DB      (D1)  base des demandes            — facultatif mais recommandé
 *              PHOTOS  (R2)  stockage des photos          — facultatif
 *   L'e-mail est OBLIGATOIRE pour que le formulaire envoie directement (sinon : WhatsApp).
 *   Secrets    RESEND_API_KEY                             — e-mail via resend.com
 *   Variables  LEAD_EMAIL_TO    destinataire(s), séparés par des virgules
 *              LEAD_EMAIL_FROM  ex. "ABS Débouchage <demandes@absdebouchage.be>" (domaine vérifié chez Resend)
 *   WhatsApp   WA_TOKEN (secret), WA_PHONE_ID, WA_TO, WA_TEMPLATE, WA_LANG (défaut "fr")
 */

const PROBLEMS = {
  wc: "WC bouché", evier: "Évier bouché", douche: "Douche ou baignoire bouchée", canalisation: "Canalisation bouchée",
  egout: "Égout bouché", odeurs: "Mauvaises odeurs", camera: "Inspection caméra", plomberie: "Plomberie, fuite", autre: "Autre problème",
};
const URGENCY = { urgent: "URGENT — intervention aujourd'hui", soon: "Dans les prochains jours", quote: "Devis, sans urgence" };
const MAX_PHOTOS = 4;
const MAX_PHOTO_BYTES = 2.5 * 1024 * 1024;   // le navigateur compresse à ~0,3–1,8 Mo ; marge de sécurité
const PHOTO_TYPES = { "image/jpeg": "jpg", "image/png": "png", "image/webp": "webp" };

const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" } });

function channels(env) {
  return {
    database: !!env.DB,
    photos: !!env.PHOTOS,
    email: !!(env.RESEND_API_KEY && env.LEAD_EMAIL_TO && env.LEAD_EMAIL_FROM),
    whatsapp: !!(env.WA_TOKEN && env.WA_PHONE_ID && env.WA_TO && env.WA_TEMPLATE),
  };
}
// Le formulaire n'envoie directement que si l'entreprise est réellement PRÉVENUE (e-mail).
// La base seule ne suffit pas : la demande y dormirait sans que personne ne la voie.
// Tant que l'e-mail n'est pas actif, le formulaire passe par WhatsApp.
const isReady = (c) => c.email;

export async function onRequestGet({ env }) {
  const c = channels(env);
  return json({ ready: isReady(c), channels: c });
}

/* ------------------------------------------------------------------ validation */
const clean = (v, max) => String(v ?? "").replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g, "").trim().slice(0, max);
const telNorm = (v) => String(v || "").replace(/[\s.\-/()]/g, "");
const telOk = (v) => /^(\+|00)[1-9][0-9]{7,14}$/.test(telNorm(v)) || /^0[1-9][0-9]{7,8}$/.test(telNorm(v));
const mailOk = (v) => !v || /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
export function region(cp) {
  const n = parseInt(cp, 10);
  if (n >= 1000 && n <= 1299) return "Bruxelles";
  if ((n >= 1300 && n <= 1499) || (n >= 4000 && n <= 7999)) return "Wallonie";
  return "Flandre";
}

export function validate(fd) {
  const f = {
    problem: clean(fd.get("problem"), 20), urgency: clean(fd.get("urgency"), 10), situation: clean(fd.get("situation"), 200),
    desc: clean(fd.get("desc"), 1500), cp: clean(fd.get("cp"), 4), city: clean(fd.get("city"), 80), addr: clean(fd.get("addr"), 160),
    name: clean(fd.get("name"), 80), tel: clean(fd.get("tel"), 25), mail: clean(fd.get("mail"), 120),
    lang: clean(fd.get("lang"), 2) === "nl" ? "nl" : "fr", page: clean(fd.get("page"), 200), consent: fd.get("consent") === "1",
  };
  const errors = [];
  if (!PROBLEMS[f.problem]) errors.push("problem");
  if (!URGENCY[f.urgency]) errors.push("urgency");
  if (!/^[1-9][0-9]{3}$/.test(f.cp)) errors.push("cp");
  if (f.city.length < 2) errors.push("city");
  if (f.name.length < 2) errors.push("name");
  if (!telOk(f.tel)) errors.push("tel");
  if (!mailOk(f.mail)) errors.push("mail");
  if (!f.consent) errors.push("consent");
  const photos = fd.getAll("photos").filter((p) => p && typeof p === "object" && "arrayBuffer" in p && p.size > 0);
  if (photos.length > MAX_PHOTOS) errors.push("photos");
  for (const p of photos) if (!PHOTO_TYPES[p.type] || p.size > MAX_PHOTO_BYTES) { errors.push("photos"); break; }
  return { f, photos, errors };
}

/* ------------------------------------------------------------------ identifiant et date */
export function newId(now = new Date()) {
  const day = new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Brussels", year: "numeric", month: "2-digit", day: "2-digit" }).format(now).replace(/-/g, "");
  const A = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ";   // sans 0/O/1/I : lisible au téléphone
  const r = crypto.getRandomValues(new Uint8Array(5));
  return `ABS-${day}-${Array.from(r, (b) => A[b % A.length]).join("")}`;
}
const brussels = (d) => new Intl.DateTimeFormat("fr-BE", { timeZone: "Europe/Brussels", dateStyle: "full", timeStyle: "short" }).format(d);

/* ------------------------------------------------------------------ e-mail (Resend) */
const h = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
function b64(buf) {
  const bytes = new Uint8Array(buf); let s = "";
  for (let i = 0; i < bytes.length; i += 0x8000) s += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  return btoa(s);
}
export function emailContent(id, at, f, photoNames) {
  const reg = region(f.cp), urgent = f.urgency === "urgent";
  const subject = `${urgent ? "🔴 URGENT · " : ""}Demande ${id} · ${PROBLEMS[f.problem]} · ${f.cp} ${f.city}`;
  const telLink = telNorm(f.tel);
  const rows = [
    ["Problème", PROBLEMS[f.problem] + (f.situation ? ` — ${f.situation}` : "")],
    ["Urgence", URGENCY[f.urgency]],
    ["Adresse", [f.addr, `${f.cp} ${f.city}`].filter(Boolean).join(", ") + ` (${reg})`],
    ["Description", f.desc || "—"],
    ["Nom", f.name], ["Téléphone", f.tel], ["E-mail", f.mail || "—"],
    ["Photos", photoNames.length ? `${photoNames.length} en pièce jointe` : "Aucune"],
    ["Langue", f.lang === "nl" ? "Néerlandais" : "Français"], ["Reçue le", brussels(at)], ["Page", f.page || "—"],
  ];
  const text = [`Nouvelle demande ${id}`, "", ...rows.map(([k, v]) => `${k} : ${v}`), "", `Appeler : ${f.tel}`].join("\n");
  const html = `<div style="font-family:Arial,sans-serif;max-width:620px;color:#0a111a">
<p style="margin:0 0 4px;font-size:13px;color:#64748b">Nouvelle demande · ${h(id)}</p>
<h1 style="margin:0 0 12px;font-size:22px">${urgent ? '<span style="color:#d92d20">URGENT · </span>' : ""}${h(PROBLEMS[f.problem])} — ${h(f.cp)} ${h(f.city)}</h1>
<p style="margin:0 0 18px"><a href="tel:${h(telLink)}" style="display:inline-block;background:#1156c7;color:#fff;text-decoration:none;font-weight:bold;padding:12px 20px;border-radius:999px">Appeler ${h(f.name)} · ${h(f.tel)}</a></p>
<table style="border-collapse:collapse;width:100%;font-size:15px">${rows.map(([k, v]) => `<tr><td style="padding:8px 10px;border-top:1px solid #e5e9f0;color:#64748b;white-space:nowrap;vertical-align:top">${h(k)}</td><td style="padding:8px 10px;border-top:1px solid #e5e9f0;white-space:pre-wrap">${h(v)}</td></tr>`).join("")}</table>
<p style="margin:18px 0 0;font-size:12px;color:#94a3b8">Envoyé par le formulaire de absdebouchage.be. Le client a accepté l'utilisation de ces données pour traiter sa demande.</p></div>`;
  return { subject, text, html };
}
async function sendEmail(env, id, at, f, photos) {
  const names = photos.map((p, i) => `${id}-photo-${i + 1}.${PHOTO_TYPES[p.type]}`);
  const { subject, text, html } = emailContent(id, at, f, names);
  const attachments = [];
  for (let i = 0; i < photos.length; i++) attachments.push({ filename: names[i], content: b64(await photos[i].arrayBuffer()) });
  const body = {
    from: env.LEAD_EMAIL_FROM, to: env.LEAD_EMAIL_TO.split(",").map((s) => s.trim()).filter(Boolean),
    subject, text, html, attachments, headers: { "X-Entity-Ref-ID": id },
  };
  if (f.mail) body.reply_to = f.mail;
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST", headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" }, body: JSON.stringify(body),
  });
  if (!r.ok) throw new Error(`resend ${r.status}: ${(await r.text()).slice(0, 300)}`);
  return true;
}

/* ------------------------------------------------------------------ WhatsApp Business (API Cloud officielle de Meta) */
async function sendWhatsApp(env, id, f) {
  // Modèle (template) à faire approuver chez Meta, avec 5 variables dans le corps :
  // {{1}} numéro de demande, {{2}} problème, {{3}} urgence, {{4}} code postal + ville, {{5}} téléphone du client
  const params = [id, PROBLEMS[f.problem], URGENCY[f.urgency], `${f.cp} ${f.city}`, f.tel].map((t) => ({ type: "text", text: String(t).slice(0, 120) }));
  const r = await fetch(`https://graph.facebook.com/v21.0/${env.WA_PHONE_ID}/messages`, {
    method: "POST", headers: { Authorization: `Bearer ${env.WA_TOKEN}`, "Content-Type": "application/json" },
    body: JSON.stringify({ messaging_product: "whatsapp", to: env.WA_TO, type: "template",
      template: { name: env.WA_TEMPLATE, language: { code: env.WA_LANG || "fr" }, components: [{ type: "body", parameters: params }] } }),
  });
  if (!r.ok) throw new Error(`whatsapp ${r.status}: ${(await r.text()).slice(0, 300)}`);
  return true;
}

/* ------------------------------------------------------------------ réception */
export async function onRequestPost({ request, env }) {
  const c = channels(env);
  if (!isReady(c)) return json({ ok: false, error: "not_configured" }, 503);

  const ct = request.headers.get("content-type") || "";
  if (!ct.includes("multipart/form-data")) return json({ ok: false, error: "bad_request" }, 400);
  const len = Number(request.headers.get("content-length") || 0);
  if (len > 12 * 1024 * 1024) return json({ ok: false, error: "too_large" }, 413);

  let fd;
  try { fd = await request.formData(); } catch { return json({ ok: false, error: "bad_request" }, 400); }
  if (clean(fd.get("website"), 200)) return json({ ok: false, error: "rejected" }, 400);   // champ piège anti-robots

  const { f, photos, errors } = validate(fd);
  if (errors.length) return json({ ok: false, error: "invalid", fields: [...new Set(errors)] }, 422);

  const at = new Date(), id = newId(at), receivedAt = at.toISOString();
  const result = { database: false, photos: false, email: false, whatsapp: false };
  const keys = [];

  if (c.photos && photos.length) {
    try {
      for (let i = 0; i < photos.length; i++) {
        const key = `demandes/${id.slice(4, 12)}/${id}/photo-${i + 1}.${PHOTO_TYPES[photos[i].type]}`;
        await env.PHOTOS.put(key, await photos[i].arrayBuffer(), { httpMetadata: { contentType: photos[i].type }, customMetadata: { demande: id } });
        keys.push(key);
      }
      result.photos = true;
    } catch (e) { console.error("photos", id, e); }
  }

  if (c.database) {
    try {
      await env.DB.prepare(
        `INSERT INTO demandes (id, received_at, lang, problem, situation, urgency, description, postal_code, city, region, address,
          name, phone, email, consent, photo_count, photo_keys, page, user_agent, status)
         VALUES (?1,?2,?3,?4,?5,?6,?7,?8,?9,?10,?11,?12,?13,?14,1,?15,?16,?17,?18,'nouvelle')`
      ).bind(id, receivedAt, f.lang, f.problem, f.situation || null, f.urgency, f.desc || null, f.cp, f.city, region(f.cp), f.addr || null,
        f.name, f.tel, f.mail || null, photos.length, JSON.stringify(keys), f.page || null, (request.headers.get("user-agent") || "").slice(0, 300)).run();
      result.database = true;
    } catch (e) { console.error("database", id, e); }
  }

  if (c.email) {
    try { result.email = await sendEmail(env, id, at, f, photos); } catch (e) { console.error("email", id, e); }
  }

  if (!result.database && !result.email) return json({ ok: false, error: "delivery_failed" }, 502);

  if (c.whatsapp) {
    try { result.whatsapp = await sendWhatsApp(env, id, f); } catch (e) { console.error("whatsapp", id, e); }
  }
  if (c.database) {
    try { await env.DB.prepare("UPDATE demandes SET email_sent=?2, whatsapp_sent=?3 WHERE id=?1").bind(id, result.email ? 1 : 0, result.whatsapp ? 1 : 0).run(); }
    catch (e) { console.error("database update", id, e); }
  }
  return json({ ok: true, id, receivedAt, delivered: result });
}

