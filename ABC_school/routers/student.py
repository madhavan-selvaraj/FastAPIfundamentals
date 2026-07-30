from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, oauth2, schemas
from ..database import get_db

router = APIRouter(tags=["Student"])


@router.get(
    "/students",
    response_model=list[schemas.StudentResponse],
    status_code=status.HTTP_200_OK,
)
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students


@router.post(
    "/students",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db),
    user_email: str = Depends(oauth2.get_current_user),
):
    new_student = models.Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@router.get(
    "/students/{id}",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_200_OK,
)
def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    return student


@router.delete("/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(
    id: int,
    db: Session = Depends(get_db),
    user_email: str = Depends(oauth2.get_current_user),
):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    db.delete(student)
    db.commit()


@router.put(
    "/students/{id}",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_200_OK,
)
def update_student(
    id: int,
    Updated_student: schemas.StudentCreate,
    db: Session = Depends(get_db),
    user_email: str = Depends(oauth2.get_current_user),
):
    student_queryy = db.query(models.Student).filter(models.Student.id == id)
    student = student_queryy.first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not Found"
        )

    student_queryy.update(Updated_student.model_dump(), synchronize_session=False)
    db.commit()
    return student_queryy.first()
