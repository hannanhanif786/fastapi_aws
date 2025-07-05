from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from app.database import get_session
from app.schemas import UserCreate, UserRead, UserUpdate
from app.models import User
from app.crud import get_users, get_user_by_id, create_user, update_user, delete_user
from app.deps import get_current_superuser

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserRead])
def list_users(skip: int = 0, limit: int = 100, session: Session = Depends(get_session), current_user: User = Depends(get_current_superuser)):
    return get_users(session, skip=skip, limit=limit)

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_new_user(user_in: UserCreate, session: Session = Depends(get_session)):
    user = create_user(session, username=user_in.username, email=user_in.email, password=user_in.password, is_superuser=user_in.is_superuser)
    return user

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_superuser)):
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/{user_id}", response_model=UserRead)
def update_existing_user(user_id: int, user_in: UserUpdate, session: Session = Depends(get_session), current_user: User = Depends(get_current_superuser)):
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = update_user(session, user, **user_in.dict(exclude_unset=True))
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_user(user_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_superuser)):
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(session, user)
    return None
