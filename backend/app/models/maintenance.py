from sqlalchemy import Column, Integer, String, DateTime, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, date
from app.db.database import Base

class Maintenance(Base):
    """Database model for maintenance records"""
    __tablename__ = "maintenance"
    
    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, ForeignKey("machines.id"))
    
    # Record details
    date = Column(Date, default=date.today)
    type = Column(String)  # preventive, corrective, predictive
    description = Column(Text)
    technician = Column(String, nullable=True)
    parts_replaced = Column(Text, nullable=True)
    cost = Column(Float, nullable=True)
    duration_hours = Column(Float, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    machine = relationship("Machine", back_populates="maintenance_records")