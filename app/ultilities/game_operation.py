# encoding: utf-8
# filename: game_operation.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.model import schemas
from uuid import uuid4
from app.dependencies.crud import get_user_by_uuid


def generate_room_dict(room_info: schemas.Room, master_uuid: str, db: Session) -> dict:
    """
    Generate dict data of a room with a `master_uuid` from a player.
    :param db:
    :param room_info:
    :param master_uuid:
    :return:
    """
    room_uuid: str = str(uuid4())

    room_for_return = {
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


def check_room_master(player_uuid: str, room_list: list[dict]):
    """
    Check if a user has already owned a room.
    :param room_list: List of all rooms.
    :param player_uuid: UUID of the user.
    :return:
    """

    for room in room_list:
        if room['master_uuid'] == player_uuid:

            return True

    return False


def check_room_member(player_uuid: str, room_lost: list[dict], room_uuid: str):
    """

    :param room_uuid: UUID of the room.
    :param player_uuid: UUID of the user.
    :param room_lost: List of all rooms.
    :return:
    """


