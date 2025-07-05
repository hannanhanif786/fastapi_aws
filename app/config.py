import os
from typing import Optional
from dotenv import load_dotenv
from enum import Enum

# Load environment variables from .env file
load_dotenv()

class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

class Settings:
    # Environment Configuration
    ENVIRONMENT: Environment = Environment(os.getenv("ENVIRONMENT", "development"))
    
    # Database Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/postgres")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "postgres")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))

    # JWT Configuration
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # Application Configuration
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI AWS Services")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # Server Configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

    # AWS Configuration
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    AWS_S3_BUCKET: str = os.getenv("AWS_S3_BUCKET", "")

    # Logging Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # CORS Configuration
    CORS_ORIGINS: list = os.getenv("CORS_ORIGINS", "*").split(",")
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", "60"))
    
    # Security
    ALLOWED_HOSTS: list = os.getenv("ALLOWED_HOSTS", "*").split(",")
    
    def __init__(self):
        # Environment-specific overrides
        self._apply_environment_overrides()
        self._validate_settings()
    
    def _apply_environment_overrides(self):
        """Apply environment-specific settings"""
        if self.ENVIRONMENT == Environment.PRODUCTION:
            self.DEBUG = False
            self.LOG_LEVEL = "WARNING"
            # Ensure production has proper secret key
            if self.SECRET_KEY == "supersecretkey":
                raise ValueError("SECRET_KEY must be changed in production!")
        
        elif self.ENVIRONMENT == Environment.STAGING:
            self.DEBUG = False
            self.LOG_LEVEL = "INFO"
            # Staging should use different database
            if not self.POSTGRES_DB.endswith("_staging"):
                self.POSTGRES_DB = f"{self.POSTGRES_DB}_staging"
        
        elif self.ENVIRONMENT == Environment.DEVELOPMENT:
            self.DEBUG = True
            self.LOG_LEVEL = "DEBUG"
    
    def _validate_settings(self):
        """Validate critical settings"""
        if not self.SECRET_KEY or self.SECRET_KEY == "supersecretkey":
            if self.ENVIRONMENT != Environment.DEVELOPMENT:
                raise ValueError("SECRET_KEY must be set for non-development environments")
        
        if self.ENVIRONMENT == Environment.PRODUCTION:
            if not self.AWS_ACCESS_KEY_ID or not self.AWS_SECRET_ACCESS_KEY:
                print("Warning: AWS credentials not set for production")
    
    @property
    def is_development(self) -> bool:
        return self.ENVIRONMENT == Environment.DEVELOPMENT
    
    @property
    def is_staging(self) -> bool:
        return self.ENVIRONMENT == Environment.STAGING
    
    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == Environment.PRODUCTION
    
    def get_database_url(self) -> str:
        """Get database URL with environment-specific modifications"""
        if self.ENVIRONMENT == Environment.STAGING:
            # Use staging database
            return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        return self.DATABASE_URL

# Create a global settings instance
settings = Settings()
