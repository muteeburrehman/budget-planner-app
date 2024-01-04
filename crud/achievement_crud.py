# crud/achievement_crud.py
import sqlite3

def create_achievement(username, achievement_name, achievement_description, points_required):
    conn = sqlite3.connect('database/budget_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO achievements (username, name, description, points_required) VALUES (?, ?, ?, ?)',
                   (username, achievement_name, achievement_description, points_required))
    conn.commit()
    conn.close()

def read_user_achievements(username):
    conn = sqlite3.connect('database/budget_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM achievements WHERE username = ?', (username,))
    user_achievements = cursor.fetchall()
    conn.close()
    return user_achievements

# Add update and delete functions as needed
