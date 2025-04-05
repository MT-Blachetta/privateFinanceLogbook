# app/crud/crud_user.py
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash
import uuid

def get_user(db: Session, user_id: uuid.UUID) -> User | None:
    """Gets a user by their ID."""
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User | None:
    """Gets a user by their email address."""
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, *, user_in: UserCreate) -> User:
    """Creates a new user."""
    hashed_password = get_password_hash(user_in.password)
    db_user = User(
        email=user_in.email,
        hashed_password=hashed_password,
        full_name=user_in.full_name,
        is_active=user_in.is_active if user_in.is_active is not None else True,
        is_superuser=user_in.is_superuser
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # Refresh to get the generated ID and defaults
    return db_user

def update_user(db: Session, *, db_user: User, user_in: UserUpdate) -> User:
    """Updates an existing user."""
    update_data = user_in.model_dump(exclude_unset=True) # Use model_dump in Pydantic v2

    if "password" in update_data and update_data["password"]:
        hashed_password = get_password_hash(update_data["password"])
        del update_data["password"] # Remove plain password from dict
        db_user.hashed_password = hashed_password # Update hashed password separately

    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Add delete_user function if needed