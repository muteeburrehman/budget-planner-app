# budgeting/models.py
class BudgetCategory:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.expenses = []


class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
