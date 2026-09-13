from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .api import aoi, dam, breach, simulation, impact, export, monitoring, health
from .config import settings
from .db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Run db init scripts
    await init_db()
    yield
    # Shutdown logic

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(health.router, prefix="/api/health", tags=["Health"])
app.include_router(aoi.router, prefix="/api/aoi", tags=["AOI"])
app.include_router(dam.router, prefix="/api/dam", tags=["Dam"])
app.include_router(breach.router, prefix="/api/breach", tags=["Breach"])
app.include_router(simulation.router, prefix="/api/simulation", tags=["Simulation"])
app.include_router(impact.router, prefix="/api/impact", tags=["Impact"])
app.include_router(export.router, prefix="/api/export", tags=["Export"])
app.include_router(monitoring.router, prefix="/api/monitoring", tags=["Monitoring"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
