from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MachineBase(BaseModel):
    """Base schema for machine data"""
    name: str
    type: str
    location: str

class MachineCreate(MachineBase):
    """Schema for machine creation"""
    installation_date: Optional[datetime] = None
    status: Optional[str] = "operational"

class MachineUpdate(BaseModel):
    """Schema for machine updates"""
    name: Optional[str] = None
    type: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    last_maintenance: Optional[datetime] = None

class MachineResponse(MachineBase):
    """Schema for machine responses"""
    id: int
    installation_date: datetime
    status: str
    last_maintenance: Optional[datetime] = None
    
    class Config:
        orm_mode = True