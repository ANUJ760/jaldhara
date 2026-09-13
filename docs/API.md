# API Documentation

## Auth Endpoints
Authenticated via Keycloak OAuth2.

## Simulation Endpoints

`POST /api/simulations`
Trigger a new simulation.
```json
{
  "dam_id": "uuid",
  "engine": "sph",
  "breach_params": {}
}
```

`GET /api/simulations/{id}`
Check status of a simulation.
```json
{
  "status": "COMPLETED",
  "result_path": "sim-output/job-123.nc"
}
```
