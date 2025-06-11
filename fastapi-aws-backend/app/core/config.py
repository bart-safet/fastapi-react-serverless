import os
from typing import List, Optional, Union
from pydantic import field_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Force load from .env file, overriding system variables
load_dotenv(".env", override=True)


class Settings(BaseSettings):
    
    # Basic app settings
    PROJECT_NAME: str = "FastAPI AWS Boilerplate"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "FastAPI application with AWS services"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    
    # CORS
    ALLOWED_HOSTS: Union[List[str], str] = ["*"]
    
    # AWS Settings
    AWS_REGION: str = "us-east-1"
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    
    # DynamoDB
    DYNAMODB_TABLE_PREFIX: str = "fastapi-app"
    USERS_TABLE_NAME: str = "fastapi-app-users"
    
    # Cognito
    COGNITO_USER_POOL_ID: Optional[str] = None
    COGNITO_CLIENT_ID: Optional[str] = None
    COGNITO_CLIENT_SECRET: Optional[str] = None
    COGNITO_REGION: str = "us-east-1"
    
    # S3
    S3_BUCKET_NAME: Optional[str] = None
    S3_REGION: str = "us-east-1"
    
    # JWT
    JWT_SECRET_KEY: str = "your-secret-key-change-this"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Cache settings
    CACHE_TTL: int = 300
    
    @field_validator("ALLOWED_HOSTS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(",") if i.strip()]
        elif isinstance(v, list):
            return v
        return ["*"]

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()