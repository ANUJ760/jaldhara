# Contributing to Jaldhara

Thank you for your interest in contributing to **Jaldhara** — the Dam Break Inundation Modelling System for SIH26161.

## Getting Started

1. **Fork** the repository and clone your fork
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Set up your development environment (see [DEPLOYMENT.md](docs/DEPLOYMENT.md))

## Development Setup

### Prerequisites
- Docker & Docker Compose
- Node.js 20+ (for frontend development)
- Python 3.12+ (for backend development)
- GDAL system libraries

### Quick Start
```bash
# Clone and start all services
git clone https://github.com/ANUJ760/jaldhara.git
cd jaldhara
cp .env.example .env
docker-compose up -d

# Frontend development
cd frontend && npm install && npm run dev

# Backend development
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Code Standards

### Python (Backend)
- Follow PEP 8 style guidelines
- Use type hints for all function signatures
- Write docstrings for all public functions and classes
- Run `ruff check .` before committing
- Run `mypy .` for type checking

### TypeScript (Frontend)
- Use strict TypeScript — no `any` types
- Follow React best practices (hooks, functional components)
- Use Tailwind CSS for styling (no inline styles or CSS modules)
- Run `npm run lint` before committing

## Pull Request Process

1. Ensure your code passes all linting and type checks
2. Update documentation if you've changed APIs or configuration
3. Add tests for new functionality
4. Write a clear PR description explaining *why* the change is needed
5. Request review from at least one maintainer

## Architecture Overview

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the full system architecture.

| Component | Tech | Directory |
|---|---|---|
| Frontend | Next.js 14 + TypeScript | `frontend/` |
| Backend | FastAPI + Python 3.12 | `backend/` |
| Database | PostgreSQL + PostGIS | `db/` |
| Auth | Keycloak | `keycloak/` |
| Storage | MinIO | `minio/` |
| SPH Engine | DualSPHysics | `engines/sph/` |
| Mesh Engine | Delft3D D-Flow FM | `engines/delft3d/` |

## Reporting Issues

- Use GitHub Issues for bug reports and feature requests
- Include steps to reproduce for bugs
- Tag issues appropriately (`bug`, `enhancement`, `documentation`)

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
