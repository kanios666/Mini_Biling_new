""" import sys
from PySide6.QtWidgets import QApplication
from app.controllers.login_controller import LoginController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginController()  # Logowanie z efektami
    window.show()
    sys.exit(app.exec())

 """

# test głównego okna
import sys
import os

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from app.controllers.main_controller import MainController

class MainWindow(MainController):
    def __init__(self):
        super().__init__()

# Inicjalizacja okna 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
