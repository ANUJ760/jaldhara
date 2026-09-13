"""
Froehlich (2008) Embankment Dam Breach Parameter Regression

Reference:
    Froehlich, D.C. (2008). "Embankment Dam Breach Parameters and Their
    Uncertainties." Journal of Hydraulic Engineering, 134(12), 1708-1721.
    DOI: 10.1061/(ASCE)0733-9429(2008)134:12(1708)

This module computes breach geometry and formation time from dam height,
reservoir volume, and failure mode using the Froehlich regression equations.
"""

import math
from enum import Enum
from dataclasses import dataclass
from typing import Optional


class FailureMode(str, Enum):
    OVERTOPPING = "overtopping"
    PIPING = "piping"
    INSTANT = "instant"


@dataclass
class BreachParameters:
    """Computed breach parameters from Froehlich regression."""
    breach_width_m: float          # Average breach width (m)
    formation_time_hrs: float      # Breach formation time (hours)
    side_slope_h_to_v: float       # Side slope (H:V ratio)
    invert_elevation_m: float      # Breach invert elevation above base (m)
    peak_discharge_cms: float      # Estimated peak discharge (m³/s)
    failure_mode: str              # Failure mode used
    dam_height_m: float            # Input dam height
    reservoir_volume_mcm: float    # Input reservoir volume


def compute_froehlich(
    dam_height_m: float,
    reservoir_volume_mcm: float,
    failure_mode: str,
    dam_crest_elevation_m: Optional[float] = None,
) -> BreachParameters:
    """
    Compute breach parameters using Froehlich (2008) regression.

    Args:
        dam_height_m: Height of the dam (m)
        reservoir_volume_mcm: Reservoir volume at time of failure (million m³)
        failure_mode: One of 'overtopping', 'piping', or 'instant'
        dam_crest_elevation_m: Optional crest elevation for invert calculation

    Returns:
        BreachParameters with computed values

    Raises:
        ValueError: If dam_height_m <= 0 or reservoir_volume_mcm <= 0
    """
    if dam_height_m <= 0:
        raise ValueError(f"Dam height must be positive, got {dam_height_m}")
    if reservoir_volume_mcm <= 0:
        raise ValueError(f"Reservoir volume must be positive, got {reservoir_volume_mcm}")

    # Convert million cubic meters to cubic meters
    V_w = reservoir_volume_mcm * 1e6  # m³
    h_b = dam_height_m                # m
    g = 9.81                          # m/s²

    # Failure mode coefficient K_o and side slopes
    mode = failure_mode.lower().strip()
    if mode == FailureMode.OVERTOPPING:
        K_o = 1.3
        side_slope = 1.0   # 1H:1V — wider breach for overtopping
    elif mode == FailureMode.PIPING:
        K_o = 1.0
        side_slope = 0.7   # 0.7H:1V — narrower for internal erosion
    elif mode == FailureMode.INSTANT:
        K_o = 1.3
        side_slope = 0.0   # Vertical walls for instantaneous collapse
    else:
        raise ValueError(
            f"Unknown failure mode '{failure_mode}'. "
            f"Use 'overtopping', 'piping', or 'instant'."
        )

    # ==========================================================
    # Froehlich (2008) Equation for average breach width:
    #   B_avg = 0.27 * K_o * V_w^0.32 * h_b^0.04  (metres)
    # ==========================================================
    breach_width = 0.27 * K_o * (V_w ** 0.32) * (h_b ** 0.04)

    # ==========================================================
    # Froehlich (2008) Equation for breach formation time:
    #   t_f = 63.2 * sqrt(V_w / (g * h_b²))  (seconds)
    # ==========================================================
    if mode == FailureMode.INSTANT:
        t_f_seconds = 0.0  # Instantaneous failure
    else:
        t_f_seconds = 63.2 * math.sqrt(V_w / (g * (h_b ** 2)))

    t_f_hours = t_f_seconds / 3600.0

    # ==========================================================
    # Invert elevation: how deep the breach cuts into the dam
    # For overtopping: breach typically extends to base → invert ≈ 0
    # For piping: invert at the pipe location, typically 0.3-0.5 * h_b
    # ==========================================================
    if mode == FailureMode.PIPING:
        invert_elevation = 0.3 * h_b  # Pipe typically in lower third
    else:
        invert_elevation = 0.0  # Full-depth breach

    if dam_crest_elevation_m is not None:
        invert_elevation = dam_crest_elevation_m - h_b + invert_elevation

    # ==========================================================
    # Peak discharge estimate using Froehlich (1995b):
    #   Q_p = 0.607 * V_w^0.295 * h_w^1.24  (m³/s)
    # where h_w = height of water above breach invert
    # ==========================================================
    h_w = h_b - (invert_elevation if dam_crest_elevation_m is None else 0)
    peak_discharge = 0.607 * (V_w ** 0.295) * (h_w ** 1.24)

    return BreachParameters(
        breach_width_m=round(breach_width, 2),
        formation_time_hrs=round(t_f_hours, 3),
        side_slope_h_to_v=side_slope,
        invert_elevation_m=round(invert_elevation, 2),
        peak_discharge_cms=round(peak_discharge, 1),
        failure_mode=mode,
        dam_height_m=dam_height_m,
        reservoir_volume_mcm=reservoir_volume_mcm,
    )


def validate_parameters(
    breach_width_m: float,
    formation_time_hrs: float,
    side_slope: float,
    dam_height_m: float,
) -> list[str]:
    """
    Validate user-overridden breach parameters against physical bounds.

    Returns a list of warning messages (empty list = all valid).
    """
    warnings: list[str] = []

    if breach_width_m <= 0:
        warnings.append("Breach width must be positive.")
    elif breach_width_m < dam_height_m * 0.5:
        warnings.append(
            f"Breach width ({breach_width_m}m) seems narrow relative to "
            f"dam height ({dam_height_m}m). Typical range: 0.5-5× dam height."
        )
    elif breach_width_m > dam_height_m * 10:
        warnings.append(
            f"Breach width ({breach_width_m}m) seems very wide relative to "
            f"dam height ({dam_height_m}m). Check units."
        )

    if formation_time_hrs < 0:
        warnings.append("Formation time cannot be negative.")
    elif formation_time_hrs > 24:
        warnings.append(
            f"Formation time ({formation_time_hrs}hrs) is unusually long. "
            "Typical range for embankment dams: 0.1-6 hours."
        )

    if side_slope < 0:
        warnings.append("Side slope ratio cannot be negative.")
    elif side_slope > 2.0:
        warnings.append(
            f"Side slope ({side_slope}H:V) is unusually flat. "
            "Typical range: 0-1.5 H:V."
        )

    return warnings


# ----- Demo convenience: Kosi Barrage defaults -----
KOSI_BARRAGE_DEFAULTS = {
    "dam_height_m": 12.0,
    "reservoir_volume_mcm": 850.0,   # Approximate for Kosi barrage pool
    "failure_mode": "overtopping",
    "dam_name": "Kosi Barrage",
    "location": {"lat": 26.5194, "lon": 86.9225},
}
