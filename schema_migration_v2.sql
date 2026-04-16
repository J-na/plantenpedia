-- ============================================================
-- Plantenpedia — Schema migratie v2
-- Voer dit script uit in de Supabase SQL Editor
-- (nadat schema.sql al is uitgevoerd)
-- ============================================================

-- ── Nieuwe kolommen op plants ────────────────────────────────
ALTER TABLE plants
    ADD COLUMN IF NOT EXISTS evergreen    BOOLEAN NOT NULL DEFAULT FALSE,
    ADD COLUMN IF NOT EXISTS hardiness    TEXT CHECK (hardiness IN (
                                              'volledig_winterhard',
                                              'winterhard',
                                              'matig_winterhard',
                                              'vorstgevoelig',
                                              'niet_winterhard'
                                          )),
    ADD COLUMN IF NOT EXISTS family       TEXT,
    ADD COLUMN IF NOT EXISTS family_common TEXT,
    ADD COLUMN IF NOT EXISTS origin       TEXT;

-- Indexen voor filterbare velden
CREATE INDEX IF NOT EXISTS idx_plants_evergreen  ON plants(evergreen);
CREATE INDEX IF NOT EXISTS idx_plants_hardiness  ON plants(hardiness);
CREATE INDEX IF NOT EXISTS idx_plants_family     ON plants(family);

-- ── Plantenfamilies tabel ─────────────────────────────────────
CREATE TABLE IF NOT EXISTS plant_families (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        TEXT NOT NULL UNIQUE,   -- wetenschappelijke familienaam (bv. Asteraceae)
    dutch_name  TEXT,                   -- Nederlandse naam (bv. Composietenfamilie)
    description TEXT,                   -- algemene informatie over de familie (markdown)
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_families_name ON plant_families(name);

CREATE TRIGGER trg_families_updated_at
    BEFORE UPDATE ON plant_families
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at();

-- Row Level Security
ALTER TABLE plant_families ENABLE ROW LEVEL SECURITY;

CREATE POLICY "public_read_families"
    ON plant_families FOR SELECT USING (true);

CREATE POLICY "service_write_families"
    ON plant_families FOR ALL USING (auth.role() = 'service_role');
