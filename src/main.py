#
# main.py
# TDX Desktop
# Created by Che Blankenship on 12/17/2021
#
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

### Pages ###
from pages.index import HomeUI
from pages.howFar.howFarUI1 import HowFarUI1
from pages.howFar.howFarUI2 import HowFarUI2
from pages.scriptA.scriptAUI1 import ScriptAUI1
from pages.scriptA.scriptAUI2 import ScriptAUI2
from pages.pathsA.pathsAUI1 import PathsAUI1
from pages.pathsA.pathsAUI2 import PathsAUI2
from pages.gudPathA.gudPathUI1 import GudPathUI1
from pages.gudPathA.gudPathUI2 import GudPathUI2
from pages.profileA.profileAUI1 import ProfileAUI1
from pages.profileA.profileAUI2 import ProfileAUI2
from pages.kml3DA.KML3DAUI1 import KML3DAUI1
from pages.kml3DA.KML3DAUI2 import KML3DAUI2
from pages.kml3DA.KML3DAUI3 import KML3DAUI3


# Global scope modules
from modules.screenTransitionModules import ScreenTransitionModules



# Script for credentials
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        ### Define main window frame size ###
        self.setWindowTitle("V3 Desktop")
        self.left = 50
        self.top = 50
        self.width = self.showMaximized()
        self.height = self.showMaximized()

        ### Global data ###
        self.screenTransition = ScreenTransitionModules()

        # Module and thread for Kizer module GudPath
        # self.gudPathGenerator = GudPath()
        # self.gudPathThread = GudPathThread(self)

        ### Set the UI at main ###
        # create a stack widget
        self.centralWidget = QStackedWidget(self)
        # declare the pages
        self.homeUI = HomeUI(self)  #home
        # Step 1
        self.howFarUI1 = HowFarUI1(self)        # How Far 1
        self.howFarUI2 = HowFarUI2(self)        # How Far 2

        # Step 2
        self.scriptUI1 = ScriptAUI1(self)       # ScriptA page 1
        self.scriptUI2 = ScriptAUI2(self)       # ScriptA page 2
        self.pathsAUI1 = PathsAUI1(self)        # Path A 1
        self.pathsAUI2 = PathsAUI2(self)        # Path A 2
        self.gudPathAUI1 = GudPathUI1(self)     # GudPath 1
        self.gudPathAUI2 = GudPathUI2(self)     # Gud Path 2
        self.profileAUI1 = ProfileAUI1(self)    # Profile A 1
        self.profileAUI2 = ProfileAUI2(self)    # Profile A 2
        self.kml3daUI1 = KML3DAUI1(self)        # KML 3DA 1
        self.kml3daUI2 = KML3DAUI2(self)        # KML 3DA 2
        self.kml3daUI3 = KML3DAUI3(self)        # KML 3DA 3

        # Step 3



        # push the pages into QStack
        self.centralWidget.addWidget(self.homeUI)       # index 0
        self.centralWidget.addWidget(self.scriptUI1)    # index 1
        self.centralWidget.addWidget(self.scriptUI2)    # index 2
        self.centralWidget.addWidget(self.pathsAUI1)    # index 3
        self.centralWidget.addWidget(self.pathsAUI2)    # index 4
        self.centralWidget.addWidget(self.gudPathAUI1)  # index 5
        self.centralWidget.addWidget(self.gudPathAUI2)  # index 6
        self.centralWidget.addWidget(self.profileAUI1)  # index 7
        self.centralWidget.addWidget(self.profileAUI2)  # index 8
        self.centralWidget.addWidget(self.kml3daUI1)    # index 9
        self.centralWidget.addWidget(self.kml3daUI2)    # index 10
        self.centralWidget.addWidget(self.kml3daUI3)    # index 11
        self.centralWidget.addWidget(self.howFarUI1)    # index 12
        self.centralWidget.addWidget(self.howFarUI2)    # index 13

        # set centralWidget to be the main object for screen transition
        self.setCentralWidget(self.centralWidget)


def main():
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    window = MainWindow()
    path = os.path.dirname(os.path.abspath(__file__))
    window.show()
    sys.exit(app.exec_())

# Execute the gui
if __name__ == "__main__":
    main()
