# settings/views.py
import tkinter as tk
from settings.controllers import save_settings

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")

        self.label_category = tk.Label(self, text="Categories:")
        self.entry_categories = tk.Entry(self)

        self.label_budget_limit = tk.Label(self, text="Budget Limit:")
        self.entry_budget_limit = tk.Entry(self)

        self.button_save_settings = tk.Button(self, text="Save Settings", command=self.save_settings)

        self.label_category.pack()
        self.entry_categories.pack()
        self.label_budget_limit.pack()
        self.entry_budget_limit.pack()
        self.button_save_settings.pack()

    def save_settings(self):
        categories = self.entry_categories.get()
        budget_limit = float(self.entry_budget_limit.get())
        save_settings(categories, budget_limit)
        self.destroy()
