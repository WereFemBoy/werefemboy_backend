from fastapi import APIRouter

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
def create_user():
    """
    ## Description

    Create a user with username, password and email.

    ## Return
    **:return:** Register Status.
    """
    pass
