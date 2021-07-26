#
# pathDesign_ui2.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import json
import io
import os
import csv
import random
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngineWidgets import *


# Data Model
from constants.accountData import AccountData
from constants.firebaseData import FirebaseData
from constants.pathDesignData import PathDesignData
from constants.antennaFile import antennaData

# Modules
from modules.pathProfileModules import PathProfileModules


# "2. Path Calculation Page"
class KMLGeneratorWidget2(QWidget):

    def __init__(self, parent=None):
        super(KMLGeneratorWidget2, self).__init__(parent)
        self.colcnt = 10
        self.rowcnt = 10
        self.initUI(parent)
        self.update()

    def initUI(self, parent):
        self.sideMenuUI(parent)
        self.accountUI(parent)
        self.progressUI(parent)
        self.parametersUI(parent)
        self.configUI(parent)

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
        self.homeBtn.clicked.connect(lambda: self.moveToHomePage(parent))

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
    def accountUI(self, parent):
        # Profile picture
        self.profilePhoto = QLabel(self)
        path = os.path.dirname(os.path.abspath(__file__))
        file = self.resource_path("user.png")
        self.profilePhoto.setPixmap(QPixmap(file)) # path starts from main.py
        # path = os.path.dirname(os.path.abspath(__file__))
        # self.profilePhoto.setPixmap(QPixmap(os.path.join("../img/user.png"))) # path starts from main.py
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
                font-size: 20px;
                border-radius: 5%;
                background-color: rgba(250, 128, 114, 1);
            }"""
        )
        self.projectNameTag.setGeometry(210, 10, 150, 50)
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
        self.mapBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToKMLGeneratorPage1(parent))

        # 2. Select site button
        self.selectSitesBtn = QPushButton(self)
        self.selectSitesBtn.setText("2. Configuration")
        self.selectSitesBtn.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 20px;
                background-color:rgba(225, 225, 225, 0);
                text-decoration: underline;
            }"""
        )
        self.selectSitesBtn.setGeometry(700, 10, 200, 50)
        self.selectSitesBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToKMLGeneratorPage2(parent))

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


    def parametersUI(self, parent):
        # parameters view wrapper
        self.paramsContainer = QWidget(self)
        self.paramsContainer.setAutoFillBackground(True)
        self.paramsContainer.setStyleSheet("""
            background-color: white;
            border-radius: 5%;
        """)
        self.paramsContainer.setGeometry(210, 70, 980, 720)

        # Message label
        self.directionMsgLabel2 = QLabel(self)
        self.directionMsgLabel2.setText("Configurate the KML file settings.")
        self.directionMsgLabel2.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 20px;
            }"""
        )
        self.directionMsgLabel2.setGeometry(240, 90, 500, 30)
        self.directionMsgLabel2.setAlignment(Qt.AlignLeft)


        # go to kml generator btn
        self.nextPageBtn = QPushButton(self)
        self.nextPageBtn.setText("Next")
        self.nextPageBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color:blue;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        self.nextPageBtn.setGeometry(1030, 740, 150, 40)
        self.nextPageBtn.clicked.connect(lambda: self.nextBtnClicked(parent))

        # select specific sites button
        self.importSitesBtn = QPushButton(self)
        self.importSitesBtn.setText("Back")
        self.importSitesBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color:blue;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        self.importSitesBtn.setGeometry(240, 740, 150, 40)
        self.importSitesBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToKMLGeneratorPage1(parent)) # validate the rows


    # Site A param UI
    def configUI(self, parent):

        ### Config UI wrapper ###
        self.siteAContainer = QWidget(self)
        self.siteAContainer.setAutoFillBackground(True)
        self.siteAContainer.setStyleSheet("""
            QWidget {
                background-color: rgba(229, 229, 229, 1);
                border-radius: 5%;
            }"""
        )
        self.siteAContainer.setGeometry(230, 150, 900, 550)

        # Site A vertical stack
        self.configVLayout = QVBoxLayout(self)
        self.configVLayout.setSpacing(10)

        # Scroll area
        self.siteAScroll = QScrollArea(self)
        self.siteAScroll.setAutoFillBackground(True)
        self.siteAScroll.setStyleSheet("""
            QScrollArea {
                background-color: rgba(225, 225, 225, 0);
                border-radius: 5%;
            }"""
        )
        # add widgets to scroll view
        self.siteAScroll.setWidget(self.siteAContainer)
        self.siteAScroll.setWidgetResizable(True)
        self.siteAScroll.setGeometry(230, 150, 900, 550)
        # define each UI field and append them to the vertical stack view
        self.dotColorUI(parent)                       #
        self.pathColorUI(parent)                      #
        self.fileHeaderUI(parent)
        self.showSiteNamesUI(parent)
        self.avoidSitesUI(parent)
        # append the vertical stack view into a container view
        self.siteAContainer.setLayout(self.configVLayout)


    # Site A latitude
    def dotColorUI(self, parent):
        # Horizontal stack
        self.dotColorHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A lat label
        self.dotColorLabel = QLabel(self)
        self.dotColorLabel.setText("Select dot color:")
        self.dotColorLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.dotColorLabel.setAlignment(Qt.AlignLeft)
        self.dotColorLabel.setFixedWidth(500)
        self.dotColorLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site A latitude text input
        # drop down
        self.dotColorOptionList = QComboBox(self)
        self.dotColorOptionList.addItems(["-- Select --", "Black", "Red", "Green", "Blue", "Yellow", "Brown", "Orange", "Light Green"])
        self.dotColorOptionList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.dotColorOptionList.activated.connect(lambda: self.dotColorSelected(parent))
        self.dotColorOptionList.setGeometry(530, 140, 150, 30)
        # Add to H stack
        self.dotColorHLayout.addWidget(self.dotColorLabel)
        self.dotColorHLayout.addWidget(self.dotColorOptionList)
        # Add to V stack
        self.configVLayout.addLayout(self.dotColorHLayout)

    # Site A latitude
    def pathColorUI(self, parent):
        # Horizontal stack
        self.pathColorHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A lat label
        self.pathColorLabel = QLabel(self)
        self.pathColorLabel.setText("Select path color:")
        self.pathColorLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.pathColorLabel.setAlignment(Qt.AlignLeft)
        self.pathColorLabel.setFixedWidth(500)
        self.pathColorLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site A latitude text input
        # drop down
        self.pathColorOptionList = QComboBox(self)
        self.pathColorOptionList.addItems(["-- Select --", "Black", "Red", "Green", "Blue", "Yellow", "Brown", "Orange", "Light Green"])
        self.pathColorOptionList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.pathColorOptionList.activated.connect(lambda: self.pathColorSelected(parent))
        self.pathColorOptionList.setGeometry(530, 140, 150, 30)
        # Add to H stack
        self.pathColorHLayout.addWidget(self.pathColorLabel)
        self.pathColorHLayout.addWidget(self.pathColorOptionList)
        # Add to V stack
        self.configVLayout.addLayout(self.pathColorHLayout)


    def fileHeaderUI(self, parent):
        # Horizontal stack
        self.fileHeaderHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A lat label
        self.fileHeaderLabel = QLabel(self)
        self.fileHeaderLabel.setText("Imported csv data has a header (Yes or No):")
        self.fileHeaderLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.fileHeaderLabel.setAlignment(Qt.AlignLeft)
        self.fileHeaderLabel.setFixedWidth(500)
        self.fileHeaderLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site A latitude text input
        # drop down
        self.fileHeaderOptionList = QComboBox(self)
        self.fileHeaderOptionList.addItems(["Yes", "No"])
        self.fileHeaderOptionList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.fileHeaderOptionList.activated.connect(lambda: self.fileHeaderSelected(parent))
        self.fileHeaderOptionList.setGeometry(530, 140, 150, 30)
        # Add to H stack
        self.fileHeaderHLayout.addWidget(self.fileHeaderLabel)
        self.fileHeaderHLayout.addWidget(self.fileHeaderOptionList)
        # Add to V stack
        self.configVLayout.addLayout(self.fileHeaderHLayout)


    def showSiteNamesUI(self, parent):
        # Horizontal stack
        self.showSiteNamesHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A lat label
        self.showSiteNamesLabel = QLabel(self)
        self.showSiteNamesLabel.setText("Show site names on Google earth (Yes or No):")
        self.showSiteNamesLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.showSiteNamesLabel.setAlignment(Qt.AlignLeft)
        self.showSiteNamesLabel.setFixedWidth(500)
        self.showSiteNamesLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site A latitude text input
        # drop down
        self.showSiteNamesOptionList = QComboBox(self)
        self.showSiteNamesOptionList.addItems(["Yes", "No"])
        self.showSiteNamesOptionList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.showSiteNamesOptionList.activated.connect(lambda: self.showSiteNamesSelected(parent))
        self.showSiteNamesOptionList.setGeometry(530, 140, 150, 30)
        # Add to H stack
        self.showSiteNamesHLayout.addWidget(self.showSiteNamesLabel)
        self.showSiteNamesHLayout.addWidget(self.showSiteNamesOptionList)
        # Add to V stack
        self.configVLayout.addLayout(self.showSiteNamesHLayout)


    def avoidSitesUI(self, parent):
        # Horizontal stack
        self.avoidSitesHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A lat label
        self.avoidSitesLabel = QLabel(self)
        self.avoidSitesLabel.setText("Avoid sites altogether (Yes or No):")
        self.avoidSitesLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.avoidSitesLabel.setAlignment(Qt.AlignLeft)
        self.avoidSitesLabel.setFixedWidth(500)
        self.avoidSitesLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site A latitude text input
        # drop down
        self.avoidSitesOptionList = QComboBox(self)
        self.avoidSitesOptionList.addItems(["No", "Yes"])
        self.avoidSitesOptionList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.avoidSitesOptionList.activated.connect(lambda: self.avoidSitesSelected(parent))
        self.avoidSitesOptionList.setGeometry(530, 140, 150, 30)
        # Add to H stack
        self.avoidSitesHLayout.addWidget(self.avoidSitesLabel)
        self.avoidSitesHLayout.addWidget(self.avoidSitesOptionList)
        # Add to V stack
        self.configVLayout.addLayout(self.avoidSitesHLayout)



    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    def dotColorSelected(self, parent):
        pass

    def pathColorSelected(self, parent):
        pass

    def fileHeaderSelected(self, parent):
        pass

    def showSiteNamesSelected(self, parent):
        pass

    def avoidSitesSelected(self, parent):
        pass

    def nextBtnClicked(self, parent):
        pass
