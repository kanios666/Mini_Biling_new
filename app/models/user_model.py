from models.db_manager import DatabaseManager

class UserModel:
    def __init__(self, db_path):
        self.db = DatabaseManager(db_path)

    def get_user_by_username(self, username):
        """Pobierz dane użytkownika na podstawie nazwy użytkownika."""
        query = "SELECT * FROM users WHERE username = ?"
        result = self.db.execute_query(query, (username,))
        return result.fetchone()

    def create_user(self, username, password_hash):
        """Dodaj nowego użytkownika do bazy danych."""
        query = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        self.db.execute_query(query, (username, password_hash))

    def update_password(self, username, new_password_hash):
        """Zaktualizuj hasło użytkownika."""
        query = "UPDATE users SET password_hash = ? WHERE username = ?"
        self.db.execute_query(query, (new_password_hash, username))
