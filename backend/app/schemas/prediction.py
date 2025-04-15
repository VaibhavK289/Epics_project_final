from pydantic import BaseModel
from typing import Dict, List, Optional, Any
from datetime import datetime

class PredictionResponse(BaseModel):
    """Schema for failure prediction response"""
    machine_id: int
    prediction_timestamp: str
    failure_probability: float
    is_failure_predicted: bool
    prediction_confidence: float
    timeframe: str
    
    class Config:
        orm_mode = True

class AnomalyResponse(BaseModel):
    """Schema for anomaly detection response"""
    machine_id: int
    analysis_timestamp: str
    anomalies_detected: bool
    anomaly_details: Dict[str, Any]
    
    class Config:
        orm_mode = True

class HealthScoreResponse(BaseModel):
    """Schema for health score response"""
    machine_id: int
    health_score: float
    health_factors: Dict[str, float]
    assessment: str
    last_updated: str
    
    class Config:
        orm_mode = True