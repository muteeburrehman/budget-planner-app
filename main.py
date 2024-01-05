import tkinter as tk
from tkinter import messagebox
from authentication.views import RegistrationForm, LoginForm
from crud.user_crud import read_user
from dashboard.views import Dashboard
from budgeting.views import BudgetingForm
from expense_tracking.views import ExpenseTrackingForm
from gamification.views import GamificationDashboard
from notifications.views import NotificationWindow
from reports_analytics.views import AnalyticsDashboard
from settings.views import SettingsWindow


class BudgetPlannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Budget Planner App")
        self.login_form = LoginForm(self, self.handle_login, self.show_registration_form, self)

        # Create and configure menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.destroy)

        # Initialize other modules (not showing by default)
        # self.dashboard = Dashboard()
        # self.budgeting_form = BudgetingForm(self, ["Groceries", "Entertainment"])
        # self.expense_tracking_form = ExpenseTrackingForm(self, ["Groceries", "Entertainment"])
        # self.gamification_dashboard = GamificationDashboard()
        # self.notification_window = NotificationWindow(self, "Test Notification")
        # self.analytics_dashboard = AnalyticsDashboard(self)
        # self.settings_window = SettingsWindow(self)

    def handle_login(self):
        username = self.login_form.entry_username.get()
        password = self.login_form.entry_password.get()
        user_data = read_user(username, password)

        if user_data is not None:
            self.login_form.destroy()

        else:
            messagebox.showinfo("Warning!", f"User Note Found!!! Please Register First!")
            self.show_registration_form()

    def show_registration_form(self):
        self.register_form = RegistrationForm()
        self.register_form.protocol("WM_DELETE_WINDOW", self.handle_registration_closed)

    def handle_registration_closed(self):
        print("Registration form closed.")
        self.register_form.destroy()

        if not self.login_form.winfo_exists():
            self.destroy()


if __name__ == "__main__":
    app = BudgetPlannerApp()
    app.mainloop()
