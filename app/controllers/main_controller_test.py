# app\controllers\main_controller_test.py
from app.views.main_window_qf import CustomFramelessWindow

class Controller:
    def __init__(self):
        self.window = None

    def show_main_window(self):
        # Tworzenie instancji frameless window
        self.window = CustomFramelessWindow()
        self.window.resize(800, 600)
        self.window.show()


 # Obsługa przycisku zamknij
        self.window.btn_zamknij.clicked.connect(self.close)