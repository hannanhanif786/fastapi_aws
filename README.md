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

## Running the App

```bash
uvicorn main:app --reload
```

## Database
- Uses PostgreSQL. Configure your database URL in the environment or settings file.
- Run Alembic migrations to set up the database schema.

## Features
- User CRUD (Create, Read, Update, Delete)
- JWT Authentication
- Only superusers can access user management endpoints 