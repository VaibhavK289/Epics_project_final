from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.models.maintenance import Maintenance
from app.schemas.maintenance import MaintenanceCreate, MaintenanceUpdate

def get_maintenance_record(db: Session, record_id: int) -> Optional[Maintenance]:
    """Get a maintenance record by ID"""
    return db.query(Maintenance).filter(Maintenance.id == record_id).first()

def get_maintenance_records(db: Session, skip: int = 0, limit: int = 100) -> List[Maintenance]:
    """Get all maintenance records with pagination"""
    return db.query(Maintenance).order_by(Maintenance.date.desc()).offset(skip).limit(limit).all()

def get_machine_maintenance_records(
    db: Session, 
    machine_id: int, 
    limit: int = 100
) -> List[Maintenance]:
    """Get maintenance records for a specific machine"""
    return db.query(Maintenance).filter(
        Maintenance.machine_id == machine_id
    ).order_by(Maintenance.date.desc()).limit(limit).all()

def get_latest_maintenance(db: Session, machine_id: int) -> Optional[Maintenance]:
    """Get the most recent maintenance record for a machine"""
    return db.query(Maintenance).filter(
        Maintenance.machine_id == machine_id
    ).order_by(Maintenance.date.desc()).first()

def create_maintenance_record(db: Session, maintenance: MaintenanceCreate) -> Maintenance:
    """Create a new maintenance record"""
    db_maintenance = Maintenance(
        machine_id=maintenance.machine_id,
        date=maintenance.date or datetime.utcnow().date(),
        type=maintenance.type,
        description=maintenance.description,
        technician=maintenance.technician,
        parts_replaced=maintenance.parts_replaced,
        cost=maintenance.cost,
        duration_hours=maintenance.duration_hours
    )
    db.add(db_maintenance)
    db.commit()
    db.refresh(db_maintenance)
    return db_maintenance

def update_maintenance_record(
    db: Session, 
    record_id: int, 
    maintenance: MaintenanceUpdate
) -> Maintenance:
    """Update a maintenance record"""
    db_maintenance = get_maintenance_record(db, record_id)
    
    # Update attributes
    update_data = maintenance.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_maintenance, key, value)
    
    db_maintenance.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_maintenance)
    return db_maintenance

def delete_maintenance_record(db: Session, record_id: int) -> None:
    """Delete a maintenance record"""
    db_maintenance = get_maintenance_record(db, record_id)
    db.delete(db_maintenance)
    db.commit()