# app\controllers\main_controller_test.py
from app.views.custom_main_window import CustomMainWindow

class MainController:
    def __init__(self):
        self.main_window = CustomMainWindow()

    def show_main_window(self):
        self.main_window.show()