-- Insert Kosi Barrage AOI (approximate bounding box around 26.4-26.7N, 86.7-87.1E)
INSERT INTO app.aoi (id, name, bbox, dem_path, conditioned)
VALUES (
    '11111111-1111-1111-1111-111111111111',
    'Kosi Barrage Region',
    ST_MakeEnvelope(86.7, 26.4, 87.1, 26.7, 4326),
    'dem-data/kosi_srtm.tif',
    true
) ON CONFLICT DO NOTHING;

-- Insert Kosi Barrage Dam Metadata (approx 26.526N, 86.927E)
INSERT INTO app.dam_metadata (id, aoi_id, name, location, height_m, reservoir_volume_mcm, dam_type, spillway_capacity_cumecs, year_built, source)
VALUES (
    '22222222-2222-2222-2222-222222222222',
    '11111111-1111-1111-1111-111111111111',
    'Kosi Barrage',
    ST_SetSRID(ST_MakePoint(86.9272, 26.5261), 4326),
    12.0,
    100.0, -- approximation for demo
    'Earth and Concrete',
    25000.0,
    1962,
    'Official Records'
) ON CONFLICT DO NOTHING;
