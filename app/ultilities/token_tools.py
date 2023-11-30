# encoding: utf-8
# filename: token_tools.py

from datetime import datetime, timedelta
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.ultilities.hash_tools import verify_password
from app.dependencies import crud
import toml

configuration = toml.load('app/config.toml')


def authenticate_user(user_name: str, password: str, db: Session):
    """
    Authenticate a user by user_name and password.
    :param user_name: user_name, a string type data.
    :param password: Password inputted from frontend.
    :param db: Session of the database.
    :return: The result of the authentication.
    """

    user = crud.get_user_by_name(user_name=user_name, db=db)

    if not user:

        return False

    elif not verify_password(plain_password=password, hashed_password=user.password):

        return False

    return True


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Function to create a JWT (JSON Web Token) with a custom expiration time.

    :param data: The data to be included in the token.
    :param expires_delta: The amount of time until the token expires. If not provided, defaults to 15 minutes.
    :return: The encoded JWT as a string.
    """

    secret_key: str = configuration['authentication']['secret_key']
    algorithm: str = configuration['authentication']['algorithm']
    data_to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    data_to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        data_to_encode, secret_key, algorithm
    )

    return encoded_jwt


def get_user_uuid_by_token(token: str):
    """
    Get uuid by token.
    :param token: Token to get uuid.
    :return: A uuid.
    """
    secret_key: str = configuration['authentication']['secret_key']
    algorithm: str = configuration['authentication']['algorithm']

    try:
        data_decoder = jwt.decode(token=token, key=secret_key, algorithms=algorithm)

        user_uuid: str = data_decoder.get('sub')

        if user_uuid is None:
            return False

        return user_uuid

    except JWTError:

        return False
