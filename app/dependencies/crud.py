# encoding: utf-8
# filename: crud.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.model import models
from app.model import schemas
from uuid import uuid4
from app.ultilities import hash_tools
from datetime import datetime


def create_user(user_reg_info: schemas.UserReg, db: Session) -> bool | None:
    """
    Create a user in a database.
    :param user_reg_info: Information of a user to register from requests body.
    :param db: Session for operating the database.
    :return:
    """
    # Generate an uuid and make the password hashed for the new user.
    user_uuid: str = str(uuid4())
    hashed_password: str = hash_tools.get_password_hashed(plain_password=user_reg_info.password)

    # Create the ORM class.
    db_user = models.Users(
        user_uuid=user_uuid,
        user_name=user_reg_info.user_name,
        nick_name=user_reg_info.user_name,
        password=hashed_password,
        email=user_reg_info.email,
        date=datetime.utcnow()
    )
    # Add the data into the database.
    try:

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return True

    except IntegrityError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e.args)
        )


def get_user_by_name(user_name: str, db: Session) -> type(models.Users) | None:
    """
    Select a user from the database by user_name.
    :param user_name: Name of the user to select.
    :param db: Session for operating the database.
    :return: An object of the user.
    """

    db_user = db.query(models.Users).filter(models.Users.user_name == user_name).first()

    return db_user


def get_user_by_uuid(user_uuid: str, db: Session) -> type(models.Users) | None:
    """
    Select a user from the database by user_uuid.
    :param user_uuid: UUID of the user to select.
    :param db: Session for operating the database.
    :return: An object of the user.
    """

    db_user = db.query(models.Users).filter(models.Users.user_uuid == user_uuid).first()

    return db_user
