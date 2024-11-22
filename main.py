import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from app.controllers.main_controller import MainController
from settings import SETTINGS

class MainWindow(MainController):
    def __init__(self):
        super().__init__()
        self.apply_settings()

    def apply_settings(self):
        self.setWindowTitle(SETTINGS["app_name"])
        self.resize(*SETTINGS["window_size"])
        if SETTINGS["borderless"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
        # Możesz dodać więcej ustawień tutaj

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
