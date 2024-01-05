# dashboard/views.py
import tkinter as tk
from dashboard.controllers import load_user_dashboard

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Budget Planner Dashboard")

        self.label_welcome = tk.Label(self, text=f"Welcome, abrar!")
        self.label_budget_overview = tk.Label(self, text="Budget Overview:")
        # Add more dashboard components as needed

        # load_user_dashboard(self)  # Load user-specific dashboard data

        self.label_welcome.pack()
        self.label_budget_overview.pack()
        # Pack additional components here
