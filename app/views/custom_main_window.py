#app\views\custom_main_window.py
from qframelesswindow import FramelessMainWindow
from .custom_title_bar import CustomTitleBar
from .main_window import Ui_MainWindow
from PySide6.QtWidgets import QApplication,QSizeGrip


class CustomMainWindow(FramelessMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.setTitleBar(CustomTitleBar(self))
        self.move(QApplication.primaryScreen().availableGeometry().center() - self.rect().center())

    def initUI(self):   
        self.titleBar.maxBtn.hide()




        # Dodanie QSizeGrip do głównego okna
        self.sizegrip = QSizeGrip(self)
        self.sizegrip.setFixedSize(24, 24)  # Ustawienie rozmiaru na 24x24
        self.sizegrip.raise_()
        
        # Przypisywanie zdarzeń z toolBarArea do metod TitleBarBase
        self.toolBarArea.installEventFilter(self.titleBar)  # Przekierowanie obsługi zdarzeń
        self.toolBarArea.mouseDoubleClickEvent = self.titleBar.mouseDoubleClickEvent
        self.toolBarArea.mousePressEvent = self.titleBar.mousePressEvent
        self.toolBarArea.mouseMoveEvent = self.titleBar.mouseMoveEvent

        # Przeciąganie okna obsługiwane przez TitleBarBase
        self.titleBar.setDoubleClickEnabled(True)  # Włączenie obsługi podwójnego kliknięcia
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.sizegrip.move(self.width() - self.sizegrip.width() , self.height() - self.sizegrip.height() )

