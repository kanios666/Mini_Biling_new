# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_windowccEkfB.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.styl = QWidget(MainWindow)
        self.styl.setObjectName(u"styl")
        self.styl.setMinimumSize(QSize(0, 0))
        self.bgApp = QFrame(self.styl)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setGeometry(QRect(10, 10, 786, 563))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgApp.sizePolicy().hasHeightForWidth())
        self.bgApp.setSizePolicy(sizePolicy)
        self.bgApp.setMinimumSize(QSize(0, 0))
        self.bgApp.setFrameShape(QFrame.StyledPanel)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lewe = QFrame(self.bgApp)
        self.lewe.setObjectName(u"lewe")
        self.lewe.setMinimumSize(QSize(312, 559))
        self.lewe.setFrameShape(QFrame.StyledPanel)
        self.lewe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.lewe)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.l_gora = QFrame(self.lewe)
        self.l_gora.setObjectName(u"l_gora")
        self.l_gora.setMinimumSize(QSize(312, 223))
        self.l_gora.setFrameShape(QFrame.StyledPanel)
        self.l_gora.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.l_gora)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_l_gora = QLabel(self.l_gora)
        self.lbl_l_gora.setObjectName(u"lbl_l_gora")

        self.verticalLayout_6.addWidget(self.lbl_l_gora)


        self.verticalLayout_2.addWidget(self.l_gora)

        self.l_dol_ = QFrame(self.lewe)
        self.l_dol_.setObjectName(u"l_dol_")
        self.l_dol_.setMinimumSize(QSize(312, 336))
        self.l_dol_.setFrameShape(QFrame.StyledPanel)
        self.l_dol_.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.l_dol_)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_l_dol = QLabel(self.l_dol_)
        self.lbl_l_dol.setObjectName(u"lbl_l_dol")

        self.verticalLayout_3.addWidget(self.lbl_l_dol, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.l_dol_)


        self.horizontalLayout.addWidget(self.lewe, 0, Qt.AlignLeft|Qt.AlignTop)

        self.prawe = QFrame(self.bgApp)
        self.prawe.setObjectName(u"prawe")
        self.prawe.setMinimumSize(QSize(468, 559))
        self.prawe.setFrameShape(QFrame.StyledPanel)
        self.prawe.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.prawe)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_close = QPushButton(self.prawe)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(28, 28))
        self.btn_close.setMaximumSize(QSize(28, 28))

        self.verticalLayout.addWidget(self.btn_close, 0, Qt.AlignRight)

        self.p_gora = QFrame(self.prawe)
        self.p_gora.setObjectName(u"p_gora")
        self.p_gora.setMinimumSize(QSize(468, 195))
        self.p_gora.setFrameShape(QFrame.StyledPanel)
        self.p_gora.setFrameShadow(QFrame.Raised)
        self.l_opis = QLabel(self.p_gora)
        self.l_opis.setObjectName(u"l_opis")
        self.l_opis.setGeometry(QRect(1, 150, 157, 16))

        self.verticalLayout.addWidget(self.p_gora, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.p_dol = QFrame(self.prawe)
        self.p_dol.setObjectName(u"p_dol")
        self.p_dol.setMinimumSize(QSize(468, 336))
        self.p_dol.setFrameShape(QFrame.StyledPanel)
        self.p_dol.setFrameShadow(QFrame.Raised)
        self.p_dol.setLineWidth(1)
        self.password = QLineEdit(self.p_dol)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(1, 40, 468, 45))
        self.password.setMinimumSize(QSize(468, 45))
        font = QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setEchoMode(QLineEdit.Password)
        self.login = QLineEdit(self.p_dol)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(1, 1, 468, 45))
        self.login.setMinimumSize(QSize(468, 45))
        self.login.setMaximumSize(QSize(468, 45))
        self.login.setFont(font)
        self.btn_zaloguj = QPushButton(self.p_dol)
        self.btn_zaloguj.setObjectName(u"btn_zaloguj")
        self.btn_zaloguj.setGeometry(QRect(20, 110, 75, 40))
        self.btn_zaloguj.setMinimumSize(QSize(0, 40))
        self.btn_zaloguj.setMaximumSize(QSize(200, 40))
        self.btn_zaloguj.setSizeIncrement(QSize(0, 0))
        self.btn_zaloguj.setBaseSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.p_dol)


        self.horizontalLayout.addWidget(self.prawe)

        MainWindow.setCentralWidget(self.styl)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_l_gora.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.lbl_l_dol.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.l_opis.setText(QCoreApplication.translate("MainWindow", u"Zaloguj si\u0119 do swojego konta!", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Has\u0142o", None))
        self.login.setText("")
        self.login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_zaloguj.setText(QCoreApplication.translate("MainWindow", u"ZALOGUJ", None))
    # retranslateUi
