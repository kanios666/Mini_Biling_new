# app/views/main_window_qf.py
from PySide6.QtWidgets import QMainWindow  # Importuj QMainWindow
from PySide6.QtCore import Qt
from app.views.main_window import Ui_MainWindow  # Import wygenerowanego UI
#from app.controllers.qframelesswindow import FramelessWindow
from qframelesswindow import FramelessWindow

class CustomFramelessWindow(FramelessWindow,  Ui_MainWindow):  # Dziedziczenie z FramelessWindow i QMainWindow
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Inicjalizacja UI
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
#        MainWindow.setCentralWidget(self.styl)
