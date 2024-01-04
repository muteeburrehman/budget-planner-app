# dashboard/controllers.py
from authentication.controllers import users

def load_user_dashboard(dashboard, user):
    # Customize this function to load user-specific data into the dashboard
    # For example, you can display user points, achievements, or other relevant information
    user_data = next((u for u in users if u.username == user.username), None)
    if user_data:
        # Load and display user data in the dashboard
        # Example: dashboard.label_points.config(text=f"Points: {user_data.points}")
        pass
    else:
        print("User not found.")
