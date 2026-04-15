-- ============================================================
-- Plantenpedia — Supabase / PostgreSQL schema
-- Voer dit script uit in de Supabase SQL Editor
-- ============================================================

-- UUID extensie (standaard al actief in Supabase)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================================
-- Hoofdtabel: planten
-- ============================================================
CREATE TABLE IF NOT EXISTS plants (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    -- Identificatie
    scientific_name TEXT NOT NULL UNIQUE,
    dutch_names     TEXT[] NOT NULL DEFAULT '{}',
    slug            TEXT UNIQUE,          -- URL-vriendelijke naam, gevuld via Python
    category        TEXT NOT NULL DEFAULT 'overig',

    -- Basisinformatie
    description     TEXT,                 -- uiterlijk & kenmerkende eigenschappen (markdown)
    distribution    TEXT,                 -- verspreidingsgebied (markdown)
    growth_habit    TEXT,                 -- groeiwijze beschrijving (markdown)
    bloom_start     SMALLINT CHECK (bloom_start BETWEEN 1 AND 12),
    bloom_end       SMALLINT CHECK (bloom_end   BETWEEN 1 AND 12),
    height_min      SMALLINT,             -- cm
    height_max      SMALLINT,             -- cm

    -- Filtervelden (geïndexeerd)
    edible          BOOLEAN NOT NULL DEFAULT FALSE,
    toxic           BOOLEAN NOT NULL DEFAULT FALSE,
    light_needs     TEXT CHECK (light_needs IN (
                        'vol_zon', 'halfschaduw', 'schaduw',
                        'zon_halfschaduw', 'halfschaduw_schaduw'
                    )),
    soil_types      TEXT[] NOT NULL DEFAULT '{}',

    -- Behoeftes
    fertilizer_needs    TEXT,             -- voeding & bemesting (markdown)
    pruning_info        TEXT,             -- snoeien (markdown)
    weed_behavior       TEXT,             -- woekerende eigenschappen (markdown)
    insects_animals     JSONB NOT NULL DEFAULT '[]',
    -- Formaat: [{"name": "Honingbij", "type": "insect", "desirable": true, "description": "..."}]
    pests_diseases      TEXT,             -- plagen & ziektes (markdown)
    ecological_value    TEXT,             -- ecologische waarde (markdown)

    -- Relatie met de mens
    edible_parts        TEXT,
    recipes             TEXT,             -- markdown
    taste               TEXT,
    nutritional_value   TEXT,             -- markdown
    toxic_info          TEXT,             -- markdown
    lookalikes          JSONB NOT NULL DEFAULT '[]',
    -- Formaat: [{"name": "Gevlekte scheerling", "difference": "...", "photo_url": "..."}]
    wood_properties     TEXT,             -- markdown (alleen voor bomen/struiken)
    medicinal_uses      TEXT,             -- markdown
    other_uses          TEXT,             -- markdown

    -- Media
    photos JSONB NOT NULL DEFAULT '[]',
    -- Formaat: [{"type": "bloeiwijze", "url": "...", "source": "Wikimedia Commons", "license": "CC BY-SA 4.0", "caption": "..."}]
    -- Typen: jonge_plant | bloeiwijze | zaad | habitus | blad | stam | vrucht | algemeen

    -- Cultivars & variëteiten
    cultivars JSONB NOT NULL DEFAULT '[]',
    -- Formaat: [{"name": "'Atropurpureum'", "description": "...", "photo_url": "...", "photo_source": "..."}]

    -- Bronnen
    sources JSONB NOT NULL DEFAULT '[]',
    -- Formaat: [{"title": "Flora van Nederland", "url": "https://...", "description": "..."}]

    -- Metadata
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================
-- Indexen voor filtering en zoeken
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_plants_category    ON plants(category);
CREATE INDEX IF NOT EXISTS idx_plants_edible      ON plants(edible);
CREATE INDEX IF NOT EXISTS idx_plants_toxic       ON plants(toxic);
CREATE INDEX IF NOT EXISTS idx_plants_light       ON plants(light_needs);
CREATE INDEX IF NOT EXISTS idx_plants_bloom       ON plants(bloom_start, bloom_end);
CREATE INDEX IF NOT EXISTS idx_plants_soil        ON plants USING GIN(soil_types);
CREATE INDEX IF NOT EXISTS idx_plants_slug        ON plants(slug);


-- ============================================================
-- Soort van de dag
-- ============================================================
CREATE TABLE IF NOT EXISTS plant_of_day (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    plant_id        UUID NOT NULL REFERENCES plants(id) ON DELETE CASCADE,
    scheduled_date  DATE NOT NULL UNIQUE,
    scheduled_by    TEXT NOT NULL DEFAULT 'systeem',
    notes           TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_pod_date ON plant_of_day(scheduled_date);

-- ============================================================
-- Trigger: updated_at automatisch bijwerken
-- ============================================================
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_plants_updated_at
    BEFORE UPDATE ON plants
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at();

-- ============================================================
-- Row Level Security (optioneel — aan te raden voor productie)
-- Laat iedereen lezen, maar alleen server-side keys schrijven
-- ============================================================
ALTER TABLE plants       ENABLE ROW LEVEL SECURITY;
ALTER TABLE plant_of_day ENABLE ROW LEVEL SECURITY;

-- Iedereen mag lezen
CREATE POLICY "public_read_plants"
    ON plants FOR SELECT USING (true);

CREATE POLICY "public_read_pod"
    ON plant_of_day FOR SELECT USING (true);

-- Schrijven alleen via service_role key (admin)
CREATE POLICY "service_write_plants"
    ON plants FOR ALL USING (auth.role() = 'service_role');

CREATE POLICY "service_write_pod"
    ON plant_of_day FOR ALL USING (auth.role() = 'service_role');
