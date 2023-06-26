# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerJLBFWv.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 633)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(450, 633))
        MainWindow.setMaximumSize(QSize(450, 633))
        self.css = QWidget(MainWindow)
        self.css.setObjectName(u"css")
        self.css.setStyleSheet(u"#css .QWidget{\n"
"	background-color: rgb(33, 37, 43);	\n"
"}\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	/*font: 10pt \"Segoe UI\";\n"
"	border: none;*/\n"
"	border-radius: 10;\n"
"}\n"
"\n"
"/*BUTTONS*/\n"
"QPushButton {	\n"
"	background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	border-color: rgb(255, 255, 255);\n"
"	border: 2;\n"
"/*	background-color:transparent;\n"
"*/\n"
"	background-color: rgb(40, 44, 52);\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(75, 84, 98);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
" QLineEdit{\n"
"	background-color: rgb(152, 171, 198);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.css)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.login_main = QWidget(self.css)
        self.login_main.setObjectName(u"login_main")
        self.gridLayout = QGridLayout(self.login_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_title = QVBoxLayout()
        self.verticalLayout_title.setObjectName(u"verticalLayout_title")
        self.verticalLayout_title.setSizeConstraint(QLayout.SetFixedSize)
        self.label_title = QLabel(self.login_main)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.label_title.setFont(font)

        self.verticalLayout_title.addWidget(self.label_title)

        self.label_welcome = QLabel(self.login_main)
        self.label_welcome.setObjectName(u"label_welcome")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_welcome.setFont(font1)

        self.verticalLayout_title.addWidget(self.label_welcome)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_title.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout_title)

        self.verticalLayout_user_name = QVBoxLayout()
        self.verticalLayout_user_name.setObjectName(u"verticalLayout_user_name")
        self.verticalLayout_user_name.setSizeConstraint(QLayout.SetFixedSize)
        self.label_user_name = QLabel(self.login_main)
        self.label_user_name.setObjectName(u"label_user_name")
        self.label_user_name.setFont(font1)

        self.verticalLayout_user_name.addWidget(self.label_user_name)

        self.input_lineEdit_user_name = QLineEdit(self.login_main)
        self.input_lineEdit_user_name.setObjectName(u"input_lineEdit_user_name")
        self.input_lineEdit_user_name.setMinimumSize(QSize(333, 47))
        self.input_lineEdit_user_name.setFont(font1)
        self.input_lineEdit_user_name.setClearButtonEnabled(False)

        self.verticalLayout_user_name.addWidget(self.input_lineEdit_user_name)


        self.verticalLayout_2.addLayout(self.verticalLayout_user_name)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalLayout_password = QVBoxLayout()
        self.verticalLayout_password.setObjectName(u"verticalLayout_password")
        self.verticalLayout_password.setSizeConstraint(QLayout.SetFixedSize)
        self.label_4 = QLabel(self.login_main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_password.addWidget(self.label_4)

        self.input_lineEdit_password = QLineEdit(self.login_main)
        self.input_lineEdit_password.setObjectName(u"input_lineEdit_password")
        self.input_lineEdit_password.setMinimumSize(QSize(333, 47))
        self.input_lineEdit_password.setFont(font1)
        self.input_lineEdit_password.setEchoMode(QLineEdit.Password)
        self.input_lineEdit_password.setDragEnabled(False)

        self.verticalLayout_password.addWidget(self.input_lineEdit_password)


        self.verticalLayout_2.addLayout(self.verticalLayout_password)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btn_login = QPushButton(self.login_main)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(333, 47))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_login.setFont(font2)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btn_login)

        self.verticalSpacer_5 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.bottomBar = QFrame(self.login_main)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.bottomBar)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.btn_close = QPushButton(self.login_main)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(28, 28))
        self.btn_close.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(25)
        self.btn_close.setFont(font3)
        self.btn_close.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")
        self.btn_close.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.btn_close, 0, 5, 1, 1)


        self.verticalLayout.addWidget(self.login_main)

        MainWindow.setCentralWidget(self.css)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_welcome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Welcome to IVS System</span></p></body></html>", None))
        self.label_user_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">User name</span></p></body></html>", None))
        self.input_lineEdit_user_name.setText("")
        self.input_lineEdit_user_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Password</span></p></body></html>", None))
        self.input_lineEdit_password.setInputMask("")
        self.input_lineEdit_password.setText("")
        self.input_lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
        self.btn_close.setText("")
    # retranslateUi

