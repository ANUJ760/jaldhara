import numpy as np
import rasterio
from rasterio.transform import from_origin

def generate_synthetic_kosi_dem(output_path: str):
    """
    Generate realistic synthetic DEM data for the Kosi area for demo purposes.
    Kosi Barrage area: ~26.4-26.7N, 86.7-87.1E
    """
    # 0.001 deg resolution approx 100m
    width = 400
    height = 300
    
    # Create base flat floodplain (elevation ~40m)
    dem = np.full((height, width), 40.0, dtype=np.float32)
    
    # Add random terrain noise
    noise = np.random.normal(0, 2, (height, width))
    dem += noise
    
    # Create River valley running north-south (x center = 200)
    for y in range(height):
        for x in range(width):
            dist_to_river = abs(x - 200)
            if dist_to_river < 50:
                # River channel is lower, ~30m
                dem[y, x] = 30.0 + (dist_to_river / 50.0) * 10.0
                
    # Dam/barrage structure (raised ridge across the river)
    # y = 150, x between 150 and 250
    for x in range(150, 251):
        dem[150, x] = 52.0  # ~12m height above 40m floodplain
        dem[149, x] = 50.0
        dem[151, x] = 50.0
    
    # Define transform
    # Top left corner: 86.7E, 26.7N
    transform = from_origin(86.7, 26.7, 0.001, 0.001)
    
    # Save as GeoTIFF
    with rasterio.open(
        output_path,
        'w',
        driver='GTiff',
        height=dem.shape[0],
        width=dem.shape[1],
        count=1,
        dtype=dem.dtype,
        crs='EPSG:4326',
        transform=transform,
    ) as dst:
        dst.write(dem, 1)
        
    return output_path
