# app\views\custom_main_window.py
# custom_main_window.py
from PySide6.QtWidgets import QWidget, QVBoxLayout
from qframelesswindow import FramelessWindow
from .main_window import Ui_MainWindow

class CustomMainWindow(FramelessWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        # Tworzymy główny widget
        self.central_widget = QWidget(self)
        layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)  # Ustawiamy centralny widget

        # Dodajemy główny widget z wygenerowanego pliku .py
        layout.addWidget(self.styl)
