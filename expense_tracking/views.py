# expense_tracking/views.py
import tkinter as tk
from expense_tracking.controllers import log_daily_expense

class ExpenseTrackingForm(tk.Toplevel):
    def __init__(self, parent, expense_categories):
        super().__init__(parent)
        self.title("Expense Tracking Form")

        self.label_category = tk.Label(self, text="Category:")
        self.category_var = tk.StringVar()
        self.category_dropdown = tk.OptionMenu(self, self.category_var, *expense_categories)

        self.label_amount = tk.Label(self, text="Amount:")
        self.entry_amount = tk.Entry(self)

        self.button_log_expense = tk.Button(self, text="Log Expense", command=self.log_expense)

        self.label_category.pack()
        self.category_dropdown.pack()
        self.label_amount.pack()
        self.entry_amount.pack()
        self.button_log_expense.pack()

    def log_expense(self):
        category = self.category_var.get()
        amount = float(self.entry_amount.get())
        log_daily_expense(category, amount)
        self.destroy()
