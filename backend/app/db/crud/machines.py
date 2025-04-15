from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.models.machine import Machine
from app.schemas.machine import MachineCreate, MachineUpdate

def get_machine(db: Session, machine_id: int) -> Optional[Machine]:
    """Get a machine by ID"""
    return db.query(Machine).filter(Machine.id == machine_id).first()

def get_machines(db: Session, skip: int = 0, limit: int = 100) -> List[Machine]:
    """Get all machines with pagination"""
    return db.query(Machine).offset(skip).limit(limit).all()

def create_machine(db: Session, machine: MachineCreate) -> Machine:
    """Create a new machine"""
    db_machine = Machine(
        name=machine.name,
        type=machine.type,
        location=machine.location,
        installation_date=machine.installation_date or datetime.utcnow(),
        status=machine.status or "operational"
    )
    db.add(db_machine)
    db.commit()
    db.refresh(db_machine)
    return db_machine

def update_machine(db: Session, machine_id: int, machine: MachineUpdate) -> Machine:
    """Update a machine's details"""
    db_machine = get_machine(db, machine_id)
    
    # Update attributes
    update_data = machine.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_machine, key, value)
    
    db.commit()
    db.refresh(db_machine)
    return db_machine

def delete_machine(db: Session, machine_id: int) -> None:
    """Delete a machine"""
    db_machine = get_machine(db, machine_id)
    db.delete(db_machine)
    db.commit()

def update_machine_status(db: Session, machine_id: int, status: str) -> Machine:
    """Update a machine's status"""
    db_machine = get_machine(db, machine_id)
    db_machine.status = status
    db.commit()
    db.refresh(db_machine)
    return db_machine

def update_machine_maintenance(db: Session, machine_id: int) -> Machine:
    """Update a machine's last maintenance date"""
    db_machine = get_machine(db, machine_id)
    db_machine.last_maintenance = datetime.utcnow()
    # If machine was in maintenance status, set it back to operational
    if db_machine.status == "maintenance":
        db_machine.status = "operational"
    db.commit()
    db.refresh(db_machine)
    return db_machine