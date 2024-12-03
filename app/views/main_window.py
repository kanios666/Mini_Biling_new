# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_testxpAFar.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 783)
        MainWindow.setMinimumSize(QSize(940, 60))
        self.styl = QWidget(MainWindow)
        self.styl.setObjectName(u"styl")
        self.verticalLayout = QVBoxLayout(self.styl)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styl)
        self.bgApp.setObjectName(u"bgApp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgApp.sizePolicy().hasHeightForWidth())
        self.bgApp.setSizePolicy(sizePolicy)
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leweMenu = QFrame(self.bgApp)
        self.leweMenu.setObjectName(u"leweMenu")
        self.leweMenu.setMinimumSize(QSize(200, 0))
        self.leweMenu.setMaximumSize(QSize(60, 16777215))
        self.leweMenu.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.leweMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.leweMenu)

        self.ContentBox = QFrame(self.bgApp)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.ContentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.naglowek = QFrame(self.ContentBox)
        self.naglowek.setObjectName(u"naglowek")
        self.naglowek.setMinimumSize(QSize(0, 60))
        self.naglowek.setMaximumSize(QSize(16777215, 60))
        self.naglowek.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.naglowek)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tytul = QFrame(self.naglowek)
        self.tytul.setObjectName(u"tytul")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tytul.sizePolicy().hasHeightForWidth())
        self.tytul.setSizePolicy(sizePolicy1)
        self.tytul.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.tytul)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbl_tytul = QLabel(self.tytul)
        self.lbl_tytul.setObjectName(u"lbl_tytul")

        self.horizontalLayout_5.addWidget(self.lbl_tytul)


        self.horizontalLayout_3.addWidget(self.tytul)

        self.nagMenu = QFrame(self.naglowek)
        self.nagMenu.setObjectName(u"nagMenu")
        self.nagMenu.setMinimumSize(QSize(0, 60))
        self.nagMenu.setMaximumSize(QSize(120, 16777215))
        self.nagMenu.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.nagMenu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_praweMenu = QPushButton(self.nagMenu)
        self.btn_praweMenu.setObjectName(u"btn_praweMenu")
        self.btn_praweMenu.setMinimumSize(QSize(28, 28))
        self.btn_praweMenu.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_praweMenu, 0, Qt.AlignTop)

        self.btn_minmalize = QPushButton(self.nagMenu)
        self.btn_minmalize.setObjectName(u"btn_minmalize")
        self.btn_minmalize.setMinimumSize(QSize(28, 28))
        self.btn_minmalize.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_minmalize, 0, Qt.AlignTop)

        self.btn_maksymalize = QPushButton(self.nagMenu)
        self.btn_maksymalize.setObjectName(u"btn_maksymalize")
        self.btn_maksymalize.setMinimumSize(QSize(28, 28))
        self.btn_maksymalize.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_maksymalize, 0, Qt.AlignTop)

        self.btn_zamknij = QPushButton(self.nagMenu)
        self.btn_zamknij.setObjectName(u"btn_zamknij")
        self.btn_zamknij.setMinimumSize(QSize(28, 28))
        self.btn_zamknij.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_zamknij, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.nagMenu)


        self.verticalLayout_2.addWidget(self.naglowek)

        self.content = QFrame(self.ContentBox)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.glowneOkno = QFrame(self.content)
        self.glowneOkno.setObjectName(u"glowneOkno")
        self.glowneOkno.setFrameShape(QFrame.StyledPanel)
        self.glowneOkno.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.glowneOkno)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_gO = QLabel(self.glowneOkno)
        self.lbl_gO.setObjectName(u"lbl_gO")

        self.verticalLayout_3.addWidget(self.lbl_gO)


        self.horizontalLayout_2.addWidget(self.glowneOkno)

        self.praweMenu = QFrame(self.content)
        self.praweMenu.setObjectName(u"praweMenu")
        self.praweMenu.setMaximumSize(QSize(200, 16777215))
        self.praweMenu.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.praweMenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_praweMenu = QLabel(self.praweMenu)
        self.lbl_praweMenu.setObjectName(u"lbl_praweMenu")

        self.verticalLayout_5.addWidget(self.lbl_praweMenu)


        self.horizontalLayout_2.addWidget(self.praweMenu)


        self.verticalLayout_2.addWidget(self.content)

        self.stopka = QFrame(self.ContentBox)
        self.stopka.setObjectName(u"stopka")
        self.stopka.setMinimumSize(QSize(0, 24))
        self.stopka.setMaximumSize(QSize(16777215, 24))
        self.stopka.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.stopka)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_autor = QLabel(self.stopka)
        self.lbl_autor.setObjectName(u"lbl_autor")
        self.lbl_autor.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_6.addWidget(self.lbl_autor)

        self.lbl_baza = QLabel(self.stopka)
        self.lbl_baza.setObjectName(u"lbl_baza")

        self.horizontalLayout_6.addWidget(self.lbl_baza)

        self.lbl_wersja = QLabel(self.stopka)
        self.lbl_wersja.setObjectName(u"lbl_wersja")
        self.lbl_wersja.setMaximumSize(QSize(175, 16777215))

        self.horizontalLayout_6.addWidget(self.lbl_wersja)

        self.size = QFrame(self.stopka)
        self.size.setObjectName(u"size")
        self.size.setMinimumSize(QSize(24, 24))
        self.size.setMaximumSize(QSize(24, 24))
        self.size.setFrameShape(QFrame.StyledPanel)
        self.size.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.size)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.size)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)


        self.horizontalLayout_6.addWidget(self.size)


        self.verticalLayout_2.addWidget(self.stopka)


        self.horizontalLayout.addWidget(self.ContentBox)


        self.verticalLayout.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styl)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_tytul.setText(QCoreApplication.translate("MainWindow", u"Tytul", None))
        self.btn_praweMenu.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_minmalize.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_maksymalize.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_zamknij.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lbl_gO.setText(QCoreApplication.translate("MainWindow", u"glowne Okno", None))
        self.lbl_praweMenu.setText(QCoreApplication.translate("MainWindow", u"prawe Menu", None))
        self.lbl_autor.setText(QCoreApplication.translate("MainWindow", u" By: Kanios", None))
        self.lbl_baza.setText(QCoreApplication.translate("MainWindow", u" db: status", None))
        self.lbl_wersja.setText(QCoreApplication.translate("MainWindow", u"ver. 0.0.1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

