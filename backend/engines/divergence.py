import numpy as np
# In a real app we'd use rasterio to read tif files

def compute_divergence(sph_raster_path: str, delft3d_raster_path: str):
    # Mock compute divergence
    return {
        "rmse": 0.5,
        "bias": 0.1,
        "f_score": 0.92,
        "divergence_raster_url": "minio_url_to_divergence"
    }
