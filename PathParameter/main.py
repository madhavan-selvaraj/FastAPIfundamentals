from fastapi import FastAPI, HTTPException

app = FastAPI()


students_list = [
    {"id": 1, "name": "Alice", "age": 20, "course": "Computer Science"},
    {"id": 2, "name": "Bob", "age": 21, "course": "Mechanical"},
    {"id": 3, "name": "Charlie", "age": 19, "course": "Electrical"},
    {"id": 4, "name": "David", "age": 22, "course": "Civil"},
]


@app.get("/")
def home() -> dict:
    return {"Messege": "Welcome to Path Parameters home page"}


@app.get("/students")
def get_students() -> list[dict]:
    return students_list


@app.get("/students/{student_id}")
def get_student(student_id: int) -> dict:
    student = next((i for i in students_list if i["id"] == student_id), None)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
