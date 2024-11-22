import sys
import os

from views.main_window import MainWindow

class MainController:
    def __init__(self):
        self.window = MainWindow()
        if not self.window:
            return
        self.setup_connections()

    def setup_connections(self):
        self.window.ui.btn_admin.clicked.connect(self.admin_mode)


