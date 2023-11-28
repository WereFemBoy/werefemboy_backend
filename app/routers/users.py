from fastapi import APIRouter
from app.model import schemas

user_router = APIRouter(
    prefix='/api/users',
    tags=['Users']
)


@user_router.post("/login")
def login_account():
    """
    ## Description

    Login a user with user_name and password.

    ## Return
    **:return:** Login Status
    """
    pass


@user_router.post('/create')
def create_user(user_reg_info: schemas.UserReg):
    """
    ## Description

    Create a user with username, password and email.

    ## Requests Body

    ```json
    {
        "user_name": "string",
        "password": "string",
        "email": "string"
    }
    ```

    ## Return
    **:return:** Register Status.
    """
    pass
