# from schemas import CreateStudent, StudentWithID
import models
from database import engine, get_db
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "THIS IS ABC SCHOOL"}


@app.get("/students")
def get_students(db: Session = Depends(get_db)):  # noqa: B008
    students = db.query(models.Student).all()
    return students


# @app.get("/students/{student_id}")
# def get_student(student_id:int) :
#     Student = next((StudentWithID(**s) for s in STUDENTS if s['id']==student_id),None)

#     if Student is None:
#         raise HTTPException(status_code=404,detail="Student not found!")
#     return Student

# @app.post("/students")
# def create_student(student_detail:CreateStudent) ->StudentWithID:
#     id = STUDENTS[-1]['id']+1
#     student = StudentWithID(id = id,**student_detail.model_dump()).model_dump()
#     STUDENTS.append(student)
#     return student

# @app.get("/sqlalchemy")
# def test_post(db:Session = Depends(get_db)):

#     students = db.query(models.Student).all()
#     return{"data":students}
