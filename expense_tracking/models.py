# expense_tracking/models.py
class ExpenseTracker:
    def __init__(self):
        self.daily_expenses = []

class DailyExpense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
