# dashboard/views.py
import tkinter as tk
from dashboard.controllers import load_user_dashboard

class Dashboard(tk.Tk):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.title("Budget Planner Dashboard")

        self.label_welcome = tk.Label(self, text=f"Welcome, {user.username}!")
        self.label_budget_overview = tk.Label(self, text="Budget Overview:")
        # Add more dashboard components as needed

        load_user_dashboard(self, user)  # Load user-specific dashboard data

        self.label_welcome.pack()
        self.label_budget_overview.pack()
        # Pack additional components here
