# app\controllers\main_controller_test.py
from app.views.main_window_qf import CustomFramelessWindow

class Controller:
    def __init__(self):
        self.window = None

    def show_main_window(self):
        self.window = CustomFramelessWindow()
        self.window.btn_zamknij.clicked.connect(self.close_main_window)  # Połącz przycisk z funkcją
        self.window.show()

    def close_main_window(self):
        self.window.close()
