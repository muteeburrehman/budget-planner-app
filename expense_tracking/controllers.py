# expense_tracking/controllers.py
from expense_tracking.models import ExpenseTracker, DailyExpense

expense_tracker = ExpenseTracker()

def log_daily_expense(category, amount):
    daily_expense = DailyExpense(category, amount)
    expense_tracker.daily_expenses.append(daily_expense)
    print(f"Expense logged for {category} category: ${amount}")
