from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Microservice Livres",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Bienvenue sur l'application de Microservice Livres"
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


# ==========================
# RECHERCHE DE LIVRES
# ==========================

@app.get("/books/search")
def search_books(
    title: str = None,
    author: str = None,
    isbn: str = None,
    db: Session = Depends(get_db)
):
    return crud.search_books(
        db,
        title,
        author,
        isbn
    )


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_book(
        db,
        book_id
    )


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


@app.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_book(
        db,
        book_id
    )

