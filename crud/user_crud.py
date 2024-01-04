# crud/user_crud.py
import sqlite3

def create_user(username, password):
    conn = sqlite3.connect('database/budget_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def read_user(username):
    conn = sqlite3.connect('database/budget_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data

def update_user_points(username, new_points):
    conn = sqlite3.connect('database/budget_database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET points = ? WHERE username = ?', (new_points, username))
    conn.commit()
    conn.close()

def delete_user(username):
    conn = sqlite3.connect('database/budget_database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    conn.close()
