import tkinter as tk
from authentication.views import RegistrationForm, LoginForm
from dashboard.views import Dashboard
from budgeting.views import BudgetingForm
from expense_tracking.views import ExpenseTrackingForm
from gamification.views import GamificationDashboard
from notifications.views import NotificationWindow
from reports_analytics.views import AnalyticsDashboard
from settings.views import SettingsWindow

# Create a simple class to represent the main application
class BudgetPlannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Budget Planner App")

        # Placeholder user for testing (replace this with your authentication logic)
        self.current_user = None

        # Create and configure menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.destroy)

        # Create and configure main dashboard
        self.dashboard = Dashboard(self, self.current_user)

        # Create and configure other modules
        self.budgeting_form = BudgetingForm(self, ["Groceries", "Entertainment"])
        self.expense_tracking_form = ExpenseTrackingForm(self, ["Groceries", "Entertainment"])
        self.gamification_dashboard = GamificationDashboard(self, self.current_user)
        self.notification_window = NotificationWindow(self, "Test Notification")
        self.analytics_dashboard = AnalyticsDashboard(self)
        self.settings_window = SettingsWindow(self)

if __name__ == "__main__":
    app = BudgetPlannerApp()
    app.mainloop()
