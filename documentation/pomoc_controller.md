https://github.com/zhiyiYo/PyQt-Frameless-Window/tree/PySide6


# Obsłufa wielu wątkow zapisanych w pyside6
QThreadPool i QRunnable:

# do kompilowania py>>exe Nutika do kodu maszynowego
Nutika

#//Ustawienia okna PySide6//////
        
    #Wyłączenie górnego paska 
    self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    
    # Przywrócenie standardowych ramek okna
    self.setWindowFlags(Qt.Window)  
    
    # Ustawienie przezroczystości okna
    self.setWindowOpacity(0.96)

    # Wyłączenie możliwości rozszerzania okna 
    self.setFixedSize(self.size())

    #Ustawia okno, aby zawsze było na wierzchu innych okien.
    self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint)

    #Usuwa pasek tytułowy okna.
    self.setWindowFlags(QtCore.Qt.WindowType.Tool)

    #Ustawia okno jako okno dialogowe.
    self.setWindowFlags(QtCore.Qt.WindowType.Dialog)

    #Okno narzędziowa
    self.setWindowFlags(QtCore.Qt.WindowType.Tool)

    #Usuwa przyciski minimalizacji i maksymalizacji z okna.
    self.setWindowFlags(QtCore.Qt.WindowType.Window | QtCore.Qt.WindowType.WindowMinimizeButtonHint | QtCore.Qt.WindowType.WindowMaximizeButtonHint)

    #Ustawia okno w trybie pełnoekranowym.
    self.showFullScreen()

    #Maksymalizuje okno
    self.showMaximized()
    self.showMinimized()

============== kropki w imporcie from

x - z miejsca 
y - jaki moduł mam imporotwać 
z - jakiej nazwy używac w programie

1. from x import y:
Importuje moduł y z miejsca x, które może być w ścieżce domyślnej Pythona (sys.path), pakietach zainstalowanych z Pythonem lub poprzez pip install.

2. from .x import y as z:
Importuje moduł y z katalogu x względem obecnego pliku w hierarchii katalogów i używa nazwy z jako aliasu.

3. from ..x import y:
Importuje moduł y z katalogu x, który znajduje się jeden poziom wyżej w hierarchii katalogów względem obecnego pliku.

4. Import z pełną ścieżką danego projektu [wszystkie klasy/funcje]
from app.controllers import plik

5. Import klasy /funkcji 
from app.controllers.plik import klasa/funkcja

Prblemy obejście 
nie działa [import całego pliku + alias] - import win32_utils as win_utils
działa - from app.controllers.gui import win32_utils as win_utils


===Pyside
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
