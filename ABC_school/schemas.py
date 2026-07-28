from pydantic import BaseModel, EmailStr

# class SubjectChoice(Enum):
#     PYTHON="Python"
#     JAVA="Java"
#     C = "C"
#     MATHEMATICS="Mathematics"
#     DATABASE = "Database"


class Subjects(BaseModel):
    name: str
    mark: int

    # @field_validator("name", mode="before")
    # @classmethod
    # def title_case(cls, value):
    #     if isinstance(value, str):
    #         return value.title()
    #     return value


class StudentBase(BaseModel):
    name: str
    age: int
    email: EmailStr
    cgpa: float
    is_active: bool
    subjects: list[Subjects] = []


class CreateStudent(StudentBase):
    pass


class StudentWithID(StudentBase):
    id: int
