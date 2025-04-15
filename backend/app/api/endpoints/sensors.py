from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta

from app.db.database import get_db
from app.schemas.sensor import SensorDataCreate, SensorDataResponse, SensorDataBatch
from app.db.crud import sensors as sensors_crud
from app.db.crud import machines as machines_crud

router = APIRouter()

@router.get("/{machine_id}", response_model=List[SensorDataResponse])
async def get_sensor_data(
    machine_id: int,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """Get sensor data for a specific machine with optional date filtering"""
    # Verify machine exists
    machine = machines_crud.get_machine(db, machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    # Set default dates if not provided
    if not end_date:
        end_date = datetime.utcnow()
    if not start_date:
        start_date = end_date - timedelta(days=7)
    
    sensor_data = sensors_crud.get_sensor_data(
        db, 
        machine_id=machine_id, 
        start_date=start_date,
        end_date=end_date,
        limit=limit
    )
    
    return sensor_data

@router.get("/{machine_id}/latest", response_model=SensorDataResponse)
async def get_latest_sensor_data(
    machine_id: int,
    db: Session = Depends(get_db)
):
    """Get the most recent sensor reading for a machine"""
    # Verify machine exists
    machine = machines_crud.get_machine(db, machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    sensor_data = sensors_crud.get_latest_sensor_data(db, machine_id)
    if not sensor_data:
        raise HTTPException(status_code=404, detail="No sensor data found for this machine")
    
    return sensor_data

@router.post("/", response_model=SensorDataResponse, status_code=status.HTTP_201_CREATED)
async def create_sensor_data(
    sensor_data: SensorDataCreate,
    db: Session = Depends(get_db)
):
    """Record a new sensor reading"""
    # Verify machine exists
    machine = machines_crud.get_machine(db, sensor_data.machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    return sensors_crud.create_sensor_data(db=db, sensor_data=sensor_data)

@router.post("/batch", response_model=List[SensorDataResponse], status_code=status.HTTP_201_CREATED)
async def create_sensor_data_batch(
    sensor_data_batch: SensorDataBatch,
    db: Session = Depends(get_db)
):
    """Record multiple sensor readings at once"""
    # Verify machine exists
    machine = machines_crud.get_machine(db, sensor_data_batch.machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    return sensors_crud.create_sensor_data_batch(
        db=db, 
        machine_id=sensor_data_batch.machine_id, 
        readings=sensor_data_batch.readings
    )

@router.get("/{machine_id}/stats", response_model=dict)
async def get_sensor_stats(
    machine_id: int,
    days: Optional[int] = Query(7, ge=1, le=365),
    db: Session = Depends(get_db)
):
    """Get statistical summary of sensor data for a machine"""
    # Verify machine exists
    machine = machines_crud.get_machine(db, machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    
    stats = sensors_crud.get_sensor_stats(
        db,
        machine_id=machine_id,
        start_date=start_date,
        end_date=end_date
    )
    
    if not stats:
        raise HTTPException(status_code=404, detail="No sensor data found for this machine in the specified period")
    
    return stats