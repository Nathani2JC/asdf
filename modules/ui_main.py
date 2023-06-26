# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainYEVJKu.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTextBrowser,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1284, 719)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp"
                        " {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	image: url(:/images/images/images/PyDracula_vertical.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	backgro"
                        "und-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	backg"
                        "round-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#ext"
                        "raContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"/* Extra Setting Menus*/\n"
"#scrollAreaWidgetContents_ss {\n"
"	background-color: transparent;\n"
"}\n"
"#scrollArea_ss {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#scrollArea_ss .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#scrollArea_"
                        "ss .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#scrollArea_ss .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bo"
                        "ttomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
""
                        "}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLine"
                        "Edit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* //////////"
                        "///////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
""
                        "     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar:"
                        ":down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    backgro"
                        "und: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	backgrou"
                        "nd-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    wid"
                        "th: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
""
                        "}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Cameras */\n"
"QVideoWidget {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QVideoWidget:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QVideoWidget:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"\n"
""
                        "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Spin box */\n"
"QDoubleSpinBox {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QDoubleSpinBox:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Cameras */\n"
"#pushButton_2 {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pushButton_2 :hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pushButton_2 :pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""
                        "\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_72 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.topLogoInfo)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.topLogoInfo)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 16777215))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalLayout_18.addWidget(self.toggleBox)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-dashboard.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_live_feed = QPushButton(self.topMenu)
        self.btn_live_feed.setObjectName(u"btn_live_feed")
        sizePolicy.setHeightForWidth(self.btn_live_feed.sizePolicy().hasHeightForWidth())
        self.btn_live_feed.setSizePolicy(sizePolicy)
        self.btn_live_feed.setMinimumSize(QSize(0, 45))
        self.btn_live_feed.setFont(font)
        self.btn_live_feed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_live_feed.setLayoutDirection(Qt.LeftToRight)
        self.btn_live_feed.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-computer.png);")

        self.verticalLayout_8.addWidget(self.btn_live_feed)

        self.btn_detections = QPushButton(self.topMenu)
        self.btn_detections.setObjectName(u"btn_detections")
        sizePolicy.setHeightForWidth(self.btn_detections.sizePolicy().hasHeightForWidth())
        self.btn_detections.setSizePolicy(sizePolicy)
        self.btn_detections.setMinimumSize(QSize(0, 45))
        self.btn_detections.setFont(font)
        self.btn_detections.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_detections.setLayoutDirection(Qt.LeftToRight)
        self.btn_detections.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-search.png);")

        self.verticalLayout_8.addWidget(self.btn_detections)

        self.btn_alert = QPushButton(self.topMenu)
        self.btn_alert.setObjectName(u"btn_alert")
        sizePolicy.setHeightForWidth(self.btn_alert.sizePolicy().hasHeightForWidth())
        self.btn_alert.setSizePolicy(sizePolicy)
        self.btn_alert.setMinimumSize(QSize(0, 45))
        self.btn_alert.setFont(font)
        self.btn_alert.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alert.setLayoutDirection(Qt.LeftToRight)
        self.btn_alert.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-bell.png);")

        self.verticalLayout_8.addWidget(self.btn_alert)

        self.btn_recordes = QPushButton(self.topMenu)
        self.btn_recordes.setObjectName(u"btn_recordes")
        sizePolicy.setHeightForWidth(self.btn_recordes.sizePolicy().hasHeightForWidth())
        self.btn_recordes.setSizePolicy(sizePolicy)
        self.btn_recordes.setMinimumSize(QSize(0, 45))
        self.btn_recordes.setFont(font)
        self.btn_recordes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_recordes.setLayoutDirection(Qt.LeftToRight)
        self.btn_recordes.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gallery.png);")

        self.verticalLayout_8.addWidget(self.btn_recordes)

        self.btn_vr_model = QPushButton(self.topMenu)
        self.btn_vr_model.setObjectName(u"btn_vr_model")
        sizePolicy.setHeightForWidth(self.btn_vr_model.sizePolicy().hasHeightForWidth())
        self.btn_vr_model.setSizePolicy(sizePolicy)
        self.btn_vr_model.setMinimumSize(QSize(0, 45))
        self.btn_vr_model.setFont(font)
        self.btn_vr_model.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_vr_model.setLayoutDirection(Qt.LeftToRight)
        self.btn_vr_model.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cube.png);")

        self.verticalLayout_8.addWidget(self.btn_vr_model)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setMinimumSize(QSize(410, 0))
        self.extraContent.setMaximumSize(QSize(16777215, 16777215))
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraContent)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.scrollArea_ss = QScrollArea(self.extraContent)
        self.scrollArea_ss.setObjectName(u"scrollArea_ss")
        self.scrollArea_ss.setMouseTracking(False)
        self.scrollArea_ss.setFocusPolicy(Qt.NoFocus)
        self.scrollArea_ss.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.scrollArea_ss.setAutoFillBackground(False)
        self.scrollArea_ss.setStyleSheet(u"")
        self.scrollArea_ss.setFrameShape(QFrame.NoFrame)
        self.scrollArea_ss.setFrameShadow(QFrame.Raised)
        self.scrollArea_ss.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_ss.setWidgetResizable(True)
        self.scrollAreaWidgetContents_ss = QWidget()
        self.scrollAreaWidgetContents_ss.setObjectName(u"scrollAreaWidgetContents_ss")
        self.scrollAreaWidgetContents_ss.setGeometry(QRect(0, 0, 393, 736))
        self.scrollAreaWidgetContents_ss.setMouseTracking(True)
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_ss)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.scrollAreaWidgetContents_ss)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.widget_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.widget_2)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_16.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.widget_2)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_16.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.widget_2)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_16.addWidget(self.btn_more)

        self.pushButton_18 = QPushButton(self.widget_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 45))
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_18)

        self.pushButton_35 = QPushButton(self.widget_2)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(0, 45))

        self.verticalLayout_16.addWidget(self.pushButton_35)

        self.pushButton_15 = QPushButton(self.widget_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 45))
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_15)

        self.pushButton_17 = QPushButton(self.widget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(0, 45))
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_17)

        self.pushButton_33 = QPushButton(self.widget_2)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(0, 45))
        self.pushButton_33.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_33)

        self.pushButton_27 = QPushButton(self.widget_2)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(0, 45))
        self.pushButton_27.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_27)

        self.pushButton_30 = QPushButton(self.widget_2)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(0, 45))
        self.pushButton_30.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_30)

        self.pushButton_31 = QPushButton(self.widget_2)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(0, 45))
        self.pushButton_31.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_31)

        self.pushButton_28 = QPushButton(self.widget_2)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(0, 45))
        self.pushButton_28.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_28)

        self.pushButton_16 = QPushButton(self.widget_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 45))
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_16)

        self.pushButton_34 = QPushButton(self.widget_2)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(0, 45))
        self.pushButton_34.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_34)

        self.pushButton_32 = QPushButton(self.widget_2)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(0, 45))
        self.pushButton_32.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_32)

        self.pushButton_29 = QPushButton(self.widget_2)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(0, 45))
        self.pushButton_29.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.pushButton_29)


        self.verticalLayout_12.addWidget(self.widget_2, 0, Qt.AlignVCenter)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents_ss)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_12.addWidget(self.widget_3, 0, Qt.AlignBottom)

        self.scrollArea_ss.setWidget(self.scrollAreaWidgetContents_ss)

        self.verticalLayout_11.addWidget(self.scrollArea_ss)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.alertsAppBtn = QPushButton(self.rightButtons)
        self.alertsAppBtn.setObjectName(u"alertsAppBtn")
        self.alertsAppBtn.setMinimumSize(QSize(28, 28))
        self.alertsAppBtn.setMaximumSize(QSize(28, 28))
        self.alertsAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-bell-ring.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/images/icons/cil-notification.png", QSize(), QIcon.Normal, QIcon.On)
        self.alertsAppBtn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.alertsAppBtn)

        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.live_feed = QWidget()
        self.live_feed.setObjectName(u"live_feed")
        self.live_feed.setStyleSheet(u"border: none;")
        self.verticalLayout_25 = QVBoxLayout(self.live_feed)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.live_cameras = QFrame(self.live_feed)
        self.live_cameras.setObjectName(u"live_cameras")
        self.live_cameras.setFrameShape(QFrame.StyledPanel)
        self.live_cameras.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.live_cameras)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.live_feed_cameras = QFrame(self.live_cameras)
        self.live_feed_cameras.setObjectName(u"live_feed_cameras")
        self.live_feed_cameras.setMinimumSize(QSize(0, 400))
        self.live_feed_cameras.setStyleSheet(u"")
        self.live_feed_cameras.setFrameShape(QFrame.StyledPanel)
        self.live_feed_cameras.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.live_feed_cameras)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.title_live_feed_1 = QLabel(self.live_feed_cameras)
        self.title_live_feed_1.setObjectName(u"title_live_feed_1")

        self.verticalLayout_54.addWidget(self.title_live_feed_1)

        self.scrollArea_live_feed = QScrollArea(self.live_feed_cameras)
        self.scrollArea_live_feed.setObjectName(u"scrollArea_live_feed")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea_live_feed.sizePolicy().hasHeightForWidth())
        self.scrollArea_live_feed.setSizePolicy(sizePolicy3)
        self.scrollArea_live_feed.setWidgetResizable(True)
        self.scrollAreaWidgetContents_live_feed = QWidget()
        self.scrollAreaWidgetContents_live_feed.setObjectName(u"scrollAreaWidgetContents_live_feed")
        self.scrollAreaWidgetContents_live_feed.setGeometry(QRect(0, 0, 1148, 545))
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContents_live_feed)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.live_feed_cameras_1 = QFrame(self.scrollAreaWidgetContents_live_feed)
        self.live_feed_cameras_1.setObjectName(u"live_feed_cameras_1")
        self.live_feed_cameras_1.setMinimumSize(QSize(0, 100))
        self.live_feed_cameras_1.setFrameShape(QFrame.StyledPanel)
        self.live_feed_cameras_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.live_feed_cameras_1)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")

        self.verticalLayout_34.addWidget(self.live_feed_cameras_1)

        self.scrollArea_live_feed.setWidget(self.scrollAreaWidgetContents_live_feed)

        self.verticalLayout_54.addWidget(self.scrollArea_live_feed)


        self.horizontalLayout_27.addWidget(self.live_feed_cameras)


        self.verticalLayout_25.addWidget(self.live_cameras)

        self.stackedWidget.addWidget(self.live_feed)
        self.live_feed_2 = QWidget()
        self.live_feed_2.setObjectName(u"live_feed_2")
        self.gridLayout_5 = QGridLayout(self.live_feed_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.live_feed_2_left = QFrame(self.live_feed_2)
        self.live_feed_2_left.setObjectName(u"live_feed_2_left")
        self.live_feed_2_left.setMinimumSize(QSize(200, 0))
        self.live_feed_2_left.setFrameShape(QFrame.StyledPanel)
        self.live_feed_2_left.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.live_feed_2_left, 1, 1, 1, 1)

        self.live_feed_2_main = QFrame(self.live_feed_2)
        self.live_feed_2_main.setObjectName(u"live_feed_2_main")
        self.live_feed_2_main.setFrameShape(QFrame.StyledPanel)
        self.live_feed_2_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.live_feed_2_main)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.live_feed_2_main_display = QWidget(self.live_feed_2_main)
        self.live_feed_2_main_display.setObjectName(u"live_feed_2_main_display")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(5)
        sizePolicy4.setHeightForWidth(self.live_feed_2_main_display.sizePolicy().hasHeightForWidth())
        self.live_feed_2_main_display.setSizePolicy(sizePolicy4)

        self.verticalLayout_71.addWidget(self.live_feed_2_main_display)

        self.live_feed_2_main_display_list = QWidget(self.live_feed_2_main)
        self.live_feed_2_main_display_list.setObjectName(u"live_feed_2_main_display_list")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.live_feed_2_main_display_list.sizePolicy().hasHeightForWidth())
        self.live_feed_2_main_display_list.setSizePolicy(sizePolicy5)
        self.live_feed_2_main_display_list.setMinimumSize(QSize(150, 0))
        self.live_feed_2_main_display_list.setMaximumSize(QSize(16777215, 50))
        self.live_feed_2_main_display_list.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_49 = QVBoxLayout(self.live_feed_2_main_display_list)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(-1, 0, -1, 0)
        self.btn_live_feed_2_main_display_list_edit = QPushButton(self.live_feed_2_main_display_list)
        self.btn_live_feed_2_main_display_list_edit.setObjectName(u"btn_live_feed_2_main_display_list_edit")

        self.verticalLayout_49.addWidget(self.btn_live_feed_2_main_display_list_edit)

        self.widget_live_feed_2_main_display_list = QWidget(self.live_feed_2_main_display_list)
        self.widget_live_feed_2_main_display_list.setObjectName(u"widget_live_feed_2_main_display_list")
        self.widget_live_feed_2_main_display_list.setMaximumSize(QSize(16777215, 0))

        self.verticalLayout_49.addWidget(self.widget_live_feed_2_main_display_list)


        self.verticalLayout_71.addWidget(self.live_feed_2_main_display_list)


        self.gridLayout_5.addWidget(self.live_feed_2_main, 1, 0, 1, 1)

        self.title_live_feed_2 = QLabel(self.live_feed_2)
        self.title_live_feed_2.setObjectName(u"title_live_feed_2")

        self.gridLayout_5.addWidget(self.title_live_feed_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.live_feed_2)
        self.vr_model = QWidget()
        self.vr_model.setObjectName(u"vr_model")
        self.horizontalLayout_20 = QHBoxLayout(self.vr_model)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, -1, -1, 0)
        self.vr_model_main = QWidget(self.vr_model)
        self.vr_model_main.setObjectName(u"vr_model_main")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(7)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.vr_model_main.sizePolicy().hasHeightForWidth())
        self.vr_model_main.setSizePolicy(sizePolicy6)
        self.verticalLayout_35 = QVBoxLayout(self.vr_model_main)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, -1, -1, 0)
        self.title_vr_model = QLabel(self.vr_model_main)
        self.title_vr_model.setObjectName(u"title_vr_model")

        self.verticalLayout_35.addWidget(self.title_vr_model)

        self.vr_model_3d = QWidget(self.vr_model_main)
        self.vr_model_3d.setObjectName(u"vr_model_3d")
        self.vr_model_3d.setStyleSheet(u"")
        self.verticalLayout_38 = QVBoxLayout(self.vr_model_3d)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.vr_model_3d)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_38.addWidget(self.widget)


        self.verticalLayout_35.addWidget(self.vr_model_3d)

        self.vr_model_3d_cordinates = QFrame(self.vr_model_main)
        self.vr_model_3d_cordinates.setObjectName(u"vr_model_3d_cordinates")
        self.vr_model_3d_cordinates.setMinimumSize(QSize(0, 100))
        self.vr_model_3d_cordinates.setMaximumSize(QSize(16777215, 120))
        self.vr_model_3d_cordinates.setFrameShape(QFrame.StyledPanel)
        self.vr_model_3d_cordinates.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.vr_model_3d_cordinates)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(9, 0, 9, 0)
        self.vr_model_3d_include = QFrame(self.vr_model_3d_cordinates)
        self.vr_model_3d_include.setObjectName(u"vr_model_3d_include")
        self.vr_model_3d_include.setMinimumSize(QSize(100, 0))
        self.vr_model_3d_include.setFrameShape(QFrame.StyledPanel)
        self.vr_model_3d_include.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.vr_model_3d_include)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, -1, -1, 0)
        self.radioButton_vr_model_3d_include = QRadioButton(self.vr_model_3d_include)
        self.radioButton_vr_model_3d_include.setObjectName(u"radioButton_vr_model_3d_include")

        self.verticalLayout_36.addWidget(self.radioButton_vr_model_3d_include)


        self.horizontalLayout_30.addWidget(self.vr_model_3d_include)

        self.vr_model_3d_position = QFrame(self.vr_model_3d_cordinates)
        self.vr_model_3d_position.setObjectName(u"vr_model_3d_position")
        self.vr_model_3d_position.setFrameShape(QFrame.StyledPanel)
        self.vr_model_3d_position.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.vr_model_3d_position)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(-1, -1, -1, 0)
        self.label_vr_model_3d_position = QLabel(self.vr_model_3d_position)
        self.label_vr_model_3d_position.setObjectName(u"label_vr_model_3d_position")

        self.verticalLayout_39.addWidget(self.label_vr_model_3d_position)

        self.horizontalLayout_3d_position = QHBoxLayout()
        self.horizontalLayout_3d_position.setObjectName(u"horizontalLayout_3d_position")
        self.verticalLayout_3d_position_x = QVBoxLayout()
        self.verticalLayout_3d_position_x.setObjectName(u"verticalLayout_3d_position_x")
        self.horizontalSlider_3d_position_x = QSlider(self.vr_model_3d_position)
        self.horizontalSlider_3d_position_x.setObjectName(u"horizontalSlider_3d_position_x")
        self.horizontalSlider_3d_position_x.setMinimum(-99)
        self.horizontalSlider_3d_position_x.setOrientation(Qt.Horizontal)

        self.verticalLayout_3d_position_x.addWidget(self.horizontalSlider_3d_position_x)

        self.vr_3d_position_x = QDoubleSpinBox(self.vr_model_3d_position)
        self.vr_3d_position_x.setObjectName(u"vr_3d_position_x")
        self.vr_3d_position_x.setMinimum(-99.989999999999995)

        self.verticalLayout_3d_position_x.addWidget(self.vr_3d_position_x)

        self.label_vr_model_3d_position_x = QLabel(self.vr_model_3d_position)
        self.label_vr_model_3d_position_x.setObjectName(u"label_vr_model_3d_position_x")

        self.verticalLayout_3d_position_x.addWidget(self.label_vr_model_3d_position_x)


        self.horizontalLayout_3d_position.addLayout(self.verticalLayout_3d_position_x)

        self.verticalLayout_3d_position_z = QVBoxLayout()
        self.verticalLayout_3d_position_z.setObjectName(u"verticalLayout_3d_position_z")
        self.horizontalSlider_3d_position_z = QSlider(self.vr_model_3d_position)
        self.horizontalSlider_3d_position_z.setObjectName(u"horizontalSlider_3d_position_z")
        self.horizontalSlider_3d_position_z.setMinimum(-99)
        self.horizontalSlider_3d_position_z.setOrientation(Qt.Horizontal)

        self.verticalLayout_3d_position_z.addWidget(self.horizontalSlider_3d_position_z)

        self.vr_3d_position_z = QDoubleSpinBox(self.vr_model_3d_position)
        self.vr_3d_position_z.setObjectName(u"vr_3d_position_z")
        self.vr_3d_position_z.setMinimum(-99.989999999999995)

        self.verticalLayout_3d_position_z.addWidget(self.vr_3d_position_z)

        self.label_vr_model_3d_position_z = QLabel(self.vr_model_3d_position)
        self.label_vr_model_3d_position_z.setObjectName(u"label_vr_model_3d_position_z")

        self.verticalLayout_3d_position_z.addWidget(self.label_vr_model_3d_position_z)


        self.horizontalLayout_3d_position.addLayout(self.verticalLayout_3d_position_z)

        self.verticalLayout_3d_position_y = QVBoxLayout()
        self.verticalLayout_3d_position_y.setObjectName(u"verticalLayout_3d_position_y")
        self.horizontalSlider_3d_position_y = QSlider(self.vr_model_3d_position)
        self.horizontalSlider_3d_position_y.setObjectName(u"horizontalSlider_3d_position_y")
        self.horizontalSlider_3d_position_y.setMinimum(-99)
        self.horizontalSlider_3d_position_y.setOrientation(Qt.Horizontal)

        self.verticalLayout_3d_position_y.addWidget(self.horizontalSlider_3d_position_y)

        self.vr_3d_position_y = QDoubleSpinBox(self.vr_model_3d_position)
        self.vr_3d_position_y.setObjectName(u"vr_3d_position_y")
        self.vr_3d_position_y.setMinimum(-99.989999999999995)

        self.verticalLayout_3d_position_y.addWidget(self.vr_3d_position_y)

        self.label_vr_model_3d_position_y = QLabel(self.vr_model_3d_position)
        self.label_vr_model_3d_position_y.setObjectName(u"label_vr_model_3d_position_y")

        self.verticalLayout_3d_position_y.addWidget(self.label_vr_model_3d_position_y)


        self.horizontalLayout_3d_position.addLayout(self.verticalLayout_3d_position_y)


        self.verticalLayout_39.addLayout(self.horizontalLayout_3d_position)


        self.horizontalLayout_30.addWidget(self.vr_model_3d_position)

        self.vr_model_3d_view = QFrame(self.vr_model_3d_cordinates)
        self.vr_model_3d_view.setObjectName(u"vr_model_3d_view")
        self.vr_model_3d_view.setFrameShape(QFrame.StyledPanel)
        self.vr_model_3d_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.vr_model_3d_view)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(-1, -1, -1, 0)
        self.label_vr_model_3d_view = QLabel(self.vr_model_3d_view)
        self.label_vr_model_3d_view.setObjectName(u"label_vr_model_3d_view")

        self.verticalLayout_62.addWidget(self.label_vr_model_3d_view)

        self.horizontalLayout_3d_position_2 = QHBoxLayout()
        self.horizontalLayout_3d_position_2.setObjectName(u"horizontalLayout_3d_position_2")
        self.verticalLayout_3d_position_x_2 = QVBoxLayout()
        self.verticalLayout_3d_position_x_2.setObjectName(u"verticalLayout_3d_position_x_2")
        self.horizontalSlider_3d_position_x_2 = QSlider(self.vr_model_3d_view)
        self.horizontalSlider_3d_position_x_2.setObjectName(u"horizontalSlider_3d_position_x_2")
        self.horizontalSlider_3d_position_x_2.setMinimum(-99)
        self.horizontalSlider_3d_position_x_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3d_position_x_2.addWidget(self.horizontalSlider_3d_position_x_2)

        self.vr_3d_position_x_2 = QDoubleSpinBox(self.vr_model_3d_view)
        self.vr_3d_position_x_2.setObjectName(u"vr_3d_position_x_2")
        self.vr_3d_position_x_2.setMinimum(-99.989999999999995)

        self.verticalLayout_3d_position_x_2.addWidget(self.vr_3d_position_x_2)

        self.label_vr_model_3d_position_x_2 = QLabel(self.vr_model_3d_view)
        self.label_vr_model_3d_position_x_2.setObjectName(u"label_vr_model_3d_position_x_2")

        self.verticalLayout_3d_position_x_2.addWidget(self.label_vr_model_3d_position_x_2)


        self.horizontalLayout_3d_position_2.addLayout(self.verticalLayout_3d_position_x_2)

        self.verticalLayout_3d_position_z_2 = QVBoxLayout()
        self.verticalLayout_3d_position_z_2.setObjectName(u"verticalLayout_3d_position_z_2")
        self.horizontalSlider_3d_position_z_2 = QSlider(self.vr_model_3d_view)
        self.horizontalSlider_3d_position_z_2.setObjectName(u"horizontalSlider_3d_position_z_2")
        self.horizontalSlider_3d_position_z_2.setMinimum(-99)
        self.horizontalSlider_3d_position_z_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3d_position_z_2.addWidget(self.horizontalSlider_3d_position_z_2)

        self.vr_3d_position_z_2 = QDoubleSpinBox(self.vr_model_3d_view)
        self.vr_3d_position_z_2.setObjectName(u"vr_3d_position_z_2")
        self.vr_3d_position_z_2.setMinimum(-99.989999999999995)

        self.verticalLayout_3d_position_z_2.addWidget(self.vr_3d_position_z_2)

        self.label_vr_model_3d_position_z_2 = QLabel(self.vr_model_3d_view)
        self.label_vr_model_3d_position_z_2.setObjectName(u"label_vr_model_3d_position_z_2")

        self.verticalLayout_3d_position_z_2.addWidget(self.label_vr_model_3d_position_z_2)


        self.horizontalLayout_3d_position_2.addLayout(self.verticalLayout_3d_position_z_2)

        self.verticalLayout_3d_position_y_2 = QVBoxLayout()
        self.verticalLayout_3d_position_y_2.setObjectName(u"verticalLayout_3d_position_y_2")
        self.horizontalSlider_3d_position_y_2 = QSlider(self.vr_model_3d_view)
        self.horizontalSlider_3d_position_y_2.setObjectName(u"horizontalSlider_3d_position_y_2")
        self.horizontalSlider_3d_position_y_2.setMinimum(-99)
        self.horizontalSlider_3d_position_y_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_3d_position_y_2.addWidget(self.horizontalSlider_3d_position_y_2)

        self.vr_3d_position_y_2 = QDoubleSpinBox(self.vr_model_3d_view)
        self.vr_3d_position_y_2.setObjectName(u"vr_3d_position_y_2")
        self.vr_3d_position_y_2.setMinimum(-99.989999999999995)

        self.verticalLayout_3d_position_y_2.addWidget(self.vr_3d_position_y_2)

        self.label_vr_model_3d_position_y_2 = QLabel(self.vr_model_3d_view)
        self.label_vr_model_3d_position_y_2.setObjectName(u"label_vr_model_3d_position_y_2")

        self.verticalLayout_3d_position_y_2.addWidget(self.label_vr_model_3d_position_y_2)


        self.horizontalLayout_3d_position_2.addLayout(self.verticalLayout_3d_position_y_2)


        self.verticalLayout_62.addLayout(self.horizontalLayout_3d_position_2)


        self.horizontalLayout_30.addWidget(self.vr_model_3d_view)


        self.verticalLayout_35.addWidget(self.vr_model_3d_cordinates)


        self.horizontalLayout_20.addWidget(self.vr_model_main)

        self.vr_model_right = QWidget(self.vr_model)
        self.vr_model_right.setObjectName(u"vr_model_right")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(3)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.vr_model_right.sizePolicy().hasHeightForWidth())
        self.vr_model_right.setSizePolicy(sizePolicy7)
        self.vr_model_right.setMinimumSize(QSize(200, 0))
        self.verticalLayout_37 = QVBoxLayout(self.vr_model_right)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, -1, -1, 0)
        self.vr_model_left_map = QWidget(self.vr_model_right)
        self.vr_model_left_map.setObjectName(u"vr_model_left_map")

        self.verticalLayout_37.addWidget(self.vr_model_left_map)

        self.map_cordinates = QFrame(self.vr_model_right)
        self.map_cordinates.setObjectName(u"map_cordinates")
        self.map_cordinates.setMinimumSize(QSize(0, 150))
        self.map_cordinates.setMaximumSize(QSize(16777215, 200))
        self.map_cordinates.setFrameShape(QFrame.StyledPanel)
        self.map_cordinates.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.map_cordinates)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_100.setContentsMargins(-1, -1, -1, 0)
        self.vr_model_map_view = QFrame(self.map_cordinates)
        self.vr_model_map_view.setObjectName(u"vr_model_map_view")
        self.vr_model_map_view.setFrameShape(QFrame.StyledPanel)
        self.vr_model_map_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.vr_model_map_view)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(-1, -1, -1, 0)
        self.label_vr_model_map_view = QLabel(self.vr_model_map_view)
        self.label_vr_model_map_view.setObjectName(u"label_vr_model_map_view")

        self.verticalLayout_98.addWidget(self.label_vr_model_map_view)

        self.horizontalLayout_map_view = QHBoxLayout()
        self.horizontalLayout_map_view.setObjectName(u"horizontalLayout_map_view")
        self.verticalLayout_map_view_x = QVBoxLayout()
        self.verticalLayout_map_view_x.setObjectName(u"verticalLayout_map_view_x")
        self.horizontalSlider_map_view_x = QSlider(self.vr_model_map_view)
        self.horizontalSlider_map_view_x.setObjectName(u"horizontalSlider_map_view_x")
        self.horizontalSlider_map_view_x.setMinimum(-99)
        self.horizontalSlider_map_view_x.setOrientation(Qt.Horizontal)

        self.verticalLayout_map_view_x.addWidget(self.horizontalSlider_map_view_x)

        self.label_vr_model_map_view_x = QLabel(self.vr_model_map_view)
        self.label_vr_model_map_view_x.setObjectName(u"label_vr_model_map_view_x")

        self.verticalLayout_map_view_x.addWidget(self.label_vr_model_map_view_x)


        self.horizontalLayout_map_view.addLayout(self.verticalLayout_map_view_x)

        self.verticalLayout_map_view_z = QVBoxLayout()
        self.verticalLayout_map_view_z.setObjectName(u"verticalLayout_map_view_z")
        self.horizontalSlider_map_view_z = QSlider(self.vr_model_map_view)
        self.horizontalSlider_map_view_z.setObjectName(u"horizontalSlider_map_view_z")
        self.horizontalSlider_map_view_z.setMinimum(-99)
        self.horizontalSlider_map_view_z.setOrientation(Qt.Horizontal)

        self.verticalLayout_map_view_z.addWidget(self.horizontalSlider_map_view_z)

        self.label_vr_model_map_view_z = QLabel(self.vr_model_map_view)
        self.label_vr_model_map_view_z.setObjectName(u"label_vr_model_map_view_z")

        self.verticalLayout_map_view_z.addWidget(self.label_vr_model_map_view_z)


        self.horizontalLayout_map_view.addLayout(self.verticalLayout_map_view_z)

        self.verticalLayout_map_view_y = QVBoxLayout()
        self.verticalLayout_map_view_y.setObjectName(u"verticalLayout_map_view_y")
        self.horizontalSlider_map_view_y = QSlider(self.vr_model_map_view)
        self.horizontalSlider_map_view_y.setObjectName(u"horizontalSlider_map_view_y")
        self.horizontalSlider_map_view_y.setMinimum(-99)
        self.horizontalSlider_map_view_y.setOrientation(Qt.Horizontal)

        self.verticalLayout_map_view_y.addWidget(self.horizontalSlider_map_view_y)

        self.label_vr_model_map_view_y = QLabel(self.vr_model_map_view)
        self.label_vr_model_map_view_y.setObjectName(u"label_vr_model_map_view_y")

        self.verticalLayout_map_view_y.addWidget(self.label_vr_model_map_view_y)


        self.horizontalLayout_map_view.addLayout(self.verticalLayout_map_view_y)


        self.verticalLayout_98.addLayout(self.horizontalLayout_map_view)


        self.verticalLayout_100.addWidget(self.vr_model_map_view)

        self.vr_model_map_position = QFrame(self.map_cordinates)
        self.vr_model_map_position.setObjectName(u"vr_model_map_position")
        self.vr_model_map_position.setFrameShape(QFrame.StyledPanel)
        self.vr_model_map_position.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.vr_model_map_position)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(-1, -1, -1, 0)
        self.label_vr_model_map_position = QLabel(self.vr_model_map_position)
        self.label_vr_model_map_position.setObjectName(u"label_vr_model_map_position")

        self.verticalLayout_99.addWidget(self.label_vr_model_map_position)

        self.horizontalLayout_map_position_4 = QHBoxLayout()
        self.horizontalLayout_map_position_4.setObjectName(u"horizontalLayout_map_position_4")
        self.verticalLayout_map_position_x_4 = QVBoxLayout()
        self.verticalLayout_map_position_x_4.setObjectName(u"verticalLayout_map_position_x_4")
        self.horizontalSlider_map_position_x_4 = QSlider(self.vr_model_map_position)
        self.horizontalSlider_map_position_x_4.setObjectName(u"horizontalSlider_map_position_x_4")
        self.horizontalSlider_map_position_x_4.setMinimum(-99)
        self.horizontalSlider_map_position_x_4.setOrientation(Qt.Horizontal)

        self.verticalLayout_map_position_x_4.addWidget(self.horizontalSlider_map_position_x_4)

        self.label_vr_model_map_position_x_4 = QLabel(self.vr_model_map_position)
        self.label_vr_model_map_position_x_4.setObjectName(u"label_vr_model_map_position_x_4")

        self.verticalLayout_map_position_x_4.addWidget(self.label_vr_model_map_position_x_4)


        self.horizontalLayout_map_position_4.addLayout(self.verticalLayout_map_position_x_4)

        self.verticalLayout_map_position_z_4 = QVBoxLayout()
        self.verticalLayout_map_position_z_4.setObjectName(u"verticalLayout_map_position_z_4")
        self.horizontalSlider_map_position_z_4 = QSlider(self.vr_model_map_position)
        self.horizontalSlider_map_position_z_4.setObjectName(u"horizontalSlider_map_position_z_4")
        self.horizontalSlider_map_position_z_4.setMinimum(-99)
        self.horizontalSlider_map_position_z_4.setOrientation(Qt.Horizontal)

        self.verticalLayout_map_position_z_4.addWidget(self.horizontalSlider_map_position_z_4)

        self.label_vr_model_map_position_z_4 = QLabel(self.vr_model_map_position)
        self.label_vr_model_map_position_z_4.setObjectName(u"label_vr_model_map_position_z_4")

        self.verticalLayout_map_position_z_4.addWidget(self.label_vr_model_map_position_z_4)


        self.horizontalLayout_map_position_4.addLayout(self.verticalLayout_map_position_z_4)

        self.verticalLayout_map_position_y_4 = QVBoxLayout()
        self.verticalLayout_map_position_y_4.setObjectName(u"verticalLayout_map_position_y_4")
        self.horizontalSlider_map_position_y_4 = QSlider(self.vr_model_map_position)
        self.horizontalSlider_map_position_y_4.setObjectName(u"horizontalSlider_map_position_y_4")
        self.horizontalSlider_map_position_y_4.setMinimum(-99)
        self.horizontalSlider_map_position_y_4.setOrientation(Qt.Horizontal)

        self.verticalLayout_map_position_y_4.addWidget(self.horizontalSlider_map_position_y_4)

        self.label_vr_model_map_position_y_4 = QLabel(self.vr_model_map_position)
        self.label_vr_model_map_position_y_4.setObjectName(u"label_vr_model_map_position_y_4")

        self.verticalLayout_map_position_y_4.addWidget(self.label_vr_model_map_position_y_4)


        self.horizontalLayout_map_position_4.addLayout(self.verticalLayout_map_position_y_4)


        self.verticalLayout_99.addLayout(self.horizontalLayout_map_position_4)


        self.verticalLayout_100.addWidget(self.vr_model_map_position)


        self.verticalLayout_37.addWidget(self.map_cordinates)


        self.horizontalLayout_20.addWidget(self.vr_model_right)

        self.stackedWidget.addWidget(self.vr_model)
        self.recordes = QWidget()
        self.recordes.setObjectName(u"recordes")
        self.verticalLayout_73 = QVBoxLayout(self.recordes)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.widget_records_top_view = QWidget(self.recordes)
        self.widget_records_top_view.setObjectName(u"widget_records_top_view")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_records_top_view)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.title_records = QLabel(self.widget_records_top_view)
        self.title_records.setObjectName(u"title_records")

        self.horizontalLayout_13.addWidget(self.title_records)

        self.horizontalSpacer_records_top_view_btn = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_records_top_view_btn)

        self.records_top_view_btn = QPushButton(self.widget_records_top_view)
        self.records_top_view_btn.setObjectName(u"records_top_view_btn")
        self.records_top_view_btn.setMinimumSize(QSize(28, 28))
        self.records_top_view_btn.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_13.addWidget(self.records_top_view_btn)


        self.verticalLayout_73.addWidget(self.widget_records_top_view)

        self.scrollArea_records = QScrollArea(self.recordes)
        self.scrollArea_records.setObjectName(u"scrollArea_records")
        self.scrollArea_records.setWidgetResizable(True)
        self.scrollAreaWidgetContents_records = QWidget()
        self.scrollAreaWidgetContents_records.setObjectName(u"scrollAreaWidgetContents_records")
        self.scrollAreaWidgetContents_records.setGeometry(QRect(0, 0, 1166, 534))
        self.scrollArea_records.setWidget(self.scrollAreaWidgetContents_records)

        self.verticalLayout_73.addWidget(self.scrollArea_records)

        self.stackedWidget.addWidget(self.recordes)
        self.alerts = QWidget()
        self.alerts.setObjectName(u"alerts")
        self.verticalLayout_74 = QVBoxLayout(self.alerts)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.title_alerts_cont = QWidget(self.alerts)
        self.title_alerts_cont.setObjectName(u"title_alerts_cont")
        self.horizontalLayout_16 = QHBoxLayout(self.title_alerts_cont)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.title_alerts = QLabel(self.title_alerts_cont)
        self.title_alerts.setObjectName(u"title_alerts")

        self.horizontalLayout_16.addWidget(self.title_alerts)

        self.horizontalSpacer_alerts = QSpacerItem(667, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_alerts)

        self.alerts_view_btn = QPushButton(self.title_alerts_cont)
        self.alerts_view_btn.setObjectName(u"alerts_view_btn")
        self.alerts_view_btn.setMinimumSize(QSize(28, 28))
        self.alerts_view_btn.setMaximumSize(QSize(28, 28))

        self.horizontalLayout_16.addWidget(self.alerts_view_btn)


        self.verticalLayout_74.addWidget(self.title_alerts_cont)

        self.scrollArea_alerts = QScrollArea(self.alerts)
        self.scrollArea_alerts.setObjectName(u"scrollArea_alerts")
        self.scrollArea_alerts.setWidgetResizable(True)
        self.scrollAreaWidgetContents_alerts = QWidget()
        self.scrollAreaWidgetContents_alerts.setObjectName(u"scrollAreaWidgetContents_alerts")
        self.scrollAreaWidgetContents_alerts.setGeometry(QRect(0, 0, 1184, 552))
        self.scrollArea_alerts.setWidget(self.scrollAreaWidgetContents_alerts)

        self.verticalLayout_74.addWidget(self.scrollArea_alerts)

        self.stackedWidget.addWidget(self.alerts)
        self.detections = QWidget()
        self.detections.setObjectName(u"detections")
        self.horizontalLayout_15 = QHBoxLayout(self.detections)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.detection_main = QFrame(self.detections)
        self.detection_main.setObjectName(u"detection_main")
        sizePolicy8 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.detection_main.sizePolicy().hasHeightForWidth())
        self.detection_main.setSizePolicy(sizePolicy8)
        self.detection_main.setFrameShape(QFrame.StyledPanel)
        self.detection_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.detection_main)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.title_detections = QLabel(self.detection_main)
        self.title_detections.setObjectName(u"title_detections")

        self.verticalLayout_90.addWidget(self.title_detections)

        self.scrollArea_detections_main = QScrollArea(self.detection_main)
        self.scrollArea_detections_main.setObjectName(u"scrollArea_detections_main")
        self.scrollArea_detections_main.setWidgetResizable(True)
        self.scrollAreaWidgetContents_detections_main = QWidget()
        self.scrollAreaWidgetContents_detections_main.setObjectName(u"scrollAreaWidgetContents_detections_main")
        self.scrollAreaWidgetContents_detections_main.setGeometry(QRect(0, 0, 571, 563))
        self.verticalLayout_70 = QVBoxLayout(self.scrollAreaWidgetContents_detections_main)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.scrollArea_detections_main.setWidget(self.scrollAreaWidgetContents_detections_main)

        self.verticalLayout_90.addWidget(self.scrollArea_detections_main)


        self.horizontalLayout_15.addWidget(self.detection_main)

        self.detections_about = QFrame(self.detections)
        self.detections_about.setObjectName(u"detections_about")
        sizePolicy8.setHeightForWidth(self.detections_about.sizePolicy().hasHeightForWidth())
        self.detections_about.setSizePolicy(sizePolicy8)
        self.detections_about.setMinimumSize(QSize(100, 0))
        self.detections_about.setFrameShape(QFrame.StyledPanel)
        self.detections_about.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.detections_about)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, -1, 0)
        self.scrollArea_detections_about = QScrollArea(self.detections_about)
        self.scrollArea_detections_about.setObjectName(u"scrollArea_detections_about")
        self.scrollArea_detections_about.setWidgetResizable(True)
        self.scrollAreaWidgetContents_detections_about = QWidget()
        self.scrollAreaWidgetContents_detections_about.setObjectName(u"scrollAreaWidgetContents_detections_about")
        self.scrollAreaWidgetContents_detections_about.setGeometry(QRect(0, 0, 580, 604))
        self.verticalLayout_33 = QVBoxLayout(self.scrollAreaWidgetContents_detections_about)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.detections_about_view_top = QFrame(self.scrollAreaWidgetContents_detections_about)
        self.detections_about_view_top.setObjectName(u"detections_about_view_top")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(10)
        sizePolicy9.setHeightForWidth(self.detections_about_view_top.sizePolicy().hasHeightForWidth())
        self.detections_about_view_top.setSizePolicy(sizePolicy9)
        self.detections_about_view_top.setMinimumSize(QSize(0, 0))
        self.detections_about_view_top.setFrameShape(QFrame.StyledPanel)
        self.detections_about_view_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.detections_about_view_top)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.scrollArea_detections_about_view_top = QScrollArea(self.detections_about_view_top)
        self.scrollArea_detections_about_view_top.setObjectName(u"scrollArea_detections_about_view_top")
        self.scrollArea_detections_about_view_top.setMinimumSize(QSize(0, 100))
        self.scrollArea_detections_about_view_top.setWidgetResizable(True)
        self.scrollAreaWidgetContents_detections_about_view_top = QWidget()
        self.scrollAreaWidgetContents_detections_about_view_top.setObjectName(u"scrollAreaWidgetContents_detections_about_view_top")
        self.scrollAreaWidgetContents_detections_about_view_top.setGeometry(QRect(0, 0, 562, 136))
        self.scrollAreaWidgetContents_detections_about_view_top.setMinimumSize(QSize(0, 100))
        self.verticalLayout_119 = QVBoxLayout(self.scrollAreaWidgetContents_detections_about_view_top)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.scrollArea_detections_about_view_top.setWidget(self.scrollAreaWidgetContents_detections_about_view_top)

        self.verticalLayout_120.addWidget(self.scrollArea_detections_about_view_top)

        self.textBrowser = QTextBrowser(self.detections_about_view_top)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_120.addWidget(self.textBrowser)


        self.verticalLayout_33.addWidget(self.detections_about_view_top)

        self.detections_avout_view_bottom = QFrame(self.scrollAreaWidgetContents_detections_about)
        self.detections_avout_view_bottom.setObjectName(u"detections_avout_view_bottom")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(7)
        sizePolicy10.setHeightForWidth(self.detections_avout_view_bottom.sizePolicy().hasHeightForWidth())
        self.detections_avout_view_bottom.setSizePolicy(sizePolicy10)
        self.detections_avout_view_bottom.setFrameShape(QFrame.StyledPanel)
        self.detections_avout_view_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.detections_avout_view_bottom)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.scrollArea_5 = QScrollArea(self.detections_avout_view_bottom)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 562, 228))
        self.verticalLayout_121 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.plainTextEdit_detections_about = QPlainTextEdit(self.scrollAreaWidgetContents_7)
        self.plainTextEdit_detections_about.setObjectName(u"plainTextEdit_detections_about")
        self.plainTextEdit_detections_about.setMinimumSize(QSize(200, 200))
        self.plainTextEdit_detections_about.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_121.addWidget(self.plainTextEdit_detections_about)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_122.addWidget(self.scrollArea_5)


        self.verticalLayout_33.addWidget(self.detections_avout_view_bottom)

        self.scrollArea_detections_about.setWidget(self.scrollAreaWidgetContents_detections_about)

        self.verticalLayout_115.addWidget(self.scrollArea_detections_about)


        self.horizontalLayout_15.addWidget(self.detections_about)

        self.stackedWidget.addWidget(self.detections)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.settings.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.settings)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget.addWidget(self.settings)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"border: none;\n"
"QVideoWidget {\n"
"	border: 5px;\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.home)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scrollArea_4 = QScrollArea(self.home)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1176, 1053))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.home_row_1 = QFrame(self.scrollAreaWidgetContents_6)
        self.home_row_1.setObjectName(u"home_row_1")
        self.home_row_1.setMinimumSize(QSize(0, 200))
        self.home_row_1.setFrameShape(QFrame.StyledPanel)
        self.home_row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.home_row_1)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_2 = QFrame(self.home_row_1)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_div_content_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.home_time = QFrame(self.frame_div_content_2)
        self.home_time.setObjectName(u"home_time")
        self.home_time.setFrameShape(QFrame.StyledPanel)
        self.home_time.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.home_time)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_home_time = QLabel(self.home_time)
        self.label_home_time.setObjectName(u"label_home_time")
        self.label_home_time.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_22.addWidget(self.label_home_time)


        self.horizontalLayout_6.addWidget(self.home_time)

        self.home_cpu = QFrame(self.frame_div_content_2)
        self.home_cpu.setObjectName(u"home_cpu")
        self.home_cpu.setFrameShape(QFrame.StyledPanel)
        self.home_cpu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.home_cpu)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_home_cpu = QLabel(self.home_cpu)
        self.label_home_cpu.setObjectName(u"label_home_cpu")
        self.label_home_cpu.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_18.addWidget(self.label_home_cpu)


        self.horizontalLayout_6.addWidget(self.home_cpu)

        self.home_gpu = QFrame(self.frame_div_content_2)
        self.home_gpu.setObjectName(u"home_gpu")
        self.home_gpu.setFrameShape(QFrame.StyledPanel)
        self.home_gpu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.home_gpu)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_home_gpu = QLabel(self.home_gpu)
        self.label_home_gpu.setObjectName(u"label_home_gpu")
        self.label_home_gpu.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_19.addWidget(self.label_home_gpu)


        self.horizontalLayout_6.addWidget(self.home_gpu)


        self.verticalLayout_21.addWidget(self.frame_div_content_2)


        self.verticalLayout_17.addWidget(self.home_row_1)

        self.label_home_camera = QLabel(self.scrollAreaWidgetContents_6)
        self.label_home_camera.setObjectName(u"label_home_camera")

        self.verticalLayout_17.addWidget(self.label_home_camera)

        self.home_row_2 = QFrame(self.scrollAreaWidgetContents_6)
        self.home_row_2.setObjectName(u"home_row_2")
        self.home_row_2.setMinimumSize(QSize(0, 400))
        self.home_row_2.setStyleSheet(u"")
        self.home_row_2.setFrameShape(QFrame.StyledPanel)
        self.home_row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.home_row_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.home_cameras = QFrame(self.home_row_2)
        self.home_cameras.setObjectName(u"home_cameras")
        self.home_cameras.setMinimumSize(QSize(0, 600))
        self.home_cameras.setFrameShape(QFrame.StyledPanel)
        self.home_cameras.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.home_cameras)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.home_camera_4 = QFrame(self.home_cameras)
        self.home_camera_4.setObjectName(u"home_camera_4")
        self.home_camera_4.setMinimumSize(QSize(160, 90))
        self.home_camera_4.setStyleSheet(u"")
        self.home_camera_4.setFrameShape(QFrame.StyledPanel)
        self.home_camera_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.home_camera_4)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(9, 9, -1, -1)
        self.label_home_camera_4 = QLabel(self.home_camera_4)
        self.label_home_camera_4.setObjectName(u"label_home_camera_4")
        self.label_home_camera_4.setStyleSheet(u"")
        self.label_home_camera_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_28.addWidget(self.label_home_camera_4)


        self.horizontalLayout_8.addWidget(self.home_camera_4)

        self.home_camera_5 = QFrame(self.home_cameras)
        self.home_camera_5.setObjectName(u"home_camera_5")
        self.home_camera_5.setMinimumSize(QSize(160, 90))
        self.home_camera_5.setFrameShape(QFrame.StyledPanel)
        self.home_camera_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.home_camera_5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(9, 9, -1, -1)
        self.label_home_camera_5 = QLabel(self.home_camera_5)
        self.label_home_camera_5.setObjectName(u"label_home_camera_5")
        self.label_home_camera_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_29.addWidget(self.label_home_camera_5)


        self.horizontalLayout_8.addWidget(self.home_camera_5)

        self.home_camera_6 = QFrame(self.home_cameras)
        self.home_camera_6.setObjectName(u"home_camera_6")
        self.home_camera_6.setMinimumSize(QSize(160, 90))
        self.home_camera_6.setFrameShape(QFrame.StyledPanel)
        self.home_camera_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.home_camera_6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(9, 9, -1, -1)
        self.label_home_camera_6 = QLabel(self.home_camera_6)
        self.label_home_camera_6.setObjectName(u"label_home_camera_6")
        self.label_home_camera_6.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_30.addWidget(self.label_home_camera_6)


        self.horizontalLayout_8.addWidget(self.home_camera_6)


        self.verticalLayout_46.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.home_camera_19 = QFrame(self.home_cameras)
        self.home_camera_19.setObjectName(u"home_camera_19")
        self.home_camera_19.setMinimumSize(QSize(160, 90))
        self.home_camera_19.setFrameShape(QFrame.StyledPanel)
        self.home_camera_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.home_camera_19)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(9, 9, -1, -1)
        self.label_home_camera_19 = QLabel(self.home_camera_19)
        self.label_home_camera_19.setObjectName(u"label_home_camera_19")
        self.label_home_camera_19.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_31.addWidget(self.label_home_camera_19)


        self.horizontalLayout_17.addWidget(self.home_camera_19)

        self.home_camera_20 = QFrame(self.home_cameras)
        self.home_camera_20.setObjectName(u"home_camera_20")
        self.home_camera_20.setMinimumSize(QSize(160, 90))
        self.home_camera_20.setFrameShape(QFrame.StyledPanel)
        self.home_camera_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.home_camera_20)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(9, 9, -1, -1)
        self.label_home_camera_20 = QLabel(self.home_camera_20)
        self.label_home_camera_20.setObjectName(u"label_home_camera_20")
        self.label_home_camera_20.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_44.addWidget(self.label_home_camera_20)


        self.horizontalLayout_17.addWidget(self.home_camera_20)

        self.home_camera_21 = QFrame(self.home_cameras)
        self.home_camera_21.setObjectName(u"home_camera_21")
        self.home_camera_21.setMinimumSize(QSize(160, 90))
        self.home_camera_21.setFrameShape(QFrame.StyledPanel)
        self.home_camera_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.home_camera_21)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(9, 9, -1, -1)
        self.label_home_camera_21 = QLabel(self.home_camera_21)
        self.label_home_camera_21.setObjectName(u"label_home_camera_21")
        self.label_home_camera_21.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_45.addWidget(self.label_home_camera_21)


        self.horizontalLayout_17.addWidget(self.home_camera_21)


        self.verticalLayout_46.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.home_camera_2 = QFrame(self.home_cameras)
        self.home_camera_2.setObjectName(u"home_camera_2")
        self.home_camera_2.setMinimumSize(QSize(160, 90))
        self.home_camera_2.setFrameShape(QFrame.StyledPanel)
        self.home_camera_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.home_camera_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(9, 9, -1, -1)
        self.label_home_camera_2 = QLabel(self.home_camera_2)
        self.label_home_camera_2.setObjectName(u"label_home_camera_2")
        self.label_home_camera_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_26.addWidget(self.label_home_camera_2)


        self.horizontalLayout_7.addWidget(self.home_camera_2)

        self.home_camera_3 = QFrame(self.home_cameras)
        self.home_camera_3.setObjectName(u"home_camera_3")
        self.home_camera_3.setMinimumSize(QSize(160, 90))
        self.home_camera_3.setFrameShape(QFrame.StyledPanel)
        self.home_camera_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.home_camera_3)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, 9, -1, -1)
        self.label_home_camera_3 = QLabel(self.home_camera_3)
        self.label_home_camera_3.setObjectName(u"label_home_camera_3")
        self.label_home_camera_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_27.addWidget(self.label_home_camera_3)


        self.horizontalLayout_7.addWidget(self.home_camera_3)

        self.home_camera_1 = QFrame(self.home_cameras)
        self.home_camera_1.setObjectName(u"home_camera_1")
        self.home_camera_1.setMinimumSize(QSize(160, 90))
        self.home_camera_1.setFrameShape(QFrame.StyledPanel)
        self.home_camera_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.home_camera_1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(9, 9, -1, -1)
        self.label_home_camera_1 = QLabel(self.home_camera_1)
        self.label_home_camera_1.setObjectName(u"label_home_camera_1")
        self.label_home_camera_1.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_23.addWidget(self.label_home_camera_1)


        self.horizontalLayout_7.addWidget(self.home_camera_1)


        self.verticalLayout_46.addLayout(self.horizontalLayout_7)


        self.verticalLayout_10.addWidget(self.home_cameras)


        self.verticalLayout_17.addWidget(self.home_row_2)

        self.home_row_3 = QFrame(self.scrollAreaWidgetContents_6)
        self.home_row_3.setObjectName(u"home_row_3")
        self.home_row_3.setMinimumSize(QSize(0, 400))
        self.home_row_3.setFrameShape(QFrame.StyledPanel)
        self.home_row_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.home_row_3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea_2 = QScrollArea(self.home_row_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1130, 418))
        self.scrollAreaWidgetContents_2.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_14 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.plainTextEdit_2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(200, 400))
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_14.addWidget(self.plainTextEdit_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 2, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_4)


        self.verticalLayout_17.addWidget(self.home_row_3)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_20.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.home)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_lock = QPushButton(self.topMenus)
        self.btn_lock.setObjectName(u"btn_lock")
        sizePolicy.setHeightForWidth(self.btn_lock.sizePolicy().hasHeightForWidth())
        self.btn_lock.setSizePolicy(sizePolicy)
        self.btn_lock.setMinimumSize(QSize(0, 45))
        self.btn_lock.setFont(font)
        self.btn_lock.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lock.setLayoutDirection(Qt.LeftToRight)
        self.btn_lock.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-lock-unlocked.png);")

        self.verticalLayout_14.addWidget(self.btn_lock)

        self.btn_sign_out = QPushButton(self.topMenus)
        self.btn_sign_out.setObjectName(u"btn_sign_out")
        sizePolicy.setHeightForWidth(self.btn_sign_out.sizePolicy().hasHeightForWidth())
        self.btn_sign_out.setSizePolicy(sizePolicy)
        self.btn_sign_out.setMinimumSize(QSize(0, 45))
        self.btn_sign_out.setFont(font)
        self.btn_sign_out.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sign_out.setLayoutDirection(Qt.LeftToRight)
        self.btn_sign_out.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-exit-to-app.png);")

        self.verticalLayout_14.addWidget(self.btn_sign_out)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(False)
        font2.setItalic(False)
        self.creditsLabel.setFont(font2)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)

        self.leftMenuBg.raise_()
        self.contentBox.raise_()
        self.extraLeftBox.raise_()

        self.verticalLayout_72.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_live_feed.setText(QCoreApplication.translate("MainWindow", u"Monitoring", None))
        self.btn_detections.setText(QCoreApplication.translate("MainWindow", u"Detections", None))
        self.btn_alert.setText(QCoreApplication.translate("MainWindow", u"Alerts", None))
        self.btn_recordes.setText(QCoreApplication.translate("MainWindow", u"Recordes", None))
        self.btn_vr_model.setText(QCoreApplication.translate("MainWindow", u"VR model", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"IVS - Intelegent Survilance System.", None))
#if QT_CONFIG(tooltip)
        self.alertsAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Alerts", None))
#endif // QT_CONFIG(tooltip)
        self.alertsAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.title_live_feed_1.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.btn_live_feed_2_main_display_list_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.title_live_feed_2.setText(QCoreApplication.translate("MainWindow", u"Live feed", None))
        self.title_vr_model.setText(QCoreApplication.translate("MainWindow", u"VR model", None))
        self.radioButton_vr_model_3d_include.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.label_vr_model_3d_position.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_vr_model_3d_position_x.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_vr_model_3d_position_z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_vr_model_3d_position_y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_vr_model_3d_view.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_vr_model_3d_position_x_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_vr_model_3d_position_z_2.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_vr_model_3d_position_y_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_vr_model_map_view.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_vr_model_map_view_x.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_vr_model_map_view_z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_vr_model_map_view_y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_vr_model_map_position.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_vr_model_map_position_x_4.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_vr_model_map_position_z_4.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_vr_model_map_position_y_4.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.title_records.setText(QCoreApplication.translate("MainWindow", u"Recordes", None))
        self.records_top_view_btn.setText("")
        self.title_alerts.setText(QCoreApplication.translate("MainWindow", u"Alerts", None))
        self.alerts_view_btn.setText("")
        self.title_detections.setText(QCoreApplication.translate("MainWindow", u"Detections", None))
        self.label_home_time.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_home_cpu.setText(QCoreApplication.translate("MainWindow", u"CPU status", None))
        self.label_home_gpu.setText(QCoreApplication.translate("MainWindow", u"GPU status", None))
        self.label_home_camera.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_home_camera_4.setText(QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.label_home_camera_5.setText(QCoreApplication.translate("MainWindow", u"Camera 2", None))
        self.label_home_camera_6.setText(QCoreApplication.translate("MainWindow", u"Camera 3", None))
        self.label_home_camera_19.setText(QCoreApplication.translate("MainWindow", u"Camera 4", None))
        self.label_home_camera_20.setText(QCoreApplication.translate("MainWindow", u"Camera 5", None))
        self.label_home_camera_21.setText(QCoreApplication.translate("MainWindow", u"Camera 6", None))
        self.label_home_camera_2.setText(QCoreApplication.translate("MainWindow", u"Camera 7", None))
        self.label_home_camera_3.setText(QCoreApplication.translate("MainWindow", u"Camera 8", None))
        self.label_home_camera_1.setText(QCoreApplication.translate("MainWindow", u"Camera 9", None))
        self.btn_lock.setText(QCoreApplication.translate("MainWindow", u"Lock", None))
        self.btn_sign_out.setText(QCoreApplication.translate("MainWindow", u"Sign out", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Nathaniel Bekalu", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

