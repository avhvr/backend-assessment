from mongoengine import Document, StringField, DateTimeField
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(Document):
    """
    TASK: Create a model for user with minimalistic
          information required for user authentication

    HINT: Do not store password as is.
    """
    username = StringField(required=True, primary_key=True)
    password_hash = StringField(required=True)

    @property
    def password(self, password):
        raise AttributeError("password: not readable")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
