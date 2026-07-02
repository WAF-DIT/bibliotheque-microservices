from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Microservice Utilisateurs",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Bienvenue dans le microservice Utilisateurs"
    }


@app.post("/users", response_model=schemas.UserResponse)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(db, user)


@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return crud.get_users(db)


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_user(db, user_id)

@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(
    user_id: int,
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return crud.update_user(db, user_id, user)


@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_user(db, user_id)

@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(
    user_id: int,
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return crud.update_user(db, user_id, user)


@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_user(db, user_id)