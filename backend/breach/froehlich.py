import math

def compute_froehlich(dam_height_m: float, reservoir_volume_mcm: float, failure_mode: str):
    """
    Froehlich (2008) regression implementation for breach parameters.
    """
    # Convert MCM to m^3
    V_w = reservoir_volume_mcm * 1e6
    h_b = dam_height_m
    g = 9.81
    
    if failure_mode.lower() == "overtopping":
        K_o = 1.3
        side_slope = 1.0 # 1H:1V
    else: # piping
        K_o = 1.0
        side_slope = 0.7 # 0.7H:1V
        
    # Breach width: B_avg = 0.27 * K_o * V_w^0.32 * h_b^0.04
    breach_width = 0.27 * K_o * (V_w ** 0.32) * (h_b ** 0.04)
    
    # Formation time: t_f = 63.2 * sqrt(V_w / (g * h_b^2))
    t_f_seconds = 63.2 * math.sqrt(V_w / (g * (h_b ** 2)))
    t_f_hours = t_f_seconds / 3600.0
    
    return {
        "breach_width_m": breach_width,
        "formation_time_hrs": t_f_hours,
        "side_slope": side_slope,
        "invert_elevation_m": 0.0 # Assumed base of dam for full breach
    }
