#main.py
import sys
from PySide6.QtWidgets import QApplication
from app.controllers.main_controller import MainController

if __name__ == "__main__":
    app = QApplication([])
    controller = MainController()
    controller.show_main_window()
    sys.exit(app.exec())
