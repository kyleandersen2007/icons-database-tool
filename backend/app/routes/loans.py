from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import schemas
from app.services import loans

router = APIRouter(prefix="/loans", tags=["loans"])

@router.get("/get_all_loans", response_model=list[schemas.LoanResponse])
def get_all_loans(active_only: bool = False, db: Session = Depends(get_db)):
    return loans.get_active_loans(db) if active_only else loans.get_all_loans(db)

@router.get("/get_loan/{loan_id}", response_model=schemas.LoanDetailResponse)
def get_loan(loan_id: str, db: Session = Depends(get_db)):
    return loans.get_loan_by_id(db, loan_id)

@router.post("/create_loan", response_model=schemas.LoanResponse, status_code=201)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    return loans.create_loan(db, loan.net_id, loan.asset_tag)

@router.post("/complete_loan/{loan_id}", response_model=schemas.LoanResponse)
def complete_loan(loan_id: str, db: Session = Depends(get_db)):
    return loans.complete_loan(db, loan_id)