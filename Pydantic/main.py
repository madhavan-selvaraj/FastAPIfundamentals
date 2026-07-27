from fastapi import FastAPI, HTTPException
from schemas import StudentBase

app = FastAPI()

students_list = [
    {
        "id": 1,
        "name": "Alice",
        "age": 20,
        "email": "alice@example.com",
        "cgpa": 8.7,
        "is_active": True,
        "subjects": ["Math", "Physics"],
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 22,
        "email": "bob@example.com",
        "cgpa": 7.9,
        "is_active": False,
        "subjects": ["Chemistry", "Biology"],
    },
]


@app.get("/")
def home() -> str:
    return "This is Pydantic Model Program Homepage"


@app.get("/students")
def get_students(name: str | None = None, age: int = 0) -> list[StudentBase]:
    new_student_list = [StudentBase(**args) for args in students_list]
    if name:
        new_student_list = [
            s for s in new_student_list if s.name.lower() == name.lower()
        ]

    if age:
        new_student_list = [s for s in new_student_list if s.age == age]

    return new_student_list


@app.get("/students/{student_id}")
def get_student(student_id: int) -> StudentBase:
    studentss = next(
        (StudentBase(**args) for args in students_list if args["id"] == student_id),
        None,
    )
    if studentss is None:
        raise HTTPException(status_code=404, detail="Student Not Found")
    return studentss
