from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

if TYPE_CHECKING:
    from app.models.loan import Loan

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    net_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    student_number: Mapped[str] = mapped_column(String(50), unique=True, index=True)

    loans: Mapped[list["Loan"]] = relationship(back_populates="user", foreign_keys="Loan.net_id")