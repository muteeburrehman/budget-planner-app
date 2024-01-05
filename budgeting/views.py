# budgeting/views.py
import tkinter as tk
from budgeting.controllers import add_expense


class BudgetingForm(tk.Toplevel):
    def __init__(self, parent, budget_categories):
        super().__init__(parent)
        self.title("Budgeting Form")

        self.label_category = tk.Label(self, text="Category:")
        self.category_var = tk.StringVar()
        self.category_dropdown = tk.OptionMenu(self, self.category_var, *budget_categories)

        self.label_amount = tk.Label(self, text="Amount:")
        self.entry_amount = tk.Entry(self)

        self.button_add_expense = tk.Button(self, text="Add Expense", command=self.add_expense)

        self.label_category.pack()
        self.category_dropdown.pack()
        self.label_amount.pack()
        self.entry_amount.pack()
        self.button_add_expense.pack()

    def add_expense(self):
        category = self.category_var.get()
        amount = float(self.entry_amount.get())
        add_expense(category, amount)
        self.destroy()
