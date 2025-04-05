# app/api/v1/api.py
from fastapi import APIRouter

from app.api.v1.endpoints import users # Import other endpoint modules here later

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(users.router, prefix="/users", tags=["Users"])
# Add other routers like payment_items, categories, etc. here
# api_router.include_router(payment_items.router, prefix="/payment-items", tags=["Payment Items"])