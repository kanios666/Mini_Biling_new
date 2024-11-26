# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_windowGTrViH.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        self.styl = QWidget(LoginWindow)
        self.styl.setObjectName(u"styl")
        self.styl.setMinimumSize(QSize(0, 0))
        self.styl.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.styl.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"STYL OKNA LOGOWANIA\n"
"ZIELONY\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"\n"
"/* Styl dla g\u0142\u00f3wnego okna */\n"
"QWidget {\n"
"    background-color: #FFFFFF;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"/* Styl dla lewego panelu */\n"
"#l_dol, #l_gora {\n"
"    background-color: #1A7466;\n"
"    color: #FFFFFF;\n"
"}\n"
"#lbl_l_dol, #lbl_l_gora {\n"
"    background-color: #1A7466;\n"
"    color: #FFFFFF;\n"
"}\n"
"/* Styl dla prawego panelu */\n"
"#p_dol, #p_gora,#p_gora2 {\n"
"    background-color: #F0F0F0;\n"
"    color: FFFFFF;\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"/* Styl dla p\u00f3l tekstowych */\n"
"QLineEdit {\n"
"    "
                        "border: none;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    background-color: #F0F0F0;/* Jasnoszary */\n"
"    border-bottom: 1px solid #C4C5CD; /* Podkre\u015blenie szare*/\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: #FFFFFF; /* Bia\u0142y po naci\u015bni\u0119ciu */\n"
"    border-bottom: 2px solid #B2CF65; /* Podkre\u015blenie jasnozielone */\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"/* Styl dla przycisku logowania -ZALOGUJ*/\n"
"#btn_zaloguj {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;\n"
"    cursor: pointer;\n"
"}\n"
"#btn_zaloguj .QPushButton:hover  {\n"
"    background-color: #B2CF65;\n"
"}\n"
"\n"
"#lbl_l_dol{ \n"
"	Font-family: 'Arial'; \n"
"	font-size: 14px;\n"
" 	color: #FFFFFF;\n"
"	font-style: it"
                        "alic;\n"
"}\n"
"\n"
"#l_opis{ \n"
"    background-color: #F0F0F0;\n"
"	font-size: 20px;\n"
" 	color: #000000;\n"
"	font-weight: bold;\n"
"	padding-left :10px;\n"
"}\n"
"\n"
"")
        self.bgApp = QFrame(self.styl)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setGeometry(QRect(10, 10, 780, 559))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgApp.sizePolicy().hasHeightForWidth())
        self.bgApp.setSizePolicy(sizePolicy)
        self.bgApp.setMinimumSize(QSize(0, 0))
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lewe = QFrame(self.bgApp)
        self.lewe.setObjectName(u"lewe")
        self.lewe.setMinimumSize(QSize(312, 559))
        self.lewe.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.lewe)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.l_gora = QFrame(self.lewe)
        self.l_gora.setObjectName(u"l_gora")
        self.l_gora.setMinimumSize(QSize(312, 223))
        self.l_gora.setFrameShape(QFrame.Shape.NoFrame)
        self.lbl_l_gora = QLabel(self.l_gora)
        self.lbl_l_gora.setObjectName(u"lbl_l_gora")
        self.lbl_l_gora.setGeometry(QRect(0, 0, 161, 17))

        self.verticalLayout_2.addWidget(self.l_gora)

        self.l_dol = QFrame(self.lewe)
        self.l_dol.setObjectName(u"l_dol")
        self.l_dol.setMinimumSize(QSize(312, 336))
        self.l_dol.setFrameShape(QFrame.Shape.NoFrame)
        self.lbl_l_dol = QLabel(self.l_dol)
        self.lbl_l_dol.setObjectName(u"lbl_l_dol")
        self.lbl_l_dol.setGeometry(QRect(10, 179, 288, 151))
        self.lbl_l_dol.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.l_dol)


        self.horizontalLayout.addWidget(self.lewe)

        self.prawe = QFrame(self.bgApp)
        self.prawe.setObjectName(u"prawe")
        self.prawe.setMinimumSize(QSize(468, 559))
        self.prawe.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout = QVBoxLayout(self.prawe)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.p_gora2 = QFrame(self.prawe)
        self.p_gora2.setObjectName(u"p_gora2")
        self.p_gora2.setMinimumSize(QSize(468, 28))
        self.p_gora2.setMaximumSize(QSize(468, 28))
        self.p_gora2.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.p_gora2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(self.p_gora2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(28, 28))
        self.btn_close.setMaximumSize(QSize(28, 28))
        self.btn_close.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.p_gora2)

        self.p_gora = QFrame(self.prawe)
        self.p_gora.setObjectName(u"p_gora")
        self.p_gora.setMinimumSize(QSize(468, 195))
        self.p_gora.setFrameShape(QFrame.Shape.NoFrame)
        self.l_opis = QLabel(self.p_gora)
        self.l_opis.setObjectName(u"l_opis")
        self.l_opis.setGeometry(QRect(0, 150, 311, 41))

        self.verticalLayout.addWidget(self.p_gora)

        self.p_dol = QFrame(self.prawe)
        self.p_dol.setObjectName(u"p_dol")
        self.p_dol.setMinimumSize(QSize(468, 336))
        self.p_dol.setFrameShape(QFrame.Shape.NoFrame)
        self.p_dol.setLineWidth(1)
        self.password = QLineEdit(self.p_dol)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(1, 40, 468, 45))
        self.password.setMinimumSize(QSize(468, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        font.setItalic(False)
        self.password.setFont(font)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.login = QLineEdit(self.p_dol)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(1, 1, 468, 45))
        self.login.setMinimumSize(QSize(468, 45))
        self.login.setMaximumSize(QSize(468, 45))
        self.login.setFont(font)
        self.btn_zaloguj = QPushButton(self.p_dol)
        self.btn_zaloguj.setObjectName(u"btn_zaloguj")
        self.btn_zaloguj.setGeometry(QRect(20, 110, 111, 51))
        self.btn_zaloguj.setMinimumSize(QSize(0, 40))
        self.btn_zaloguj.setSizeIncrement(QSize(0, 0))
        self.btn_zaloguj.setBaseSize(QSize(0, 0))
        self.btn_zaloguj.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.btn_zaloguj.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.p_dol)


        self.horizontalLayout.addWidget(self.prawe)

        #LoginWindow.setCentralWidget(self.styl)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        #LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.lbl_l_gora.setText(QCoreApplication.translate("LoginWindow", u"MINI BILING", None))
        self.lbl_l_dol.setText(QCoreApplication.translate("LoginWindow", u"TextLabel", None))
        self.btn_close.setText(QCoreApplication.translate("LoginWindow", u"PushButton", None))
        self.l_opis.setText(QCoreApplication.translate("LoginWindow", u"Zaloguj si\u0119 do swojego konta", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Has\u0142o", None))
        self.login.setText("")
        self.login.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.btn_zaloguj.setText(QCoreApplication.translate("LoginWindow", u"ZALOGUJ", None))
    # retranslateUi

