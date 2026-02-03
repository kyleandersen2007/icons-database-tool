from datetime import datetime, UTC
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Loan, User, Hardware
from fastapi import HTTPException
from app.utils import generate_loan_id

def get_all_loans(db: Session) -> list[Loan]:
    return list(db.scalars(select(Loan)).all())

def get_active_loans(db: Session) -> list[Loan]:
    return list(db.scalars(select(Loan).where(Loan.returned_at.is_(None))).all())

def get_active_loans_by_user(db: Session, net_id: str) -> list[Loan]:
    query = select(Loan).where(Loan.net_id == net_id, Loan.returned_at.is_(None))
    return list(db.scalars(query).all())

def get_loan_by_id(db: Session, loan_id: str) -> Loan:
    loan = db.scalars(select(Loan).where(Loan.loan_id == loan_id)).first()
    if not loan:
        raise HTTPException(f"Loan {loan_id} not found")
    return loan

def create_loan(db: Session, net_id: str, asset_tag: str) -> Loan:
    user = db.scalars(select(User).where(User.net_id == net_id)).first()
    if not user:
        raise HTTPException(f"User {net_id} not found")

    hardware = db.scalars(select(Hardware).where(Hardware.asset_tag == asset_tag)).first()
    if not hardware:
        raise HTTPException(f"Hardware {asset_tag} not found")

    if not hardware.available:
        raise HTTPException(409, "Hardware unavailable")

    loan = Loan(
        loan_id=generate_loan_id(net_id, asset_tag),
        net_id=net_id,
        asset_tag=asset_tag
    )

    hardware.available = False

    db.add(loan)
    db.commit()
    db.refresh(loan)
    return loan

def complete_loan(db: Session, loan_id: str) -> Loan:
    loan = get_loan_by_id(db, loan_id)

    if loan.returned_at:
        raise HTTPException(409, "Loan already returned")

    loan.returned_at = datetime.now(UTC)
    loan.hardware.available = True

    db.commit()
    db.refresh(loan)
    return loan