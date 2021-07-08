#
# main.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import json
import io
import os
import csv
import math
# import sip
# import folium
import pyrebase
import dataclasses
from geopy.distance import geodesic
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QStackedLayout
from PyQt5.QtWebEngineWidgets import *

# Gui
from gui.login_ui import LogInWidget
from gui.signup_ui import SignUpWidget
from gui.home_ui import HomeWidget
from gui.pathDesign_ui0 import PathDesignWidget0
from gui.pathDesign_ui1 import PathDesignWidget1
from gui.pathDesign_ui2 import PathDesignWidget2
from gui.pathDesign_ui3 import PathDesignWidget3


# Data Model
from constants.accountData import AccountData
from constants.firebaseData import FirebaseData
from constants.pathDesignData import PathDesignData

# Modules
from modules.pathProfileModules import PathProfileModules
from modules.screenTransitionModules import ScreenTransitionModules
from modules.popUpModules import PopUpModules


# Script for credentials
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        ### Global data ###
        # Account data
        self.accountData = AccountData(None, None, None, None, None)
        # Firebase data
        self.firebaseData = FirebaseData()
        # Path design data
        self.pathDesignData = PathDesignData(None, None, None, None, None, None, None, None, None, None, None, None)
        # Screen Transition modules
        self.screenTransitionModules = ScreenTransitionModules()
        # Path profile calculation modules
        self.pathCalc = PathProfileModules()
        # Pop up modules
        self.popUp = PopUpModules()


        ### window frame ###
        self.setWindowTitle("TDX Desktop")
        self.left = 100
        self.top = 50
        self.width = 1200
        self.height = 800
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMinimumHeight(800)
        self.setMinimumWidth(1200)
        self.setMaximumHeight(800)
        self.setMaximumWidth(1200)

        ### Set the UI at main ###
        self.central_widget = QStackedWidget(self)
        self.logInWidget = LogInWidget(self)
        self.signUpWidget = SignUpWidget(self)
        self.homeWidget = HomeWidget(self)
        self.pathDesignWidget0 = PathDesignWidget0(self)
        self.pathDesignWidget1 = PathDesignWidget1(self)
        self.pathDesignWidget2 = PathDesignWidget2(self)
        self.pathDesignWidget3 = PathDesignWidget3(self)
        # add widgets
        self.central_widget.addWidget(self.logInWidget)         # index 0
        self.central_widget.addWidget(self.signUpWidget)        # index 1
        self.central_widget.addWidget(self.homeWidget)          # index 2
        self.central_widget.addWidget(self.pathDesignWidget0)   # index 3
        self.central_widget.addWidget(self.pathDesignWidget1)   # index 4
        self.central_widget.addWidget(self.pathDesignWidget2)   # index 5
        self.central_widget.addWidget(self.pathDesignWidget3)   # index 6
        self.setCentralWidget(self.central_widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    path = os.path.dirname(os.path.abspath(__file__))
    # app.setWindowIcon(QIcon(os.path.join(path, "/img/sd-icon.png")))
    window.show()
    sys.exit(app.exec_())

# Execute the gui
if __name__ == "__main__":
    main()
