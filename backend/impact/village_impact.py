"""
Village Impact Analysis for Dam Break Inundation

Computes flood wave arrival time, maximum depth, velocity, and evacuation
priority for settlements downstream of a dam breach. Uses simplified
flood wave propagation based on distance and terrain.

The village data is based on real settlements in the Kosi River floodplain
downstream of the Kosi Barrage in Bihar, India.
"""

import math
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class VillageData:
    """Settlement data for impact analysis."""
    name: str
    lat: float
    lon: float
    population: int
    district: str
    elevation_m: float = 50.0


# Real villages in the Kosi floodplain downstream of the Kosi Barrage
# Coordinates and populations are approximate but realistic
KOSI_FLOODPLAIN_VILLAGES: list[VillageData] = [
    # --- Supaul District (closest to barrage) ---
    VillageData("Birpur", 26.5050, 86.9300, 28_000, "Supaul", 52),
    VillageData("Nirmali", 26.3140, 86.5870, 18_000, "Supaul", 48),
    VillageData("Basantpur", 26.4800, 86.9100, 3_500, "Supaul", 51),
    VillageData("Pratapganj", 26.4450, 86.8800, 5_200, "Supaul", 50),
    VillageData("Kishanpur", 26.4200, 86.9500, 4_100, "Supaul", 49),
    VillageData("Pipra", 26.3900, 86.8500, 2_800, "Supaul", 48),
    VillageData("Supaul", 26.1230, 86.5950, 42_000, "Supaul", 42),

    # --- Saharsa District ---
    VillageData("Saharsa", 25.8770, 86.5990, 156_000, "Saharsa", 38),
    VillageData("Mahishi", 25.9490, 86.4600, 12_000, "Saharsa", 40),
    VillageData("Simri Bakhtiarpur", 25.9950, 86.6000, 8_500, "Saharsa", 41),

    # --- Madhepura District ---
    VillageData("Madhepura", 25.9210, 86.7930, 74_000, "Madhepura", 39),
    VillageData("Udakishunganj", 25.9800, 86.8500, 6_200, "Madhepura", 42),
    VillageData("Murliganj", 25.8900, 86.9950, 8_700, "Madhepura", 38),
    VillageData("Gamharia", 26.2000, 86.8700, 3_900, "Madhepura", 45),

    # --- Purnia / Araria (further downstream) ---
    VillageData("Purnia", 25.7780, 87.4730, 282_000, "Purnia", 36),
    VillageData("Araria", 26.1500, 87.5140, 98_000, "Araria", 44),
    VillageData("Forbesganj", 26.3050, 87.2650, 52_000, "Araria", 46),

    # --- Katihar (confluence area) ---
    VillageData("Katihar", 25.5410, 87.5720, 240_000, "Katihar", 32),

    # --- Khagaria ---
    VillageData("Khagaria", 25.5020, 86.4690, 50_000, "Khagaria", 34),

    # --- Small settlements very close to barrage ---
    VillageData("Kusaha", 26.5300, 86.9500, 1_500, "Supaul", 53),
    VillageData("Bhantabari", 26.5100, 86.9600, 2_200, "Supaul", 52),
    VillageData("Rajbiraj Tola", 26.4900, 86.9200, 1_800, "Supaul", 51),
    VillageData("Ghoghardiha", 26.3500, 86.7300, 4_600, "Supaul", 47),
]


@dataclass
class VillageImpact:
    """Impact assessment result for a single village."""
    village_name: str
    district: str
    lat: float
    lon: float
    population: int
    distance_km: float
    arrival_time_hrs: float
    max_depth_m: float
    max_velocity_ms: float
    evacuation_priority: float
    risk_level: str  # CRITICAL, HIGH, MEDIUM, LOW


def _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Haversine distance between two points in kilometers."""
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(dlon / 2) ** 2
    )
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def _risk_level(priority: float) -> str:
    """Classify risk level from evacuation priority score."""
    if priority >= 50_000:
        return "CRITICAL"
    elif priority >= 10_000:
        return "HIGH"
    elif priority >= 2_000:
        return "MEDIUM"
    else:
        return "LOW"


def compute_impact(
    job_id: int,
    barrage_lat: float = 26.5194,
    barrage_lon: float = 86.9225,
    peak_discharge_cms: float = 12_000.0,
    wave_speed_ms: float = 5.0,
    villages: Optional[list[VillageData]] = None,
) -> list[dict]:
    """
    Compute village-level impact analysis for a dam breach scenario.

    The analysis uses simplified flood wave propagation:
    - Arrival time ∝ distance / wave_speed
    - Max depth decays exponentially with distance
    - Velocity decays with distance from breach
    - Evacuation priority = population × (1 / arrival_time_hours)

    Args:
        job_id: Simulation job ID for linking results
        barrage_lat: Dam/barrage latitude
        barrage_lon: Dam/barrage longitude
        peak_discharge_cms: Peak breach discharge (m³/s)
        wave_speed_ms: Flood wave propagation speed (m/s)
        villages: Optional custom village list (defaults to Kosi floodplain)

    Returns:
        List of village impact dictionaries sorted by evacuation priority
    """
    if villages is None:
        villages = KOSI_FLOODPLAIN_VILLAGES

    wave_speed_kmh = wave_speed_ms * 3.6  # Convert m/s to km/h
    # Discharge scaling factor: higher discharge → deeper flood
    q_factor = (peak_discharge_cms / 10_000.0) ** 0.5

    impacts: list[VillageImpact] = []

    for v in villages:
        dist_km = _haversine_km(barrage_lat, barrage_lon, v.lat, v.lon)

        # Skip villages beyond 200km — unrealistic for this scenario
        if dist_km > 200:
            continue

        # --- Arrival time ---
        # Wave slows as it spreads: effective speed = base_speed / (1 + 0.01*dist)
        effective_speed = wave_speed_kmh / (1 + 0.01 * dist_km)
        arrival_time_hrs = max(0.05, dist_km / effective_speed)

        # --- Max depth (m) ---
        # Exponential decay: depth = base_depth * exp(-decay * dist)
        base_depth = 6.0 * q_factor
        depth_decay = 0.015
        max_depth = max(0.1, base_depth * math.exp(-depth_decay * dist_km))

        # --- Max velocity (m/s) ---
        base_velocity = 8.0 * q_factor
        vel_decay = 0.02
        max_velocity = max(0.2, base_velocity * math.exp(-vel_decay * dist_km))

        # --- Evacuation priority ---
        evac_priority = v.population * (1.0 / arrival_time_hrs)

        impact = VillageImpact(
            village_name=v.name,
            district=v.district,
            lat=v.lat,
            lon=v.lon,
            population=v.population,
            distance_km=round(dist_km, 1),
            arrival_time_hrs=round(arrival_time_hrs, 2),
            max_depth_m=round(max_depth, 2),
            max_velocity_ms=round(max_velocity, 2),
            evacuation_priority=round(evac_priority, 0),
            risk_level=_risk_level(evac_priority),
        )
        impacts.append(impact)

    # Sort by evacuation priority (highest first)
    impacts.sort(key=lambda x: x.evacuation_priority, reverse=True)

    return [asdict(imp) for imp in impacts]


def compute_evacuation_routes(impacts: list[dict]) -> list[dict]:
    """
    Generate evacuation route suggestions based on impact analysis.
    Routes point away from the flood direction (generally west/south
    from the Kosi floodplain toward higher ground).
    """
    routes = []
    for imp in impacts:
        if imp["risk_level"] in ("CRITICAL", "HIGH"):
            # Suggest evacuation to higher ground (west/northwest)
            safe_lat = imp["lat"] + 0.05
            safe_lon = imp["lon"] - 0.1
            routes.append({
                "village_name": imp["village_name"],
                "risk_level": imp["risk_level"],
                "available_time_hrs": imp["arrival_time_hrs"],
                "evacuation_direction": "Northwest to higher ground",
                "safe_point": {"lat": round(safe_lat, 4), "lon": round(safe_lon, 4)},
                "estimated_distance_km": round(
                    _haversine_km(imp["lat"], imp["lon"], safe_lat, safe_lon), 1
                ),
            })
    return routes
