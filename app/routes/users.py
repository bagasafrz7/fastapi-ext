from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from starlette import status

from app.database import User, get_db_session
from app.schema import UsersCreate, UsersRead

users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.get("/", response_model=list[UsersRead])
def get_users(db: Session = Depends(get_db_session)):
    users = db.exec(select(User)).all()
    return users


@users_router.get("/user_id", response_model=UsersRead)
def get_user(user_id: int, db: Session = Depends(get_db_session)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@users_router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: UsersCreate, db: Session = Depends(get_db_session)):
    new_user = User(name=user.name, address=user.address, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user.model_dump()


@users_router.patch("/{user_id}", response_model=UsersRead)
def update_user(user_id: int, user: UsersCreate, db: Session = Depends(get_db_session)):
    db_user = db.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )

    db_user.name = user.name
    db_user.address = user.address
    db_user.age = user.age
    db.commit()
    db.refresh(db_user)

    return db_user.model_dump()


@users_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db_session)):
    db_user = db.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    db.delete(db_user)
    db.commit()
