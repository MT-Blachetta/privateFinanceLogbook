# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_new_user(
    *,
    db: Session = Depends(get_db),
    user_in: schemas.UserCreate
) -> schemas.User:
    """
    Create new user.
    """
    user = crud.crud_user.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this email already exists in the system.",
        )
    new_user = crud.crud_user.create_user(db=db, user_in=user_in)
    return new_user

# --- Placeholder for other user routes (GET /me, GET /{user_id}, PUT, DELETE) ---
# These will require authentication later

# Example: Get a user (will need auth later)
# @router.get("/{user_id}", response_model=schemas.User)
# def read_user_by_id(
#     user_id: uuid.UUID,
#     db: Session = Depends(get_db)
# ):
#     db_user = crud.crud_user.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user