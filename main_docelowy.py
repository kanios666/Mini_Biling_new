from PySide6.QtWidgets import QApplication
from app.controllers.main_controller_test import Controller

if __name__ == "__main__":
    app = QApplication([])
    controller = Controller()
    controller.show_main_window()
    app.exec()
