import sqlite3


def create_user(username, password):
    with sqlite3.connect('database/budget_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                points INTEGER DEFAULT 0
            )
        ''')
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()


def read_user(username, password):
    with sqlite3.connect('database/budget_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND  password = ?', (username, password))
        user_data = cursor.fetchone()
    return user_data


def update_user_points(username, new_points):
    with sqlite3.connect('database/budget_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET points = ? WHERE username = ?', (new_points, username))
        conn.commit()


def delete_user(username):
    with sqlite3.connect('database/budget_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE username = ?', (username,))
        conn.commit()
