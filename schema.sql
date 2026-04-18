-- ============================================================
-- Plantenpedia — Volledig databaseschema (idempotent)
--
-- Voer dit script uit in de Supabase SQL Editor om de database
-- aan te maken of bij te werken. Het script is idempotent:
-- veilig om meerdere keren uit te voeren op een bestaande DB.
--
-- Huidige versie bevat alle wijzigingen t/m v3.
-- ============================================================

-- UUID extensie (standaard al actief in Supabase)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


-- ============================================================
-- Tabel: plants
-- ============================================================
CREATE TABLE IF NOT EXISTS plants (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    -- Identificatie
    scientific_name TEXT NOT NULL UNIQUE,
    dutch_names     TEXT[] NOT NULL DEFAULT '{}',
    slug            TEXT UNIQUE,          -- URL-vriendelijke naam, gevuld via Python
    category        TEXT NOT NULL DEFAULT 'overig',
    -- Geldige waarden: vaste_plant | eenjarige | tweejarige | bol_knol | kuipplant
    --                  wilde_plant | waterplant | keukenkruid | gras | heester
    --                  wintergroene_heester | boom | conifeer | klimplant | roos | overig

    -- Basisinformatie
    description     TEXT,                 -- uiterlijk & kenmerkende eigenschappen (markdown)
    distribution    TEXT,                 -- verspreidingsgebied (markdown)
    growth_habit    TEXT,                 -- groeiwijze & hoogte (markdown)
    bloom_start     SMALLINT CHECK (bloom_start BETWEEN 1 AND 12),
    bloom_end       SMALLINT CHECK (bloom_end   BETWEEN 1 AND 12),
    height_min      SMALLINT,             -- minimale hoogte in cm
    height_max      SMALLINT,             -- maximale hoogte in cm

    -- Herkomst & taxonomie (toegevoegd v2)
    family          TEXT,                 -- wetenschappelijke familienaam
    family_common   TEXT,                 -- Nederlandse familienaam
    origin          TEXT,                 -- geografische herkomst

    -- Winterhardheid & groeiwijze (toegevoegd v2)
    evergreen       BOOLEAN NOT NULL DEFAULT FALSE,
    hardiness       TEXT CHECK (hardiness IN (
                        'volledig_winterhard',
                        'winterhard',
                        'matig_winterhard',
                        'vorstgevoelig',
                        'niet_winterhard'
                    )),

    -- Onderhoud (toegevoegd v3)
    maintenance_level TEXT CHECK (maintenance_level IN ('laag', 'midden', 'hoog')),

    -- Filtervelden (geïndexeerd)
    edible          BOOLEAN NOT NULL DEFAULT FALSE,
    toxic           BOOLEAN NOT NULL DEFAULT FALSE,
    light_needs     TEXT CHECK (light_needs IN (
                        'vol_zon', 'halfschaduw', 'schaduw',
                        'zon_halfschaduw', 'halfschaduw_schaduw'
                    )),
    soil_types      TEXT[] NOT NULL DEFAULT '{}',
    -- Geldige waarden: zand | leem | klei | veen | humus | kalk | normaal | nat | droog

    -- Behoeftes & ecologie
    fertilizer_needs    TEXT,             -- voeding & bemesting (markdown)
    pruning_info        TEXT,             -- snoeiadviezen (markdown)
    weed_behavior       TEXT,             -- woekerende of zelfzaaiende eigenschappen (markdown)
    pests_diseases      TEXT,             -- plagen & ziektes + ecologische aanpak (markdown)
    ecological_value    TEXT,             -- ecologische waarde & rol in ecosysteem (markdown)
    insects_animals     JSONB NOT NULL DEFAULT '[]',
    -- Formaat: [{"name": "Honingbij", "type": "insect", "desirable": true, "description": "..."}]
    -- type-waarden: insect | vlinder | vogel | zoogdier | overig

    -- Relatie met de mens
    edible_parts        TEXT,             -- welke delen zijn eetbaar
    recipes             TEXT,             -- bereidingswijzen en receptideeën (markdown)
    taste               TEXT,             -- smaakbeschrijving
    nutritional_value   TEXT,             -- voedingswaarde (markdown)
    toxic_info          TEXT,             -- giftige delen, symptomen, risico's (markdown)
    medicinal_uses      TEXT,             -- medicinale toepassingen (markdown)
    other_uses          TEXT,             -- overige toepassingen: vezel, kleurstof, etc. (markdown)
    wood_properties     TEXT,             -- houtkenmerken (alleen bomen/struiken, markdown)
    lookalikes          JSONB NOT NULL DEFAULT '[]',
    -- Formaat: [{"name": "Gevlekte scheerling", "difference": "...", "photo_url": "..."}]

    -- Media
    photos JSONB NOT NULL DEFAULT '[]',
    -- Formaat: [{"url": "...", "source": "Wikimedia Commons", "license": "CC BY-SA 4.0", "caption": "..."}]
    -- Foto-typen (optioneel "type" veld): jonge_plant | bloeiwijze | zaad | habitus | blad | stam | vrucht | algemeen

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
-- Tabel: plant_families  (toegevoegd v2)
-- ============================================================
CREATE TABLE IF NOT EXISTS plant_families (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        TEXT NOT NULL UNIQUE,   -- wetenschappelijke familienaam (bijv. Asteraceae)
    dutch_name  TEXT,                   -- Nederlandse naam (bijv. Composietenfamilie)
    description TEXT,                   -- algemene beschrijving (markdown)
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);


-- ============================================================
-- Tabel: plant_of_day
-- ============================================================
CREATE TABLE IF NOT EXISTS plant_of_day (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    plant_id        UUID NOT NULL REFERENCES plants(id) ON DELETE CASCADE,
    scheduled_date  DATE NOT NULL UNIQUE,
    scheduled_by    TEXT NOT NULL DEFAULT 'systeem',
    notes           TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);


-- ============================================================
-- Indexen
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_plants_category      ON plants(category);
CREATE INDEX IF NOT EXISTS idx_plants_edible        ON plants(edible);
CREATE INDEX IF NOT EXISTS idx_plants_toxic         ON plants(toxic);
CREATE INDEX IF NOT EXISTS idx_plants_light         ON plants(light_needs);
CREATE INDEX IF NOT EXISTS idx_plants_bloom         ON plants(bloom_start, bloom_end);
CREATE INDEX IF NOT EXISTS idx_plants_soil          ON plants USING GIN(soil_types);
CREATE INDEX IF NOT EXISTS idx_plants_slug          ON plants(slug);
CREATE INDEX IF NOT EXISTS idx_plants_evergreen     ON plants(evergreen);
CREATE INDEX IF NOT EXISTS idx_plants_hardiness     ON plants(hardiness);
CREATE INDEX IF NOT EXISTS idx_plants_family        ON plants(family);
CREATE INDEX IF NOT EXISTS idx_plants_maintenance   ON plants(maintenance_level);
CREATE INDEX IF NOT EXISTS idx_families_name        ON plant_families(name);
CREATE INDEX IF NOT EXISTS idx_pod_date             ON plant_of_day(scheduled_date);


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

CREATE TRIGGER trg_families_updated_at
    BEFORE UPDATE ON plant_families
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at();


-- ============================================================
-- Row Level Security
-- Iedereen mag lezen; schrijven alleen via service_role key
-- ============================================================
ALTER TABLE plants         ENABLE ROW LEVEL SECURITY;
ALTER TABLE plant_of_day   ENABLE ROW LEVEL SECURITY;
ALTER TABLE plant_families ENABLE ROW LEVEL SECURITY;

CREATE POLICY IF NOT EXISTS "public_read_plants"
    ON plants FOR SELECT USING (true);

CREATE POLICY IF NOT EXISTS "public_read_pod"
    ON plant_of_day FOR SELECT USING (true);

CREATE POLICY IF NOT EXISTS "public_read_families"
    ON plant_families FOR SELECT USING (true);

CREATE POLICY IF NOT EXISTS "service_write_plants"
    ON plants FOR ALL USING (auth.role() = 'service_role');

CREATE POLICY IF NOT EXISTS "service_write_pod"
    ON plant_of_day FOR ALL USING (auth.role() = 'service_role');

CREATE POLICY IF NOT EXISTS "service_write_families"
    ON plant_families FOR ALL USING (auth.role() = 'service_role');
