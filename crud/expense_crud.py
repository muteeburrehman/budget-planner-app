# crud/expense_crud.py
import sqlite3

def create_expense(user_id, category, amount):
    conn = sqlite3.connect('database/budget_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (user_id, category, amount) VALUES (?, ?, ?)', (user_id, category, amount))
    conn.commit()
    conn.close()

def read_expenses(user_id):
    conn = sqlite3.connect('database/budget_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses WHERE user_id = ?', (user_id,))
    expenses = cursor.fetchall()
    conn.close()
    return expenses

# Add update and delete functions as needed
