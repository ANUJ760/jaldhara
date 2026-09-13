# Jaldhara — Dam Break Inundation Modelling System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Problem Statement
**SIH26161 (NTRO, Disaster Management)**
Dam Break Inundation Modelling System

## Description
Jaldhara is a comprehensive, production-grade system for modelling dam break inundation scenarios. It integrates high-resolution DEMs, hydrological data, and state-of-the-art simulation engines (DualSPHysics, Delft3D) to provide rapid, accurate, and actionable inundation maps for disaster management authorities (DDMAs).

## Architecture

```mermaid
graph TD
    A[Frontend: Next.js] -->|REST/GraphQL| B(Backend: FastAPI)
    A -->|Auth| K[Keycloak]
    B -->|Task Queue| C[Celery / Redis]
    B -->|Metadata & Vector Data| D[(PostgreSQL + PostGIS)]
    B -->|Raster & Engine Data| M[(MinIO Object Storage)]
    C -->|Dispatch| E[DualSPHysics Engine]
    C -->|Dispatch| F[Delft3D Engine]
    E -->|Write| M
    F -->|Write| M
```

## Tech Stack
- **Frontend**: Next.js (React), TypeScript, Tailwind CSS, Mapbox/DeckGL
- **Backend**: Python, FastAPI, SQLAlchemy, GeoPandas, Rasterio
- **Database**: PostgreSQL with PostGIS
- **Cache/Queue**: Redis + Celery
- **Object Storage**: MinIO (S3-compatible)
- **Authentication**: Keycloak
- **Simulation Engines**: DualSPHysics, Delft3D D-Flow FM

## Quick Start
1. Copy environment variables: `cp .env.example .env`
2. Start the stack: `docker-compose up -d`
3. The frontend is available at `http://localhost:3000`
4. Backend API docs at `http://localhost:8000/docs`

## API Documentation
See [docs/API.md](docs/API.md) for details.

## Screenshots
*(Add screenshots here)*

## Team
*(Add team info here)*

## License
MIT License
