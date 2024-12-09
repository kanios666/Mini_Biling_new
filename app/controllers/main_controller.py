# app/controllers/main_controller.py

from app.views.custom_main_window import CustomMainWindow
class MainController:
    def __init__(self):
        self.ui = CustomMainWindow()

    def show_main_window(self):
        self.ui.show() 

""" 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from app.views.main_window import Ui_MainWindow
class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # Bez obramowania
        self.setAttribute(Qt.WA_TranslucentBackground)  # Przezroczyste tło

 """
""" from PySide6.QtWidgets import QMainWindow
from app.views.main_window_c import Ui_MainWindow
from app.utilities.config_loader_json import Settings # Import Settings 

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 """
# Pozostałe ustawienia  
        
        
"""         self.ui.apply_settings(settings)
        self.ui.load_themes(settings["themes"])
        self.ui.listbox_themes.currentIndexChanged.connect(self.change_theme)
        self.ui.btn_admin.clicked.connect(self.on_button_click)
        self.settings = settings

    def on_button_click(self):
        print("Admin Mode activated!")
        # Dodaj tutaj logikę, która ma być wykonana po naciśnięciu przycisku

    def change_theme(self):
        selected_theme = self.ui.listbox_themes.currentText()
        theme_path = self.settings["themes"].get(selected_theme, "")
        if theme_path and os.path.exists(theme_path):
            with open(theme_path, "r") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet) """


