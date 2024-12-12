#main.py
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from app.controllers.main_controller import MainController

if __name__ == "__main__":
    app = QApplication([]) 
    # Unikaj problemów z natywnymi widgetami
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

    controller = MainController()
    controller.show_main_window()
    sys.exit(app.exec())



