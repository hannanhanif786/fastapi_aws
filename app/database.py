from sqlmodel import SQLModel, create_engine, Session
from app.models import User
from app.config import settings

engine = create_engine(settings.get_database_url(), echo=settings.DEBUG)

def get_session():
    with Session(engine) as session:
        yield session
