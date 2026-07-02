from sqlalchemy.orm import Session

from app import models, schemas


def create_borrow(
    db: Session,
    borrow: schemas.BorrowCreate
):

    db_borrow = models.Borrow(
        user_id=borrow.user_id,
        book_id=borrow.book_id,
        date_emprunt=borrow.date_emprunt
    )

    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)

    return db_borrow


def get_history(db: Session):

    return db.query(models.Borrow).all()


def get_borrow(
    db: Session,
    borrow_id: int
):

    return (
        db.query(models.Borrow)
        .filter(models.Borrow.id == borrow_id)
        .first()
    )

from datetime import date, timedelta


def return_book(
    db: Session,
    borrow_id: int
):

    borrow = (
        db.query(models.Borrow)
        .filter(models.Borrow.id == borrow_id)
        .first()
    )

    if borrow:

        borrow.retourne = True
        borrow.date_retour = date.today()

        db.commit()
        db.refresh(borrow)

    return borrow


def get_late_books(db: Session):

    limite = date.today() - timedelta(days=14)

    return (
        db.query(models.Borrow)
        .filter(
            models.Borrow.date_emprunt < limite,
            models.Borrow.retourne == False
        )
        .all()
    )