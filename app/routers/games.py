# encoding: utf-8
# filename: games.py

from fastapi import APIRouter, Depends, HTTPException, WebSocket
from sqlalchemy.orm import Session
from app.dependencies.oauth2scheme import oauth2Scheme
from app.model import schemas
from app.ultilities import game_operation, token_tools
from app.dependencies.db import get_db

game_router = APIRouter(
    prefix='/api/games',
    tags=['Games']
)


# @game_router.websocket('/room/list')
# async def get_room_list(websocket: WebSocket, token: str = Depends(oauth2Scheme)):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")
