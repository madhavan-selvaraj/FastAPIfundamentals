from pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    cgpa: float
    is_active: bool
    subjects: list[str]
