import sys 
from app.views.custom_main_window import CustomMainWindow
from PySide6.QtWidgets import QApplication
from ..utilities.themes_controller import ThemeController

class MainController:
    def __init__(self):
        self.ui = CustomMainWindow()

        # Stwórz kontroler dla stylów
        self.theme_controller = ThemeController(self.ui, default_stylesheet="domyślny")

    def show_main_window(self):
        self.ui.show() 
