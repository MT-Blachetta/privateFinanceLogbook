# app/db/base_class.py
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData

# Recommended naming convention for constraints for Alembic compatibility
# See: https://alembic.sqlalchemy.org/en/latest/naming.html
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

class Base(DeclarativeBase):
    metadata = metadata
    # You can define common attributes or methods for all models here
    # e.g., id: Mapped[int] = mapped_column(primary_key=True) if using integer IDs
    pass