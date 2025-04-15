from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional, Dict, Any
from datetime import datetime
import pandas as pd

from app.models.sensor import SensorData
from app.schemas.sensor import SensorDataCreate, SensorDataCreateBase

def get_sensor_data(
    db: Session, 
    machine_id: int, 
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    limit: int = 100
) -> List[SensorData]:
    """Get sensor data for a machine with optional date filtering"""
    query = db.query(SensorData).filter(SensorData.machine_id == machine_id)
    
    if start_date:
        query = query.filter(SensorData.timestamp >= start_date)
    if end_date:
        query = query.filter(SensorData.timestamp <= end_date)
    
    return query.order_by(SensorData.timestamp.desc()).limit(limit).all()

def get_recent_sensor_data(db: Session, machine_id: int, limit: int = 100) -> List[SensorData]:
    """Get the most recent sensor data for a machine"""
    return db.query(SensorData).filter(
        SensorData.machine_id == machine_id
    ).order_by(SensorData.timestamp.desc()).limit(limit).all()

def get_latest_sensor_data(db: Session, machine_id: int) -> Optional[SensorData]:
    """Get the most recent sensor reading for a machine"""
    return db.query(SensorData).filter(
        SensorData.machine_id == machine_id
    ).order_by(SensorData.timestamp.desc()).first()

def create_sensor_data(db: Session, sensor_data: SensorDataCreate) -> SensorData:
    """Record a new sensor reading"""
    db_sensor_data = SensorData(
        machine_id=sensor_data.machine_id,
        timestamp=sensor_data.timestamp or datetime.utcnow(),
        temperature=sensor_data.temperature,
        vibration=sensor_data.vibration,
        pressure=sensor_data.pressure,
        rpm=sensor_data.rpm,
        voltage=sensor_data.voltage,
        current=sensor_data.current,
        noise_level=sensor_data.noise_level
    )
    db.add(db_sensor_data)
    db.commit()
    db.refresh(db_sensor_data)
    return db_sensor_data

def create_sensor_data_batch(
    db: Session, 
    machine_id: int, 
    readings: List[SensorDataCreateBase]
) -> List[SensorData]:
    """Record multiple sensor readings at once"""
    db_readings = []
    
    for reading in readings:
        db_reading = SensorData(
            machine_id=machine_id,
            timestamp=reading.timestamp or datetime.utcnow(),
            temperature=reading.temperature,
            vibration=reading.vibration,
            pressure=reading.pressure,
            rpm=reading.rpm,
            voltage=reading.voltage,
            current=reading.current,
            noise_level=reading.noise_level
        )
        db.add(db_reading)
        db_readings.append(db_reading)
    
    db.commit()
    
    # Refresh all objects
    for reading in db_readings:
        db.refresh(reading)
    
    return db_readings

def get_sensor_stats(
    db: Session, 
    machine_id: int, 
    start_date: datetime, 
    end_date: datetime
) -> Dict[str, Any]:
    """Calculate statistical metrics for sensor data"""
    # Get data for the period
    data = get_sensor_data(db, machine_id, start_date, end_date, limit=10000)
    
    if not data:
        return None
    
    # Convert to DataFrame for easier statistical analysis
    df = pd.DataFrame([{
        'timestamp': item.timestamp,
        'temperature': item.temperature,
        'vibration': item.vibration,
        'pressure': item.pressure,
        'rpm': item.rpm,
        'voltage': item.voltage if item.voltage else 0,
        'current': item.current if item.current else 0,
        'noise_level': item.noise_level if item.noise_level else 0
    } for item in data])
    
    # Calculate statistics for each sensor type
    stats = {}
    for column in ['temperature', 'vibration', 'pressure', 'rpm', 'voltage', 'current', 'noise_level']:
        if column in df.columns:
            stats[column] = {
                'mean': float(df[column].mean()),
                'min': float(df[column].min()),
                'max': float(df[column].max()),
                'std': float(df[column].std()),
                'median': float(df[column].median()),
                'count': int(df[column].count())
            }
    
    return {
        'machine_id': machine_id,
        'start_date': start_date.isoformat(),
        'end_date': end_date.isoformat(),
        'data_points': len(df),
        'statistics': stats
    }