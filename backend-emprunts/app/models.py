from sqlalchemy import Boolean, Column, Date, Integer

from app.database import Base


class Borrow(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    book_id = Column(Integer, nullable=False)

    date_emprunt = Column(Date, nullable=False)

    date_retour = Column(Date)

    retourne = Column(Boolean, default=False)