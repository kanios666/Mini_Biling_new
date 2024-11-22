# models/database.py

import sqlite3
from cryptography.fernet import Fernet
import os

class Database:
    def __init__(self, db_path, key_path):
        self.db_path = 'database/app.db'
        self.key_path = key_path
        self.connection = None
        self.cursor = None

    def connect(self):
        """Tworzymy połączenie z bazą danych"""
        key = self._load_key()
        password = self._decrypt_password(key)
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def _load_key(self):
        """Załaduj klucz szyfrowania z pliku"""
        with open(self.key_path, 'rb') as f:
            return f.read()

    def _decrypt_password(self, key):
        """Odszyfruj hasło z pliku encrypted_password.key"""
        cipher = Fernet(key)
        with open('encrypted_password.key', 'rb') as f:
            encrypted_password = f.read()
        return cipher.decrypt(encrypted_password).decode()

    def execute_query(self, query, params=None):
        """Wykonaj zapytanie SQL"""
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self):
        """Pobierz wszystkie wyniki zapytania"""
        return self.cursor.fetchall()

    def close(self):
        """Zamknij połączenie z bazą"""
        if self.connection:
            self.connection.close()
