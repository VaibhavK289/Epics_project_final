import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
import logging
from typing import Dict, Any

# Import ML model for anomaly detection
from app.ml.model import detect_anomalies

# Setup logging
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Data storage directory
DATA_DIR = Path("./data/sensor_data")
DATA_DIR.mkdir(exist_ok=True, parents=True)

def process_sensor_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process incoming sensor data and detect anomalies
    
    Args:
        data: Dictionary with raw sensor data
        
    Returns:
        Dictionary with processed data including anomaly flags
    """
    # Add timestamp if not present
    if 'timestamp' not in data:
        data['timestamp'] = datetime.now().isoformat()
        
    # Calculate derived features
    if 'vibration' in data and 'rpm' in data and data['rpm'] > 0:
        data['vibration_to_rpm_ratio'] = data['vibration'] / data['rpm']
    else:
        data['vibration_to_rpm_ratio'] = 0
        
    if 'temperature' in data and 'pressure' in data and data['pressure'] > 0:
        data['temperature_pressure_ratio'] = data['temperature'] / data['pressure']
    else:
        data['temperature_pressure_ratio'] = 0
    
    # Detect anomalies
    anomalies = detect_anomalies(data)
    
    # Merge anomaly results with data
    processed_data = {**data, **anomalies}
    
    return processed_data

def store_data(data: Dict[str, Any]):
    """
    Store processed sensor data to CSV file
    
    Args:
        data: Dictionary with processed sensor data
    """
    try:
        # Ensure machine_id exists
        if 'machine_id' not in data:
            logger.error("Cannot store data: machine_id is missing")
            return
            
        machine_id = data['machine_id']
        file_path = DATA_DIR / f"{machine_id}_sensor_data.csv"
        
        # Convert to DataFrame for easier CSV handling
        df = pd.DataFrame([data])
        
        # If file exists, append to it, otherwise create new file
        if file_path.exists():
            df.to_csv(file_path, mode='a', header=False, index=False)
        else:
            df.to_csv(file_path, index=False)
            
        logger.info(f"Stored sensor data for machine {machine_id}")
        
    except Exception as e:
        logger.error(f"Error storing sensor data: {e}")

def get_historical_data(machine_id: str, days: int = 30):
    """
    Retrieve historical sensor data for a machine
    
    Args:
        machine_id: ID of the machine
        days: Number of days of history to retrieve
        
    Returns:
        DataFrame with historical data
    """
    file_path = DATA_DIR / f"{machine_id}_sensor_data.csv"
    
    if not file_path.exists():
        return pd.DataFrame()
        
    try:
        # Read CSV
        df = pd.read_csv(file_path)
        
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Filter by date range if specified
        if days > 0:
            cutoff_date = pd.Timestamp.now() - pd.Timedelta(days=days)
            df = df[df['timestamp'] >= cutoff_date]
            
        return df
        
    except Exception as e:
        logger.error(f"Error retrieving historical data: {e}")
        return pd.DataFrame()

def aggregate_sensor_data(machine_id: str, interval: str = 'D'):
    """
    Aggregate sensor data by time interval
    
    Args:
        machine_id: ID of the machine
        interval: Time interval for aggregation ('D' for daily, 'H' for hourly, etc.)
        
    Returns:
        DataFrame with aggregated data
    """
    df = get_historical_data(machine_id)
    
    if df.empty:
        return df
        
    try:
        # Convert timestamp to datetime if not already
        if not pd.api.types.is_datetime64_any_dtype(df['timestamp']):
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
        # Set timestamp as index for resampling
        df = df.set_index('timestamp')
        
        # Resample and aggregate
        aggregated = df.resample(interval).agg({
            'temperature': 'mean',
            'vibration': 'mean',
            'pressure': 'mean',
            'rpm': 'mean',
            'anomaly_detected': 'sum',
            'machine_id': 'first'  # Keep machine_id
        }).reset_index()
        
        return aggregated
        
    except Exception as e:
        logger.error(f"Error aggregating sensor data: {e}")
        return pd.DataFrame()