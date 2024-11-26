https://github.com/zhiyiYo/PyQt-Frameless-Window/tree/PySide6

#//Ustawienia okna PySide6//////
        
    #Wyłączenie górnego paska 
    self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    
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

