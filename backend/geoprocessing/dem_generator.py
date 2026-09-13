"""
Synthetic DEM Generator for the Kosi Barrage Area

Generates a realistic synthetic Digital Elevation Model (DEM) for demo
purposes since Bhuvan data requires manual download with registration.

The generated terrain includes:
- Kosi River valley running roughly north to south
- Flat alluvial floodplain on both sides
- Barrage/dam structure at the correct geographic location
- Realistic elevation values (30-80m range for the Gangetic plain)
- Natural-looking terrain with Perlin-like noise
- Tributary channels

Output: GeoTIFF with EPSG:4326 CRS
AOI: 26.4°N–26.7°N, 86.7°E–87.1°E (~33km × 44km)
"""

import numpy as np

try:
    import rasterio
    from rasterio.transform import from_origin
    HAS_RASTERIO = True
except ImportError:
    HAS_RASTERIO = False


def _smooth_noise(shape: tuple[int, int], scale: float = 50.0) -> np.ndarray:
    """Generate smooth noise using interpolated random grid (poor man's Perlin)."""
    h, w = shape
    # Create small random grid and upscale
    small_h = max(2, int(h / scale))
    small_w = max(2, int(w / scale))
    small = np.random.RandomState(42).randn(small_h, small_w)

    # Bilinear interpolation to full size
    from numpy import interp
    y_coords = np.linspace(0, small_h - 1, h)
    x_coords = np.linspace(0, small_w - 1, w)

    # Interpolate rows
    result = np.zeros((h, w), dtype=np.float32)
    for i, y in enumerate(y_coords):
        y0, y1 = int(y), min(int(y) + 1, small_h - 1)
        fy = y - y0
        row = small[y0] * (1 - fy) + small[y1] * fy
        result[i] = np.interp(x_coords, np.arange(small_w), row)

    return result


def generate_synthetic_kosi_dem(
    output_path: str,
    resolution_deg: float = 0.001,
    bbox: tuple[float, float, float, float] = (86.7, 26.4, 87.1, 26.7),
) -> str:
    """
    Generate a realistic synthetic DEM for the Kosi Barrage area.

    Args:
        output_path: Path to save the GeoTIFF
        resolution_deg: Resolution in degrees (~100m at 0.001°)
        bbox: Bounding box (west, south, east, north)

    Returns:
        Path to the generated GeoTIFF file

    The generated terrain models:
    - Kosi River valley (30-35m elevation) running N-S
    - Flat floodplain (38-45m) on both sides
    - Gentle slope from north (higher, ~50m) to south (lower, ~35m)
    - Dam/barrage structure (~52m, i.e. ~12m above riverbed) at 26.52°N
    - Tributary channels from NW and NE
    - Natural terrain undulation
    """
    west, south, east, north = bbox
    width = int((east - west) / resolution_deg)
    height = int((north - south) / resolution_deg)

    rng = np.random.RandomState(2008)  # Seed: 2008 Kosi flood year

    # === Base elevation: gentle south-sloping plain ===
    y_grid = np.linspace(0, 1, height)[:, np.newaxis]  # 0=north, 1=south
    x_grid = np.linspace(0, 1, width)[np.newaxis, :]
    # North ~50m, South ~35m
    dem = 50.0 - 15.0 * y_grid + np.zeros((height, width), dtype=np.float32)

    # === Add smooth terrain noise (±3m) ===
    noise1 = _smooth_noise((height, width), scale=30.0) * 3.0
    noise2 = _smooth_noise((height, width), scale=80.0) * 1.5
    dem += noise1 + noise2

    # === Kosi River channel (runs N-S with slight meander) ===
    barrage_x_frac = (86.9225 - west) / (east - west)  # River at barrage longitude
    for y_idx in range(height):
        y_frac = y_idx / height
        # River meanders slightly: sinusoidal offset
        meander = 0.03 * np.sin(y_frac * 6 * np.pi)
        river_center = barrage_x_frac + meander
        river_center_px = int(river_center * width)

        for x_idx in range(width):
            dist_to_river = abs(x_idx - river_center_px)
            # Main channel: 20 pixels wide (~2km)
            if dist_to_river < 10:
                # Deep channel bed
                channel_depth = 8.0 * (1.0 - (dist_to_river / 10.0) ** 2)
                dem[y_idx, x_idx] -= channel_depth
            elif dist_to_river < 30:
                # Floodplain near river: slightly lower
                bank_factor = (dist_to_river - 10) / 20.0
                dem[y_idx, x_idx] -= 2.0 * (1.0 - bank_factor)

    # === Tributary from NW (Kamla River approximation) ===
    for y_idx in range(int(0.3 * height)):
        x_center = int(0.2 * width + y_idx * 0.8)
        if 0 <= x_center < width:
            for dx in range(-5, 6):
                xi = x_center + dx
                if 0 <= xi < width:
                    depth = 3.0 * (1.0 - (abs(dx) / 5.0) ** 2)
                    dem[y_idx, xi] -= depth

    # === Tributary from NE (Kosi branch) ===
    for y_idx in range(int(0.4 * height)):
        x_center = int(0.8 * width - y_idx * 0.3)
        if 0 <= x_center < width:
            for dx in range(-4, 5):
                xi = x_center + dx
                if 0 <= xi < width:
                    depth = 2.5 * (1.0 - (abs(dx) / 4.0) ** 2)
                    dem[y_idx, xi] -= depth

    # === Kosi Barrage structure ===
    # Location: 26.5194°N → row index
    barrage_y = int((north - 26.5194) / resolution_deg)
    barrage_x_start = int((86.88 - west) / resolution_deg)
    barrage_x_end = int((86.96 - west) / resolution_deg)

    if 0 <= barrage_y < height:
        for x_idx in range(max(0, barrage_x_start), min(width, barrage_x_end)):
            # Main barrage wall: 12m above riverbed (~52m absolute)
            dem[barrage_y, x_idx] = max(dem[barrage_y, x_idx], 52.0)
            # Approach ramps (1 row above and below)
            if barrage_y > 0:
                dem[barrage_y - 1, x_idx] = max(dem[barrage_y - 1, x_idx], 49.0)
            if barrage_y < height - 1:
                dem[barrage_y + 1, x_idx] = max(dem[barrage_y + 1, x_idx], 49.0)
            if barrage_y > 1:
                dem[barrage_y - 2, x_idx] = max(dem[barrage_y - 2, x_idx], 46.0)
            if barrage_y < height - 2:
                dem[barrage_y + 2, x_idx] = max(dem[barrage_y + 2, x_idx], 46.0)

    # === Add fine-grain noise (±0.5m) ===
    fine_noise = rng.normal(0, 0.5, (height, width)).astype(np.float32)
    dem += fine_noise

    # Ensure no negative elevations
    dem = np.maximum(dem, 0.5)

    # === Write GeoTIFF ===
    if not HAS_RASTERIO:
        # Fallback: save as raw numpy
        np.save(output_path.replace('.tif', '.npy'), dem)
        return output_path.replace('.tif', '.npy')

    transform = from_origin(west, north, resolution_deg, resolution_deg)

    with rasterio.open(
        output_path,
        "w",
        driver="GTiff",
        height=dem.shape[0],
        width=dem.shape[1],
        count=1,
        dtype=np.float32,
        crs="EPSG:4326",
        transform=transform,
        compress="deflate",
        nodata=-9999.0,
    ) as dst:
        dst.write(dem, 1)
        dst.update_tags(
            AREA_OR_POINT="Area",
            TIFFTAG_IMAGEDESCRIPTION=(
                "Synthetic DEM for Kosi Barrage area (SIH26161 Jaldhara prototype). "
                "Not real elevation data."
            ),
        )

    return output_path


def generate_kosi_river_geometry() -> dict:
    """
    Generate a GeoJSON LineString for the Kosi River channel
    for burning into the DEM during conditioning.
    """
    # Simplified Kosi River centerline from barrage to downstream
    coordinates = [
        [86.9225, 26.7000],  # North entry
        [86.9300, 26.6500],
        [86.9200, 26.6000],
        [86.9350, 26.5500],
        [86.9225, 26.5194],  # Barrage location
        [86.9100, 26.4800],
        [86.9250, 26.4400],
        [86.9000, 26.4000],  # South exit
    ]
    return {
        "type": "Feature",
        "properties": {"name": "Kosi River", "type": "river_channel"},
        "geometry": {"type": "LineString", "coordinates": coordinates},
    }


def generate_barrage_geometry() -> dict:
    """
    Generate a GeoJSON Polygon for the Kosi Barrage footprint
    for inserting as a raised ridge in the conditioned DEM.
    """
    # Barrage is roughly 1.15km wide across the river
    return {
        "type": "Feature",
        "properties": {
            "name": "Kosi Barrage",
            "height_m": 12.0,
            "crest_elevation_m": 52.0,
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [86.88, 26.5184],
                [86.96, 26.5184],
                [86.96, 26.5204],
                [86.88, 26.5204],
                [86.88, 26.5184],
            ]],
        },
    }
