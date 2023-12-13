# encoding: utf-8
# filename: games.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.oauth2scheme import oauth2Scheme
from app.model import schemas
from app.ultilities import game_operation, token_tools
from app.dependencies.db import get_db

game_router = APIRouter(
    prefix='/api/games',
    tags=['Games']
)

# List of room for gaming.
# room_list: list[dict[str, str | list[dict[str, str]]]] = []
#
#
# @game_router.get('/rooms')
# def get_rooms():
#     """
#     ## Description
#
#     Get a list of the rooms.
#
#     ## Return
#     **:return:** A list of existing rooms.
#     """
#
#     list_for_return = []
#
#     if len(room_list) != 0:
#         for room in room_list:
#             room_temp_list = {
#                 "room_uuid": room['room_uuid'],
#                 "master_uuid": room['master_uuid'],
#                 "name": room['name'],
#                 "players count": len(room['player_list'])
#             }
#             list_for_return.append(room_temp_list)
#
#     return list_for_return
#
#
# @game_router.post('/rooms/create')
# def create_rooms(room_info: schemas.Room, token: str = Depends(oauth2Scheme), db: Session = Depends(get_db)):
#     """
#     ## Description
#
#     Create a room to start a game.
#
#     You need to provider a JSON data like here:
#
#
#     ## Parameters
#     * **:param** room_info: Requests Body of the information for creating a new room.
#     * **:param** token: Token from the player.
#
#     ## Requests Body
#
#     JSON: **{"name": "string", "password": ""}**
#
#     ## Return
#     **:return:** Creation Status.
#     """
#
#     master_uuid = token_tools.get_user_uuid_by_token(token=token)
#     data_room = game_operation.generate_room_dict(room_info=room_info, master_uuid=master_uuid, db=db)
#
#     if game_operation.check_room_member(player_uuid=master_uuid, room_list=room_list, room_uuid=None):
#         raise HTTPException(
#             status_code=400,
#             detail="You have already been a member in a room. Creating other rooms is refused."
#         )
#
#     try:
#         room_list.append(data_room)
#
#         return {
#             'status': 'ok'
#         }
#
#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail="Failed to create room: " + data_room['room_uuid']
#                    + '\n' + str(e)
#         )
#
#
# @game_router.post('/rooms/join/{room_uuid}')
# def join_room(room_uuid: str, token: str = Depends(oauth2Scheme), db: Session = Depends(get_db)):
#     """
#     ## Description
#
#     Join a room with room_uuid.
#
#     ## Parameters
#
#     * **:param** db: Session of the database.
#     * **:param** room_uuid: The UUID of the room to join.
#     * **:param** token: Token of the player.
#
#     ## Return
#
#     * **:return**: Status of the operation.
#     """
#
#     player_uuid = token_tools.get_user_uuid_by_token(token=token)
#
#     if game_operation.check_room_member(player_uuid=player_uuid, room_list=room_list, room_uuid=room_uuid):
#         raise HTTPException(
#             status_code=400,
#             detail="You have already been a member in a room. Joining other rooms is refused."
#         )
#
#     try:
#         player_data = game_operation.generate_player_dict(player_uuid=player_uuid, db=db)
#         for i in range(0, len(room_list)):
#             if room_list[i]['room_uuid'] == room_uuid:
#                 room_list[i]['player_list'].append(player_data)
#
#         return {
#             'status': 'ok'
#         }
#
#     except Exception as e:
#
#         raise HTTPException(
#             status_code=500,
#             detail="Joining room failed\n" + str(e)
#         )
#
#
# @game_router.put('/rooms/quit/{room_uuid}')
# def quit_room(room_uuid: str, token: str = Depends(oauth2Scheme)):
#     """
#     ## Description
#
#     Quit a room with room_uuid.
#
#     ## Parameters
#
#     * **:param** room_uuid: The UUID of the room to quit.
#     * **:param** token: The player's token.
#
#     ## Return
#
#     * **:return**: Status of the operation.
#     """
#
#     player_uuid: str = token_tools.get_user_uuid_by_token(token=token)
#
#     if game_operation.check_room_master(player_uuid=player_uuid, room_list=room_list, room_uuid=room_uuid):
#         raise HTTPException(
#             status_code=400,
#             detail="You are a master of a room, you're not allowed to quit, but you can delete it."
#         )
#
#     if game_operation.check_room_member(player_uuid=player_uuid, room_list=room_list, room_uuid=room_uuid):
#         for room in room_list:
#             if room['room_uuid'] == room_uuid:
#                 for player in room['player_list']:
#                     if player['player_uuid'] == player_uuid:
#                         room['player_list'].remove(player)
#
#                         return {
#                             'status': 'ok'
#                         }
#
#     else:
#         raise HTTPException(
#             status_code=400,
#             detail="You haven't joint any rooms yet!"
#         )
#
#
# @game_router.put('/rooms/{room_uuid}/remove/{player_uuid}')
# def remove_player(room_uuid: str, player_uuid: str, token: str = Depends(oauth2Scheme)):
#     """
#     ## Description
#
#     Delete a player from a room.
#
#     It is a privilege of a master owning a room.
#
#     ## Parameters
#
#     * **:param** room_uuid: UUID of the room.
#     * **:param** player_uuid: UUID of the player to delete.
#     * **:param** token: Token of the master.
#     * **:param** db: Session of the database.
#
#     ## Return
#
#     * **:return**: Status of the operation.
#     """
#
#     master_uuid = token_tools.get_user_uuid_by_token(token=token)
#
#     if not game_operation.check_room_master(player_uuid=master_uuid, room_list=room_list, room_uuid=room_uuid):
#         raise HTTPException(
#             status_code=400,
#             detail="You are not a master of a room, permission denied."
#         )
#
#     if not game_operation.check_room_member(player_uuid=player_uuid, room_list=room_list, room_uuid=room_uuid):
#         raise HTTPException(
#             status_code=400,
#             detail="The player has not joint any rooms or not existed in this room."
#         )
#
#     if player_uuid == master_uuid:
#         raise HTTPException(
#             status_code=400,
#             detail="You can not remove yourself!"
#         )
#
#     for room in room_list:
#         if room['room_uuid'] == room_uuid:
#             for player in room['player_list']:
#                 if player['player_uuid'] == player_uuid:
#                     room['player_list'].remove(player)
#                     return {
#                         'status': 'ok'
#                     }
#         else:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Room does not exist!"
#             )
#
#
# @game_router.delete('/rooms/delete/{room_uuid}')
# def delete_room(room_uuid: str, token: str = Depends(oauth2Scheme)):
#     """
#     ## Description
#
#     Delete a room with room_uuid.
#
#     ## Parameters
#
#     * **:param** room_uuid: UUID of the room.
#     * **:param** token: Token of the player.
#
#     ## Return
#
#     * **:return**: Status of the operation.
#     """
#
#     player_uuid: str = token_tools.get_user_uuid_by_token(token=token)
#
#     if game_operation.check_room_master(player_uuid=player_uuid, room_list=room_list, room_uuid=room_uuid):
#         for room in room_list:
#             if room['room_uuid'] == room_uuid and room['master_uuid'] == player_uuid:
#                 room_list.remove(room)
#
#         return {
#             'status': 'ok'
#         }
#
#     else:
#         raise HTTPException(
#             status_code=400,
#             detail="You're not the of this room, permission denied."
#         )
