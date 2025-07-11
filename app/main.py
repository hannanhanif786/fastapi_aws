from fastapi import FastAPI
from app.routes_users import router as users_router
from app.routes_auth import router as auth_router
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.include_router(users_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI User CRUD API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "environment": settings.ENVIRONMENT.value}
