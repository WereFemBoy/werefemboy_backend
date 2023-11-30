# encoding: utf-8
# filename: oauth2scheme.py

from fastapi.security import OAuth2PasswordBearer

oauth2Scheme = OAuth2PasswordBearer(tokenUrl='/api/users/login')
