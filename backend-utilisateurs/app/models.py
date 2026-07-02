from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    nom = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    type_utilisateur = Column(String, nullable=False)

    actif = Column(Boolean, default=True)