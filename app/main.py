# encoding: utf-8
# Filename: main.py

from fastapi import FastAPI
from datetime import datetime
from app.model import models
from app.dependencies.db import engine
from app.routers import users, games
import platform

document_description = '''

## Introduction

Here is the API document of the WereFemboy backend.

You can read the documents of the APIs and test.
'''

tags_meta = [
    {
        "name": "default",
        "description": "Operations to check the information of services."
    },
    {
        "name": "Users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "Games",
        "description": "Operations with games. The main logic to play the game is here.",
    },
]

models.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="WereFemBoy Game API",
    description=document_description,
    version="0.0.1",
    openapi_tags=tags_meta
)


app.include_router(users.user_router)
app.include_router(games.game_router)


@app.get('/')
def system_info():
    """
    ## Description
    * Show the information of the backend:
        * API Version
        * Server Time UTC
        * Server Local Time
        * OS
        * Python Version

    ## Return

    * **:return**: Backend info.
    """

    return {
        "Server Time UTC": datetime.utcnow(),
        "Server Local Time": datetime.now(),
        "OS": platform.platform(),
        "Python Version": platform.python_version()
    }


