# authentication/views.py
import tkinter as tk
from authentication.controllers import register_user, authenticate_user

class RegistrationForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("User Registration")

        self.label_username = tk.Label(self, text="Username:")
        self.entry_username = tk.Entry(self)

        self.label_password = tk.Label(self, text="Password:")
        self.entry_password = tk.Entry(self, show="*")

        self.button_register = tk.Button(self, text="Register", command=self.register_user)

        self.label_username.pack()
        self.entry_username.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.button_register.pack()

    def register_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        register_user(username, password)
        self.destroy()


class LoginForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("User Login")

        self.label_username = tk.Label(self, text="Username:")
        self.entry_username = tk.Entry(self)

        self.label_password = tk.Label(self, text="Password:")
        self.entry_password = tk.Entry(self, show="*")

        self.button_login = tk.Button(self, text="Login", command=self.authenticate_user)

        self.label_username.pack()
        self.entry_username.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.button_login.pack()

    def authenticate_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if authenticate_user(username, password):
            print("Login successful")
        else:
            print("Login failed")
