import logging
from models import User
from flask import jsonify
from tasks import user_task

logger = logging.getLogger("default")


class UserService(object):
    """
    service function for user related business logic
    """

    @staticmethod
    def login_user(data):
        """
        TASKS: write the logic here for user login
               authenticate user credentials as per your
               schema and return the identifier user.

               raise appropriate errors wherever necessary
        """
        if data:
            username = data.get('username')
            password = data.get('password')
            if username and password:
                user = User.objects(username=username).first()
                if user is not None and user.verify_password(password):
                    logger.info(f"'{user.id}' is authenticated")
                    user_task.lastlogin.delay(user.id)
                    return jsonify({
                        "message": f"'{user.id}' is authenticated",
                    }), 200
                return jsonify({
                    "messaget": "Invalid username or password!"
                }), 401
            return jsonify({
                "messaget": "Empty username or password!"
            }), 400
        return jsonify({
            "message": "No JSON data found in the request!"
        }), 400



    @staticmethod
    def register_user(data):
        """
        TASKS: write the logic here for registering new user.

               raise appropriate errors wherever necessary
        """
        if data:
            username = data.get('username')
            password = data.get('password')
            if username and password:
                user = User.objects(username=username).first()
                if user is None:
                    user = User(username)
                    user.password = password
                    user.save()
                    logger.info(f"Registering new user '{user.id}'")
                    return jsonify({
                        "message": f"'{user.id}' is registered",
                    }), 201
                return jsonify({
                    "message": f"'{username}' already exists!"
                }), 400
            return jsonify({
                "message": f"Empty username or password!"
            }), 400
        return jsonify({
            "message": "No JSON data found in the request!"
        }), 400
