from datetime import datetime
import json

def run_gee_pipeline(aoi_id: int):
    # Mocking Google Earth Engine pipeline
    # NDWI/MNDWI computation from Sentinel-2
    # SAR backscatter water detection from Sentinel-1
    # Rolling 30-day baseline comparison
    # Anomaly detection
    
    mock_result = {
        "timestamp": datetime.utcnow().isoformat(),
        "satellite": "SENTINEL1",
        "water_extent_geojson": {"type": "FeatureCollection", "features": []},
        "ndwi_mean": 0.45,
        "baseline_ndwi_mean": 0.20,
        "anomaly_detected": True
    }
    
    return mock_result
