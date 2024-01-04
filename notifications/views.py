# notifications/views.py
import tkinter as tk
from notifications.controllers import show_notification

class NotificationWindow(tk.Toplevel):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.title("Notification")

        self.label_message = tk.Label(self, text=message)
        self.button_close = tk.Button(self, text="Close", command=self.destroy)

        self.label_message.pack()
        self.button_close.pack()

        # Optionally, call a function to handle the notification (e.g., mark as read)
        show_notification(message)
