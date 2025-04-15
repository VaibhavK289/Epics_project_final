from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.machine import MachineCreate, MachineUpdate, MachineResponse
from app.db.crud import machines as machines_crud

router = APIRouter()

@router.get("/", response_model=List[MachineResponse])
async def get_machines(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """Get all machines with pagination"""
    machines = machines_crud.get_machines(db, skip=skip, limit=limit)
    return machines

@router.post("/", response_model=MachineResponse, status_code=status.HTTP_201_CREATED)
async def create_machine(
    machine: MachineCreate, 
    db: Session = Depends(get_db)
):
    """Create a new machine"""
    return machines_crud.create_machine(db=db, machine=machine)

@router.get("/{machine_id}", response_model=MachineResponse)
async def get_machine(
    machine_id: int, 
    db: Session = Depends(get_db)
):
    """Get a specific machine by ID"""
    db_machine = machines_crud.get_machine(db, machine_id=machine_id)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    return db_machine

@router.put("/{machine_id}", response_model=MachineResponse)
async def update_machine(
    machine_id: int, 
    machine: MachineUpdate, 
    db: Session = Depends(get_db)
):
    """Update a machine's details"""
    db_machine = machines_crud.get_machine(db, machine_id=machine_id)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machines_crud.update_machine(db=db, machine_id=machine_id, machine=machine)

@router.delete("/{machine_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_machine(
    machine_id: int, 
    db: Session = Depends(get_db)
):
    """Delete a machine"""
    db_machine = machines_crud.get_machine(db, machine_id=machine_id)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    machines_crud.delete_machine(db=db, machine_id=machine_id)
    return None

@router.get("/{machine_id}/status", response_model=dict)
async def get_machine_status(
    machine_id: int, 
    db: Session = Depends(get_db)
):
    """Get the current status of a machine"""
    db_machine = machines_crud.get_machine(db, machine_id=machine_id)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    return {
        "machine_id": db_machine.id,
        "status": db_machine.status,
        "last_updated": db_machine.last_maintenance.isoformat() if db_machine.last_maintenance else None
    }

@router.put("/{machine_id}/status", response_model=dict)
async def update_machine_status(
    machine_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    """Update the status of a machine"""
    valid_statuses = ["operational", "maintenance", "warning", "critical"]
    if status not in valid_statuses:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
        )
    
    db_machine = machines_crud.get_machine(db, machine_id=machine_id)
    if db_machine is None:
        raise HTTPException(status_code=404, detail="Machine not found")
    
    updated_machine = machines_crud.update_machine_status(db=db, machine_id=machine_id, status=status)
    
    return {
        "machine_id": updated_machine.id,
        "status": updated_machine.status,
        "last_updated": updated_machine.last_maintenance.isoformat() if updated_machine.last_maintenance else None
    }