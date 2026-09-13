# Deployment Guide

## Prerequisites
- Docker & Docker Compose
- 16GB+ RAM (preferred for simulations)
- GPU support (optional but highly recommended for DualSPHysics)

## Development Setup
```bash
cp .env.example .env
make dev
```

## Production Setup
- Update `.env` with secure credentials.
- Use `docker-compose.yml` for single-node.
- For multi-node, deploy using Kubernetes or Docker Swarm onto MeghRaj instances.

## Environment Variables
- `DATABASE_URL`
- `REDIS_URL`
- `MINIO_ROOT_USER`, `MINIO_ROOT_PASSWORD`
- `KEYCLOAK_ADMIN`, `KEYCLOAK_ADMIN_PASSWORD`
