#
# pathDesign_ui1.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import json
import io
import os
import csv
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


# Data Model
from constants.accountData import AccountData
from constants.firebaseData import FirebaseData
from constants.pathDesignData import PathDesignData
from constants.siteData import SiteData

# "1. Import / Select sites Page"
class KMLGeneratorWidget1(QWidget):

    def __init__(self, parent=None):
        super(KMLGeneratorWidget1, self).__init__(parent)
        self.colcnt = 5
        self.rowcnt = 5
        self.initUI(parent)

    def initUI(self, parent):
        self.sideMenuUI(parent)
        self.accountUI()
        self.progressUI(parent)
        self.mapTableViewUI(parent)

    def sideMenuUI(self, parent):
        # left wrapper
        self.leftContainer = QWidget(self)
        self.leftContainer.setAutoFillBackground(True)
        self.leftContainer.setStyleSheet("""
            background-color:rgba(8, 44, 108, 1);
        """)
        self.leftContainer.setGeometry(0, 0, 1200/6, 800)

        # Home Button
        self.homeBtn = QPushButton(self)
        self.homeBtn.setText("Home")
        self.homeBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color: rgba(8, 44, 108, 1);
                border: 0px solid white;
            }"""
        )
        self.homeBtn.setGeometry(0, 350, 1200/6, 50)
        self.homeBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToHomePage(parent))

        # Network Configuration
        self.nwcfBtn = QPushButton(self)
        self.nwcfBtn.setText("Network Configuration")
        self.nwcfBtn.setStyleSheet("""
            QPushButton {
                color: rgba(8, 44, 108, 1);
                font-size: 15px;
                background-color: white;
                border: 0px solid white;
            }"""
        )
        self.nwcfBtn.setGeometry(0, 400, 1200/6, 50)
        self.nwcfBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToPathDesignPage0(parent))

        # FAQ
        self.faqBtn = QPushButton(self)
        self.faqBtn.setText("FAQ")
        self.faqBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color: rgba(8, 44, 108, 1);
                border: 0px solid white;
            }"""
        )
        self.faqBtn.setGeometry(0, 450, 1200/6, 50)
        self.faqBtn.clicked.connect(lambda: parent.popUp.upCommingFunctionality())

        # Check out
        self.checkOutBtn = QPushButton(self)
        self.checkOutBtn.setText("Check out")
        self.checkOutBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color: rgba(8, 44, 108, 1);
                border: 0px solid white;
            }"""
        )
        self.checkOutBtn.setGeometry(0, 500, 1200/6, 50)
        self.checkOutBtn.clicked.connect(lambda: parent.popUp.upCommingFunctionality())


    # account UI
    def accountUI(self):
        # Profile picture
        self.profilePhoto = QLabel(self)
        file = self.resource_path("user.png")
        self.profilePhoto.setPixmap(QPixmap(file)) # path starts from main.py
        self.profilePhoto.setGeometry(68, 50, 64, 64)
        self.profilePhoto.setAlignment(Qt.AlignCenter)

        # Full name label
        self.userNameLabel = QLabel(self)
        self.userNameLabel.setText("User Profile")
        self.userNameLabel.setStyleSheet("""
            QLabel {
                color : rgba(239, 240, 242, 1);
                font-size: 10px;
            }"""
        )
        self.userNameLabel.setGeometry(0, 110, 200, 30)
        self.userNameLabel.setAlignment(Qt.AlignCenter)

        # Email
        self.usersEmailLabel = QLabel(self)
        self.usersEmailLabel.setText("j.lewandowski@theta.com")
        self.usersEmailLabel.setStyleSheet("""
            QLabel {
                color : rgba(239, 240, 242, 1);
                font-size: 10px;
            }"""
        )
        self.usersEmailLabel.setGeometry(0, 130, 200, 30)
        self.usersEmailLabel.setAlignment(Qt.AlignCenter)

        # Settings btn
        self.profileSettingsBtn = QPushButton(self)
        self.profileSettingsBtn.setText("Open profile settings")
        self.profileSettingsBtn.setStyleSheet("""
            QPushButton {
                color: rgba(8, 44, 108, 1);
                font-size: 10px;
                background-color: rgba(225, 225, 225, 0.7);
                border: 0px solid rgba(225, 225, 225, 0.7);
                border-radius: 5%;
            }"""
        )
        self.profileSettingsBtn.setGeometry(35, 160, 130, 20)
        self.profileSettingsBtn.clicked.connect(lambda: parent.popUp.upCommingFunctionality())



    def progressUI(self, parent):
        # current project name tag UI
        self.projectNameTag = QPushButton(self)
        self.projectNameTag.setText("KML Generator")
        self.projectNameTag.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 17px;
                border-radius: 5%;
                background-color: rgba(250, 128, 114, 1);
            }"""
        )
        self.projectNameTag.setGeometry(210, 10, 150, 50)
        # self.projectNameTag.clicked.connect(self.button01Clicked)
        self.projectNameTag.setEnabled(False)

        # progress UI wrapper
        self.progressBarContainer = QWidget(self)
        self.progressBarContainer.setAutoFillBackground(True)
        self.progressBarContainer.setStyleSheet("""
            background-color:white;
            border-radius: 5%;
        """)
        self.progressBarContainer.setGeometry(380, 10, 810, 50)

        # 1. Import/select sites button
        self.mapBtn = QPushButton(self)
        self.mapBtn.setText("1. Import site data")
        self.mapBtn.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 20px;
                background-color:rgba(225, 225, 225, 0);
                text-decoration: underline;
            }"""
        )
        self.mapBtn.setGeometry(450, 10, 200, 50)
        self.mapBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToPathDesignPage1(parent))

        # 2. Select site button
        self.selectSitesBtn = QPushButton(self)
        self.selectSitesBtn.setText("2. Configuration")
        self.selectSitesBtn.setStyleSheet("""
            QPushButton {
                color: lightgray;
                font-size: 20px;
                background-color:rgba(225, 225, 225, 0);
            }"""
        )
        self.selectSitesBtn.setGeometry(700, 10, 200, 50)

        # 3. Configure parameters
        self.selectSitesBtn = QPushButton(self)
        self.selectSitesBtn.setText("3. KML profile")
        self.selectSitesBtn.setStyleSheet("""
            QPushButton {
                color: lightgray;
                font-size: 20px;
                background-color:rgba(225, 225, 225, 0);
            }"""
        )
        self.selectSitesBtn.setGeometry(950, 10, 200, 50)


    def mapTableViewUI(self, parent):
        # map/table view wrapper
        self.maptableContainer = QWidget(self)
        self.maptableContainer.setAutoFillBackground(True)
        self.maptableContainer.setStyleSheet("""
            background-color: white;
            border-radius: 5%;
        """)
        self.maptableContainer.setGeometry(210, 70, 980, 720)

        # Open file button
        self.importSitesBtn = QPushButton(self)
        self.importSitesBtn.setText("Click here to import site data")
        self.importSitesBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color:blue;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        self.importSitesBtn.setGeometry(220, 80, 250, 30)
        self.importSitesBtn.clicked.connect(lambda: self.openSheet(parent))

        # or skip and select sites from map view
        self.directionMsgLabel = QLabel(self)
        self.directionMsgLabel.setText("or enter site data manually into the table.")
        self.directionMsgLabel.setStyleSheet("""
            QLabel {
                color : gray;
                font-size: 15px;
            }"""
        )
        self.directionMsgLabel.setGeometry(410, 80, 400, 30)
        self.directionMsgLabel.setAlignment(Qt.AlignCenter)



        # Table view
        self.tablewidget = QTableWidget(self)
        self.tablewidget.setRowCount(10)
        self.tablewidget.setColumnCount(10)
        self.colHeaders = ["Index", "Site1", "Latitude1", "Longitude1", "Site2", "Latitude2", "Longitude2", "TowerHeight1", "TowerHeight2"]
        self.tablewidget.setHorizontalHeaderLabels(self.colHeaders)
        self.tablewidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tablewidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.directionMsgLabel.setStyleSheet("""
            QTableWidget {
                background-color: red;
                border: 3px solid blue;
            }"""
        )
        self.tablewidget.setGeometry(220, 120, 960, 600)


        # select specific sites button
        self.importSitesBtn = QPushButton(self)
        self.importSitesBtn.setText("Next")
        self.importSitesBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color:blue;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        self.importSitesBtn.setGeometry(1030, 740, 150, 40)
        # self.importSitesBtn.clicked.connect(lambda: self.moveToPathDesignPage2(parent)) # validate the rows



    def openSheet(self, parent):
        self.fileDialogWidget = QFileDialog(self)
        # self.fileName = self.fileDialogWidget.getOpenFileName(self, 'Open file', os.path.expanduser('~') + '/', "Geo-data files (*.csv *.xlsx *.kml)")
        self.fileName = self.fileDialogWidget.getOpenFileName(self, 'Open file', os.path.expanduser('~') + '/', "Geo-data files (*.csv)")
        self.loadCSV(parent, self.fileName[0])


    def loadCSV(self, parent, fileName):
        if fileName != '':
            with open(fileName, newline='') as csv_file:
                self.tablewidget.setRowCount(0)
                self.tablewidget.setColumnCount(9)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.tablewidget.rowCount()
                    self.tablewidget.insertRow(row)
                    if len(row_data) > 5:
                        self.tablewidget.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.tablewidget.setItem(row, column, item)
            self.tablewidget.update()
            # parent.pathDesignData.setFilePath(str(fileName)) # save file path & name
        else:
            print("Invalid file path")


    def button01Clicked(self):
        print("Network Config Clicked!")

    def button03Clicked(self):
        print("Network Config Clicked!")

    def moveToHomePage(self, parent):
        parent.central_widget.setCurrentIndex(2)

    def moveToPathDesignPage1(self, parent):
        parent.central_widget.setCurrentIndex(3)

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def moveToKMLGeneratorPage2(self, parent):
        #
        
        # Change page
        parent.screenTransitionModules.moveToPathDesignPage2(parent)
