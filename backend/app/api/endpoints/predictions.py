from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any
import pandas as pd

from app.db.database import get_db
from app.ml.model import MLModel
from app.main import get_ml_model
from app.db.crud import sensors as sensors_crud
from app.schemas.prediction import PredictionResponse, AnomalyResponse, HealthScoreResponse

router = APIRouter()

@router.get("/{machine_id}", response_model=PredictionResponse)
async def get_failure_prediction(
    machine_id: int,
    db: Session = Depends(get_db),
    ml_model: MLModel = Depends(get_ml_model)
):
    """Get failure prediction for a specific machine"""
    # Get recent sensor data for the machine
    sensor_data = sensors_crud.get_recent_sensor_data(db, machine_id, limit=100)
    
    if not sensor_data:
        raise HTTPException(status_code=404, detail="No sensor data found for this machine")
    
    # Convert to list of dictionaries for ML model
    sensor_data_dicts = [data.__dict__ for data in sensor_data]
    for data in sensor_data_dicts:
        # Remove SQLAlchemy state attributes
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
    
    # Get prediction
    prediction = ml_model.predict_failure(sensor_data_dicts)
    
    return {
        "machine_id": machine_id,
        "prediction_timestamp": pd.Timestamp.now().isoformat(),
        "failure_probability": prediction["failure_probability"],
        "is_failure_predicted": prediction["is_failure_predicted"],
        "prediction_confidence": prediction["prediction_confidence"],
        "timeframe": prediction["timeframe"]
    }

@router.get("/{machine_id}/anomalies", response_model=AnomalyResponse)
async def get_anomalies(
    machine_id: int,
    db: Session = Depends(get_db),
    ml_model: MLModel = Depends(get_ml_model)
):
    """Detect anomalies for a specific machine"""
    # Get recent sensor data for the machine
    sensor_data = sensors_crud.get_recent_sensor_data(db, machine_id, limit=100)
    
    if not sensor_data:
        raise HTTPException(status_code=404, detail="No sensor data found for this machine")
    
    # Convert to list of dictionaries for ML model
    sensor_data_dicts = [data.__dict__ for data in sensor_data]
    for data in sensor_data_dicts:
        # Remove SQLAlchemy state attributes
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
    
    # Detect anomalies
    anomalies = ml_model.detect_anomalies(sensor_data_dicts)
    
    return {
        "machine_id": machine_id,
        "analysis_timestamp": anomalies["analysis_timestamp"],
        "anomalies_detected": anomalies["anomalies_detected"],
        "anomaly_details": anomalies["anomaly_details"]
    }

@router.get("/{machine_id}/health", response_model=HealthScoreResponse)
async def get_health_score(
    machine_id: int,
    db: Session = Depends(get_db),
    ml_model: MLModel = Depends(get_ml_model)
):
    """Get health score for a specific machine"""
    # Get recent sensor data for the machine
    sensor_data = sensors_crud.get_recent_sensor_data(db, machine_id, limit=100)
    
    if not sensor_data:
        raise HTTPException(status_code=404, detail="No sensor data found for this machine")
    
    # Convert to list of dictionaries for ML model
    sensor_data_dicts = [data.__dict__ for data in sensor_data]
    for data in sensor_data_dicts:
        # Remove SQLAlchemy state attributes
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
    
    # Calculate health score
    health = ml_model.get_health_score(sensor_data_dicts)
    
    return {
        "machine_id": machine_id,
        "health_score": health["health_score"],
        "health_factors": health["health_factors"],
        "assessment": health["assessment"],
        "last_updated": health["last_updated"]
    }