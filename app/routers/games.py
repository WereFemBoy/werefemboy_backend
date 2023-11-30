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
room_list: list[dict] = []


@game_router.get('/rooms')
def get_rooms():
    """
    ## Description

    Get a list of the rooms.

    ## Return
    **:return:** A list of existing rooms.
    """

    # list_for_return = []

    return room_list


@game_router.post('/rooms/create')
def create_rooms(room_info: schemas.Room, token: str = Depends(oauth2Scheme), db: Session = Depends(get_db)):
    """
    ## Description

    Create a room to start a game.

    You need to provider a JSON data like here:


    ## Parameters
    * **:param** room_info: Requests Body of the information for creating a new room.
    * **:param** token: Token from the player.

    ## Requests Body

    ```json
    {
        "name": "string",
        "password": ""
    }
    ```

    ## Return
    **:return:** Creation Status.
    """
    master_uuid = token_tools.get_user_uuid_by_token(token=token)
    data_room = game_operation.generate_room_dict(room_info=room_info, master_uuid=master_uuid, db=db)

    if game_operation.check_room_master(player_uuid=master_uuid, room_list=room_list):

        raise HTTPException(
            status_code=400,
            detail="You have already owned a room. Creating multi rooms is refused."
        )

    try:
        room_list.append(data_room)

        return {
            'status': 'ok'
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Failed to create room: " + data_room['room_uuid']
                   + '\n' + str(e)
        )


@game_router.post('/rooms/join/{room_uuid}')
def join_room(room_uuid: str, token: str = Depends(oauth2Scheme)):
    """

    :param room_uuid:
    :param token:
    :return:
    """
    pass


@game_router.put('/rooms/quit/{room_uuid}')
def quit_room(room_uuid: str, token: str = Depends(oauth2Scheme)):
    """

    :param room_uuid:
    :param token:
    :return:
    """
    pass


@game_router.delete('/rooms/delete/{room_uuid}')
def delete_room(room_uuid: str, token: str = Depends(oauth2Scheme)):
    """

    :param room_uuid:
    :param token:
    :return:
    """
    pass


@game_router.get('/status/{room_uuid}')
def check_status(room_uuid: str, token: str = Depends(oauth2Scheme)):
    """
    ## Description

    Check the status of a player, which controls the actions of all players.

    ## Parameters

    * **:param** room_uuid: String. Uuid of the room.
    * **:param** token: String. Token of the player.

    ## Return

    * **:return:** Boolean data, tells the player if there's his/her turn.
    """

    pass
