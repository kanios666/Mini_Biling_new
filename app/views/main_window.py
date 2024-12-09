# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowJUsdnx.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 668)
        MainWindow.setMinimumSize(QSize(940, 668))
        MainWindow.setStyleSheet(u"")
        self.styl = QWidget(MainWindow)
        self.styl.setObjectName(u"styl")
        self.styl.setMinimumSize(QSize(940, 668))
        self.styl.setStyleSheet(u"\n"
"#MainWindow, #styl, #BgApp {\n"
"    background-color: transparent;\n"
"    border-radius: 10px; \n"
"     /*zaokr\u0105glenia*/\n"
"}\n"
" #leftMenu, #lmTop{\n"
"	border-top-left-radius: 10px; \n"
"}\n"
"#leftMenu, #lm_bottom{\n"
"	border-bottom-left-radius: 10px; \n"
"}\n"
"#central, #statusBar{\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
" #toolBarArea, #central,#top_btns {\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"/*#Wyglad wewn\u0119trznych okien*/\n"
"#leftMenu, #rightMenu {\n"
"    background-color: #1A7466;\n"
"}\n"
"#central {\n"
"   background-color: #F0F0F0;\n"
"}\n"
"#toolBarArea {\n"
"	background-color: #1A7466;\n"
"}\n"
"\n"
"/*Stopka*/\n"
"#statusBar{\n"
"	background-color: #000000;\n"
"}\n"
"#lbl_db_status, #lbl_autor, #lbl_ver{\n"
"	color: #FFFFFF;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.styl)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.BgApp = QFrame(self.styl)
        self.BgApp.setObjectName(u"BgApp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BgApp.sizePolicy().hasHeightForWidth())
        self.BgApp.setSizePolicy(sizePolicy)
        self.BgApp.setMinimumSize(QSize(940, 668))
        self.BgApp.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.BgApp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.BgApp)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(0, 668))
        self.leftMenu.setMaximumSize(QSize(200, 16777215))
        self.leftMenu.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lm_top = QFrame(self.leftMenu)
        self.lm_top.setObjectName(u"lm_top")
        self.lm_top.setMinimumSize(QSize(0, 60))
        self.lm_top.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.lm_top)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 0, 9)
        self.btn_menu = QPushButton(self.lm_top)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy1)
        self.btn_menu.setMinimumSize(QSize(0, 45))
        self.btn_menu.setMaximumSize(QSize(45, 16777215))

        self.verticalLayout_4.addWidget(self.btn_menu)


        self.verticalLayout_6.addWidget(self.lm_top, 0, Qt.AlignTop)

        self.lm_midlle = QFrame(self.leftMenu)
        self.lm_midlle.setObjectName(u"lm_midlle")
        self.lm_midlle.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.lm_midlle)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 9, 0, 0)
        self.btn_tablica = QPushButton(self.lm_midlle)
        self.btn_tablica.setObjectName(u"btn_tablica")
        sizePolicy1.setHeightForWidth(self.btn_tablica.sizePolicy().hasHeightForWidth())
        self.btn_tablica.setSizePolicy(sizePolicy1)
        self.btn_tablica.setMinimumSize(QSize(0, 45))
        self.btn_tablica.setMaximumSize(QSize(45, 16777215))

        self.verticalLayout_8.addWidget(self.btn_tablica)

        self.btn_ewidencja = QPushButton(self.lm_midlle)
        self.btn_ewidencja.setObjectName(u"btn_ewidencja")
        sizePolicy1.setHeightForWidth(self.btn_ewidencja.sizePolicy().hasHeightForWidth())
        self.btn_ewidencja.setSizePolicy(sizePolicy1)
        self.btn_ewidencja.setMinimumSize(QSize(0, 45))
        self.btn_ewidencja.setMaximumSize(QSize(45, 16777215))

        self.verticalLayout_8.addWidget(self.btn_ewidencja)

        self.btn_rozliczenia = QPushButton(self.lm_midlle)
        self.btn_rozliczenia.setObjectName(u"btn_rozliczenia")
        sizePolicy1.setHeightForWidth(self.btn_rozliczenia.sizePolicy().hasHeightForWidth())
        self.btn_rozliczenia.setSizePolicy(sizePolicy1)
        self.btn_rozliczenia.setMinimumSize(QSize(0, 45))
        self.btn_rozliczenia.setMaximumSize(QSize(45, 16777215))

        self.verticalLayout_8.addWidget(self.btn_rozliczenia)


        self.verticalLayout_6.addWidget(self.lm_midlle, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.lm_botton = QFrame(self.leftMenu)
        self.lm_botton.setObjectName(u"lm_botton")
        self.lm_botton.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.lm_botton)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(9, 9, 0, 9)
        self.btn_settings_user = QPushButton(self.lm_botton)
        self.btn_settings_user.setObjectName(u"btn_settings_user")
        sizePolicy1.setHeightForWidth(self.btn_settings_user.sizePolicy().hasHeightForWidth())
        self.btn_settings_user.setSizePolicy(sizePolicy1)
        self.btn_settings_user.setMinimumSize(QSize(0, 45))
        self.btn_settings_user.setMaximumSize(QSize(45, 16777215))

        self.verticalLayout_9.addWidget(self.btn_settings_user)


        self.verticalLayout_6.addWidget(self.lm_botton, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.central = QFrame(self.BgApp)
        self.central.setObjectName(u"central")
        self.central.setMinimumSize(QSize(0, 668))
        self.central.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.central)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolBarArea = QFrame(self.central)
        self.toolBarArea.setObjectName(u"toolBarArea")
        self.toolBarArea.setMinimumSize(QSize(0, 60))
        self.toolBarArea.setMaximumSize(QSize(16777215, 60))
        self.toolBarArea.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.toolBarArea)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolBar = QFrame(self.toolBarArea)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy2)
        self.toolBar.setMinimumSize(QSize(0, 60))
        self.toolBar.setMaximumSize(QSize(16777215, 60))
        self.toolBar.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.toolBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbl_tB = QLabel(self.toolBar)
        self.lbl_tB.setObjectName(u"lbl_tB")
        self.lbl_tB.setMinimumSize(QSize(0, 60))
        self.lbl_tB.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_5.addWidget(self.lbl_tB)


        self.horizontalLayout_3.addWidget(self.toolBar)

        self.top_btns = QFrame(self.toolBarArea)
        self.top_btns.setObjectName(u"top_btns")
        self.top_btns.setMinimumSize(QSize(0, 60))
        self.top_btns.setMaximumSize(QSize(120, 60))
        self.top_btns.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.btn_process = QPushButton(self.top_btns)
        self.btn_process.setObjectName(u"btn_process")
        self.btn_process.setMinimumSize(QSize(28, 28))
        self.btn_process.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_process, 0, Qt.AlignTop)

        self.btn_minimize = QPushButton(self.top_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(28, 28))
        self.btn_minimize.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_minimize, 0, Qt.AlignTop)

        self.btn_maximize = QPushButton(self.top_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(28, 28))
        self.btn_maximize.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_maximize, 0, Qt.AlignTop)

        self.btn_close = QPushButton(self.top_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(28, 28))
        self.btn_close.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_close, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.top_btns)


        self.verticalLayout_2.addWidget(self.toolBarArea)

        self.contentArea = QFrame(self.central)
        self.contentArea.setObjectName(u"contentArea")
        self.contentArea.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.contentArea)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_content_frame = QFrame(self.contentArea)
        self.main_content_frame.setObjectName(u"main_content_frame")
        self.main_content_frame.setFrameShape(QFrame.StyledPanel)
        self.main_content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_content_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cbx_themes = QComboBox(self.main_content_frame)
        self.cbx_themes.setObjectName(u"cbx_themes")
        self.cbx_themes.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.cbx_themes)

        self.lbl_main_content_frame = QLabel(self.main_content_frame)
        self.lbl_main_content_frame.setObjectName(u"lbl_main_content_frame")

        self.verticalLayout_3.addWidget(self.lbl_main_content_frame, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.main_content_frame)

        self.rightMenu = QFrame(self.contentArea)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMaximumSize(QSize(200, 16777215))
        self.rightMenu.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_rightMenu = QLabel(self.rightMenu)
        self.lbl_rightMenu.setObjectName(u"lbl_rightMenu")

        self.verticalLayout_5.addWidget(self.lbl_rightMenu, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rightMenu)


        self.verticalLayout_2.addWidget(self.contentArea)

        self.statusBar = QFrame(self.central)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 24))
        self.statusBar.setMaximumSize(QSize(16777215, 24))
        self.statusBar.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_autor = QLabel(self.statusBar)
        self.lbl_autor.setObjectName(u"lbl_autor")
        self.lbl_autor.setMinimumSize(QSize(271, 0))

        self.horizontalLayout_6.addWidget(self.lbl_autor)

        self.lbl_db_status = QLabel(self.statusBar)
        self.lbl_db_status.setObjectName(u"lbl_db_status")
        self.lbl_db_status.setMinimumSize(QSize(270, 0))

        self.horizontalLayout_6.addWidget(self.lbl_db_status)

        self.lbl_ver = QLabel(self.statusBar)
        self.lbl_ver.setObjectName(u"lbl_ver")
        self.lbl_ver.setMinimumSize(QSize(175, 0))
        self.lbl_ver.setMaximumSize(QSize(175, 16777215))

        self.horizontalLayout_6.addWidget(self.lbl_ver)

        self.sizegrip = QFrame(self.statusBar)
        self.sizegrip.setObjectName(u"sizegrip")
        self.sizegrip.setMinimumSize(QSize(24, 24))
        self.sizegrip.setMaximumSize(QSize(24, 24))
        self.sizegrip.setFrameShape(QFrame.StyledPanel)
        self.sizegrip.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.sizegrip)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbl_sizegrip = QLabel(self.sizegrip)
        self.lbl_sizegrip.setObjectName(u"lbl_sizegrip")
        self.lbl_sizegrip.setMinimumSize(QSize(24, 24))
        self.lbl_sizegrip.setMaximumSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.lbl_sizegrip)


        self.horizontalLayout_6.addWidget(self.sizegrip)


        self.verticalLayout_2.addWidget(self.statusBar)


        self.horizontalLayout.addWidget(self.central)


        self.verticalLayout.addWidget(self.BgApp)

        MainWindow.setCentralWidget(self.styl)
        self.statusBar_2 = QStatusBar(MainWindow)
        self.statusBar_2.setObjectName(u"statusBar_2")
        MainWindow.setStatusBar(self.statusBar_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_tablica.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_ewidencja.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_rozliczenia.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_settings_user.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lbl_tB.setText(QCoreApplication.translate("MainWindow", u"Tytul", None))
        self.btn_process.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_minimize.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_maximize.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lbl_main_content_frame.setText(QCoreApplication.translate("MainWindow", u"glowne Okno", None))
        self.lbl_rightMenu.setText(QCoreApplication.translate("MainWindow", u"prawe Menu", None))
        self.lbl_autor.setText(QCoreApplication.translate("MainWindow", u" By: Kanios", None))
        self.lbl_db_status.setText(QCoreApplication.translate("MainWindow", u" db: status", None))
        self.lbl_ver.setText(QCoreApplication.translate("MainWindow", u"ver. 0.0.1", None))
        self.lbl_sizegrip.setText(QCoreApplication.translate("MainWindow", u"SG", None))
    # retranslateUi

