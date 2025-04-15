import joblib
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional, Union
import os

class MLModel:
    """Machine Learning model for predictive maintenance"""
    
    def __init__(self, model_path: str):
        """Initialize the ML model
        
        Args:
            model_path: Path to the saved model file
        """
        self.model_path = model_path
        self.model = self._load_model()
        self.feature_names = ['temperature', 'vibration', 'pressure', 'rpm', 'voltage', 'current', 'noise_level']
    
    def _load_model(self):
        """Load the trained model from disk"""
        if os.path.exists(self.model_path):
            try:
                return joblib.load(self.model_path)
            except Exception as e:
                print(f"Error loading model: {e}")
                # Return dummy model in case loading fails
                return DummyModel()
        else:
            print(f"Model file not found at {self.model_path}, using dummy model")
            return DummyModel()
    
    def predict_failure(self, sensor_data: List[Dict]) -> Dict:
        """Predict likelihood of failure based on sensor readings
        
        Args:
            sensor_data: List of sensor reading dictionaries
        
        Returns:
            Dictionary containing prediction results
        """
        # Convert sensor data to DataFrame
        df = pd.DataFrame(sensor_data)
        
        # Ensure all required features are present
        for feature in self.feature_names:
            if feature not in df.columns:
                df[feature] = 0.0
        
        # Extract features for prediction
        X = df[self.feature_names].values
        
        # Make prediction
        failure_prob = self.model.predict_proba(X)[:, 1]
        failure_threshold = 0.5
        
        return {
            "failure_probability": float(failure_prob.mean()),
            "is_failure_predicted": bool(failure_prob.mean() > failure_threshold),
            "prediction_confidence": float(np.abs(0.5 - failure_prob.mean()) * 2),  # Confidence score
            "timeframe": "7 days",  # Prediction timeframe
        }
    
    def detect_anomalies(self, sensor_data: List[Dict]) -> Dict:
        """Detect anomalies in sensor data
        
        Args:
            sensor_data: List of sensor reading dictionaries
        
        Returns:
            Dictionary containing anomaly detection results
        """
        # Convert sensor data to DataFrame
        df = pd.DataFrame(sensor_data)
        
        # Simple anomaly detection based on thresholds
        anomalies = {}
        
        # Temperature anomalies
        if 'temperature' in df.columns:
            temp_mean = df['temperature'].mean()
            temp_std = df['temperature'].std()
            temp_anomaly = df['temperature'] > (temp_mean + 2 * temp_std)
            if temp_anomaly.any():
                anomalies['temperature'] = {
                    'detected': True,
                    'anomaly_score': float((temp_anomaly.sum() / len(df)) * 100),
                    'threshold': float(temp_mean + 2 * temp_std)
                }
        
        # Vibration anomalies
        if 'vibration' in df.columns:
            vib_mean = df['vibration'].mean()
            vib_std = df['vibration'].std()
            vib_anomaly = df['vibration'] > (vib_mean + 2 * vib_std)
            if vib_anomaly.any():
                anomalies['vibration'] = {
                    'detected': True,
                    'anomaly_score': float((vib_anomaly.sum() / len(df)) * 100),
                    'threshold': float(vib_mean + 2 * vib_std)
                }
        
        return {
            "anomalies_detected": len(anomalies) > 0,
            "anomaly_details": anomalies,
            "analysis_timestamp": pd.Timestamp.now().isoformat()
        }
    
    def get_health_score(self, sensor_data: List[Dict]) -> Dict:
        """Calculate machine health score based on sensor data
        
        Args:
            sensor_data: List of sensor reading dictionaries
        
        Returns:
            Dictionary containing health score and details
        """
        # Convert sensor data to DataFrame
        df = pd.DataFrame(sensor_data)
        
        # Simple health score calculation
        health_factors = {}
        health_scores = []
        
        # Temperature health factor
        if 'temperature' in df.columns:
            temp_mean = df['temperature'].mean()
            temp_health = max(0, min(100, 100 - (max(0, temp_mean - 50) * 2)))
            health_factors['temperature'] = float(temp_health)
            health_scores.append(temp_health)
        
        # Vibration health factor
        if 'vibration' in df.columns:
            vib_mean = df['vibration'].mean()
            vib_health = max(0, min(100, 100 - (vib_mean * 10)))
            health_factors['vibration'] = float(vib_health)
            health_scores.append(vib_health)
        
        # Overall health score
        overall_health = float(np.mean(health_scores)) if health_scores else 80.0
        
        return {
            "health_score": overall_health,
            "health_factors": health_factors,
            "assessment": self._get_health_assessment(overall_health),
            "last_updated": pd.Timestamp.now().isoformat()
        }
    
    def _get_health_assessment(self, health_score: float) -> str:
        """Get textual assessment based on health score"""
        if health_score >= 90:
            return "Excellent"
        elif health_score >= 70:
            return "Good"
        elif health_score >= 50:
            return "Fair"
        elif health_score >= 30:
            return "Poor"
        else:
            return "Critical"


class DummyModel:
    """Dummy model that returns random predictions when no real model is available"""
    
    def predict_proba(self, X):
        """Return random probabilities"""
        n_samples = X.shape[0]
        return np.random.random((n_samples, 2))