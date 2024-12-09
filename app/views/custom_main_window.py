from qframelesswindow import FramelessMainWindow, TitleBarBase
from qframelesswindow.titlebar import MinimizeButton, MaximizeButton, CloseButton
from .main_window import Ui_MainWindow
from PySide6.QtWidgets import QSizeGrip

class CustomMainWindow(FramelessMainWindow, Ui_MainWindow):
    #Klasa dziedzicząca po FramelessMainWindow z dostosowaną obsługą paska tytułowego, przycisków i przeciągania okna.
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Ukrywanie paska tytułu
        self.titleBar.hide()
        
        # Styl i funkcjonalność przycisków na podstawie dziedziczenia z FramelessMainWindow
        self.btn_close.setStyleSheet(CloseButton(self).styleSheet())
        #self.btn_minimize.setStyleSheet(MinimizeButton(self).styleSheet())
        #self.btn_maximize.setStyleSheet(MaximizeButton(self).styleSheet())

        # Podłączanie sygnałów do przycisków
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_maximize.clicked.connect(self.toggle_maximize)
        
        # Przypisanie istniejących przycisków z TitleBarBase do funkcji zamykania, maksymalizacji, minimalizacji
        self.btn_close = self.titleBar.closeBtn
        self.minimize_button = self.titleBar.minBtn
        self.maximize_button = self.titleBar.maxBtn
        
        #Dodanie istniejącego sizeGrip w głównym interfejsie
        self.sizegrip = QSizeGrip(self)
        self.sizegrip.setStyleSheet("background: transparent;")
        self.sizegrip.setParent(self)
        self.sizegrip.raise_()  # Ustawienie sizeGrip na wierzchu 
        
        """        
        # Ustawienia SizeGrip na podstawie istniejącego QFrame
        self.sizegrip.setStyleSheet("background: transparent;")
        self.sizegrip.raise_()  # Upewnij się, że sizeGrip znajduje się na wierzchu innych elementów
        self.statusBar.setContentsMargins(4, 4, 4, 4)  # Dostosowanie marginesów """
        
        # Przypisywanie zdarzeń z toolBarArea do metod TitleBarBase
        self.toolBarArea.installEventFilter(self.titleBar)  # Przekierowanie obsługi zdarzeń
        self.toolBarArea.mouseDoubleClickEvent = self.titleBar.mouseDoubleClickEvent
        self.toolBarArea.mousePressEvent = self.titleBar.mousePressEvent
        self.toolBarArea.mouseMoveEvent = self.titleBar.mouseMoveEvent

        # Przeciąganie okna obsługiwane przez TitleBarBase
        self.titleBar.setDoubleClickEnabled(True)  # Włączenie obsługi podwójnego kliknięcia
        
    def toggle_maximize(self):
            #Deleguje wywołanie do ukrytej metody toggleMaxState w TitleBarBase, aby uniknąć efektów ubocznych związanych z dziedziczeniem.
            TitleBarBase._TitleBarBase__toggleMaxState(self.titleBar)
            
    def Close_btn(self):
            CloseButton(self.titleBar)