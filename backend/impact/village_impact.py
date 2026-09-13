def compute_impact(job_id: int):
    # Hardcode realistic Kosi area villages with real names/coordinates
    villages = [
        {"village_name": "Kusaha", "lat": 26.45, "lon": 86.95, "population": 1500},
        {"village_name": "Bhantabari", "lat": 26.48, "lon": 86.98, "population": 2200},
        {"village_name": "Madhepur", "lat": 26.35, "lon": 86.85, "population": 5000}
    ]
    
    impacts = []
    # Mock computation based on distance from barrage (~26.525, 86.93)
    barrage_lat, barrage_lon = 26.525, 86.93
    
    for v in villages:
        dist = ((v["lat"] - barrage_lat)**2 + (v["lon"] - barrage_lon)**2)**0.5
        dist_km = dist * 111 # rough approx
        
        # arrival time based on distance (assuming wave speed 5 m/s = 18 km/h)
        arrival_time_hrs = max(0.1, dist_km / 18.0)
        
        # Max depth decays with distance
        max_depth_m = max(0.5, 5.0 - (dist_km * 0.1))
        
        # velocity decays with distance
        max_velocity_ms = max(0.5, 6.0 - (dist_km * 0.15))
        
        # Priority score = population * (1/arrival_time_hours)
        evac_priority = v["population"] * (1.0 / arrival_time_hrs)
        
        impacts.append({
            "village_name": v["village_name"],
            "lat": v["lat"],
            "lon": v["lon"],
            "arrival_time_hrs": arrival_time_hrs,
            "max_depth_m": max_depth_m,
            "max_velocity_ms": max_velocity_ms,
            "population": v["population"],
            "evacuation_priority": evac_priority
        })
        
    return impacts
