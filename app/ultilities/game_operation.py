# encoding: utf-8
# filename: game_operation.py

from sqlalchemy.orm import Session
from app.model import schemas
from uuid import uuid4
from app.dependencies.crud import get_user_by_uuid


def generate_room_dict(room_info: schemas.Room, master_uuid: str, db: Session):
    """
    Generate dict data of a room with a `master_uuid` from a player.
    :param db:
    :param room_info:
    :param master_uuid:
    :return:
    """
    room_uuid: str = str(uuid4())

    room_for_return: dict = {
        "room_uuid": room_uuid,
        "master_uuid": master_uuid,
        "name": room_info.name,
        "password": room_info.password,
        "player_list": []
    }

    master_as_player = generate_player_dict(player_uuid=master_uuid, db=db)
    room_for_return['player_list'].append(master_as_player)

    return room_for_return


def generate_player_dict(player_uuid: str, db: Session):
    """
    Generate the dict data for a user.
    :param player_uuid:
    :param db: Session
    :return:
    """
    user = get_user_by_uuid(user_uuid=player_uuid, db=db)

    player_data = {
        "player_uuid": player_uuid,
        "name": user.nick_name,
        "ready": False
    }

    return player_data


def check_room_master(room_uuid: str, player_uuid: str, room_list: list[dict[str, str | list[dict[str, str]]]]):
    """
    Check if a user has already owned a room.
    :param room_uuid: UUID of the room.
    :param room_list: List of all rooms.
    :param player_uuid: UUID of the user.
    :return: Status of the operation.
    """

    for room in room_list:
        if room['room_uuid'] == room_uuid:
            if room['master_uuid'] == player_uuid:
                return True

    return False


def check_room_member(room_uuid: str | None, player_uuid: str, room_list: list[dict[str, str | list[dict[str, str]]]]):
    """
    Check if a user has already in a room.
    :param room_uuid:
    :param player_uuid: UUID of the user.
    :param room_list: List of all rooms.
    :return: Status of the operation.
    """

    for room in room_list:
        if room['room_uuid'] == room_uuid and room_uuid is not None:
            for player in room['player_list']:
                if player_uuid == player['player_uuid']:
                    return True
        else:
            for player in room['player_list']:
                if player_uuid == player['player_uuid']:
                    return True
    return False
