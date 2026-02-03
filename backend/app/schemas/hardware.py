from pydantic import BaseModel, ConfigDict

class HardwareCreate(BaseModel):
    name: str

class HardwareResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    serial_number: str
    asset_tag: str
    available: bool