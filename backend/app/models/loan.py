from datetime import datetime, UTC
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base
from app.models.user import User
from app.models.hardware import Hardware

class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True)
    loan_id: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    net_id: Mapped[str] = mapped_column(ForeignKey("users.net_id"))
    asset_tag: Mapped[str] = mapped_column(ForeignKey("hardware.asset_tag"))
    rented_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    returned_at: Mapped[datetime | None] = mapped_column(default=None)

    user: Mapped[User] = relationship(back_populates="loans")
    hardware: Mapped[Hardware] = relationship(back_populates="loans")