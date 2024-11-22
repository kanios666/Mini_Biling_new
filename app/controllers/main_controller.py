# app\controllers\main_controller.py
import sys
from app.views.main_window import MainWindow

class MainController:
    def __init__(self):
        try:
            # Tworzenie głównego okna
            self.window = MainWindow()
        except Exception as e:
            print(f"Error initializing MainWindow: {e}")
            sys.exit(1)

        if not self.window:
            print("MainWindow failed to initialize.")
            return

        self.setup_connections()

    def setup_connections(self):
        try:
            # Łączenie przycisków z metodami
            self.window.ui.btn_admin.clicked.connect(self.admin_mode)
        except AttributeError as e:
            print(f"Error setting up connections: {e}")
            sys.exit(1)

    def admin_mode(self):
        # Przykładowa metoda wywoływana po kliknięciu przycisku
        print("Admin mode activated!")
