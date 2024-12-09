from PySide6 import QtCore, QtGui, QtWidgets

def hex2QColor(c):
    """Convert Hex color to QColor"""
    r = int(c[0:2], 16)
    g = int(c[2:4], 16)
    b = int(c[4:6], 16)
    return QtGui.QColor(r, g, b)

class RoundedWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(RoundedWindow, self).__init__(parent)

        # make the window frameless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.backgroundColor = hex2QColor("efefef")
        self.foregroundColor = hex2QColor("efefef")
        self.borderRadius = 10
        self.draggable = True
        self.dragging_threshould = 5
        self.__mousePressPos = None
        self.__mouseMovePos = None
        
    
        #Size Grip 
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)  # Dodanie marginesów
        layout.setSpacing(0)
        size_grip = QtWidgets.QSizeGrip(self)
        layout.addWidget(size_grip, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)



        self.setMinimumSize(320, 240)

    def paintEvent(self, event):
        # get current window size
        s = self.size()
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing, True)
        qp.setPen(self.foregroundColor)
        qp.setBrush(self.backgroundColor)
        qp.drawRoundedRect(0, 0, s.width(), s.height(),
                           self.borderRadius, self.borderRadius)
        qp.end()

    def mousePressEvent(self, event):
        if self.draggable and event.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = event.globalPos()                # global
            self.__mouseMovePos = event.globalPos() - self.pos()    # local
        super(RoundedWindow, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() & QtCore.Qt.LeftButton:
            globalPos = event.globalPos()
            moved = globalPos - self.__mousePressPos
            if moved.manhattanLength() > self.dragging_threshould:
                # move when user drag window more than dragging_threshould
                diff = globalPos - self.__mouseMovePos
                self.move(diff)
                self.__mouseMovePos = globalPos - self.pos()
        super(RoundedWindow, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            if event.button() == QtCore.Qt.LeftButton:
                moved = event.globalPos() - self.__mousePressPos
                if moved.manhattanLength() > self.dragging_threshould:
                    # do not call click event or so on
                    event.ignore()
                self.__mousePressPos = None
        super(RoundedWindow, self).mouseReleaseEvent(event)

        # close event
        if event.button() == QtCore.Qt.RightButton:
            QtGui.qApp.exit()




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = RoundedWindow()
    main.show()
    sys.exit(app.exec())
