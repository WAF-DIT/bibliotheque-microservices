from sqlalchemy.orm import Session

from app import models, schemas


def create_user(db: Session, user: schemas.UserCreate):

    db_user = models.User(
        nom=user.nom,
        email=user.email,
        type_utilisateur=user.type_utilisateur
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_users(db: Session):

    return db.query(models.User).all()


def get_user(db: Session, user_id: int):

    return (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

def update_user(
    db: Session,
    user_id: int,
    user_data: schemas.UserCreate
):

    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if user:
        user.nom = user_data.nom
        user.email = user_data.email
        user.type_utilisateur = user_data.type_utilisateur

        db.commit()
        db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):

    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if user:
        db.delete(user)
        db.commit()

    return user

def update_user(
    db: Session,
    user_id: int,
    user_data: schemas.UserCreate
):

    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if user:

        user.nom = user_data.nom
        user.email = user_data.email
        user.type_utilisateur = user_data.type_utilisateur

        db.commit()
        db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):

    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if user:
        db.delete(user)
        db.commit()

    return user