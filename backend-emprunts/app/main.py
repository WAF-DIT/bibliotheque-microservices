from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Microservice Emprunts",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Bienvenue dans le microservice Emprunts"
    }


@app.post("/borrow",
          response_model=schemas.BorrowResponse)
def create_borrow(
    borrow: schemas.BorrowCreate,
    db: Session = Depends(get_db)
):
    return crud.create_borrow(
        db,
        borrow
    )


@app.get("/history",
         response_model=list[schemas.BorrowResponse])
def get_history(
    db: Session = Depends(get_db)
):
    return crud.get_history(db)


@app.get("/history/{borrow_id}",
         response_model=schemas.BorrowResponse)
def get_borrow(
    borrow_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_borrow(
        db,
        borrow_id
    )

@app.post(
    "/return/{borrow_id}",
    response_model=schemas.BorrowResponse
)
def return_book(
    borrow_id: int,
    db: Session = Depends(get_db)
):
    return crud.return_book(
        db,
        borrow_id
    )


@app.get(
    "/late-books",
    response_model=list[schemas.BorrowResponse]
)
def get_late_books(
    db: Session = Depends(get_db)
):
    return crud.get_late_books(db)