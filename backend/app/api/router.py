from fastapi import APIRouter
from app.api.endpoints import machines, sensors, predictions, dashboard, maintenance

# Create main API router
api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(machines.router, prefix="/machines", tags=["machines"])
api_router.include_router(sensors.router, prefix="/sensor-data", tags=["sensor-data"])
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(maintenance.router, prefix="/maintenance", tags=["maintenance"])