import logging
from flask import request
from services import UserService

logger = logging.getLogger("default")


def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"


def login():
    """
    TASKS: write the logic here to parse a json request
           and send the parsed parameters to the appropriate service.
    """
    data = request.get_json(silent=True)
    logger.info(f"Checking Login user")
    return UserService.login_user(data)


def register():
    """
    TASKS: write the logic here to parse a json request
           and send the parsed parameters to the appropriate service.
    """
    data = request.get_json(silent=True)
    logger.info(f"Checking Register user")
    return UserService.register_user(data)
