from sqlalchemy import Column, INT, VARCHAR, CHAR, TEXT, DATETIME, JSON
from app.dependencies.db import Base


class Users(Base):
    __tablename__ = 'player_users'
    id = Column(INT, primary_key=True, index=True, autoincrement=True, comment='Index Key')
    user_uuid = Column(CHAR(36), unique=True, nullable=False, comment='UUID of this user. Unchangeable.')
    user_name = Column(VARCHAR(36), unique=True, nullable=False, comment='Name of this user to login. Unchangeable.')
    nick_name = Column(VARCHAR(36), nullable=False, comment='Name of this user to display. Changeable.')
    password = Column(TEXT, nullable=False, comment='Password')
    win = Column(INT, default=0, nullable=False, comment='Times of winning a game.')
    fail = Column(INT, default=0, nullable=False, comment='Times of failing a game.')
    raped = Column(INT, default=0, nullable=False, comment='Numbers of raping a girl as a femboy or futa.')
    being_raped = Column(INT, default=0, nullable=False, comment='Times of being raped as a girl by a futa or femboy.')
    email = Column(VARCHAR(64), unique=True, nullable=False, comment='Email Address of this user.')
    date = Column(DATETIME, nullable=False, comment='The date and time of this user to register an account.')


class GameResult(Base):
    __tablename__ = 'game_result'
    id = Column(INT, primary_key=True, index=True, autoincrement=True, comment="Index Key")
    game_uuid = Column(CHAR(36), unique=True, nullable=False, comment="UUID of this game. Unchangeable.")
    winner_roles = Column(VARCHAR(6), nullable=False, comment="The winner of this game, girls, femboy or futa")
    players = Column(JSON, nullable=False)
    start_time = Column(DATETIME, nullable=False)
    end_time = Column(DATETIME, nullable=False)
