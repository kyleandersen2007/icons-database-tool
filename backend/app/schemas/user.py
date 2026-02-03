from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    name: str
    net_id: str
    student_number: str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    net_id: str
    student_number: str