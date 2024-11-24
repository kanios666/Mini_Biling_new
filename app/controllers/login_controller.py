# app/controllers/login_controller.py
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget
from app.views.login_window import Ui_LoginWindow

#import bcrypt

class LoginController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        
# Pozostałe ustawienia
        
"""    self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setPlaceholderText("Username")
        self.layout.addWidget(self.lineEdit_username)

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setPlaceholderText("Password")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.lineEdit_password)

        self.pushButton_login = QPushButton("Login", self)
        self.pushButton_login.clicked.connect(self.handle_login)
        self.layout.addWidget(self.pushButton_login)
        
  
        # Ładuj teksty z pliku JSON
        self.texts = self.load_texts("texts.json")
        self.current_text_index = 0
        
        # Timer do zmiany tekstu co 20 sekund
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_text)
        self.timer.start(20000)  # 20 sekund
        
        # Obsługa przycisków strzałek
        self.ui.pushButton_up.clicked.connect(self.change_text_up)
        self.ui.pushButton_down.clicked.connect(self.change_text_down)


    def handle_login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        
        
    def load_texts(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding='utf-8') as file:
                data = json.load(file)
                return data.get("texts", [])
        return []

    def change_text_down(self):
        self.current_text_index = (self.current_text_index + 1) % len(self.texts)
        self.ui.label_text.setText(self.texts[self.current_text_index])

    def change_text_up(self):
        self.current_text_index = (self.current_text_index - 1) % len(self.texts)
        self.ui.label_text.setText(self.texts[self.current_text_index])
        
    def open_main_window(self):
        self.main_window = MainController(settings)
        self.main_window.show()
        self.close()
 """



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

