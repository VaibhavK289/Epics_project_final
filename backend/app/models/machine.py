from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Machine(Base):
    """Database model for machines"""
    __tablename__ = "machines"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    location = Column(String)
    installation_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="operational")  # operational, maintenance, warning, critical
    last_maintenance = Column(DateTime, nullable=True)
    
    # Relationships
    sensor_data = relationship("SensorData", back_populates="machine", cascade="all, delete-orphan")
    maintenance_records = relationship("Maintenance", back_populates="machine", cascade="all, delete-orphan")