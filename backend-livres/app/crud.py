from sqlalchemy.orm import Session

from app import models, schemas


def create_book(db: Session, book: schemas.BookCreate):

    db_book = models.Book(
        title=book.title,
        author=book.author,
        isbn=book.isbn,
        publication_year=book.publication_year
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def get_books(db: Session):

    return db.query(models.Book).all()

def get_book(db: Session, book_id: int):

    return (
        db.query(models.Book)
        .filter(models.Book.id == book_id)
        .first()
    )

def delete_book(db: Session, book_id: int):

    book = (
        db.query(models.Book)
        .filter(models.Book.id == book_id)
        .first()
    )

    if book:
        db.delete(book)
        db.commit()

    return book

def update_book(
    db: Session,
    book_id: int,
    book_data: schemas.BookCreate
):

    book = (
        db.query(models.Book)
        .filter(models.Book.id == book_id)
        .first()
    )

    if book:

        book.title = book_data.title
        book.author = book_data.author
        book.isbn = book_data.isbn
        book.publication_year = book_data.publication_year

        db.commit()
        db.refresh(book)

    return book