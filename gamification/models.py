# gamification/models.py
class Player:
    def __init__(self, username, points=0, achievements=[]):
        self.username = username
        self.points = points
        self.achievements = achievements

class Achievement:
    def __init__(self, name, description, points_required):
        self.name = name
        self.description = description
        self.points_required = points_required
