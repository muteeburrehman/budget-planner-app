# authentication/controllers.py
from authentication.models import User

users = []  # In-memory user database for simplicity


def register_user(username, password):
    new_user = User(username, password)
    users.append(new_user)


def authenticate_user(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False
