from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.schemas.user import UserResponse
from app.schemas.hardware import HardwareResponse

class LoanCreate(BaseModel):
    net_id: str
    asset_tag: str

class LoanResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    loan_id: str
    net_id: str
    asset_tag: str
    rented_at: datetime
    returned_at: datetime | None

class LoanDetailResponse(LoanResponse):
    user: UserResponse
    hardware: HardwareResponse