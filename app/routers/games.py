from fastapi import APIRouter
from app.model import schemas

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

    list_for_return = []

    for item in room_list:

        temp_dict = {

        }

        list_for_return.append(temp_dict)


@game_router.post('/rooms/create')
def create_rooms(room_info: schemas.Room):
    """
    ## Description

    Create a room to start a game.

    You need to provider a JSON data like here:

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

    pass


@game_router.post('/rooms/join/{room_uuid}')
def join_room(room_uuid: str):
    pass


@game_router.put('/rooms/quit/{room_uuid}')
def quit_room():
    pass


@game_router.delete('/rooms/delete/{room_uuid}')
def delete_room(room_uuid: str):
    pass


@game_router.get('/status/{room_uuid}/{user_uuid}')
def check_status(room_uuid: str, user_uuid: str):
    """
    ## Description

    Check the status of a player, which controls the actions of all players.

    ## Parameters

    * **:param** room_uuid: String. Uuid of the room.
    * **:param** user_uuid: String. Uuid of the player.

    ## Return

    * **:return:** Boolean data, tells the player if there's his/her turn.
    """

    pass
