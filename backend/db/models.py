import enum
from sqlalchemy import Column, Integer, String, Float, Boolean, JSON, DateTime, ForeignKey, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from geoalchemy2 import Geometry

Base = declarative_base()

class EngineEnum(str, enum.Enum):
    SPH = "SPH"
    DELFT3D = "DELFT3D"
    BOTH = "BOTH"

class StatusEnum(str, enum.Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class SatelliteEnum(str, enum.Enum):
    SENTINEL1 = "SENTINEL1"
    SENTINEL2 = "SENTINEL2"

class AOI(Base):
    __tablename__ = "aoi"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bbox = Column(Geometry('POLYGON', srid=4326))
    dem_path = Column(String)
    conditioned = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DamMetadata(Base):
    __tablename__ = "dam_metadata"
    id = Column(Integer, primary_key=True, index=True)
    aoi_id = Column(Integer, ForeignKey("aoi.id"))
    name = Column(String)
    location = Column(Geometry('POINT', srid=4326))
    height_m = Column(Float)
    reservoir_volume_mcm = Column(Float)
    dam_type = Column(String)
    spillway_capacity = Column(Float)
    year_built = Column(Integer)
    source = Column(String)

class Job(Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, index=True)
    aoi_id = Column(Integer, ForeignKey("aoi.id"))
    dam_id = Column(Integer, ForeignKey("dam_metadata.id"))
    engine = Column(Enum(EngineEnum))
    status = Column(Enum(StatusEnum), default=StatusEnum.PENDING)
    breach_params = Column(JSON)
    started_at = Column(DateTime(timezone=True))
    completed_at = Column(DateTime(timezone=True))
    result_path = Column(String)
    error_msg = Column(String)

class GEEReading(Base):
    __tablename__ = "gee_reading"
    id = Column(Integer, primary_key=True, index=True)
    aoi_id = Column(Integer, ForeignKey("aoi.id"))
    timestamp = Column(DateTime(timezone=True))
    satellite = Column(Enum(SatelliteEnum))
    water_extent_geojson = Column(JSON)
    ndwi_mean = Column(Float)
    baseline_ndwi_mean = Column(Float)
    anomaly_detected = Column(Boolean, default=False)
