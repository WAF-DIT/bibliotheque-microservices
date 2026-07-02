from datetime import date

from pydantic import BaseModel


class BorrowBase(BaseModel):
    user_id: int
    book_id: int
    date_emprunt: date


class BorrowCreate(BorrowBase):
    pass


class BorrowResponse(BorrowBase):
    id: int
    retourne: bool
    date_retour: date | None = None

    class Config:
        from_attributes = True