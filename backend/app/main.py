from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import os

from app.api.router import api_router
from app.core.config import settings
from app.db.database import engine, Base, get_db
from app.ml.model import MLModel

app = FastAPI(
    title=settings.APP_NAME,
    description="Predictive Maintenance API for Machine Health Monitoring",
    version="1.0.0",
)

# Configure CORS to allow requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api")

# Initialize ML model at startup
ml_model = None

@app.on_event("startup")
async def startup_event():
    """Initialize components on application startup"""
    global ml_model
    # Create DB tables if they don't exist
    Base.metadata.create_all(bind=engine)
    
    # Initialize ML model
    model_path = os.path.join("data", "ml_models", "failure_prediction_model.joblib")
    ml_model = MLModel(model_path)
    print("ML model loaded successfully")

@app.on_event("shutdown")
async def shutdown_event():
    """Clean up resources on application shutdown"""
    # Close any open connections or resources
    print("Application shutting down")

@app.get("/")
async def root():
    """Root endpoint for health check"""
    return {"status": "online", "message": "Predictive Maintenance API is running"}

# Make ML model available to endpoints
def get_ml_model():
    """Dependency to provide ML model to endpoints"""
    return ml_model