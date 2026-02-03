from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User
from fastapi import HTTPException

def get_all(db: Session) -> list[User]:
    return list(db.scalars(select(User)).all())

def get_by_student_number(db: Session, student_number: str) -> User:
    user = db.scalar(select(User).where(User.student_number == student_number))
    if not user:
        raise HTTPException(404, "User not found")
    return user

def add_user(db: Session, name: str, net_id: str, student_number: str) -> User:
    user = User(name=name, net_id=net_id, student_number=student_number)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, student_number: str) -> None:
    user = get_by_student_number(db, student_number)
    db.delete(user)
    db.commit()