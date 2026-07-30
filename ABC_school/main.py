from fastapi import FastAPI

from .database import Base, engine
from .routers import student, user, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "THIS IS ABC SCHOOL"}


app.include_router(student.router)
app.include_router(user.router)
app.include_router(auth.router)
