# app/views/login.py
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("app/ui/login.ui", self)
