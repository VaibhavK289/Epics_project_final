from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime

class PredictionResult(BaseModel):
    """
    Schema for failure prediction results
    """
    failure_probability: float = Field(..., ge=0.0, le=1.0, description="Probability of failure")
    estimated_time_to_failure: Optional[str] = None
    estimated_failure_date: Optional[str] = None
    failure_type: Optional[str] = None
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence in prediction")
    
    class Config:
        schema_extra = {
            "example": {
                "failure_probability": 0.35,
                "estimated_time_to_failure": "4-7 days",
                "estimated_failure_date": "2025-04-21",
                "failure_type": "Bearing Failure",
                "confidence": 0.85
            }
        }

class AnomalyResult(BaseModel):
    """
    Schema for anomaly detection results
    """
    timestamp: str
    machine_id: str
    anomaly_type: str
    severity: str
    parameters: Dict[str, Any]
    
    class Config:
        schema_extra = {
            "example": {
                "timestamp": "2025-04-14T08:15:30",
                "machine_id": "machine001",
                "anomaly_type": "Vibration",
                "severity": "Medium",
                "parameters": {
                    "temperature": 78.2,
                    "vibration": 5.7,
                    "pressure": 1.03,
                    "rpm": 2480
                }
            }
        }

class HealthScoreResult(BaseModel):
    """
    Schema for machine health score
    """
    machine_id: str
    health_score: float = Field(..., ge=0.0, le=100.0)
    last_updated: datetime
    trend: str  # "improving", "stable", "degrading"
    contributing_factors: List[Dict[str, Any]]
    
    class Config:
        schema_extra = {
            "example": {
                "machine_id": "machine001",
                "health_score": 87.5,
                "last_updated": "2025-04-14T14:30:00",
                "trend": "stable",
                "contributing_factors": [
                    {"factor": "vibration", "impact": "low"},
                    {"factor": "temperature", "impact": "medium"}
                ]
            }
        }

class MaintenanceRecommendation(BaseModel):
    """
    Schema for maintenance recommendations
    """
    machine_id: str
    recommendation_type: str  # "preventive", "corrective", "condition-based"
    priority: str  # "low", "medium", "high", "critical"
    description: str
    estimated_time: Optional[str] = None
    parts_needed: Optional[List[str]] = None
    recommended_date: Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "machine_id": "machine001",
                "recommendation_type": "preventive",
                "priority": "medium",
                "description": "Replace bearing assembly due to increasing vibration patterns",
                "estimated_time": "2 hours",
                "parts_needed": ["Bearing assembly", "Lubricant"],
                "recommended_date": "2025-04-20"
            }
        }