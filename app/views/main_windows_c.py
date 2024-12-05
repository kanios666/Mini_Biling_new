from PySide6.QtCore import (QCoreApplication, QSize, Qt, QMetaObject)
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QFrame, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QSpacerItem, QSizePolicy, QMainWindow, QDesktopWidget)
from PySide6.QtWidgets import QGraphicsDropShadowEffect

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 668)
        MainWindow.setMinimumSize(QSize(940, 668))
        
        # Przekształcamy okno na Frameless
        MainWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        
        # Dodanie cienia do okna (dla lepszego efektu wizualnego)
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(25)
        shadow_effect.setColor(QColor(0, 0, 0, 160))
        shadow_effect.setOffset(0, 0)
        MainWindow.setGraphicsEffect(shadow_effect)

        self.styl = QWidget(MainWindow)
        self.styl.setObjectName(u"styl")
        self.verticalLayout = QVBoxLayout(self.styl)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        # Tło aplikacji
        self.bgApp = QFrame(self.styl)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        
        # Lewe menu
        self.leweMenu = QFrame(self.bgApp)
        self.leweMenu.setObjectName(u"leweMenu")
        self.leweMenu.setMinimumSize(QSize(200, 0))
        self.leweMenu.setMaximumSize(QSize(60, 16777215))
        self.leweMenu.setFrameShape(QFrame.NoFrame)
        
        self.verticalLayout_6 = QVBoxLayout(self.leweMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        # Dodanie przycisku menu
        self.lm_gora = QFrame(self.leweMenu)
        self.lm_gora.setObjectName(u"lm_gora")
        self.lm_gora.setMinimumSize(QSize(0, 60))
        self.lm_gora.setFrameShape(QFrame.NoFrame)
        
        self.verticalLayout_4 = QVBoxLayout(self.lm_gora)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_Menu = QPushButton(self.lm_gora)
        self.btn_Menu.setObjectName(u"btn_Menu")
        self.btn_Menu.setMinimumSize(QSize(0, 45))
        self.btn_Menu.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout_4.addWidget(self.btn_Menu)
        self.verticalLayout_6.addWidget(self.lm_gora, 0, Qt.AlignTop)

        # Przyciski w środku menu
        self.lm_srodek = QFrame(self.leweMenu)
        self.lm_srodek.setObjectName(u"lm_srodek")
        self.lm_srodek.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.lm_srodek)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        
        # Przycisk tablica
        self.btn_tablica = QPushButton(self.lm_srodek)
        self.btn_tablica.setObjectName(u"btn_tablica")
        self.btn_tablica.setMinimumSize(QSize(0, 45))
        self.btn_tablica.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout_8.addWidget(self.btn_tablica)
        
        # Przycisk ewidencja
        self.btn_ewidencja = QPushButton(self.lm_srodek)
        self.btn_ewidencja.setObjectName(u"btn_ewidencja")
        self.btn_ewidencja.setMinimumSize(QSize(0, 45))
        self.btn_ewidencja.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout_8.addWidget(self.btn_ewidencja)

        # Przycisk rozliczenia
        self.btn_rozliczenia = QPushButton(self.lm_srodek)
        self.btn_rozliczenia.setObjectName(u"btn_rozliczenia")
        self.btn_rozliczenia.setMinimumSize(QSize(0, 45))
        self.btn_rozliczenia.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout_8.addWidget(self.btn_rozliczenia)
        
        self.verticalLayout_6.addWidget(self.lm_srodek, 0, Qt.AlignTop)

        # Spacer na dole
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(self.verticalSpacer)

        # Dolne menu z ustawieniami
        self.lm_dol = QFrame(self.leweMenu)
        self.lm_dol.setObjectName(u"lm_dol")
        self.lm_dol.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.lm_dol)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_ustawienia = QPushButton(self.lm_dol)
        self.btn_ustawienia.setObjectName(u"btn_ustawienia")
        self.btn_ustawienia.setMinimumSize(QSize(0, 45))
        self.btn_ustawienia.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout_9.addWidget(self.btn_ustawienia)
        self.verticalLayout_6.addWidget(self.lm_dol, 0, Qt.AlignBottom)

        self.horizontalLayout.addWidget(self.leweMenu)

        # Główna zawartość
        self.ContentBox = QFrame(self.bgApp)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setFrameShape(QFrame.NoFrame)
        
        self.verticalLayout_2 = QVBoxLayout(self.ContentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        # Nagłówek
        self.naglowek = QFrame(self.ContentBox)
        self.naglowek.setObjectName(u"naglowek")
        self.naglowek.setMinimumSize(QSize(0, 60))
        self.naglowek.setMaximumSize(QSize(16777215, 60))
        self.naglowek.setFrameShape(QFrame.NoFrame)
        
        self.horizontalLayout_3 = QHBoxLayout(self.naglowek)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        
        self.tytul = QFrame(self.naglowek)
        self.tytul.setObjectName(u"tytul")
        self.tytul.setFrameShape(QFrame.NoFrame)
        
        self.horizontalLayout_5 = QHBoxLayout(self.tytul)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        
        self.lbl_tytul = QLabel(self.tytul)
        self.lbl_tytul.setObjectName(u"lbl_tytul")
        self.horizontalLayout_5.addWidget(self.lbl_tytul)
        self.horizontalLayout_3.addWidget(self.tytul)

        # Menu nagłówka
        self.nagMenu = QFrame(self.naglowek)
        self.nagMenu.setObjectName(u"nagMenu")
        self.nagMenu.setFrameShape(QFrame.NoFrame)
        
        self.horizontalLayout_4 = QHBoxLayout(self.nagMenu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        
        self.btn_zamknij = QPushButton(self.nagMenu)
        self.btn_zamknij.setObjectName(u"btn_zamknij")
        self.btn_zamknij.setMaximumSize(QSize(45, 16777215))
        self.horizontalLayout_4.addWidget(self.btn_zamknij)
        self.horizontalLayout_3.addWidget(self.nagMenu)

        self.verticalLayout_2.addWidget(self.naglowek)

        # Właściwa zawartość
        self.main_content = QFrame(self.ContentBox)
        self.main_content.setObjectName(u"main_content")
        self.verticalLayout_2.addWidget(self.main_content)

        self.horizontalLayout.addWidget(self.ContentBox)
        self.verticalLayout.addWidget(self.bgApp)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_Menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_tablica.setText(QCoreApplication.translate("MainWindow", u"Tablica", None))
        self.btn_ewidencja.setText(QCoreApplication.translate("MainWindow", u"Ewidencja", None))
        self.btn_rozliczenia.setText(QCoreApplication.translate("MainWindow", u"Rozliczenia", None))
        self.btn_ustawienia.setText(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
        self.lbl_tytul.setText(QCoreApplication.translate("MainWindow", u"Main Window", None))
        self.btn_zamknij.setText(QCoreApplication.translate("MainWindow", u"Zamknij", None))
