from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class SensorDataCreateBase(BaseModel):
    """Base schema for sensor data creation"""
    timestamp: Optional[datetime] = None
    temperature: float = Field(..., description="Temperature in Celsius")
    vibration: float = Field(..., description="Vibration amplitude")
    pressure: float = Field(..., description="Pressure in Bar")
    rpm: float = Field(..., description="Rotations per minute")
    voltage: Optional[float] = None
    current: Optional[float] = None
    noise_level: Optional[float] = None

class SensorDataCreate(SensorDataCreateBase):
    """Schema for sensor data creation"""
    machine_id: int

class SensorDataBatch(BaseModel):
    """Schema for batch sensor data creation"""
    machine_id: int
    readings: List[SensorDataCreateBase]

class SensorDataResponse(SensorDataCreate):
    """Schema for sensor data responses"""
    id: int
    timestamp: datetime
    
    class Config:
        orm_mode = True