from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import schemas
from app.services import hardware

router = APIRouter(prefix="/hardware", tags=["hardware"])

@router.get("/get_all_hardware", response_model=list[schemas.HardwareResponse])
def get_all_hardware(available_only: bool = False, db: Session = Depends(get_db)):
    return hardware.get_available(db) if available_only else hardware.get_all(db)

@router.get("/get_hardware/{serial_number}", response_model=schemas.HardwareResponse)
def get_hardware_by_sn(serial_number: str, db: Session = Depends(get_db)):
    return hardware.get_hardware_by_sn(db, serial_number)

@router.post("/create_hardware", response_model=schemas.HardwareResponse, status_code=201)
def add_hardware(hw: schemas.HardwareCreate, db: Session = Depends(get_db)):
    return hardware.add_hardware(db, hw.name)

@router.delete("/delete_hardware/{serial_number}", response_model=schemas.MessageResponse)
def remove_hardware(serial_number: str, db: Session = Depends(get_db)):
    hardware.remove_hardware(db, serial_number)
    return {"message": f"Hardware {serial_number} deleted"}