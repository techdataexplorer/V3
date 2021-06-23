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
#import sip
import folium
import urllib.request
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


# Data Model
from constants.accountData import AccountData
from constants.firebaseData import FirebaseData
from constants.pathDesignData import PathDesignData


# Modules
from modules.pathProfileModules import PathProfileModules


# "3. Path Profile Page"
class PathDesignWidget3(QWidget):

    def __init__(self, parent=None):
        super(PathDesignWidget3, self).__init__(parent)
        self.initUI(parent)


    def initUI(self, parent):
        self.sideMenuUI(parent)
        self.accountUI(parent)
        self.progressUI(parent)
        self.resultsUI(parent)
        self.calculationsUI(parent)

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
        self.profilePhoto.setPixmap(QPixmap("./img/user.png")) # path starts from main.py
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
        self.projectNameTag.setText("Path Design")
        self.projectNameTag.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 20px;
                border-radius: 5%;
                background-color: rgba(124, 145, 254, 1);
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
        self.mapBtn.setText("1. Import/select sites")
        self.mapBtn.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 20px;
                background-color:rgba(225, 225, 225, 0);
                text-decoration: underline;
            }"""
        )
        self.mapBtn.setGeometry(450, 10, 200, 50)
        self.mapBtn.clicked.connect(lambda: self.moveToPathDesignPage1(parent))

        # 2. Select site button
        self.selectSitesBtn = QPushButton(self)
        self.selectSitesBtn.setText("2. Path calculation")
        self.selectSitesBtn.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 20px;
                background-color:rgba(225, 225, 225, 0);
                text-decoration: underline;
            }"""
        )
        self.selectSitesBtn.setGeometry(700, 10, 200, 50)
        self.selectSitesBtn.clicked.connect(lambda: self.moveToPathDesignPage2(parent))

        # 3. Configure parameters
        self.selectSitesBtn = QPushButton(self)
        self.selectSitesBtn.setText("3. Path profile")
        self.selectSitesBtn.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 20px;
                background-color:rgba(225, 225, 225, 0);
                text-decoration: underline;
            }"""
        )
        self.selectSitesBtn.setGeometry(950, 10, 200, 50)


    def resultsUI(self, parent):
        # parameters view wrapper
        self.resultsContainer = QWidget(self)
        self.resultsContainer.setAutoFillBackground(True)
        self.resultsContainer.setStyleSheet("""
            background-color: white;
            border-radius: 5%;
        """)
        self.resultsContainer.setGeometry(210, 70, 980, 720)

        # Message label
        self.directionMsgLabel2 = QLabel(self)
        self.directionMsgLabel2.setText("Calculation results.")
        self.directionMsgLabel2.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 20px;
            }"""
        )
        self.directionMsgLabel2.setGeometry(240, 90, 500, 30)
        self.directionMsgLabel2.setAlignment(Qt.AlignLeft)


        # go to path calculation btn
        self.nextPageBtn = QPushButton(self)
        self.nextPageBtn.setText("Done")
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
        self.nextPageBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToPathDesignPage0(parent))

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
        self.importSitesBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToPathDesignPage2(parent)) # validate the rows


    # Site A param UI
    def calculationsUI(self, parent):

        ### Site A wrapper ###
        self.siteAContainer = QWidget(self)
        self.siteAContainer.setAutoFillBackground(True)
        self.siteAContainer.setStyleSheet("""
            QWidget {
                background-color: rgba(229, 229, 229, 1);
                border-radius: 5%;
            }"""
        )
        self.siteAContainer.setGeometry(230, 140, 940, 590)

        # Site A vertical stack
        self.resultVLayout = QVBoxLayout(self)
        self.resultVLayout.setSpacing(10)

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
        self.siteAScroll.setGeometry(230, 140, 940, 590)
        # define each UI field and append them to the vertical stack view
        ## section 1 ##
        self.pathProfileImageTitleUI()
        self.pathProfileImg()
        self.pathCalculationOutputUI()
        self.EIRPUI()
        self.azimuthUI()
        self.pathDistanceUI()
        self.freeSpaceLossUI()
        self.receivedSignalLevelUI()
        self.flatFadeMarginUI()
        self.dispersiveFadeMarginUI()
        self.northAmericanMethologyUI()
        self.americanFlatFadingMultipathOutageSecondsUI()
        self.americanDispersiveMultipathOutageSecondsUI()
        self.americanRainOutageSecondsUI()
        self.americanAvailabilityVigantsBarnettUI()
        self.ITURMethologyUI()
        self.ITURFlatFadingMultipathOutageSecondsUI()
        self.ITURDispersiveMultipathOutageSecondsUI()
        self.ITURRainOutageSecondsUI()
        self.ITURAvailabilityVigantsBarnettUI()
        # append the vertical stack view into a container view
        self.siteAContainer.setLayout(self.resultVLayout)



    # Path Calculation Output
    def pathProfileImageTitleUI(self):
        # Horizontal stack
        self.pathProfileImageTitleHLayout = QHBoxLayout() # remove 'self' due to err msg
        # pathProfileImageTitle label
        self.pathProfileImageTitleLabel = QLabel(self)
        self.pathProfileImageTitleLabel.setText("Path Profile")
        self.pathProfileImageTitleLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 25px;
                text-decoration: underline;
            }"""
        )
        self.pathProfileImageTitleLabel.setAlignment(Qt.AlignCenter)
        self.pathProfileImageTitleLabel.setFixedWidth(900)
        self.pathProfileImageTitleLabel.setFixedHeight(80)
        self.pathProfileImageTitleLabel.setContentsMargins(10, 15, 10, 10) # margin
        # Add to H stack
        self.pathProfileImageTitleHLayout.addWidget(self.pathProfileImageTitleLabel)
        # Add to V stack
        self.resultVLayout.addLayout(self.pathProfileImageTitleHLayout)


    def pathProfileImg(self):
        # Horizontal stack
        self.pathProfileHLayout = QHBoxLayout() # remove 'self' due to err msg
        self.pathProfileLabel = QLabel(self)
        # url = 'https://cloudrf.com/API/archive/data?ppa=0621081638_TEST_PPA&uid=32004'
        # data = urllib.request.urlopen(url).read()
        # image = QImage()
        # image.loadFromData(data)
        # image = "./img/path-profile.png"
        self.pathProfileLabel.setPixmap(QPixmap("./img/placeholder.png")) # path starts from main.py

        self.pathProfileLabel.setAlignment(Qt.AlignCenter)
        self.pathProfileLabel.setFixedWidth(900)
        self.pathProfileLabel.setFixedHeight(450)
        self.pathProfileLabel.setScaledContents(True)
        # Add to H stack
        self.pathProfileHLayout.addWidget(self.pathProfileLabel)
        # Add to V stack
        self.resultVLayout.addLayout(self.pathProfileHLayout)


    # Path Calculation Output
    def pathCalculationOutputUI(self):
        # Horizontal stack
        self.pathCalculationOutputHLayout = QHBoxLayout() # remove 'self' due to err msg
        # pathCalculationOutput label
        self.pathCalculationOutputLabel = QLabel(self)
        self.pathCalculationOutputLabel.setText("Path Calculation Results")
        self.pathCalculationOutputLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 25px;
                text-decoration: underline;
            }"""
        )
        self.pathCalculationOutputLabel.setAlignment(Qt.AlignCenter)
        self.pathCalculationOutputLabel.setFixedWidth(900)
        self.pathCalculationOutputLabel.setFixedHeight(80)
        self.pathCalculationOutputLabel.setContentsMargins(10, 15, 10, 10) # margin
        # Add to H stack
        self.pathCalculationOutputHLayout.addWidget(self.pathCalculationOutputLabel)
        # Add to V stack
        self.resultVLayout.addLayout(self.pathCalculationOutputHLayout)


    # EIRP
    def EIRPUI(self):
        # Horizontal stack
        self.EIRPHLayout = QHBoxLayout() # remove 'self' due to err msg
        # EIRP label
        self.EIRPLabel = QLabel(self)
        self.EIRPLabel.setText("EIRP:")
        self.EIRPLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.EIRPLabel.setAlignment(Qt.AlignLeft)
        self.EIRPLabel.setFixedWidth(750)
        self.EIRPLabel.setContentsMargins(10, 15, 10, 10) # margin
        # EIRP result (read only)
        self.EIRPTextBox = QLineEdit(self)
        self.EIRPTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.EIRPTextBox.setText("---")
        self.EIRPTextBox.setAlignment(Qt.AlignLeft)
        self.EIRPTextBox.setFixedWidth(150)
        self.EIRPTextBox.setReadOnly(True)
        # Add to H stack
        self.EIRPHLayout.addWidget(self.EIRPLabel)
        self.EIRPHLayout.addWidget(self.EIRPTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.EIRPHLayout)


    # Azimuth
    def azimuthUI(self):
        # Horizontal stack
        self.azimuthHLayout = QHBoxLayout() # remove 'self' due to err msg
        # azimuth label
        self.azimuthLabel = QLabel(self)
        self.azimuthLabel.setText("Azimuth:")
        self.azimuthLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.azimuthLabel.setAlignment(Qt.AlignLeft)
        self.azimuthLabel.setFixedWidth(750)
        self.azimuthLabel.setContentsMargins(10, 15, 10, 10) # margin
        # azimuth result (read only)
        self.azimuthTextBox = QLineEdit(self)
        self.azimuthTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.azimuthTextBox.setText("---")
        self.azimuthTextBox.setAlignment(Qt.AlignLeft)
        self.azimuthTextBox.setFixedWidth(150)
        self.azimuthTextBox.setReadOnly(True)
        # Add to H stack
        self.azimuthHLayout.addWidget(self.azimuthLabel)
        self.azimuthHLayout.addWidget(self.azimuthTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.azimuthHLayout)


    # Path Distance
    def pathDistanceUI(self):
        # Horizontal stack
        self.pathDistanceHLayout = QHBoxLayout() # remove 'self' due to err msg
        # pathDistance label
        self.pathDistanceLabel = QLabel(self)
        self.pathDistanceLabel.setText("Path Distance:")
        self.pathDistanceLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.pathDistanceLabel.setAlignment(Qt.AlignLeft)
        self.pathDistanceLabel.setFixedWidth(750)
        self.pathDistanceLabel.setContentsMargins(10, 15, 10, 10) # margin
        # pathDistance result (read only)
        self.pathDistanceTextBox = QLineEdit(self)
        self.pathDistanceTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.pathDistanceTextBox.setText("---")
        self.pathDistanceTextBox.setAlignment(Qt.AlignLeft)
        self.pathDistanceTextBox.setFixedWidth(150)
        self.pathDistanceTextBox.setReadOnly(True)
        # Add to H stack
        self.pathDistanceHLayout.addWidget(self.pathDistanceLabel)
        self.pathDistanceHLayout.addWidget(self.pathDistanceTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.pathDistanceHLayout)


    # Free Space Loss
    def freeSpaceLossUI(self):
        # Horizontal stack
        self.freeSpaceLossHLayout = QHBoxLayout() # remove 'self' due to err msg
        # freeSpaceLoss label
        self.freeSpaceLossLabel = QLabel(self)
        self.freeSpaceLossLabel.setText("Free Space Loss (dB):")
        self.freeSpaceLossLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.freeSpaceLossLabel.setAlignment(Qt.AlignLeft)
        self.freeSpaceLossLabel.setFixedWidth(750)
        self.freeSpaceLossLabel.setContentsMargins(10, 15, 10, 10) # margin
        # freeSpaceLoss result (read only)
        self.freeSpaceLossTextBox = QLineEdit(self)
        self.freeSpaceLossTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.freeSpaceLossTextBox.setText("---")
        self.freeSpaceLossTextBox.setAlignment(Qt.AlignLeft)
        self.freeSpaceLossTextBox.setFixedWidth(150)
        self.freeSpaceLossTextBox.setReadOnly(True)
        # Add to H stack
        self.freeSpaceLossHLayout.addWidget(self.freeSpaceLossLabel)
        self.freeSpaceLossHLayout.addWidget(self.freeSpaceLossTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.freeSpaceLossHLayout)


    # Received Signal Level
    def receivedSignalLevelUI(self):
        # Horizontal stack
        self.receivedSignalLevelHLayout = QHBoxLayout() # remove 'self' due to err msg
        # receivedSignalLevel label
        self.receivedSignalLevelLabel = QLabel(self)
        self.receivedSignalLevelLabel.setText("Received Signal Level (dBm):")
        self.receivedSignalLevelLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.receivedSignalLevelLabel.setAlignment(Qt.AlignLeft)
        self.receivedSignalLevelLabel.setFixedWidth(750)
        self.receivedSignalLevelLabel.setContentsMargins(10, 15, 10, 10) # margin
        # receivedSignalLevel result (read only)
        self.receivedSignalLevelTextBox = QLineEdit(self)
        self.receivedSignalLevelTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.receivedSignalLevelTextBox.setText("---")
        self.receivedSignalLevelTextBox.setAlignment(Qt.AlignLeft)
        self.receivedSignalLevelTextBox.setFixedWidth(150)
        self.receivedSignalLevelTextBox.setReadOnly(True)
        # Add to H stack
        self.receivedSignalLevelHLayout.addWidget(self.receivedSignalLevelLabel)
        self.receivedSignalLevelHLayout.addWidget(self.receivedSignalLevelTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.receivedSignalLevelHLayout)


    # flatFadeMargin
    def flatFadeMarginUI(self):
        # Horizontal stack
        self.flatFadeMarginHLayout = QHBoxLayout() # remove 'self' due to err msg
        # flatFadeMargin label
        self.flatFadeMarginLabel = QLabel(self)
        self.flatFadeMarginLabel.setText("Flat Fade Margin (dB):")
        self.flatFadeMarginLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.flatFadeMarginLabel.setAlignment(Qt.AlignLeft)
        self.flatFadeMarginLabel.setFixedWidth(750)
        self.flatFadeMarginLabel.setContentsMargins(10, 15, 10, 10) # margin
        # flatFadeMargin result (read only)
        self.flatFadeMarginTextBox = QLineEdit(self)
        self.flatFadeMarginTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.flatFadeMarginTextBox.setText("---")
        self.flatFadeMarginTextBox.setAlignment(Qt.AlignLeft)
        self.flatFadeMarginTextBox.setFixedWidth(150)
        self.flatFadeMarginTextBox.setReadOnly(True)
        # Add to H stack
        self.flatFadeMarginHLayout.addWidget(self.flatFadeMarginLabel)
        self.flatFadeMarginHLayout.addWidget(self.flatFadeMarginTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.flatFadeMarginHLayout)


    # Dispersive Fade Margin
    def dispersiveFadeMarginUI(self):
        # Horizontal stack
        self.dispersiveFadeMarginHLayout = QHBoxLayout() # remove 'self' due to err msg
        # dispersiveFadeMargin label
        self.dispersiveFadeMarginLabel = QLabel(self)
        self.dispersiveFadeMarginLabel.setText("Dispersive Fade Margin (dB):")
        self.dispersiveFadeMarginLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.dispersiveFadeMarginLabel.setAlignment(Qt.AlignLeft)
        self.dispersiveFadeMarginLabel.setFixedWidth(750)
        self.dispersiveFadeMarginLabel.setContentsMargins(10, 15, 10, 10) # margin
        # dispersiveFadeMargin result (read only)
        self.dispersiveFadeMarginTextBox = QLineEdit(self)
        self.dispersiveFadeMarginTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.dispersiveFadeMarginTextBox.setText("---")
        self.dispersiveFadeMarginTextBox.setAlignment(Qt.AlignLeft)
        self.dispersiveFadeMarginTextBox.setFixedWidth(150)
        self.dispersiveFadeMarginTextBox.setReadOnly(True)
        # Add to H stack
        self.dispersiveFadeMarginHLayout.addWidget(self.dispersiveFadeMarginLabel)
        self.dispersiveFadeMarginHLayout.addWidget(self.dispersiveFadeMarginTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.dispersiveFadeMarginHLayout)


    # northAmericanMethology
    def northAmericanMethologyUI(self):
        # Horizontal stack
        self.northAmericanMethologyHLayout = QHBoxLayout() # remove 'self' due to err msg
        # northAmericanMethology label
        self.northAmericanMethologyLabel = QLabel(self)
        self.northAmericanMethologyLabel.setText("Availability: North American Methology")
        self.northAmericanMethologyLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 25px;
                text-decoration: underline;
            }"""
        )
        self.northAmericanMethologyLabel.setAlignment(Qt.AlignCenter)
        self.northAmericanMethologyLabel.setFixedWidth(900)
        self.northAmericanMethologyLabel.setFixedHeight(80)
        self.northAmericanMethologyLabel.setContentsMargins(10, 15, 10, 10) # margin
        # Add to H stack
        self.northAmericanMethologyHLayout.addWidget(self.northAmericanMethologyLabel)
        # Add to V stack
        self.resultVLayout.addLayout(self.northAmericanMethologyHLayout)


    # American Flat Fading Multipath Outage Seconds
    def americanFlatFadingMultipathOutageSecondsUI(self):
        # Horizontal stack
        self.americanFlatFadingMultipathOutageSecondsHLayout = QHBoxLayout() # remove 'self' due to err msg
        # americanFlatFadingMultipathOutageSeconds label
        self.americanFlatFadingMultipathOutageSecondsLabel = QLabel(self)

        self.americanFlatFadingMultipathOutageSecondsLabel.setText("Annual two-way American Flat Fading Multipath Outage Seconds:")
        self.americanFlatFadingMultipathOutageSecondsLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.americanFlatFadingMultipathOutageSecondsLabel.setAlignment(Qt.AlignLeft)
        self.americanFlatFadingMultipathOutageSecondsLabel.setFixedWidth(750)
        self.americanFlatFadingMultipathOutageSecondsLabel.setContentsMargins(10, 15, 10, 10) # margin
        # americanFlatFadingMultipathOutageSeconds result (read only)
        self.americanFlatFadingMultipathOutageSecondsTextBox = QLineEdit(self)
        self.americanFlatFadingMultipathOutageSecondsTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.americanFlatFadingMultipathOutageSecondsTextBox.setText("---")
        self.americanFlatFadingMultipathOutageSecondsTextBox.setAlignment(Qt.AlignLeft)
        self.americanFlatFadingMultipathOutageSecondsTextBox.setFixedWidth(150)
        self.americanFlatFadingMultipathOutageSecondsTextBox.setReadOnly(True)
        # Add to H stack
        self.americanFlatFadingMultipathOutageSecondsHLayout.addWidget(self.americanFlatFadingMultipathOutageSecondsLabel)
        self.americanFlatFadingMultipathOutageSecondsHLayout.addWidget(self.americanFlatFadingMultipathOutageSecondsTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.americanFlatFadingMultipathOutageSecondsHLayout)


    # American Dispersive Multipath Outage Seconds
    def americanDispersiveMultipathOutageSecondsUI(self):
        # Horizontal stack
        self.americanDispersiveMultipathOutageSecondsHLayout = QHBoxLayout() # remove 'self' due to err msg
        # americanDispersiveMultipathOutageSeconds label
        self.americanDispersiveMultipathOutageSecondsLabel = QLabel(self)
        self.americanDispersiveMultipathOutageSecondsLabel.setText("Annual two-way Dispersive Multipath Outage Seconds:")
        self.americanDispersiveMultipathOutageSecondsLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.americanDispersiveMultipathOutageSecondsLabel.setAlignment(Qt.AlignLeft)
        self.americanDispersiveMultipathOutageSecondsLabel.setFixedWidth(750)
        self.americanDispersiveMultipathOutageSecondsLabel.setContentsMargins(10, 15, 10, 10) # margin
        # americanDispersiveMultipathOutageSeconds result (read only)
        self.americanDispersiveMultipathOutageSecondsTextBox = QLineEdit(self)
        self.americanDispersiveMultipathOutageSecondsTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.americanDispersiveMultipathOutageSecondsTextBox.setText("---")
        self.americanDispersiveMultipathOutageSecondsTextBox.setAlignment(Qt.AlignLeft)
        self.americanDispersiveMultipathOutageSecondsTextBox.setFixedWidth(150)
        self.americanDispersiveMultipathOutageSecondsTextBox.setReadOnly(True)
        # Add to H stack
        self.americanDispersiveMultipathOutageSecondsHLayout.addWidget(self.americanDispersiveMultipathOutageSecondsLabel)
        self.americanDispersiveMultipathOutageSecondsHLayout.addWidget(self.americanDispersiveMultipathOutageSecondsTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.americanDispersiveMultipathOutageSecondsHLayout)


    # American Rain Outage Seconds
    def americanRainOutageSecondsUI(self):
        # Horizontal stack
        self.americanRainOutageSecondsHLayout = QHBoxLayout() # remove 'self' due to err msg
        # americanRainOutageSeconds label
        self.americanRainOutageSecondsLabel = QLabel(self)
        self.americanRainOutageSecondsLabel.setText("Annual two-way Rain Outage Seconds:")
        self.americanRainOutageSecondsLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.americanRainOutageSecondsLabel.setAlignment(Qt.AlignLeft)
        self.americanRainOutageSecondsLabel.setFixedWidth(750)
        self.americanRainOutageSecondsLabel.setContentsMargins(10, 15, 10, 10) # margin
        # americanRainOutageSeconds result (read only)
        self.americanRainOutageSecondsTextBox = QLineEdit(self)
        self.americanRainOutageSecondsTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.americanRainOutageSecondsTextBox.setText("---")
        self.americanRainOutageSecondsTextBox.setAlignment(Qt.AlignLeft)
        self.americanRainOutageSecondsTextBox.setFixedWidth(150)
        self.americanRainOutageSecondsTextBox.setReadOnly(True)
        # Add to H stack
        self.americanRainOutageSecondsHLayout.addWidget(self.americanRainOutageSecondsLabel)
        self.americanRainOutageSecondsHLayout.addWidget(self.americanRainOutageSecondsTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.americanRainOutageSecondsHLayout)


    # American Rain Outage Seconds
    def americanAvailabilityVigantsBarnettUI(self):
        # Horizontal stack
        self.americanAvailabilityVigantsBarnettHLayout = QHBoxLayout() # remove 'self' due to err msg
        # americanAvailabilityVigantsBarnett label
        self.americanAvailabilityVigantsBarnettLabel = QLabel(self)
        self.americanAvailabilityVigantsBarnettLabel.setText("Annual two-way Availability Vigants-Barnett & Crane:")
        self.americanAvailabilityVigantsBarnettLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.americanAvailabilityVigantsBarnettLabel.setAlignment(Qt.AlignLeft)
        self.americanAvailabilityVigantsBarnettLabel.setFixedWidth(750)
        self.americanAvailabilityVigantsBarnettLabel.setContentsMargins(10, 15, 10, 10) # margin
        # americanAvailabilityVigantsBarnett result (read only)
        self.americanAvailabilityVigantsBarnettTextBox = QLineEdit(self)
        self.americanAvailabilityVigantsBarnettTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.americanAvailabilityVigantsBarnettTextBox.setText("---")
        self.americanAvailabilityVigantsBarnettTextBox.setAlignment(Qt.AlignLeft)
        self.americanAvailabilityVigantsBarnettTextBox.setFixedWidth(150)
        self.americanAvailabilityVigantsBarnettTextBox.setReadOnly(True)
        # Add to H stack
        self.americanAvailabilityVigantsBarnettHLayout.addWidget(self.americanAvailabilityVigantsBarnettLabel)
        self.americanAvailabilityVigantsBarnettHLayout.addWidget(self.americanAvailabilityVigantsBarnettTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.americanAvailabilityVigantsBarnettHLayout)


    # ITURMethology
    def ITURMethologyUI(self):
        # Horizontal stack
        self.ITURMethologyHLayout = QHBoxLayout() # remove 'self' due to err msg
        # ITURMethology label
        self.ITURMethologyLabel = QLabel(self)
        self.ITURMethologyLabel.setText("Availability: ITU-R Methology")
        self.ITURMethologyLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 25px;
                text-decoration: underline;
            }"""
        )
        self.ITURMethologyLabel.setAlignment(Qt.AlignCenter)
        self.ITURMethologyLabel.setFixedWidth(900)
        self.ITURMethologyLabel.setFixedHeight(80)
        self.ITURMethologyLabel.setContentsMargins(10, 15, 10, 10) # margin
        # Add to H stack
        self.ITURMethologyHLayout.addWidget(self.ITURMethologyLabel)
        # Add to V stack
        self.resultVLayout.addLayout(self.ITURMethologyHLayout)


    # American Flat Fading Multipath Outage Seconds
    def ITURFlatFadingMultipathOutageSecondsUI(self):
        # Horizontal stack
        self.ITURFlatFadingMultipathOutageSecondsHLayout = QHBoxLayout() # remove 'self' due to err msg
        # ITURFlatFadingMultipathOutageSeconds label
        self.ITURFlatFadingMultipathOutageSecondsLabel = QLabel(self)

        self.ITURFlatFadingMultipathOutageSecondsLabel.setText("Annual two-way ITU-R Flat Fading Multipath Outage Seconds:")
        self.ITURFlatFadingMultipathOutageSecondsLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.ITURFlatFadingMultipathOutageSecondsLabel.setAlignment(Qt.AlignLeft)
        self.ITURFlatFadingMultipathOutageSecondsLabel.setFixedWidth(750)
        self.ITURFlatFadingMultipathOutageSecondsLabel.setContentsMargins(10, 15, 10, 10) # margin
        # ITURFlatFadingMultipathOutageSeconds result (read only)
        self.ITURFlatFadingMultipathOutageSecondsTextBox = QLineEdit(self)
        self.ITURFlatFadingMultipathOutageSecondsTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.ITURFlatFadingMultipathOutageSecondsTextBox.setText("---")
        self.ITURFlatFadingMultipathOutageSecondsTextBox.setAlignment(Qt.AlignLeft)
        self.ITURFlatFadingMultipathOutageSecondsTextBox.setFixedWidth(150)
        self.ITURFlatFadingMultipathOutageSecondsTextBox.setReadOnly(True)
        # Add to H stack
        self.ITURFlatFadingMultipathOutageSecondsHLayout.addWidget(self.ITURFlatFadingMultipathOutageSecondsLabel)
        self.ITURFlatFadingMultipathOutageSecondsHLayout.addWidget(self.ITURFlatFadingMultipathOutageSecondsTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.ITURFlatFadingMultipathOutageSecondsHLayout)


    # Dispersive Multipath Outage Seconds
    def ITURDispersiveMultipathOutageSecondsUI(self):
        # Horizontal stack
        self.ITURDispersiveMultipathOutageSecondsHLayout = QHBoxLayout() # remove 'self' due to err msg
        # ITURDispersiveMultipathOutageSeconds label
        self.ITURDispersiveMultipathOutageSecondsLabel = QLabel(self)
        self.ITURDispersiveMultipathOutageSecondsLabel.setText("Annual two-way ITU-R Dispersive Multipath Outage Seconds:")
        self.ITURDispersiveMultipathOutageSecondsLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.ITURDispersiveMultipathOutageSecondsLabel.setAlignment(Qt.AlignLeft)
        self.ITURDispersiveMultipathOutageSecondsLabel.setFixedWidth(750)
        self.ITURDispersiveMultipathOutageSecondsLabel.setContentsMargins(10, 15, 10, 10) # margin
        # ITURDispersiveMultipathOutageSeconds result (read only)
        self.ITURDispersiveMultipathOutageSecondsTextBox = QLineEdit(self)
        self.ITURDispersiveMultipathOutageSecondsTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.ITURDispersiveMultipathOutageSecondsTextBox.setText("---")
        self.ITURDispersiveMultipathOutageSecondsTextBox.setAlignment(Qt.AlignLeft)
        self.ITURDispersiveMultipathOutageSecondsTextBox.setFixedWidth(150)
        self.ITURDispersiveMultipathOutageSecondsTextBox.setReadOnly(True)
        # Add to H stack
        self.ITURDispersiveMultipathOutageSecondsHLayout.addWidget(self.ITURDispersiveMultipathOutageSecondsLabel)
        self.ITURDispersiveMultipathOutageSecondsHLayout.addWidget(self.ITURDispersiveMultipathOutageSecondsTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.ITURDispersiveMultipathOutageSecondsHLayout)


    # ITU-R Rain Outage Seconds
    def ITURRainOutageSecondsUI(self):
        # Horizontal stack
        self.ITURRainOutageSecondsHLayout = QHBoxLayout() # remove 'self' due to err msg
        # ITURRainOutageSeconds label
        self.ITURRainOutageSecondsLabel = QLabel(self)
        self.ITURRainOutageSecondsLabel.setText("Annual two-way ITU-R Rain Outage Seconds:")
        self.ITURRainOutageSecondsLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.ITURRainOutageSecondsLabel.setAlignment(Qt.AlignLeft)
        self.ITURRainOutageSecondsLabel.setFixedWidth(750)
        self.ITURRainOutageSecondsLabel.setContentsMargins(10, 15, 10, 10) # margin
        # ITURRainOutageSeconds result (read only)
        self.ITURRainOutageSecondsTextBox = QLineEdit(self)
        self.ITURRainOutageSecondsTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.ITURRainOutageSecondsTextBox.setText("---")
        self.ITURRainOutageSecondsTextBox.setAlignment(Qt.AlignLeft)
        self.ITURRainOutageSecondsTextBox.setFixedWidth(150)
        self.ITURRainOutageSecondsTextBox.setReadOnly(True)
        # Add to H stack
        self.ITURRainOutageSecondsHLayout.addWidget(self.ITURRainOutageSecondsLabel)
        self.ITURRainOutageSecondsHLayout.addWidget(self.ITURRainOutageSecondsTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.ITURRainOutageSecondsHLayout)


    # ITU-R Rain Outage Seconds
    def ITURAvailabilityVigantsBarnettUI(self):
        # Horizontal stack
        self.ITURAvailabilityVigantsBarnettHLayout = QHBoxLayout() # remove 'self' due to err msg
        # ITURAvailabilityVigantsBarnett label
        self.ITURAvailabilityVigantsBarnettLabel = QLabel(self)
        self.ITURAvailabilityVigantsBarnettLabel.setText("Annual two-way ITU-R Availability Vigants-Barnett & Crane:")
        self.ITURAvailabilityVigantsBarnettLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.ITURAvailabilityVigantsBarnettLabel.setAlignment(Qt.AlignLeft)
        self.ITURAvailabilityVigantsBarnettLabel.setFixedWidth(750)
        self.ITURAvailabilityVigantsBarnettLabel.setContentsMargins(10, 15, 10, 10) # margin
        # ITURAvailabilityVigantsBarnett result (read only)
        self.ITURAvailabilityVigantsBarnettTextBox = QLineEdit(self)
        self.ITURAvailabilityVigantsBarnettTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.ITURAvailabilityVigantsBarnettTextBox.setText("---")
        self.ITURAvailabilityVigantsBarnettTextBox.setAlignment(Qt.AlignLeft)
        self.ITURAvailabilityVigantsBarnettTextBox.setFixedWidth(150)
        self.ITURAvailabilityVigantsBarnettTextBox.setReadOnly(True)
        # Add to H stack
        self.ITURAvailabilityVigantsBarnettHLayout.addWidget(self.ITURAvailabilityVigantsBarnettLabel)
        self.ITURAvailabilityVigantsBarnettHLayout.addWidget(self.ITURAvailabilityVigantsBarnettTextBox)
        # Add to V stack
        self.resultVLayout.addLayout(self.ITURAvailabilityVigantsBarnettHLayout)


    def moveToHomePage(self, parent):
        parent.central_widget.setCurrentIndex(2)

    def moveToPathDesignPage0(self, parent):
        parent.central_widget.setCurrentIndex(3)

    def moveToPathDesignPage1(self, parent):
        parent.central_widget.setCurrentIndex(4)

    def moveToPathDesignPage2(self, parent):
        parent.central_widget.setCurrentIndex(5)

    def button03Clicked(self, parent):
        print("Network config btn clicked")
        test = PathProfileModules()
        test.pathProfileAPI(parent)
