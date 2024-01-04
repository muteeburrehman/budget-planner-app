# authentication/models.py

class User:
    def __init__(self, username, password, points=0, achievements=[]):
        self.username = username
        self.password = password
        self.points = points
        self.achievements = achievements
