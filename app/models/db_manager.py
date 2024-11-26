import sqlite3
from sqlite3 import Error

class DatabaseManager:
    def __init__(self, db_path):
        """Inicjalizacja połączenia z bazą danych."""
        self.db_path = db_path

    def connect(self):
        """Nawiązanie połączenia z bazą danych."""
        try:
            return sqlite3.connect(self.db_path)
        except Error as e:
            print(f"Błąd połączenia z bazą danych: {e}")
            return None

    def execute_query(self, query, params=()):
        """Wykonanie zapytania SQL."""
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
                return cursor
            except Error as e:
                print(f"Błąd podczas wykonania zapytania: {e}")
            finally:
                connection.close()
