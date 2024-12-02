# app\views\main_window_qf.py
from PySide6.QtWidgets import QMainWindow  # Importuj QMainWindow
from PySide6.QtCore import Qt
from app.views.main_window import Ui_MainWindow  # Import wygenerowanego UI
from app.controllers.qframelesswindow import FramelessWindow


class CustomFramelessWindow(FramelessWindow, Ui_MainWindow):  # Dziedziczenie z FramelessWindow
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Inicjalizacja UI