import asyncio
from geoalchemy2.elements import WKTElement
from .session import engine, async_session
from .models import Base, AOI, DamMetadata

async def init_db():
    async with engine.begin() as conn:
        # Create all tables (ensure PostGIS is enabled in your database beforehand)
        await conn.run_sync(Base.metadata.create_all)
        
    async with async_session() as session:
        # Seed Kosi Barrage Data if empty
        # Kosi Barrage approx: 26.525N, 86.93E
        bbox_wkt = "POLYGON((86.7 26.4, 87.1 26.4, 87.1 26.7, 86.7 26.7, 86.7 26.4))"
        point_wkt = "POINT(86.93 26.525)"
        
        # Check if exists
        result = await session.execute(Base.metadata.tables['aoi'].select())
        if not result.first():
            aoi = AOI(
                name="Kosi Barrage Area",
                bbox=WKTElement(bbox_wkt, srid=4326)
            )
            session.add(aoi)
            await session.commit()
            await session.refresh(aoi)
            
            dam = DamMetadata(
                aoi_id=aoi.id,
                name="Kosi Barrage",
                location=WKTElement(point_wkt, srid=4326),
                height_m=12.0,
                reservoir_volume_mcm=150.0, # Approximate
                dam_type="Barrage",
                source="Seed Data"
            )
            session.add(dam)
            await session.commit()
