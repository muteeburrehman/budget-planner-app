# gamification/views.py
import tkinter as tk
from gamification.controllers import show_player_stats


class GamificationDashboard(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Gamification Dashboard")

        self.label_username = tk.Label(self, text=f"Player: Player")
        self.label_points = tk.Label(self, text=f"Points: Points")
        self.button_show_stats = tk.Button(self, text="Show Player Stats", command=self.show_stats)

        self.label_username.pack()
        self.label_points.pack()
        self.button_show_stats.pack()

    def show_stats(self):
        show_player_stats(self)
