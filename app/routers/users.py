# encoding: utf-8
# Filename: users.py

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError
from datetime import timedelta

from app.ultilities import token_tools, user_tools
from app.dependencies.db import get_db
from app.dependencies.crud import get_user_by_name, create_user
from app.model import schemas
import toml

configuration = toml.load('app/config.toml')

user_router = APIRouter(
    prefix='/api/users',
    tags=['Users'],
    dependencies=[Depends(get_db)],
    responses={
        404: {
            'description': 'Not found.'
        }
    }
)


@user_router.post("/login")
def login_account(user_login: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    ## Description

    Login a user with user_name and password.

    ## Return
    **:return:** Login Status
    """

    user_authentication = token_tools.authenticate_user(
        user_name=user_login.username, password=user_login.password, db=db)

    if not user_authentication:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password.",
            headers={'WWW-Authenticate': 'Bearer'}
        )

    try:

        user = get_user_by_name(user_name=user_login.username, db=db)

        access_token_expires = timedelta(minutes=configuration['authentication']['access_token_expire_minutes'])

        access_token = token_tools.create_access_token(
            data={'sub': user.user_uuid},
            expires_delta=access_token_expires
        )

    except JWTError as e:
        raise HTTPException(
            status_code=401,
            detail='Unable to create token. \n' + str(e),
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return {'access_token': access_token}


@user_router.post('/create')
def sign_up_account(user_reg_info: schemas.UserReg, db: Session = Depends(get_db)):
    """
    ## Description

    Create a user with username, password and email.

    ## Requests Body

    JSON: **{"user_name": "string", "password": "string", "email": "string"}**


    ## Return
    **:return:** Register Status.
    """

    if get_user_by_name(user_name=user_reg_info.user_name, db=db):
        raise HTTPException(
            status_code=400,
            detail="Username has been used!"
        )

    if create_user(user_reg_info=user_reg_info, db=db):
        user_uuid: str = get_user_by_name(user_name=user_reg_info.user_name, db=db).user_uuid
        if not user_tools.create_user_directory(user_uuid=user_uuid):
            raise HTTPException(
                status_code=500,
                detail="Failed to create static directory!"
            )

        return {
            'status': 'ok'
        }


@user_router.post('/avatar/upload')
def upload_avatar():
    pass
