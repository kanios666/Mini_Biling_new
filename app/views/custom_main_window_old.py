#app\views\custom_main_window.py
from qframelesswindow import FramelessMainWindow
from qframelesswindow.titlebar import TitleBarBase
from qframelesswindow.titlebar import MinimizeButton, MaximizeButton, CloseButton
from qframelesswindow.windows.window_effect import WindowsWindowEffect
from .main_window import Ui_MainWindow
from PySide6.QtWidgets import QSizeGrip
from PySide6.QtGui import QPainterPath, QRegion  # Importowanie QPainterPath
from PySide6.QtCore import Qt  # Importowanie QRegion oraz Qt



class CustomMainWindow(FramelessMainWindow, Ui_MainWindow):
    #Klasa dziedzicząca po FramelessMainWindow z dostosowaną obsługą paska tytułowego, przycisków i przeciągania okna.
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.setWindowTitle("Custom Frameless MainWindow") 
        self.titleBar.raise_()

        action = QAction("BT", self)
        toolbar.addAction(action)
        
    def initUI(self):   
        # Ukrywanie paska tytułu i status Baru
        #self.titleBar.hide()
        #self.setStatusBar(None)
        
        
        #self.setWindowFlags(Qt.FramelessWindowHint)  # Wyłączenie systemowej ramki   
        #self.setWindowFlags(Qt.WindowTransparentForInput)
     
        #self.setWindowMask()  
        # Utworzenie obiektu WindowsWindowEffect
        #self.windowEffect = WindowsWindowEffect(self)  
        #self.setWindowOpacity(1) #super        # Dodanie zaokrąglonych rogów z promieniem 15px
        #self.windowEffect.removeBackgroundEffect(self.winId())
        #self.windowEffect.addShadowEffect(self.winId())
        # Dodanie efektu Acrylic
        #self.windowEffect.setAcrylicEffect(self.winId(), gradientColor="000000", enableShadow=True)

        # Dodanie QSizeGrip do głównego okna
        self.sizegrip = QSizeGrip(self)
        self.sizegrip.setFixedSize(24, 24)  # Ustawienie rozmiaru na 20x20
        self.sizegrip.raise_()
        
        # Przypisywanie zdarzeń z toolBarArea do metod TitleBarBase
        self.toolBarArea.installEventFilter(self.titleBar)  # Przekierowanie obsługi zdarzeń
        self.toolBarArea.mouseDoubleClickEvent = self.titleBar.mouseDoubleClickEvent
        self.toolBarArea.mousePressEvent = self.titleBar.mousePressEvent
        self.toolBarArea.mouseMoveEvent = self.titleBar.mouseMoveEvent

        # Przeciąganie okna obsługiwane przez TitleBarBase
        self.titleBar.setDoubleClickEnabled(True)  # Włączenie obsługi podwójnego kliknięcia
        
        
        #/////////////////////////////////////////////////////////////////////////////////////////
        # Tworzenie instancji bibliotekowych przycisków do kopiowania ich funkcjonalności
        """ self.close_button = CloseButton(self)
        self.minimize_button = MinimizeButton(self)
        self.maximize_button = MaximizeButton(self)
       
        # Umiejscowienie przycisków w oknie (np. w górnym rogu)
        self.minimize_button.move(self.width() - 105, 0)
        self.maximize_button.move(self.width() - 70, 0)
        self.close_button.move(self.width() - 100, 0)
        
        # Przypisanie zdarzeń kliknięć
        self.minimize_button.clicked.connect(self.showMinimized)
        self.maximize_button.clicked.connect(self.toggle_maximize)
        self.close_button.clicked.connect(self.close) """

        
    def toggle_maximize(self):
            #Deleguje wywołanie do ukrytej metody toggleMaxState w TitleBarBase, aby uniknąć efektów ubocznych związanych z dziedziczeniem.
            TitleBarBase._TitleBarBase__toggleMaxState(self.titleBar)
         
    def resizeEvent(self, event):
        super().resizeEvent(event)
       # self.setWindowMask()
        self.sizegrip.move(self.width() - self.sizegrip.width() - 4, self.height() - self.sizegrip.height() - 4)
        
        """ self.minimize_button.move(self.width() - 115, 0)
        self.maximize_button.move(self.width() - 80, 00)
        self.close_button.move(self.width() - 40, 0) """
        
        

          
        
        
        
    """   
    def copy_button_behavior(self, target_button, source_button):
      
        #Kopiuje wygląd, zdarzenia i funkcjonalność z przycisku źródłowego do docelowego.
        
        # Kopiowanie stylu
        target_button.setStyleSheet(source_button.styleSheet())

        # Delegowanie zdarzeń
        target_button.enterEvent = source_button.enterEvent
        target_button.leaveEvent = source_button.leaveEvent
        target_button.mousePressEvent = source_button.mousePressEvent
        target_button.mouseReleaseEvent = source_button.mouseReleaseEvent
        # Podłączanie sygnałów do przycisków
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_maximize.clicked.connect(self.toggle_maximize)
             """
    """
    def setWindowMask(self):
        # Ustawienie zaokrąglonych rogów przy użyciu QPainterPath
        radius = 12
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        path.addRoundedRect(self.rect(), radius, radius)  # Zaokrąglamy rogi
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region) 
      
      """  
    """
        #customize the style of title bar button
        self.minBtn.setHoverColor(Qt.white)
        self.minBtn.setHoverBackgroundColor(QColor(0, 100, 182))
        self.minBtn.setPressedColor(Qt.white)
        self.minBtn.setPressedBackgroundColor(QColor(54, 57, 65))

        # use qss to customize title bar button
        #self.maxBtn.setStyleSheet("""
            #TitleBarButton {
                #qproperty-hoverColor: white;
                #qproperty-hoverBackgroundColor: rgb(0, 100, 182);
               # qproperty-pressedColor: white;
               # qproperty-pressedBackgroundColor: rgb(54, 57, 65);
           # }
        #""")
       # """
         
    """ 
        def apply_button_functionality(self):

        #Przypisuje zdarzenia i zachowania przycisków (zamknięcia, minimalizacji, maksymalizacji)
        #bez jawnego tworzenia nowych instancji w layout'cie.

        # Tworzymy instancje przycisków do obsługi zdarzeń
        close_button = CloseButton(self)
        minimize_button = MinimizeButton(self)
        maximize_button = MaximizeButton(self)

        # Delegujemy zdarzenia do istniejących przycisków
        self.btn_close.enterEvent = close_button.enterEvent
        self.btn_close.leaveEvent = close_button.leaveEvent
        self.btn_close.mousePressEvent = close_button.mousePressEvent
        self.btn_close.mouseReleaseEvent = close_button.mouseReleaseEvent

        self.btn_minimize.enterEvent = minimize_button.enterEvent
        self.btn_minimize.leaveEvent = minimize_button.leaveEvent
        self.btn_minimize.mousePressEvent = minimize_button.mousePressEvent
        self.btn_minimize.mouseReleaseEvent = minimize_button.mouseReleaseEvent

        self.btn_maximize.enterEvent = maximize_button.enterEvent
        self.btn_maximize.leaveEvent = maximize_button.leaveEvent
        self.btn_maximize.mousePressEvent = maximize_button.mousePressEvent
        self.btn_maximize.mouseReleaseEvent = maximize_button.mouseReleaseEvent"""