from database import Base
from sqlalchemy import Boolean, Column, Float, Integer, String


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    cgpa = Column(Float, nullable=False)
    status = Column(Boolean, server_default="TRUE", nullable=False)
