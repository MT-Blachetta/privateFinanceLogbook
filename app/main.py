# app/main.py
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.api import api_router
# from app.db.session import engine # For creating tables if not using Alembic initially
# from app.db.base_class import Base # For creating tables if not using Alembic initially

# --- Optional: Create database tables (if not using Alembic yet) ---
# This is simple but not recommended for production (use Alembic migrations)
# def create_tables():
#     Base.metadata.create_all(bind=engine)
# create_tables()
# ------------------------------------------------------------------


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json" # Standard location for OpenAPI spec
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include the API router
app.include_router(api_router, prefix=settings.API_V1_STR)

# --- Root endpoint ---
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}

# --- Add other middleware or startup/shutdown events if needed ---