# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_new_desingeDDkPer.ui'
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(992, 809)
        MainWindow.setMinimumSize(QSize(940, 668))
        MainWindow.setStyleSheet(u"")
        self.styl = QWidget(MainWindow)
        self.styl.setObjectName(u"styl")
        self.styl.setMinimumSize(QSize(940, 668))
        self.styl.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.styl)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CentralArea = QFrame(self.styl)
        self.CentralArea.setObjectName(u"CentralArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CentralArea.sizePolicy().hasHeightForWidth())
        self.CentralArea.setSizePolicy(sizePolicy)
        self.CentralArea.setMinimumSize(QSize(940, 668))
        self.CentralArea.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_28 = QVBoxLayout(self.CentralArea)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.toolBarArea = QFrame(self.CentralArea)
        self.toolBarArea.setObjectName(u"toolBarArea")
        self.toolBarArea.setMinimumSize(QSize(0, 60))
        self.toolBarArea.setMaximumSize(QSize(16777215, 60))
        self.toolBarArea.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.toolBarArea)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolBar = QFrame(self.toolBarArea)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy1)
        self.toolBar.setMinimumSize(QSize(0, 60))
        self.toolBar.setMaximumSize(QSize(16777215, 60))
        self.toolBar.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.toolBar)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbl_tB = QLabel(self.toolBar)
        self.lbl_tB.setObjectName(u"lbl_tB")
        self.lbl_tB.setMinimumSize(QSize(0, 60))
        self.lbl_tB.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_7.addWidget(self.lbl_tB)


        self.horizontalLayout_4.addWidget(self.toolBar)


        self.verticalLayout_28.addWidget(self.toolBarArea)

        self.ContentArea = QFrame(self.CentralArea)
        self.ContentArea.setObjectName(u"ContentArea")
        self.ContentArea.setMinimumSize(QSize(940, 668))
        self.ContentArea.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.ContentArea)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.ContentArea)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(0, 668))
        self.leftMenu.setMaximumSize(QSize(63, 16777215))
        self.leftMenu.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_20 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.lm_top = QFrame(self.leftMenu)
        self.lm_top.setObjectName(u"lm_top")
        self.lm_top.setMinimumSize(QSize(0, 60))
        self.lm_top.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_21 = QVBoxLayout(self.lm_top)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, 0, 9)
        self.btn_menu = QPushButton(self.lm_top)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy2)
        self.btn_menu.setMinimumSize(QSize(0, 45))
        self.btn_menu.setMaximumSize(QSize(45, 16777215))

        self.verticalLayout_21.addWidget(self.btn_menu)


        self.verticalLayout_20.addWidget(self.lm_top, 0, Qt.AlignTop)

        self.lm_midlle = QFrame(self.leftMenu)
        self.lm_midlle.setObjectName(u"lm_midlle")
        self.lm_midlle.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_22 = QVBoxLayout(self.lm_midlle)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, 9, 0, 0)
        self.btn_tablica = QPushButton(self.lm_midlle)
        self.btn_tablica.setObjectName(u"btn_tablica")
        sizePolicy2.setHeightForWidth(self.btn_tablica.sizePolicy().hasHeightForWidth())
        self.btn_tablica.setSizePolicy(sizePolicy2)
        self.btn_tablica.setMinimumSize(QSize(0, 45))
        self.btn_tablica.setMaximumSize(QSize(45, 16777215))

        self.verticalLayout_22.addWidget(self.btn_tablica)

        self.btn_ewidencja = QPushButton(self.lm_midlle)
        self.btn_ewidencja.setObjectName(u"btn_ewidencja")
        sizePolicy2.setHeightForWidth(self.btn_ewidencja.sizePolicy().hasHeightForWidth())
        self.btn_ewidencja.setSizePolicy(sizePolicy2)
        self.btn_ewidencja.setMinimumSize(QSize(0, 45))
        self.btn_ewidencja.setMaximumSize(QSize(45, 16777215))

        self.verticalLayout_22.addWidget(self.btn_ewidencja)

        self.btn_rozliczenia = QPushButton(self.lm_midlle)
        self.btn_rozliczenia.setObjectName(u"btn_rozliczenia")
        sizePolicy2.setHeightForWidth(self.btn_rozliczenia.sizePolicy().hasHeightForWidth())
        self.btn_rozliczenia.setSizePolicy(sizePolicy2)
        self.btn_rozliczenia.setMinimumSize(QSize(0, 45))
        self.btn_rozliczenia.setMaximumSize(QSize(45, 16777215))

        self.verticalLayout_22.addWidget(self.btn_rozliczenia)


        self.verticalLayout_20.addWidget(self.lm_midlle, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer)

        self.lm_botton = QFrame(self.leftMenu)
        self.lm_botton.setObjectName(u"lm_botton")
        self.lm_botton.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_23 = QVBoxLayout(self.lm_botton)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(9, 9, 0, 9)
        self.btn_settings_user = QPushButton(self.lm_botton)
        self.btn_settings_user.setObjectName(u"btn_settings_user")
        sizePolicy2.setHeightForWidth(self.btn_settings_user.sizePolicy().hasHeightForWidth())
        self.btn_settings_user.setSizePolicy(sizePolicy2)
        self.btn_settings_user.setMinimumSize(QSize(0, 45))
        self.btn_settings_user.setMaximumSize(QSize(45, 16777215))

        self.verticalLayout_23.addWidget(self.btn_settings_user)


        self.verticalLayout_20.addWidget(self.lm_botton, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.contentArea = QFrame(self.ContentArea)
        self.contentArea.setObjectName(u"contentArea")
        self.contentArea.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_29 = QVBoxLayout(self.contentArea)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.MainArea = QFrame(self.contentArea)
        self.MainArea.setObjectName(u"MainArea")
        self.MainArea.setFrameShape(QFrame.StyledPanel)
        self.MainArea.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.MainArea)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.leftMenu_mini = QFrame(self.MainArea)
        self.leftMenu_mini.setObjectName(u"leftMenu_mini")
        self.leftMenu_mini.setMinimumSize(QSize(150, 0))
        self.leftMenu_mini.setMaximumSize(QSize(150, 16777215))
        self.leftMenu_mini.setFrameShape(QFrame.StyledPanel)
        self.leftMenu_mini.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.leftMenu_mini)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_10.addWidget(self.leftMenu_mini)

        self.Main_Content_Area = QFrame(self.MainArea)
        self.Main_Content_Area.setObjectName(u"Main_Content_Area")
        self.Main_Content_Area.setFrameShape(QFrame.StyledPanel)
        self.Main_Content_Area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.Main_Content_Area)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.MainHeading = QFrame(self.Main_Content_Area)
        self.MainHeading.setObjectName(u"MainHeading")
        self.MainHeading.setMinimumSize(QSize(0, 60))
        self.MainHeading.setMaximumSize(QSize(16777215, 60))
        self.MainHeading.setFrameShape(QFrame.StyledPanel)
        self.MainHeading.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.MainHeading)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.MainHeading)
        self.label.setObjectName(u"label")

        self.verticalLayout_30.addWidget(self.label)


        self.verticalLayout_25.addWidget(self.MainHeading)

        self.Main = QFrame(self.Main_Content_Area)
        self.Main.setObjectName(u"Main")
        self.Main.setFrameShape(QFrame.StyledPanel)
        self.Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.Main)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.cbx_themes = QComboBox(self.Main)
        self.cbx_themes.setObjectName(u"cbx_themes")
        self.cbx_themes.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_19.addWidget(self.cbx_themes)

        self.lineEdit = QLineEdit(self.Main)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_19.addWidget(self.lineEdit)

        self.lbl_main_content_frame = QLabel(self.Main)
        self.lbl_main_content_frame.setObjectName(u"lbl_main_content_frame")

        self.verticalLayout_19.addWidget(self.lbl_main_content_frame)


        self.verticalLayout_25.addWidget(self.Main)


        self.horizontalLayout_10.addWidget(self.Main_Content_Area)

        self.rightMenu = QFrame(self.MainArea)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMaximumSize(QSize(200, 16777215))
        self.rightMenu.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_26 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.lbl_rightMenu = QLabel(self.rightMenu)
        self.lbl_rightMenu.setObjectName(u"lbl_rightMenu")

        self.verticalLayout_26.addWidget(self.lbl_rightMenu, 0, Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.rightMenu)


        self.verticalLayout_29.addWidget(self.MainArea)

        self.statusBar = QFrame(self.contentArea)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 24))
        self.statusBar.setMaximumSize(QSize(16777215, 24))
        self.statusBar.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lbl_autor = QLabel(self.statusBar)
        self.lbl_autor.setObjectName(u"lbl_autor")
        self.lbl_autor.setMinimumSize(QSize(271, 0))

        self.horizontalLayout_11.addWidget(self.lbl_autor)

        self.lbl_db_status = QLabel(self.statusBar)
        self.lbl_db_status.setObjectName(u"lbl_db_status")
        self.lbl_db_status.setMinimumSize(QSize(270, 0))

        self.horizontalLayout_11.addWidget(self.lbl_db_status)

        self.lbl_ver = QLabel(self.statusBar)
        self.lbl_ver.setObjectName(u"lbl_ver")
        self.lbl_ver.setMinimumSize(QSize(175, 0))
        self.lbl_ver.setMaximumSize(QSize(175, 16777215))

        self.horizontalLayout_11.addWidget(self.lbl_ver)

        self.sizegrip = QFrame(self.statusBar)
        self.sizegrip.setObjectName(u"sizegrip")
        self.sizegrip.setMinimumSize(QSize(24, 24))
        self.sizegrip.setMaximumSize(QSize(24, 24))
        self.sizegrip.setFrameShape(QFrame.StyledPanel)
        self.sizegrip.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.sizegrip)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_11.addWidget(self.sizegrip)


        self.verticalLayout_29.addWidget(self.statusBar)


        self.horizontalLayout.addWidget(self.contentArea)


        self.verticalLayout_28.addWidget(self.ContentArea)


        self.verticalLayout.addWidget(self.CentralArea)

        MainWindow.setCentralWidget(self.styl)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_tB.setText(QCoreApplication.translate("MainWindow", u"Tytul", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_tablica.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_ewidencja.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_rozliczenia.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_settings_user.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lbl_main_content_frame.setText(QCoreApplication.translate("MainWindow", u"glowne Okno", None))
        self.lbl_rightMenu.setText(QCoreApplication.translate("MainWindow", u"Lista zada\u0144", None))
        self.lbl_autor.setText(QCoreApplication.translate("MainWindow", u" By: Kanios", None))
        self.lbl_db_status.setText(QCoreApplication.translate("MainWindow", u" db: status", None))
        self.lbl_ver.setText(QCoreApplication.translate("MainWindow", u"ver. 0.0.1", None))
    # retranslateUi

