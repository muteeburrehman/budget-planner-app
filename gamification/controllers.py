# gamification/controllers.py
from gamification.models import Player, Achievement

players = []  # In-memory player database for simplicity

def initialize_player(username):
    player = Player(username)
    players.append(player)
    return player

def earn_points(player, amount):
    player.points += amount

def unlock_achievement(player, achievement):
    player.achievements.append(achievement)
    print(f"Achievement unlocked: {achievement.name}")

def show_player_stats(dashboard):
    # Customize this function to display additional player statistics in the dashboard
    player = players[0]  # For simplicity, assuming there is only one player
    dashboard.label_points.config(text=f"Points: {player.points}")
    print(f"Player stats displayed for {player.username}")
