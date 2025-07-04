from typing import Optional, List
from sqlmodel import Session, select
from app.models import User
from app.auth import get_password_hash, verify_password


def get_user_by_username(session: Session, username: str) -> Optional[User]:
    return session.exec(select(User).where(User.username == username)).first()

def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
    return session.get(User, user_id)

def get_users(session: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return session.exec(select(User).offset(skip).limit(limit)).all()

def create_user(session: Session, username: str, email: str, password: str, is_superuser: bool = False) -> User:
    hashed_password = get_password_hash(password)
    user = User(username=username, email=email, hashed_password=hashed_password, is_superuser=is_superuser)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def update_user(session: Session, user: User, **kwargs) -> User:
    for key, value in kwargs.items():
        if key == "password" and value:
            user.hashed_password = get_password_hash(value)
        elif hasattr(user, key) and value is not None:
            setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(session: Session, user: User):
    session.delete(user)
    session.commit() 