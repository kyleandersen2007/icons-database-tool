from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

if TYPE_CHECKING:
    from app.models.loan import Loan

class Hardware(Base):
    __tablename__ = "hardware"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    serial_number: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    asset_tag: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    available: Mapped[bool] = mapped_column(default=True, index=True)

    loans: Mapped[list["Loan"]] = relationship(back_populates="hardware", foreign_keys="Loan.asset_tag")