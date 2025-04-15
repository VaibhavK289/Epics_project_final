from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import date

class MachineBase(BaseModel):
    """Base machine schema with common attributes"""
    name: str
    type: str
    location: str
    
class MachineCreate(MachineBase):
    """Schema for creating a new machine"""
    install_date: str
    
class MachineUpdate(BaseModel):
    """Schema for updating an existing machine"""
    name: Optional[str] = None
    type: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    
class Machine(MachineBase):
    """Complete machine schema with all attributes"""
    id: str
    install_date: str
    status: str
    last_maintenance: Optional[str] = None
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "machine001",
                "name": "CNC Machine Alpha",
                "type": "CNC",
                "location": "Factory Floor A",
                "install_date": "2023-01-15",
                "status": "operational",
                "last_maintenance": "2025-03-01"
            }
        }

class MachineStatus(BaseModel):
    """Schema for machine status updates"""
    status: str = Field(..., description="Current operational status of the machine")
    updated_at: str
    notes: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "status": "maintenance",
                "updated_at": "2025-04-14T10:30:00",
                "notes": "Scheduled maintenance due to vibration warning"
            }
        }

class MachineSummary(BaseModel):
    """Schema for machine summary statistics"""
    id: str
    name: str
    status: str
    health_score: float
    anomaly_count_7d: int
    last_maintenance_date: Optional[str] = None
    next_maintenance_date: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "id": "machine001",
                "name": "CNC Machine Alpha",
                "status": "operational",
                "health_score": 92.5,
                "anomaly_count_7d": 1,
                "last_maintenance_date": "2025-03-01",
                "next_maintenance_date": "2025-06-01"
            }
        }