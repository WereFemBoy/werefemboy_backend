# encoding: utf-8
# filename: user_tools.py

from pathlib import Path
import toml

configuration: dict = toml.load('app/config.toml')
static_directory: str = configuration['static']['static_directory']


def create_user_directory(user_uuid: str) -> bool:
    """
    Create a directory for the new user.
    :type user_uuid: String, UUID of the user.
    :return: Status of the operation.
    """

    user_directory = Path(static_directory).joinpath(user_uuid)

    try:
        user_directory.mkdir(exist_ok=True)

        return True

    except IOError:

        return False
