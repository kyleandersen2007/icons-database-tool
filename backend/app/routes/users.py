from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import schemas
from app.services import users

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/get_all_users", response_model=list[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return users.get_all(db)

@router.get("/retrieve_user/{student_number}", response_model=schemas.UserResponse)
def retrieve_user(student_number: str, db: Session = Depends(get_db)):
    return users.get_by_student_number(db, student_number)

@router.post("/add_user", response_model=schemas.UserResponse, status_code=201)
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return users.add_user(db, user.name, user.net_id, user.student_number)

@router.delete("/remove_user/{student_number}", response_model=schemas.MessageResponse)
def remove_user(student_number: str, db: Session = Depends(get_db)):
    users.delete_user(db, student_number)
    return {"message": f"User {student_number} deleted"}