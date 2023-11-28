# encoding: utf-8
# filename: db.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import toml

configuration = toml.load('app/config.toml')

# Url of the database, read from the configuration file.
DATABASE_URL = 'mysql://' \
               + configuration['database']['user_name'] + ":" \
               + configuration['database']['password'] + '@' \
               + configuration['database']['address'] + '/' \
               + configuration['database']['db_name']


# Create ORM engine.
engine = create_engine(DATABASE_URL)

# Create the Local Session class.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the father class `Base` for creating object models.
Base = declarative_base()


# Create a function to create a session to database for using `Depends()`.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

