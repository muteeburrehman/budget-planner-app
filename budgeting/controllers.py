# budgeting/controllers.py
from budgeting.models import BudgetCategory, Expense

budget_categories = [BudgetCategory("Groceries", 200), BudgetCategory("Entertainment", 100)]

def add_expense(category, amount):
    for budget_category in budget_categories:
        if budget_category.name == category:
            expense = Expense(category, amount)
            budget_category.expenses.append(expense)
            print(f"Expense added to {category} category: ${amount}")
            break
