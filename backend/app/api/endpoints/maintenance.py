from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta

from app.db.database import get_db
from app.schemas.maintenance import MaintenanceCreate, MaintenanceUpdate, MaintenanceResponse
from app.db.crud import maintenance as maintenance_crud
from app.db.crud import machines as machines_crud

router = APIRouter()

@router.get("/", response_model=List[MaintenanceResponse])
async def get_all_maintenance_records(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all maintenance records with pagination"""
    records = maintenance_crud.get_maintenance_records(db, skip=skip, limit=limit)
    return records

@router.get("/{machine_id}", response_model=List[MaintenanceResponse])
async def get_machine_maintenance_records(
    machine_id: int,
    db: Session = Depends(get_db)
):
    """Get maintenance records for a specific machine"""
    # Verify machine exists
    machine = machines_crud.get_machine(db, machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    records = maintenance_crud.get_machine_maintenance_records(db, machine_id=machine_id)
    return records

@router.post("/", response_model=MaintenanceResponse, status_code=status.HTTP_201_CREATED)
async def create_maintenance_record(
    maintenance: MaintenanceCreate,
    db: Session = Depends(get_db)
):
    """Create a new maintenance record"""
    # Verify machine exists
    machine = machines_crud.get_machine(db, maintenance.machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    # Create maintenance record
    record = maintenance_crud.create_maintenance_record(db=db, maintenance=maintenance)
    
    # Update machine's last maintenance date
    machines_crud.update_machine_maintenance(db=db, machine_id=maintenance.machine_id)
    
    return record

@router.get("/{machine_id}/latest", response_model=MaintenanceResponse)
async def get_latest_maintenance(
    machine_id: int,
    db: Session = Depends(get_db)
):
    """Get the most recent maintenance record for a machine"""
    # Verify machine exists
    machine = machines_crud.get_machine(db, machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    record = maintenance_crud.get_latest_maintenance(db, machine_id=machine_id)
    if not record:
        raise HTTPException(status_code=404, detail="No maintenance records found for this machine")
    
    return record

@router.put("/{record_id}", response_model=MaintenanceResponse)
async def update_maintenance_record(
    record_id: int,
    maintenance: MaintenanceUpdate,
    db: Session = Depends(get_db)
):
    """Update a maintenance record"""
    # Check if record exists
    record = maintenance_crud.get_maintenance_record(db, record_id=record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Maintenance record not found")
    
    return maintenance_crud.update_maintenance_record(
        db=db, 
        record_id=record_id, 
        maintenance=maintenance
    )

@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_maintenance_record(
    record_id: int,
    db: Session = Depends(get_db)
):
    """Delete a maintenance record"""
    # Check if record exists
    record = maintenance_crud.get_maintenance_record(db, record_id=record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Maintenance record not found")
    
    maintenance_crud.delete_maintenance_record(db=db, record_id=record_id)
    return None

@router.get("/{machine_id}/schedule", response_model=dict)
async def get_maintenance_schedule(
    machine_id: int,
    db: Session = Depends(get_db)
):
    """Get maintenance schedule and recommendations for a machine"""
    # Verify machine exists
    machine = machines_crud.get_machine(db, machine_id)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    # Get latest maintenance date
    latest = maintenance_crud.get_latest_maintenance(db, machine_id=machine_id)
    latest_date = latest.date if latest else None
    
    # Calculate next scheduled maintenance
    next_date = None
    if latest_date:
        next_date = latest_date + timedelta(days=90)  # Default 90 days maintenance interval
    
    # Get maintenance history
    history = maintenance_crud.get_machine_maintenance_records(db, machine_id=machine_id, limit=5)
    history_summary = [
        {"date": record.date.isoformat(), "type": record.type, "description": record.description}
        for record in history
    ]
    
    return {
        "machine_id": machine_id,
        "last_maintenance": latest_date.isoformat() if latest_date else None,
        "next_scheduled": next_date.isoformat() if next_date else None,
        "days_until_next": (next_date - datetime.utcnow().date()).days if next_date else None,
        "maintenance_history": history_summary,
        "maintenance_interval": 90,  # Days
        "recommendation": "Regular maintenance recommended" if next_date else "Initial maintenance recommended"
    }