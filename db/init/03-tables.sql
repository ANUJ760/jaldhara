CREATE TABLE IF NOT EXISTS app.aoi (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    bbox GEOMETRY(Polygon, 4326) NOT NULL,
    dem_path TEXT,
    conditioned BOOLEAN DEFAULT false,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS app.dam_metadata (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aoi_id UUID REFERENCES app.aoi(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    location GEOMETRY(Point, 4326) NOT NULL,
    height_m FLOAT,
    reservoir_volume_mcm FLOAT,
    dam_type TEXT,
    spillway_capacity_cumecs FLOAT,
    year_built INT,
    source TEXT
);

CREATE TABLE IF NOT EXISTS app.jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aoi_id UUID REFERENCES app.aoi(id) ON DELETE CASCADE,
    dam_id UUID REFERENCES app.dam_metadata(id) ON DELETE CASCADE,
    engine TEXT NOT NULL,
    status TEXT NOT NULL,
    breach_params JSONB,
    started_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ,
    result_path TEXT,
    error_msg TEXT
);

CREATE TABLE IF NOT EXISTS app.gee_readings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aoi_id UUID REFERENCES app.aoi(id) ON DELETE CASCADE,
    timestamp TIMESTAMPTZ NOT NULL,
    satellite TEXT,
    water_extent JSONB,
    ndwi_mean FLOAT,
    baseline_ndwi_mean FLOAT,
    anomaly_detected BOOLEAN
);
