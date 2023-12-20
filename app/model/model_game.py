# encoding: UTF-8
# filename: model_game.py
from typing import Literal, Self


class Player:
    def __init__(self, player_uuid: str, name: str):
        self.player_uuid = player_uuid
        self.name = name
        self.role: Role | None = None
        self.is_alive = True
        self.votes = 0

    def assign_role(self, role: str):
        self.role = role

    def voted(self, count: int = 1):
        self.votes += count

    def reset_votes(self):
        self.votes = 0


class Role:
    def __init__(self, name: Literal['girl', 'futa', 'femboy']):
        self.name = name

    def rape(self, player: Player):
        """
        Rape a player as femboy or futa.
        :param player:
        :return:
        """
        if self.name == 'futa' or self.name == 'femboy':
            if player.role.name == 'girl' or player.role.name == 'futa':
                player.is_alive = False
                return {
                    "player_uuid": player.player_uuid,
                    "identification": player.role.name
                }
            else:
                return False

    def check_skirt(self, player: Player):
        """
        Check a skirt of a player.
        :param player:
        :return:
        """

        if self.name == 'futa' or self.name == 'girl':
            return {
                    "player_uuid": player.player_uuid,
                    "identification": player.role.name
                }


class Room:
    def __init__(self, room_uuid: str, host_uuid: str, room_name: str, room_passwd: str, max_players: int):
        self.room_uuid = room_uuid
        self.room_name = room_name
        self.host_uuid = host_uuid
        self.room_passwd = room_passwd
        self.max_players = max_players
        self.status: Literal['waiting', 'playing'] = 'waiting'
        self.player_list: list[Player] = []

    def add_player(self, player: Player):
        if len(self.player_list) < self.max_players:
            self.player_list.append(player)

    def remove_player(self, player: Player):
        if player in self.player_list:
            self.player_list.remove(player)

    def verify_pass(self, password: str):
        if self.room_passwd != '':
            if self.room_passwd == password:
                return True
            else:
                return False
        else:
            return True
