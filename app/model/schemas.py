from pydantic import BaseModel


# Request Bodies
class Room(BaseModel):
    name: str
    password: str = ''


class UserReg(BaseModel):
    user_name: str = ''
    password: str = ''
    email: str = ''

