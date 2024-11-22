from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = self.load_ui()

    def load_ui(self):
        try:
            ui_file = QFile("app/ui/main_window.ui")
            if not ui_file.open(QFile.ReadOnly):
                print("Failed to open UI file")
                return None
            loader = QUiLoader()
            ui = loader.load(ui_file, self)
            ui_file.close()
            return ui
        except Exception as e:
            print(f"Error loading UI: {e}")
            return None
