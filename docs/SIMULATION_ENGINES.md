# Simulation Engines

## DualSPHysics (SPH)
- Uses Smoothed Particle Hydrodynamics.
- Best for extreme near-field breach phenomena (rapid wave onset, high turbulence).
- Requires GPU acceleration for reasonable runtime.

## Delft3D D-Flow FM
- Best for far-field inundation modelling over large floodplains.
- Uses shallow water equations (SWE).
- Outputs NetCDF files.

## Divergence Analysis
- The backend compares the high-fidelity near-field results (SPH) with far-field inputs (Delft3D) to harmonize boundary conditions between models.
