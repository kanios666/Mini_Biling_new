import json
import random
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from app.views.login_window import Ui_LoginWindow
from app.controllers.qframelesswindow import FramelessDialog


class LoginController(FramelessDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        
    
        # Pozostałe ustawienia
        #////////////////////////////////////////
        
        # Usuń obramowanie okna 
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        
        # Obsługa txt logowania
        self.ui.login.setFocus()
        self.setTabOrder(self.ui.login, self.ui.password) 
        
        # Obsługa przycisku zamknij
        self.ui.btn_close.clicked.connect(self.close)
        
        # Wczytaj sentencje z pliku JSON
        self.sentencje_login = self.load_sentencje()

        # Losowanie tekstu i ustawienie go w lbl_l_dol
        losowany_tekst = random.choice(self.sentencje_login)
        self.ui.lbl_l_dol.setText(f'"{losowany_tekst}"')

    def load_sentencje(self):
        # Dynamiczne określenie ścieżki do pliku JSON
        app_path = os.path.abspath(os.getcwd())
        file_path = os.path.normpath(os.path.join(app_path, "app/resources/sentencje.json"))
               
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("texts", [])



        # Hashowanie hasła
"""         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Weryfikacja hasła
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        self.open_main_window()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")


if __name__ == "__main__":
    app = QApplication([])
    window = Ui_LoginWindow()
    window.show()
    app.exec()
"""







""" 
from app.models.user_model import UserModel

class LoginController:
    def __init__(self, view):
        self.view = view

    def login(self, username, password):
        if UserModel.authenticate(username, password):
            print("Login successful")
            return True
        else:
            print("Invalid credentials")
            return False

    def change_password(self, username, new_password):
        UserModel.change_password(username, new_password)
        print("Password changed successfully")
 """

