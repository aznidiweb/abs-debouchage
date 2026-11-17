-- Base des demandes d'intervention (Cloudflare D1)
-- À exécuter une fois : wrangler d1 execute abs-demandes --remote --file=migrations/0001_demandes.sql
CREATE TABLE IF NOT EXISTS demandes (
  id            TEXT PRIMARY KEY,          -- ex. ABS-20261117-K7Q2M
  received_at   TEXT NOT NULL,             -- date et heure de réception (ISO 8601, UTC)
  lang          TEXT NOT NULL,             -- fr | nl
  problem       TEXT NOT NULL,             -- wc, evier, douche, canalisation, egout, odeurs, camera, plomberie, autre
  situation     TEXT,                      -- situation choisie à l'étape 2 (facultatif)
  urgency       TEXT NOT NULL,             -- urgent | soon | quote
  description   TEXT,
  postal_code   TEXT NOT NULL,
  city          TEXT NOT NULL,
  region        TEXT NOT NULL,             -- Bruxelles | Wallonie | Flandre (déduit du code postal)
  address       TEXT,
  name          TEXT NOT NULL,
  phone         TEXT NOT NULL,
  email         TEXT,
  consent       INTEGER NOT NULL DEFAULT 1,
  photo_count   INTEGER NOT NULL DEFAULT 0,
  photo_keys    TEXT,                      -- JSON : emplacements des photos dans R2
  page          TEXT,
  user_agent    TEXT,
  email_sent    INTEGER NOT NULL DEFAULT 0,
  whatsapp_sent INTEGER NOT NULL DEFAULT 0,
  status        TEXT NOT NULL DEFAULT 'nouvelle'   -- nouvelle | rappelée | planifiée | terminée | annulée
);
CREATE INDEX IF NOT EXISTS demandes_received ON demandes (received_at DESC);
CREATE INDEX IF NOT EXISTS demandes_status ON demandes (status, received_at DESC);
