from pydantic import BaseModel

from app.schemas.user import UserCreate, UserResponse
from app.schemas.hardware import HardwareCreate, HardwareResponse
from app.schemas.loan import LoanCreate, LoanResponse, LoanDetailResponse

class MessageResponse(BaseModel):
    message: str