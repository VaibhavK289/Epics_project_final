from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime

class SensorData(BaseModel):
    """
    Schema for raw sensor data submission
    """
    machine_id: str
    timestamp: Optional[str] = None
    temperature: float = Field(..., description="Temperature in Celsius")
    vibration: float = Field(..., description="Vibration amplitude")
    pressure: float = Field(..., description="Pressure in bar")
    rpm: float = Field(..., description="Rotations per minute")
    
    class Config:
        schema_extra = {
            "example": {
                "machine_id": "machine001",
                "timestamp": "2025-04-14T12:30:45",
                "temperature": 75.4,
                "vibration": 2.1,
                "pressure": 1.05,
                "rpm": 2500
            }
        }

class ProcessedSensorData(SensorData):
    """
    Schema for processed sensor data with anomaly detection
    """
    vibration_to_rpm_ratio: Optional[float] = None
    temperature_pressure_ratio: Optional[float] = None
    anomaly_detected: bool = False
    anomaly_probability: Optional[float] = None
    temperature_anomaly: Optional[bool] = False
    vibration_anomaly: Optional[bool] = False
    pressure_anomaly: Optional[bool] = False
    rpm_anomaly: Optional[bool] = False
    
    class Config:
        schema_extra = {
            "example": {
                "machine_id": "machine001",
                "timestamp": "2025-04-14T12:30:45",
                "temperature": 75.4,
                "vibration": 2.1,
                "pressure": 1.05,
                "rpm": 2500,
                "vibration_to_rpm_ratio": 0.00084,
                "temperature_pressure_ratio": 71.81,
                "anomaly_detected": False,
                "anomaly_probability": 0.15,
                "temperature_anomaly": False,
                "vibration_anomaly": False,
                "pressure_anomaly": False,
                "rpm_anomaly": False
            }
        }

class SensorDataBatch(BaseModel):
    """
    Schema for batch sensor data submission
    """
    data: List[SensorData]
    
class SensorDataSummary(BaseModel):
    """
    Schema for summarized sensor data statistics
    """
    machine_id: str
    start_date: datetime
    end_date: datetime
    data_points: int
    average_temperature: float
    average_vibration: float
    average_pressure: float
    average_rpm: float
    anomaly_count: int
    
    class Config:
        schema_extra = {
            "example": {
                "machine_id": "machine001",
                "start_date": "2025-04-07T00:00:00",
                "end_date": "2025-04-14T23:59:59",
                "data_points": 168,
                "average_temperature": 72.5,
                "average_vibration": 1.8,
                "average_pressure": 1.02,
                "average_rpm": 2450,
                "anomaly_count": 3
            }
        }