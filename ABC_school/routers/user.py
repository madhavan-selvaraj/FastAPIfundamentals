from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(tags=["User"])


@router.get(
    "/users", response_model=list[schemas.UserResponse], status_code=status.HTTP_200_OK
)
def get_users(db: Session = Depends(get_db)):
    return (db.query(models.User)).all()


@router.post(
    "/users", response_model=schemas.UserResponse, status_code=status.HTTP_200_OK
)
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
