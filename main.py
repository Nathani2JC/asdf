import sys
import os
from typing import Optional

# import PySide6.QtCore
import PySide6.QtWidgets
# import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from ai import *

# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"


# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

# LOGIN PAGE
class LoginWindows(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        #STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus(self):
                UIFunctions.maximize_restore(self)
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # LOG IN BUTTON
        widgets.btn_login.clicked.connect(self.login)
        widgets.btn_close.clicked.connect(self.close)

    def login(self):
        username = widgets.input_lineEdit_user_name.text()
        password = widgets.input_lineEdit_password.text()
        print("Username:", username)
        print("Password:", password)
        if username == "admin" and password == "admin": # Login if password and usernamae is correct
            self.close()
            window = MainWindow()
            window.show()

# MAIN PAGE CONFIGURATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "IVS - Modern GUI"
        description = "IVS APP - Makes your life secure."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_live_feed.clicked.connect(self.buttonClick)
        widgets.btn_detections.clicked.connect(self.buttonClick)
        widgets.btn_alert.clicked.connect(self.buttonClick)
        widgets.btn_recordes.clicked.connect(self.buttonClick)
        widgets.btn_vr_model.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW Live_feed PAGE
        if btnName == "btn_live_feed":
            widgets.stackedWidget.setCurrentWidget(widgets.live_feed)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW DETECTIONS PAGE
        if btnName == "btn_detections":
            widgets.stackedWidget.setCurrentWidget(widgets.detections) 
            UIFunctions.resetStyle(self, btnName) 
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW ALERTS PAGEif
        if btnName == "btn_alert":
            widgets.stackedWidget.setCurrentWidget(widgets.alerts)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            
        # SHOW RECORDINGS PAGE
        if btnName == "btn_recordes":
            widgets.stackedWidget.setCurrentWidget(widgets.recordes)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW VR_MODEL PAGE
        if btnName == "btn_vr_model":
            widgets.stackedWidget.setCurrentWidget(widgets.vr_model)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # SET IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_image(self, image):
        # Set the image to the label
        self.lable.setPixmap(QPixmap.fromImage(image))

# START LOGIN PAGE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # window = LoginWindows()
    window.show()
    sys.exit(app.exec())


