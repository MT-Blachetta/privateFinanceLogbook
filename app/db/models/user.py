from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func
import uuid # Using UUID for primary keys

from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    full_name: Mapped[str | None] = mapped_column(String(255), index=True) # Optional full name
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean(), default=False) # Optional superuser flag
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # --- Relationships (will be added later) ---
    # payment_items: Mapped[List["PaymentItem"]] = relationship(back_populates="owner")
    # recipients: Mapped[List["Recipient"]] = relationship(back_populates="owner")
    # categories: Mapped[List["Category"]] = relationship(back_populates="owner")
    # category_types: Mapped[List["CategoryType"]] = relationship(back_populates="owner")

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"