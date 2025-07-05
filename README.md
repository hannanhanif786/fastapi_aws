# FastAPI User CRUD with Superuser Authorization

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   # Quick setup for development
   make setup-dev
   
   # Or manually copy the configuration file
   cp config.env.development .env
   
   # Edit .env file with your actual values
   # Make sure to change the SECRET_KEY for production
   ```

## Environment Management

The application supports multiple environments: **development**, **staging**, and **production**.

### Quick Environment Setup

```bash
# Development environment
make setup-dev

# Staging environment  
make setup-staging

# Production environment
make setup-prod
```

### Environment-Specific Configuration Files

- `config.env.development` - Development settings
- `config.env.staging` - Staging settings  
- `config.env.production` - Production settings

### Running in Different Environments

```bash
# Local development
make run-dev

# Local staging
make run-staging

# Local production
make run-prod

# Docker development
make docker-dev

# Docker staging
make docker-staging
```

## Environment Variables

The application uses the following environment variables (see `config.env.*` files for examples):

### Database Configuration
- `DATABASE_URL`: PostgreSQL connection string
- `POSTGRES_USER`: Database username
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_DB`: Database name
- `POSTGRES_HOST`: Database host
- `POSTGRES_PORT`: Database port

### JWT Configuration
- `SECRET_KEY`: Secret key for JWT token signing (change in production!)
- `ALGORITHM`: JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time

### Application Configuration
- `APP_NAME`: Application name
- `DEBUG`: Debug mode (True/False)
- `ENVIRONMENT`: Environment (development/staging/production)
- `HOST`: Server host
- `PORT`: Server port
- `LOG_LEVEL`: Logging level
- `CORS_ORIGINS`: Allowed CORS origins
- `RATE_LIMIT_PER_MINUTE`: API rate limiting
- `ALLOWED_HOSTS`: Allowed host names

### AWS Configuration (for future use)
- `AWS_ACCESS_KEY_ID`: AWS access key
- `AWS_SECRET_ACCESS_KEY`: AWS secret key
- `AWS_REGION`: AWS region
- `AWS_S3_BUCKET`: S3 bucket name

## Running the App

### Option 1: Using Make commands (Recommended)
```bash
# Development
make run-dev

# Staging
make run-staging

# Production
make run-prod
```

### Option 2: Using the run script
```bash
python run.py
```

### Option 3: Using uvicorn directly
```bash
uvicorn app.main:app --reload
```

### Option 4: Using Docker Compose
```bash
# Development with Docker
make docker-dev

# Staging with Docker
make docker-staging
```

## Database
- Uses PostgreSQL. Configure your database URL in the `.env` file.
- Run Alembic migrations to set up the database schema:
  ```bash
  alembic upgrade head
  ```

## Features
- User CRUD (Create, Read, Update, Delete)
- JWT Authentication
- Only superusers can access user management endpoints
- Multi-environment configuration (dev/staging/prod)
- Environment-specific settings and validation
- Docker support for all environments
- AWS integration ready
- Health check endpoint
- Rate limiting configuration
- CORS configuration 