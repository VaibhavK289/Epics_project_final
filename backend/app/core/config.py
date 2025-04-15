 """Application settings loaded from environment variables"""
    
    # API settings
    APP_NAME: str = "Predictive Maintenance API"
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Environment settings
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # Database settings
    DATABASE_URL: Optional[PostgresDsn] = None
    
    # CORS settings
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    
    @validator("ALLOWED_ORIGINS", pre=True)
    def parse_allowed_origins(cls, v):
        """Parse ALLOWED_ORIGINS from comma-separated string"""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    # Model settings
    MODEL_PATH: str = os.path.join("data", "ml_models", "failure_prediction_model.joblib")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Initialize settings
settings = Settings()