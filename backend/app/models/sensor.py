
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class SensorData(Base):
    """Database model for sensor readings"""
    __tablename__ = "sensor_data"
    
    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("machines.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    # Sensor readings
    temperature = Column(Float)
    vibration = Column(Float)
    pressure = Column(Float)
    rpm = Column(Float)
    voltage = Column(Float, nullable=True)
    current = Column(Float, nullable=True)
    noise_level = Column(Float, nullable=True)
    
    # Relationship
    machine = relationship("Machine", back_populates="sensor_data")