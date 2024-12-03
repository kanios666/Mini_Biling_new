# app\views\main_window_qf.py
from PySide6.QtWidgets import QMainWindow  # Importuj QMainWindow
from PySide6.QtCore import Qt
from app.views.main_window import Ui_MainWindow  # Import wygenerowanego UI

class CustomFramelessWindow(QMainWindow):  # Zmiana na QMainWindow
    def __init__(self):
        super().__init__()
        
        # Załaduj UI z wygenerowanego pliku
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Inicjalizuj UI bezpośrednio w oknie głównym
        
        # Opcjonalne dostosowanie, np. wyłączenie ramki
        self.setWindowFlag(Qt.FramelessWindowHint)  # Usunięcie ramki okna
