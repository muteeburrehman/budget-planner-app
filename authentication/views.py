import tkinter as tk
from tkinter import messagebox
from crud.user_crud import create_user, read_user


class RegistrationForm(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("User Registration")

        self.minsize(300, 250)
        self.maxsize(300, 250)

        self.label_username = tk.Label(self, text="Username:")
        self.entry_username = tk.Entry(self)

        self.label_password = tk.Label(self, text="Password:")
        self.entry_password = tk.Entry(self, show="*")

        self.button_register = tk.Button(self, text="Register", command=self.register_user)

        # Add padding between widgets
        pad_y = 5
        self.label_username.pack(pady=pad_y)
        self.entry_username.pack(pady=pad_y)
        self.label_password.pack(pady=pad_y)
        self.entry_password.pack(pady=pad_y)
        self.button_register.pack(pady=pad_y)

    def register_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Check if the user already exists
        existing_user = read_user(username, password)
        if existing_user:
            messagebox.showinfo("User Exists", f"The user '{username}' already exists.")
        else:
            create_user(username, password)
            print('User registered: name -', username, ' password -', password)
            self.destroy()


class LoginForm(tk.Toplevel):
    def __init__(self, parent, handle_login, show_registration_form, main_app):
        super().__init__(parent)
        self.title("User Login")

        self.minsize(300, 250)
        self.maxsize(300, 250)

        self.label_username = tk.Label(self, text="Username:")
        self.entry_username = tk.Entry(self)

        self.label_password = tk.Label(self, text="Password:")
        self.entry_password = tk.Entry(self, show="*")

        self.button_login = tk.Button(self, text="Login", command=self.authenticate_user)
        self.button_register = tk.Button(self, text="Register", command=show_registration_form)

        # Add padding between widgets
        pad_y = 5
        self.label_username.pack(pady=pad_y)
        self.entry_username.pack(pady=pad_y)
        self.label_password.pack(pady=pad_y)
        self.entry_password.pack(pady=pad_y)
        self.button_login.pack(pady=pad_y)
        self.button_register.pack(pady=pad_y)

        # Align buttons in x-axis
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.BOTTOM, padx=pad_y)
        self.button_login.pack(side=tk.LEFT, padx=10)
        self.button_register.pack(side=tk.RIGHT, padx=10)

        self.handle_login = handle_login
        self.protocol("WM_DELETE_WINDOW", self.handle_window_closed)
        self.main_app = main_app

    def handle_window_closed(self):
        self.main_app.destroy()

    def authenticate_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.handle_login()
        user_data = read_user(username, password)

        if user_data is not None:
            print("Login successful")
        else:
            print("Login failed")