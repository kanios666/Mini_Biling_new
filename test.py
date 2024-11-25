import sys

from PySide6.QtWidgets import QApplication
from app.controllers.windows.qframelesswindow import Dupa3


class Window(Dupa3):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        #self.setWindowTitle("PySide6-Frameless-Window")
        #self.titleBar.raise_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    app.exec()