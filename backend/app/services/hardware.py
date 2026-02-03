from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Hardware
from fastapi import HTTPException
from app.utils import generate_serial_number, generate_asset_tag

def get_all(db: Session) -> list[Hardware]:
    return list(db.scalars(select(Hardware)).all())

def get_hardware_by_sn(db: Session, serial_number: str) -> Hardware:
    hardware = db.scalar(select(Hardware).where(Hardware.serial_number == serial_number))
    if not hardware:
        raise HTTPException(404, f"Hardware {serial_number} not found")
    return hardware

def get_available(db: Session) -> list[Hardware]:
    return list(db.scalars(select(Hardware).where(Hardware.available == True)).all())

def add_hardware(db: Session, name: str) -> Hardware:
    hardware = Hardware(
        name=name,
        serial_number=generate_serial_number(),
        asset_tag=generate_asset_tag()
    )
    db.add(hardware)
    db.commit()
    db.refresh(hardware)
    return hardware

def remove_hardware(db: Session, serial_number: str):
    hardware = get_hardware_by_sn(db, serial_number)
    db.delete(hardware)
    db.commit()