import sys
import os

from app.controllers.json_settings import Settings # Import Settings 

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from app.controllers.main_controller import MainController

os.environ["QT_FONT_DPI"] = "96"
class MainWindow(MainController):
    def __init__(self):
        super().__init__()

        # Załaduj Settings
        settings = Settings()
        self.settings = settings.items
        
        
        # Ustaw główne okno
        self.hide_grips = True # Show/Hide resize grips

        self.show()   
        
# Inicjalizacja okna 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
