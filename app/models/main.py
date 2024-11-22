import sqlite3

class UserModel:
    @staticmethod
    def authenticate(username, password):
        conn = sqlite3.connect('database/app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user
