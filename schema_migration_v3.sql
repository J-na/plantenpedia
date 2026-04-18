-- ============================================================
-- Plantenpedia — Schema migratie v3
-- Voer dit script uit in de Supabase SQL Editor
-- (nadat schema.sql én schema_migration_v2.sql al zijn uitgevoerd)
-- ============================================================

-- Onderhoudsintensiviteit (laag / midden / hoog)
ALTER TABLE plants
    ADD COLUMN IF NOT EXISTS maintenance_level TEXT
        CHECK (maintenance_level IN ('laag', 'midden', 'hoog'));

CREATE INDEX IF NOT EXISTS idx_plants_maintenance ON plants(maintenance_level);
