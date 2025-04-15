from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

class MaintenanceBase(BaseModel):
    """Base schema for maintenance records"""
    type: str = Field(..., description="Type of maintenance: preventive, corrective, predictive")
    description: str
    technician: Optional[str] = None
    parts_replaced: Optional[str] = None
    cost: Optional[float] = None
    duration_hours: Optional[float] = None

class MaintenanceCreate(MaintenanceBase):
    """Schema for maintenance record creation"""
    machine_id: int
    date: Optional[date] = None

class MaintenanceUpdate(BaseModel):
    """Schema for maintenance record updates"""
    type: Optional[str] = None
    description: Optional[str] = None
    technician: Optional[str] = None
    parts_replaced: Optional[str] = None
    cost: Optional[float] = None
    duration_hours: Optional[float] = None
    date: Optional[date] = None

class MaintenanceResponse(MaintenanceBase):
    """Schema for maintenance record responses"""
    id: int
    machine_id: int
    date: date
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True