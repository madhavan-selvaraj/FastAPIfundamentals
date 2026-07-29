from pydantic import BaseModel, ConfigDict, EmailStr


class StudentCreate(BaseModel):
    name: str
    age: int
    email: EmailStr
    cgpa: float


class StudentResponse(StudentCreate):
    id: int
    status: bool
    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)
