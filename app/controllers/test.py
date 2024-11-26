# app/controllers/test.py
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from app.themes.themes import Themes
from app.views.test import Ui_MainWindow
from app.controllers.qframelesswindow import FramelessWindow


class TestController(FramelessWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Wywołuje konstruktor WindowsFramelessWindowBase
        self.ui = Ui_MainWindow()
        self.setupUi(self)  # Ustawia interfejs użytkownika z Ui_LoginWindow



        
        


        # Dodanie dostępnych motywów do QComboBox
        available_themes = Themes.get_available_themes()
        self.ui.CB.addItems(available_themes)
        
        # Połączenie sygnału currentIndexChanged z funkcją load_theme
        sself.ui.CB.addItems.currentIndexChanged.connect(self.load_theme)

    def load_theme(self):
        theme_name = self.CB.currentText()
        self.themes = Themes(theme_name)
        self.apply_theme()

    def apply_theme(self):
        # Załaduj plik .qss i zastosuj styl do aplikacji
        qss = self.themes.load_qss()
        self.setStyleSheet(qss)

