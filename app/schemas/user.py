# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import uuid
from datetime import datetime

# --- Base Schema ---
class UserBase(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    full_name: Optional[str] = Field(None, example="Jane Doe")
    is_active: Optional[bool] = True
    is_superuser: bool = False

# --- Schema for Creation (receives password) ---
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, example="strongpassword123")

# --- Schema for Updating (password is optional) ---
class UserUpdate(UserBase):
    email: Optional[EmailStr] = Field(None, example="user@example.com") # Allow email update if needed
    password: Optional[str] = Field(None, min_length=8, example="newstrongpassword123")

# --- Schema for Reading from DB (includes hashed password, internal use) ---
class UserInDBBase(UserBase):
    id: uuid.UUID
    hashed_password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True # Renamed from orm_mode in Pydantic v2

# --- Schema for API Response (excludes password) ---
class User(UserBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# --- Schema for Token Data ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None