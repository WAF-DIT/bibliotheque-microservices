from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import Base, engine, get_db
from app.models import Book

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Microservice Livres",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Bienvenue sur l'application de MicroService Livres"
    }


@app.post("/books", response_model=schemas.BookResponse)
def create_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_db)
):
    return crud.create_book(db, book)


@app.get("/books", response_model=list[schemas.BookResponse])
def get_books(
    db: Session = Depends(get_db)
):
    return crud.get_books(db)

@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_book(db, book_id)

@app.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_book(db, book_id)

@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(
    book_id: int,
    book: schemas.BookCreate,
    db: Session = Depends(get_db)
):
    return crud.update_book(
        db,
        book_id,
        book
    )