import sys
import os

from PySide6.QtWidgets import QApplication


from settings import SETTINGS
from app.controllers.main_controller import MainController

if __name__ == "__main__":
    print("Starting application..._1")  # Debugging point
    app = QApplication(sys.argv)
    print("Starting application..._2")  # Debugging point
    
    # Opcjonalnie ustaw nazwę aplikacji
    app.setApplicationName(SETTINGS["app_name"])
    print("Starting application..._3")  # Debugging point

    # Ładowanie stylu (QSS)
    with open(SETTINGS["theme"], "r") as file:
        app.setStyleSheet(file.read())
    print("Starting application..._4")  # Debugging point


    # Start aplikacji
    controller = MainController()
    controller.run()
    print("Starting application..._5")  # Debugging point

    sys.exit(app.exec())
