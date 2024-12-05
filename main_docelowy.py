# main_docelowy.py
from PySide6.QtWidgets import QApplication
from app.controllers.main_controller_test import MainController

if __name__ == "__main__":
    app = QApplication([])
    controller = MainController()
    controller.show_main_window()
    app.exec()
