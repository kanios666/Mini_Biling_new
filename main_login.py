#main.py
import sys
from PySide6.QtWidgets import QApplication
from controllers.login_controller import LoginController

if __name__ == "__main__":
    app = QApplication([])
    controller = LoginController()
    controller.show_main_window()
    sys.exit(app.exec())




