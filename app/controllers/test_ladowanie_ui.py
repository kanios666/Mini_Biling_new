import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(r"app\ui\test.ui", self)

        #self.setWindowFlags(QtCore.Qt.WindowType.Window | QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
        
        # Wyłączenie obramowania okna
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()

        # Ustawienie przezroczystości okna
        self.setWindowOpacity(0.96)




app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()