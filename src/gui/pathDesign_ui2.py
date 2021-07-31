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
from constants.radioFile import radioData

# Modules
from modules.pathProfileModules import PathProfileModules


# "2. Path Calculation Page"
class PathDesignWidget2(QWidget):

    def __init__(self, parent=None):
        super(PathDesignWidget2, self).__init__(parent)
        self.colcnt = 10
        self.rowcnt = 10
        self.initUI(parent)
        self.update()

    def initUI(self, parent):
        self.sideMenuUI(parent)
        self.accountUI(parent)
        self.progressUI(parent)
        self.parametersUI(parent)
        self.siteAUI(parent)
        self.siteBUI(parent)

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
        self.mapBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToPathDesignPage1(parent))

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
        self.selectSitesBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToPathDesignPage2(parent))

        # 3. Configure parameters
        self.selectSitesBtn = QPushButton(self)
        self.selectSitesBtn.setText("3. Path profile")
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
        self.directionMsgLabel2.setText("Enter the values for each site.")
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
        # self.nextPageBtn.clicked.connect(lambda: self.moveToPathDesignPage3(parent))
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
        self.importSitesBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToPathDesignPage1(parent)) # validate the rows


    # Site A param UI
    def siteAUI(self, parent):

        ### Site A wrapper ###
        self.siteAContainer = QWidget(self)
        self.siteAContainer.setAutoFillBackground(True)
        self.siteAContainer.setStyleSheet("""
            QWidget {
                background-color: rgba(229, 229, 229, 1);
                border-radius: 5%;
            }"""
        )
        self.siteAContainer.setGeometry(230, 180, 450, 550)

        # Site A vertical stack
        self.siteAVLayout = QVBoxLayout(self)
        self.siteAVLayout.setSpacing(10)

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
        self.siteAScroll.setGeometry(230, 180, 450, 550)
        # define each UI field and append them to the vertical stack view
        ## section 1 ##
        self.siteALabelUI()                     # Site A Label
        self.siteARoleOptionUI(parent)          # Site A role option
        self.siteALatUI()                       # Site A Latitude
        self.siteALngUI()                       # Site A Longitude
        self.siteATowerHeightUI()               # Site A Tower Height
        self.siteAAntennaGainUI()               # Site A Antenna Gain
        self.siteAAntennaHeightUI()             # Site A Antenna Height
        self.siteAAntennaTypeUI()               # Site A Antenna Type
        self.siteATransmitPowerUI()             # Site A Transmit Power
        self.siteATXCouplingLossUI()            # Site A TX Coupling Loss
        self.siteARXCouplingLossUI()            # Site A RX Coupling Loss
        self.siteAFieldMarginUI()               # Site A Field Margin
        self.siteAMiscLossesUI()                # Site A Misc Losses
        self.siteARXThresholdUI()               # Site A RX Threshold
        ## section 2 ##
        self.siteAFrequencyUI()                 # Site A Frequency
        self.siteAPolarizationUI()      # Site A Polarization
        self.siteARadioTypeUI()                 # Site A Radio type
        self.siteAModulationUI()                # Site A Modulation
        self.siteABandwidthUI()                 # Site A Bandwidth
        self.siteADataRateUI()                  # Site A Data Rate
        self.siteAAtmAbsUI()                    # Site A Atmospheric Absorption
        self.siteARelativeDispersionFactorUI()  # Site A Relative Dispersion Factor
        # append the vertical stack view into a container view
        self.siteAContainer.setLayout(self.siteAVLayout)

    # Site A label
    def siteALabelUI(self):
        self.siteALabel = QLabel(self)
        self.siteALabel.setText("Site A")
        self.siteALabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
                text-decoration: underline;
            }"""
        )
        self.siteALabel.setGeometry(240, 140, 300, 30)
        self.siteALabel.setAlignment(Qt.AlignLeft)

    # Site A Dropdown menu to choose transmitter or receiver
    def siteARoleOptionUI(self, parent):
        # drop down
        self.siteARoleOptionList = QComboBox(self)
        self.siteARoleOptionList.addItems(["-- Select --", "Transmitter", "Receiver"])
        self.siteARoleOptionList.activated.connect(lambda: self.dropDownAItemSelected(parent))
        self.siteARoleOptionList.setGeometry(530, 140, 150, 30)


    # Site A latitude
    def siteALatUI(self):
        # Horizontal stack
        self.siteALatHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A lat label
        self.siteALatLabel = QLabel(self)
        self.siteALatLabel.setText("Latitude:")
        self.siteALatLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteALatLabel.setAlignment(Qt.AlignLeft)
        self.siteALatLabel.setFixedWidth(230)
        self.siteALatLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site A latitude text input
        self.siteALatTextBox = QDoubleSpinBox(self)
        self.siteALatTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteALatTextBox.setFixedWidth(170)
        self.siteALatTextBox.setFixedHeight(30)
        self.siteALatTextBox.setRange(-90, 90)
        self.siteALatTextBox.setDecimals(4)
        # Add to H stack
        self.siteALatHLayout.addWidget(self.siteALatLabel)
        self.siteALatHLayout.addWidget(self.siteALatTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteALatHLayout)

    # Site A longitude
    def siteALngUI(self):
        # Horizontal stack
        self.siteALngHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A lng label
        self.siteALngLabel = QLabel(self)
        self.siteALngLabel.setText("Longitude:")
        self.siteALngLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteALngLabel.setAlignment(Qt.AlignLeft)
        self.siteALngLabel.setFixedWidth(230)
        self.siteALngLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B latitude text input
        self.siteALngTextBox = QDoubleSpinBox(self)
        self.siteALngTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteALngTextBox.setFixedWidth(170)
        self.siteALngTextBox.setFixedHeight(30)
        self.siteALngTextBox.setRange(-180, 180)
        self.siteALngTextBox.setDecimals(4)
        # Add to H stack
        self.siteALngHLayout.addWidget(self.siteALngLabel)
        self.siteALngHLayout.addWidget(self.siteALngTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteALngHLayout)

    # Site A tower height above ground level
    def siteATowerHeightUI(self):
        # Horizontal stack
        self.siteATHHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A tower height label
        self.siteATHLabel = QLabel(self)
        self.siteATHLabel.setText("Tower Height AGL (ft):")
        self.siteATHLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteATHLabel.setAlignment(Qt.AlignLeft)
        self.siteATHLabel.setFixedWidth(230)
        self.siteATHLabel.setContentsMargins(10, 15, 10, 10) # margin
        # Site A tower height text input
        self.siteATHTextBox = QDoubleSpinBox(self)
        self.siteATHTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteATHTextBox.setFixedWidth(170)
        self.siteATHTextBox.setFixedHeight(30)
        self.siteATHTextBox.setRange(0, 2000)
        # Add to H stack
        self.siteATHHLayout.addWidget(self.siteATHLabel)
        self.siteATHHLayout.addWidget(self.siteATHTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteATHHLayout)

    # Site A Antenna Height above ground level (AGL)
    def siteAAntennaHeightUI(self):
        # Horizontal stack
        self.siteAAntennaHeightHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B antenna height label
        self.siteAAntennaHeightLabel = QLabel(self)
        self.siteAAntennaHeightLabel.setText("Antenna Height AGL (ft):")
        self.siteAAntennaHeightLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteAAntennaHeightLabel.setAlignment(Qt.AlignLeft)
        self.siteAAntennaHeightLabel.setFixedWidth(230)
        self.siteAAntennaHeightLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B antenna height text input
        self.siteAAntennaHeightTextBox = QDoubleSpinBox(self)
        self.siteAAntennaHeightTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteAAntennaHeightTextBox.setFixedWidth(170)
        self.siteAAntennaHeightTextBox.setFixedHeight(30)
        self.siteAAntennaHeightTextBox.setRange(0, 2000)
        # Add to H stack
        self.siteAAntennaHeightHLayout.addWidget(self.siteAAntennaHeightLabel)
        self.siteAAntennaHeightHLayout.addWidget(self.siteAAntennaHeightTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteAAntennaHeightHLayout)

    # Site A antenna gein
    def siteAAntennaGainUI(self):
        # Horizontal stack
        self.siteAAntennaGainHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B antenna gain label
        self.siteAAntennaGainLabel = QLabel(self)
        self.siteAAntennaGainLabel.setText("Antenna Gain (dbi):")
        self.siteAAntennaGainLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteAAntennaGainLabel.setAlignment(Qt.AlignLeft)
        self.siteAAntennaGainLabel.setFixedWidth(230)
        self.siteAAntennaGainLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B antenna gain text input
        self.siteAAntennaGainTextBox = QDoubleSpinBox(self)
        self.siteAAntennaGainTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteAAntennaGainTextBox.setFixedWidth(170)
        self.siteAAntennaGainTextBox.setFixedHeight(30)
        self.siteAAntennaGainTextBox.setRange(0, 100)
        # Add to H stack
        self.siteAAntennaGainHLayout.addWidget(self.siteAAntennaGainLabel)
        self.siteAAntennaGainHLayout.addWidget(self.siteAAntennaGainTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteAAntennaGainHLayout)

    # Site A Antenna Type
    def siteAAntennaTypeUI(self):
        # Antenna data
        # antennaDataList = random.choice(antennaData)
        # Horizontal stack
        self.siteAAntennaTypeHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B antenna gain label
        self.siteAAntennaTypeLabel = QLabel(self)
        self.siteAAntennaTypeLabel.setText("Antenna Type:")
        self.siteAAntennaTypeLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteAAntennaTypeLabel.setAlignment(Qt.AlignLeft)
        self.siteAAntennaTypeLabel.setFixedWidth(150)
        self.siteAAntennaTypeLabel.setContentsMargins(10, 15, 10, 10) # margin
        # drop down
        self.siteAAntennaTypeList = QComboBox(self)
        # self.siteAAntennaTypeList.addItems(["-Select Antenna Type-", "NOKIA", "FPA5250D06-N", "HPX2F-52", "PAR10-59"])
        self.siteAAntennaTypeList.addItems(antennaData)
        self.siteAAntennaTypeList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteAAntennaTypeList.setFixedWidth(250)
        # Add to H stack
        self.siteAAntennaTypeHLayout.addWidget(self.siteAAntennaTypeLabel)
        self.siteAAntennaTypeHLayout.addWidget(self.siteAAntennaTypeList)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteAAntennaTypeHLayout)


    # Site A transmit power
    def siteATransmitPowerUI(self):
        # Horizontal stack
        self.siteATransmitPowerHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A transmit power label
        self.siteATransmitPowerLabel = QLabel(self)
        self.siteATransmitPowerLabel.setText("Transmit Power (dbm):")
        self.siteATransmitPowerLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteATransmitPowerLabel.setAlignment(Qt.AlignLeft)
        self.siteATransmitPowerLabel.setFixedWidth(230)
        self.siteATransmitPowerLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B transmit power text input
        self.siteATransmitPowerTextBox = QDoubleSpinBox(self)
        self.siteATransmitPowerTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteATransmitPowerTextBox.setFixedWidth(170)
        self.siteATransmitPowerTextBox.setFixedHeight(30)
        self.siteATransmitPowerTextBox.setRange(0, 100)
        # Add to H stack
        self.siteATransmitPowerHLayout.addWidget(self.siteATransmitPowerLabel)
        self.siteATransmitPowerHLayout.addWidget(self.siteATransmitPowerTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteATransmitPowerHLayout)


    # Site A TX Coupling Loss
    def siteATXCouplingLossUI(self):
        # Horizontal stac
        self.siteATXCouplingLossHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B TX coupling loss label
        self.siteATXCouplingLossLabel = QLabel(self)
        self.siteATXCouplingLossLabel.setText("TX Coupling Loss (dB):")
        self.siteATXCouplingLossLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteATXCouplingLossLabel.setAlignment(Qt.AlignLeft)
        self.siteATXCouplingLossLabel.setFixedWidth(230)
        self.siteATXCouplingLossLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B TX coupling loss text box
        self.siteATXCouplingLossTextBox = QDoubleSpinBox(self)
        self.siteATXCouplingLossTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteATXCouplingLossTextBox.setFixedWidth(170)
        self.siteATXCouplingLossTextBox.setFixedHeight(30)
        self.siteATXCouplingLossTextBox.setRange(0, 100)

        # Add to H stack
        self.siteATXCouplingLossHLayout.addWidget(self.siteATXCouplingLossLabel)
        self.siteATXCouplingLossHLayout.addWidget(self.siteATXCouplingLossTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteATXCouplingLossHLayout)

    # Site A RX Coupling Loss
    def siteARXCouplingLossUI(self):
        # Horizontal stac
        self.siteARXCouplingLossHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B RX coupling loss label
        self.siteARXCouplingLossLabel = QLabel(self)
        self.siteARXCouplingLossLabel.setText("RX Coupling Loss (dB):")
        self.siteARXCouplingLossLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteARXCouplingLossLabel.setAlignment(Qt.AlignLeft)
        self.siteARXCouplingLossLabel.setFixedWidth(230)
        self.siteARXCouplingLossLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B RX coupling loss text box
        self.siteARXCouplingLossTextBox = QDoubleSpinBox(self)
        self.siteARXCouplingLossTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteARXCouplingLossTextBox.setFixedWidth(170)
        self.siteARXCouplingLossTextBox.setFixedHeight(30)
        self.siteARXCouplingLossTextBox.setRange(0, 100)
        # Add to H stack
        self.siteARXCouplingLossHLayout.addWidget(self.siteARXCouplingLossLabel)
        self.siteARXCouplingLossHLayout.addWidget(self.siteARXCouplingLossTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteARXCouplingLossHLayout)

    # Site A Field Margin
    def siteAFieldMarginUI(self):
        # Horizontal stac
        self.siteAFieldMarginHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B field margin label
        self.siteAFieldMarginLabel = QLabel(self)
        self.siteAFieldMarginLabel.setText("Field Margin:")
        self.siteAFieldMarginLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteAFieldMarginLabel.setAlignment(Qt.AlignLeft)
        self.siteAFieldMarginLabel.setFixedWidth(230)
        self.siteAFieldMarginLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B field margin text box
        self.siteAFieldMarginTextBox = QDoubleSpinBox(self)
        self.siteAFieldMarginTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteAFieldMarginTextBox.setFixedWidth(170)
        self.siteAFieldMarginTextBox.setFixedHeight(30)
        self.siteAFieldMarginTextBox.setRange(0, 100)
        # Add to H stack
        self.siteAFieldMarginHLayout.addWidget(self.siteAFieldMarginLabel)
        self.siteAFieldMarginHLayout.addWidget(self.siteAFieldMarginTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteAFieldMarginHLayout)


    # Site A Misc Losses
    def siteAMiscLossesUI(self):
        # Horizontal stac
        self.siteAMiscLossesHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B Misc losses label
        self.siteAMiscLossesLabel = QLabel(self)
        self.siteAMiscLossesLabel.setText("Misc Losses:")
        self.siteAMiscLossesLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteAMiscLossesLabel.setAlignment(Qt.AlignLeft)
        self.siteAMiscLossesLabel.setFixedWidth(230)
        self.siteAMiscLossesLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B misc losses text box
        self.siteAMiscLossesTextBox = QDoubleSpinBox(self)
        self.siteAMiscLossesTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteAMiscLossesTextBox.setFixedWidth(170)
        self.siteAMiscLossesTextBox.setFixedHeight(30)
        self.siteAMiscLossesTextBox.setRange(0, 100)
        # Add to H stack
        self.siteAMiscLossesHLayout.addWidget(self.siteAMiscLossesLabel)
        self.siteAMiscLossesHLayout.addWidget(self.siteAMiscLossesTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteAMiscLossesHLayout)


    # Site A Receive Threshold
    def siteARXThresholdUI(self):
        # Horizontal stack
        self.siteARXThresholdHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B Receive Threshold label
        self.siteARXThresholdLabel = QLabel(self)
        self.siteARXThresholdLabel.setText("RX Threshold (dbm):")
        self.siteARXThresholdLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteARXThresholdLabel.setAlignment(Qt.AlignLeft)
        self.siteARXThresholdLabel.setFixedWidth(230)
        self.siteARXThresholdLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B Receive Threshold text input
        self.siteARXThresholdTextBox = QDoubleSpinBox(self)
        self.siteARXThresholdTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteARXThresholdTextBox.setFixedWidth(170)
        self.siteARXThresholdTextBox.setFixedHeight(30)
        self.siteARXThresholdTextBox.setRange(-100, 0)
        # Add to H stack
        self.siteARXThresholdHLayout.addWidget(self.siteARXThresholdLabel)
        self.siteARXThresholdHLayout.addWidget(self.siteARXThresholdTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteARXThresholdHLayout)



    # Site A Transmit Frequency (MHz)
    def siteAFrequencyUI(self):
        # Horizontal stack
        self.siteAFrequencyHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A transmit frequency label
        self.siteAFrequencyLabel = QLabel(self)
        self.siteAFrequencyLabel.setText("Frequency (MHz):")
        self.siteAFrequencyLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteAFrequencyLabel.setAlignment(Qt.AlignLeft)
        self.siteAFrequencyLabel.setFixedWidth(230)
        self.siteAFrequencyLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B transmit frequency text input
        self.siteAFrequencyTextBox = QDoubleSpinBox(self)
        self.siteAFrequencyTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteAFrequencyTextBox.setFixedWidth(170)
        self.siteAFrequencyTextBox.setFixedHeight(30)
        self.siteAFrequencyTextBox.setRange(100, 30000)
        self.siteAFrequencyTextBox.setValue(100)
        # Add to H stack
        self.siteAFrequencyHLayout.addWidget(self.siteAFrequencyLabel)
        self.siteAFrequencyHLayout.addWidget(self.siteAFrequencyTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteAFrequencyHLayout)

    # Site A Polarization
    def siteAPolarizationUI(self):
        # Horizontal stack
        self.siteAPolarizationHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A vertical polarization label
        self.siteAPolarizationLabel = QLabel(self)
        self.siteAPolarizationLabel.setText("Polarization:")
        self.siteAPolarizationLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteAPolarizationLabel.setAlignment(Qt.AlignLeft)
        self.siteAPolarizationLabel.setFixedWidth(230)
        self.siteAPolarizationLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site A polarization selection view
        self.siteAPolarizationTextBox = QComboBox(self)
        self.siteAPolarizationTextBox.addItems(["Vertical", "Horizontal"])
        self.siteAPolarizationTextBox.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteAPolarizationTextBox.setFixedWidth(170)

        # Add to H stack
        self.siteAPolarizationHLayout.addWidget(self.siteAPolarizationLabel)
        self.siteAPolarizationHLayout.addWidget(self.siteAPolarizationTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteAPolarizationHLayout)


    # Site A Radio Type
    def siteARadioTypeUI(self):
        # Horizontal stack
        self.siteARadioTypeHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B antenna gain label
        self.siteARadioTypeLabel = QLabel(self)
        self.siteARadioTypeLabel.setText("Radio:")
        self.siteARadioTypeLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteARadioTypeLabel.setAlignment(Qt.AlignLeft)
        self.siteARadioTypeLabel.setFixedWidth(80)
        self.siteARadioTypeLabel.setContentsMargins(10, 15, 10, 10) # margin
        # drop down
        self.siteARadioTypeList = QComboBox(self)
        self.siteARadioTypeList.addItems(radioData)
        self.siteARadioTypeList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteARadioTypeList.setFixedWidth(320)
        # Add to H stack
        self.siteARadioTypeHLayout.addWidget(self.siteARadioTypeLabel)
        self.siteARadioTypeHLayout.addWidget(self.siteARadioTypeList)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteARadioTypeHLayout)


    # Site A Modulation
    def siteAModulationUI(self):
        # Horizontal stack
        self.siteAModulationHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A modulation label
        self.siteAModulationLabel = QLabel(self)
        self.siteAModulationLabel.setText("Modulation (QAM):")
        self.siteAModulationLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteAModulationLabel.setAlignment(Qt.AlignLeft)
        self.siteAModulationLabel.setFixedWidth(230)
        self.siteAModulationLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B modulation text input
        self.siteAModulationTextBox = QDoubleSpinBox(self)
        self.siteAModulationTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteAModulationTextBox.setFixedWidth(170)
        self.siteAModulationTextBox.setFixedHeight(30)
        self.siteAModulationTextBox.setRange(2, 4096)
        # Add to H stack
        self.siteAModulationHLayout.addWidget(self.siteAModulationLabel)
        self.siteAModulationHLayout.addWidget(self.siteAModulationTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteAModulationHLayout)


    # Site A Bandwidth
    def siteABandwidthUI(self):
        # Horizontal stack
        self.siteABandwidthHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A bandwidth label
        self.siteABandwidthLabel = QLabel(self)
        self.siteABandwidthLabel.setText("Bandwidth (MHz):")
        self.siteABandwidthLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteABandwidthLabel.setAlignment(Qt.AlignLeft)
        self.siteABandwidthLabel.setFixedWidth(230)
        self.siteABandwidthLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B bandwidth text input
        self.siteABandwidthTextBox = QDoubleSpinBox(self)
        self.siteABandwidthTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteABandwidthTextBox.setFixedWidth(170)
        self.siteABandwidthTextBox.setFixedHeight(30)
        self.siteABandwidthTextBox.setRange(1, 100)
        # Add to H stack
        self.siteABandwidthHLayout.addWidget(self.siteABandwidthLabel)
        self.siteABandwidthHLayout.addWidget(self.siteABandwidthTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteABandwidthHLayout)


    # Site A Data Rate
    def siteADataRateUI(self):
        # Horizontal stack
        self.siteADataRateHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A data rate label
        self.siteADataRateLabel = QLabel(self)
        self.siteADataRateLabel.setText("Data Rate (Mb/s):")
        self.siteADataRateLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteADataRateLabel.setAlignment(Qt.AlignLeft)
        self.siteADataRateLabel.setFixedWidth(230)
        self.siteADataRateLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B data rate text input
        self.siteADataRateTextBox = QDoubleSpinBox(self)
        self.siteADataRateTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteADataRateTextBox.setFixedWidth(170)
        self.siteADataRateTextBox.setFixedHeight(30)
        self.siteADataRateTextBox.setRange(1, 4000)
        # Add to H stack
        self.siteADataRateHLayout.addWidget(self.siteADataRateLabel)
        self.siteADataRateHLayout.addWidget(self.siteADataRateTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteADataRateHLayout)


    # Site A Atmospheric Absorption
    def siteAAtmAbsUI(self):
        # Horizontal stack
        self.siteAAtmAbsHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A atmospheric absorption label
        self.siteAAtmAbsLabel = QLabel(self)
        self.siteAAtmAbsLabel.setText("Atmospheric Absorption:")
        self.siteAAtmAbsLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteAAtmAbsLabel.setAlignment(Qt.AlignLeft)
        self.siteAAtmAbsLabel.setFixedWidth(230)
        self.siteAAtmAbsLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site A atmospheric absorption text input
        self.siteAAtmAbsTextBox = QDoubleSpinBox(self)
        self.siteAAtmAbsTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteAAtmAbsTextBox.setFixedWidth(170)
        self.siteAAtmAbsTextBox.setFixedHeight(30)
        self.siteAAtmAbsTextBox.setRange(0, 4000)
        # Add to H stack
        self.siteAAtmAbsHLayout.addWidget(self.siteAAtmAbsLabel)
        self.siteAAtmAbsHLayout.addWidget(self.siteAAtmAbsTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteAAtmAbsHLayout)


    # Site A Relative Dispersion Factor
    def siteARelativeDispersionFactorUI(self):
        # Horizontal stack
        self.siteARelativeDispersionFactorHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A atmospheric absorption label
        self.siteARelativeDispersionFactorLabel = QLabel(self)
        self.siteARelativeDispersionFactorLabel.setText("Relative Dispersion Factor:")
        self.siteARelativeDispersionFactorLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteARelativeDispersionFactorLabel.setAlignment(Qt.AlignLeft)
        self.siteARelativeDispersionFactorLabel.setFixedWidth(230)
        self.siteARelativeDispersionFactorLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site A atmospheric absorption text input
        self.siteARelativeDispersionFactorTextBox = QDoubleSpinBox(self)
        self.siteARelativeDispersionFactorTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteARelativeDispersionFactorTextBox.setFixedWidth(170)
        self.siteARelativeDispersionFactorTextBox.setFixedHeight(30)
        self.siteARelativeDispersionFactorTextBox.setRange(0, 4000)
        # Add to H stack
        self.siteARelativeDispersionFactorHLayout.addWidget(self.siteARelativeDispersionFactorLabel)
        self.siteARelativeDispersionFactorHLayout.addWidget(self.siteARelativeDispersionFactorTextBox)
        # Add to V stack
        self.siteAVLayout.addLayout(self.siteARelativeDispersionFactorHLayout)



    def siteBUI(self, parent):

        ### Site B wrapper ###
        self.siteBContainer = QWidget(self)
        self.siteBContainer.setAutoFillBackground(True)
        self.siteBContainer.setStyleSheet("""
            QWidget {
                background-color: rgba(229, 229, 229, 1);
                border-radius: 5%;
            }"""
        )
        self.siteBContainer.setGeometry(710, 180, 450, 550)

        # Site B vertical stack
        self.siteBVLayout = QVBoxLayout(self)
        self.siteBVLayout.setSpacing(10)

        # Scroll area
        self.siteBScroll = QScrollArea(self)
        self.siteBScroll.setAutoFillBackground(True)
        self.siteBScroll.setStyleSheet("""
            QScrollArea {
                background-color: rgba(225, 225, 225, 0);
                border-radius: 5%;
            }"""
        )
        # add widgets to scroll view
        self.siteBScroll.setWidget(self.siteBContainer)
        self.siteBScroll.setWidgetResizable(True)
        self.siteBScroll.setGeometry(710, 180, 450, 550)
        # define each UI field and append them to the vertical stack view
        self.siteBLabelUI()                     # Site B Label
        self.siteBRoleOptionUI(parent)          # Site B dropdown menu
        self.siteBLatUI()                       # Site B Latitude
        self.siteBLngUI()                       # Site B Longitude
        self.siteBTowerHeightUI()               # Site B Tower Height
        self.siteBAntennaGainUI()               # Site B Antenna Gain
        self.siteBAntennaHeightUI()             # Site B Antenna Height
        self.siteBAntennaTypeUI()               # Site B Antenna Type
        self.siteBTransmitPowerUI()             # Site B Transmit Power
        self.siteBTXCouplingLossUI()            # Site B TX Coupling Loss
        self.siteBRXCouplingLossUI()            # Site B RX Coupling Loss
        self.siteBFieldMarginUI()               # Site B Field Margin
        self.siteBMiscLossesUI()                # Site B Misc Losses
        self.siteBRXThresholdUI()               # Site B RX Threshold
        self.siteBFrequencyUI()                 # Site B Frequency
        self.siteBPolarizationUI()      # Site B Polarization
        self.siteBRadioTypeUI()                 # Site B Radio type
        self.siteBModulationUI()                # Site B Modulation
        self.siteBBandwidthUI()                 # Site B Bandwidth
        self.siteBDataRateUI()                  # Site B Data Rate
        self.siteBAtmAbsUI()                    # Site B Atmospheric Absorption
        self.siteBRelativeDispersionFactorUI()  # Site B Relative Dispersion Factor
        # append the vertical stack view into a container view
        self.siteBContainer.setLayout(self.siteBVLayout)

    # Site B label
    def siteBLabelUI(self):
        self.siteBLabel = QLabel(self)
        self.siteBLabel.setText("Site B")
        self.siteBLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
                text-decoration: underline;
            }"""
        )
        self.siteBLabel.setGeometry(720, 140, 300, 30)
        self.siteBLabel.setAlignment(Qt.AlignLeft)

    # Site B Dropdown menu to choose transmitter or receiver
    def siteBRoleOptionUI(self, parent):
        # drop down
        self.siteBRoleOptionList = QComboBox(self)
        self.siteBRoleOptionList.addItems(["-- Select --", "Transmitter", "Receiver"])
        self.siteBRoleOptionList.activated.connect(lambda: self.dropDownBItemSelected(parent))
        self.siteBRoleOptionList.setGeometry(1010, 140, 150, 30)


    # Site B latitude
    def siteBLatUI(self):
        # Horizontal stack
        self.siteBLatHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B lat label
        self.siteBLatLabel = QLabel(self)
        self.siteBLatLabel.setText("Latitude:")
        self.siteBLatLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBLatLabel.setAlignment(Qt.AlignLeft)
        self.siteBLatLabel.setFixedWidth(230)
        self.siteBLatLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBLatTextBox = QDoubleSpinBox(self)
        self.siteBLatTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBLatTextBox.setFixedWidth(170)
        self.siteBLatTextBox.setFixedHeight(30)
        self.siteBLatTextBox.setRange(-90, 90)
        self.siteBLatTextBox.setDecimals(4)
        # Add to H stack
        self.siteBLatHLayout.addWidget(self.siteBLatLabel)
        self.siteBLatHLayout.addWidget(self.siteBLatTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBLatHLayout)

    # Site B longitude
    def siteBLngUI(self):
        # Horizontal stack
        self.siteBLngHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B lng label
        self.siteBLngLabel = QLabel(self)
        self.siteBLngLabel.setText("Longitude:")
        self.siteBLngLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBLngLabel.setAlignment(Qt.AlignLeft)
        self.siteBLngLabel.setFixedWidth(230)
        self.siteBLngLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBLngTextBox = QDoubleSpinBox(self)
        self.siteBLngTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBLngTextBox.setFixedWidth(170)
        self.siteBLngTextBox.setFixedHeight(30)
        self.siteBLngTextBox.setRange(-180, 180)
        self.siteBLngTextBox.setDecimals(4)
        # Add to H stack
        self.siteBLngHLayout.addWidget(self.siteBLngLabel)
        self.siteBLngHLayout.addWidget(self.siteBLngTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBLngHLayout)

    # Site B tower height above ground level
    def siteBTowerHeightUI(self):
        # Horizontal stack
        self.siteBTHHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B tower height label
        self.siteBTHLabel = QLabel(self)
        self.siteBTHLabel.setText("Tower Height AGL:")
        self.siteBTHLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBTHLabel.setAlignment(Qt.AlignLeft)
        self.siteBTHLabel.setFixedWidth(230)
        self.siteBTHLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBTHTextBox = QDoubleSpinBox(self)
        self.siteBTHTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBTHTextBox.setFixedWidth(170)
        self.siteBTHTextBox.setFixedHeight(30)
        self.siteBTHTextBox.setRange(0, 2000)
        # Add to H stack
        self.siteBTHHLayout.addWidget(self.siteBTHLabel)
        self.siteBTHHLayout.addWidget(self.siteBTHTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBTHHLayout)

    # Site B Antenna Height above ground level (AGL)
    def siteBAntennaHeightUI(self):
        # Horizontal stack
        self.siteBAntennaHeightHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B antenna height label
        self.siteBAntennaHeightLabel = QLabel(self)
        self.siteBAntennaHeightLabel.setText("Antenna Height AGL:")
        self.siteBAntennaHeightLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBAntennaHeightLabel.setAlignment(Qt.AlignLeft)
        self.siteBAntennaHeightLabel.setFixedWidth(230)
        self.siteBAntennaHeightLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBAntennaHeightTextBox = QDoubleSpinBox(self)
        self.siteBAntennaHeightTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBAntennaHeightTextBox.setFixedWidth(170)
        self.siteBAntennaHeightTextBox.setFixedHeight(30)
        self.siteBAntennaHeightTextBox.setRange(0, 2000)
        # Add to H stack
        self.siteBAntennaHeightHLayout.addWidget(self.siteBAntennaHeightLabel)
        self.siteBAntennaHeightHLayout.addWidget(self.siteBAntennaHeightTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBAntennaHeightHLayout)

    # Site B antenna gein
    def siteBAntennaGainUI(self):
        # Horizontal stack
        self.siteBAntennaGainHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B antenna gain label
        self.siteBAntennaGainLabel = QLabel(self)
        self.siteBAntennaGainLabel.setText("Antenna Gain (dbi):")
        self.siteBAntennaGainLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBAntennaGainLabel.setAlignment(Qt.AlignLeft)
        self.siteBAntennaGainLabel.setFixedWidth(230)
        self.siteBAntennaGainLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBAntennaGainTextBox = QDoubleSpinBox(self)
        self.siteBAntennaGainTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBAntennaGainTextBox.setFixedWidth(170)
        self.siteBAntennaGainTextBox.setFixedHeight(30)
        self.siteBAntennaGainTextBox.setRange(0, 100)
        # Add to H stack
        self.siteBAntennaGainHLayout.addWidget(self.siteBAntennaGainLabel)
        self.siteBAntennaGainHLayout.addWidget(self.siteBAntennaGainTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBAntennaGainHLayout)

    # Site B Antenna Type
    def siteBAntennaTypeUI(self):
        # Horizontal stack
        self.siteBAntennaTypeHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B antenna gain label
        self.siteBAntennaTypeLabel = QLabel(self)
        self.siteBAntennaTypeLabel.setText("Antenna Type:")
        self.siteBAntennaTypeLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBAntennaTypeLabel.setAlignment(Qt.AlignLeft)
        self.siteBAntennaTypeLabel.setFixedWidth(150)
        self.siteBAntennaTypeLabel.setContentsMargins(10, 15, 10, 10) # margin
        # drop down
        self.siteBAntennaTypeList = QComboBox(self)
        self.siteBAntennaTypeList.addItems(antennaData)
        self.siteBAntennaTypeList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBAntennaTypeList.setFixedWidth(250)
        # Add to H stack
        self.siteBAntennaTypeHLayout.addWidget(self.siteBAntennaTypeLabel)
        self.siteBAntennaTypeHLayout.addWidget(self.siteBAntennaTypeList)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBAntennaTypeHLayout)


    # Site B transmit power
    def siteBTransmitPowerUI(self):
        # Horizontal stack
        self.siteBTransmitPowerHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B transmit power label
        self.siteBTransmitPowerLabel = QLabel(self)
        self.siteBTransmitPowerLabel.setText("Transmit Power (dbm):")
        self.siteBTransmitPowerLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBTransmitPowerLabel.setAlignment(Qt.AlignLeft)
        self.siteBTransmitPowerLabel.setFixedWidth(230)
        self.siteBTransmitPowerLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBTransmitPowerTextBox = QDoubleSpinBox(self)
        self.siteBTransmitPowerTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBTransmitPowerTextBox.setFixedWidth(170)
        self.siteBTransmitPowerTextBox.setFixedHeight(30)
        self.siteBTransmitPowerTextBox.setRange(0, 100)
        # Add to H stack
        self.siteBTransmitPowerHLayout.addWidget(self.siteBTransmitPowerLabel)
        self.siteBTransmitPowerHLayout.addWidget(self.siteBTransmitPowerTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBTransmitPowerHLayout)


    # Site B TX Coupling Loss
    def siteBTXCouplingLossUI(self):
        # Horizontal stac
        self.siteBTXCouplingLossHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B TX coupling loss label
        self.siteBTXCouplingLossLabel = QLabel(self)
        self.siteBTXCouplingLossLabel.setText("TX Coupling Loss (dB):")
        self.siteBTXCouplingLossLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBTXCouplingLossLabel.setAlignment(Qt.AlignLeft)
        self.siteBTXCouplingLossLabel.setFixedWidth(230)
        self.siteBTXCouplingLossLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBTXCouplingLossTextBox = QDoubleSpinBox(self)
        self.siteBTXCouplingLossTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBTXCouplingLossTextBox.setFixedWidth(170)
        self.siteBTXCouplingLossTextBox.setFixedHeight(30)
        self.siteBTXCouplingLossTextBox.setRange(0, 100)
        # Add to H stack
        self.siteBTXCouplingLossHLayout.addWidget(self.siteBTXCouplingLossLabel)
        self.siteBTXCouplingLossHLayout.addWidget(self.siteBTXCouplingLossTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBTXCouplingLossHLayout)

    # Site B RX Coupling Loss
    def siteBRXCouplingLossUI(self):
        # Horizontal stac
        self.siteBRXCouplingLossHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B RX coupling loss label
        self.siteBRXCouplingLossLabel = QLabel(self)
        self.siteBRXCouplingLossLabel.setText("RX Coupling Loss (dB):")
        self.siteBRXCouplingLossLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBRXCouplingLossLabel.setAlignment(Qt.AlignLeft)
        self.siteBRXCouplingLossLabel.setFixedWidth(230)
        self.siteBRXCouplingLossLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBRXCouplingLossTextBox = QDoubleSpinBox(self)
        self.siteBRXCouplingLossTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBRXCouplingLossTextBox.setFixedWidth(170)
        self.siteBRXCouplingLossTextBox.setFixedHeight(30)
        self.siteBRXCouplingLossTextBox.setRange(0, 100)
        # Add to H stack
        self.siteBRXCouplingLossHLayout.addWidget(self.siteBRXCouplingLossLabel)
        self.siteBRXCouplingLossHLayout.addWidget(self.siteBRXCouplingLossTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBRXCouplingLossHLayout)

    # Site B Field Margin
    def siteBFieldMarginUI(self):
        # Horizontal stac
        self.siteBFieldMarginHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B field margin label
        self.siteBFieldMarginLabel = QLabel(self)
        self.siteBFieldMarginLabel.setText("Field Margin:")
        self.siteBFieldMarginLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBFieldMarginLabel.setAlignment(Qt.AlignLeft)
        self.siteBFieldMarginLabel.setFixedWidth(230)
        self.siteBFieldMarginLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBFieldMarginTextBox = QDoubleSpinBox(self)
        self.siteBFieldMarginTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBFieldMarginTextBox.setFixedWidth(170)
        self.siteBFieldMarginTextBox.setFixedHeight(30)
        self.siteBFieldMarginTextBox.setRange(0, 100)
        # Add to H stack
        self.siteBFieldMarginHLayout.addWidget(self.siteBFieldMarginLabel)
        self.siteBFieldMarginHLayout.addWidget(self.siteBFieldMarginTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBFieldMarginHLayout)


    # Site B Misc Losses
    def siteBMiscLossesUI(self):
        # Horizontal stac
        self.siteBMiscLossesHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B Misc losses label
        self.siteBMiscLossesLabel = QLabel(self)
        self.siteBMiscLossesLabel.setText("Misc Losses:")
        self.siteBMiscLossesLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBMiscLossesLabel.setAlignment(Qt.AlignLeft)
        self.siteBMiscLossesLabel.setFixedWidth(230)
        self.siteBMiscLossesLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBMiscLossesTextBox = QDoubleSpinBox(self)
        self.siteBMiscLossesTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBMiscLossesTextBox.setFixedWidth(170)
        self.siteBMiscLossesTextBox.setFixedHeight(30)
        self.siteBMiscLossesTextBox.setRange(0, 100)
        # Add to H stack
        self.siteBMiscLossesHLayout.addWidget(self.siteBMiscLossesLabel)
        self.siteBMiscLossesHLayout.addWidget(self.siteBMiscLossesTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBMiscLossesHLayout)


    # Site B Receive Threshold
    def siteBRXThresholdUI(self):
        # Horizontal stack
        self.siteBRXThresholdHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B Receive Threshold label
        self.siteBRXThresholdLabel = QLabel(self)
        self.siteBRXThresholdLabel.setText("RX Threshold (dbm):")
        self.siteBRXThresholdLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBRXThresholdLabel.setAlignment(Qt.AlignLeft)
        self.siteBRXThresholdLabel.setFixedWidth(230)
        self.siteBRXThresholdLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBRXThresholdTextBox = QDoubleSpinBox(self)
        self.siteBRXThresholdTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBRXThresholdTextBox.setFixedWidth(170)
        self.siteBRXThresholdTextBox.setFixedHeight(30)
        self.siteBRXThresholdTextBox.setRange(-100, 0)
        # Add to H stack
        self.siteBRXThresholdHLayout.addWidget(self.siteBRXThresholdLabel)
        self.siteBRXThresholdHLayout.addWidget(self.siteBRXThresholdTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBRXThresholdHLayout)


    # Site B Transmit Frequency (MHz)
    def siteBFrequencyUI(self):
        # Horizontal stack
        self.siteBFrequencyHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B transmit frequency label
        self.siteBFrequencyLabel = QLabel(self)
        self.siteBFrequencyLabel.setText("Frequency (MHz):")
        self.siteBFrequencyLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBFrequencyLabel.setAlignment(Qt.AlignLeft)
        self.siteBFrequencyLabel.setFixedWidth(230)
        self.siteBFrequencyLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBFrequencyTextBox = QDoubleSpinBox(self)
        self.siteBFrequencyTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBFrequencyTextBox.setFixedWidth(170)
        self.siteBFrequencyTextBox.setFixedHeight(30)
        self.siteBFrequencyTextBox.setRange(100, 30000)
        # Add to H stack
        self.siteBFrequencyHLayout.addWidget(self.siteBFrequencyLabel)
        self.siteBFrequencyHLayout.addWidget(self.siteBFrequencyTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBFrequencyHLayout)

    # Site B Polarization
    def siteBPolarizationUI(self):
        # Horizontal stack
        self.siteBPolarizationHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B vertical polarization label
        self.siteBPolarizationLabel = QLabel(self)
        self.siteBPolarizationLabel.setText("Polarization:")
        self.siteBPolarizationLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBPolarizationLabel.setAlignment(Qt.AlignLeft)
        self.siteBPolarizationLabel.setFixedWidth(230)
        self.siteBPolarizationLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBPolarizationTextBox = QComboBox(self)
        self.siteBPolarizationTextBox.addItems(["Vertical", "Horizontal"])
        self.siteBPolarizationTextBox.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBPolarizationTextBox.setFixedWidth(170)
        # Add to H stack
        self.siteBPolarizationHLayout.addWidget(self.siteBPolarizationLabel)
        self.siteBPolarizationHLayout.addWidget(self.siteBPolarizationTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBPolarizationHLayout)


    # Site B Radio Type
    def siteBRadioTypeUI(self):
        # Horizontal stack
        self.siteBRadioTypeHLayout = QHBoxLayout() # remove 'self' due to err msg
        # site B antenna gain label
        self.siteBRadioTypeLabel = QLabel(self)
        self.siteBRadioTypeLabel.setText("Radio:")
        self.siteBRadioTypeLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBRadioTypeLabel.setAlignment(Qt.AlignLeft)
        self.siteBRadioTypeLabel.setFixedWidth(80)
        self.siteBRadioTypeLabel.setContentsMargins(10, 15, 10, 10) # margin
        # drop down
        self.siteBRadioTypeList = QComboBox(self)
        self.siteBRadioTypeList.addItems(radioData)
        self.siteBRadioTypeList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBRadioTypeList.setFixedWidth(320)
        # Add to H stack
        self.siteBRadioTypeHLayout.addWidget(self.siteBRadioTypeLabel)
        self.siteBRadioTypeHLayout.addWidget(self.siteBRadioTypeList)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBRadioTypeHLayout)


    # Site B Modulation
    def siteBModulationUI(self):
        # Horizontal stack
        self.siteBModulationHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B modulation label
        self.siteBModulationLabel = QLabel(self)
        self.siteBModulationLabel.setText("Modulation (QAM):")
        self.siteBModulationLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBModulationLabel.setAlignment(Qt.AlignLeft)
        self.siteBModulationLabel.setFixedWidth(230)
        self.siteBModulationLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBModulationTextBox = QDoubleSpinBox(self)
        self.siteBModulationTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBModulationTextBox.setFixedWidth(170)
        self.siteBModulationTextBox.setFixedHeight(30)
        self.siteBModulationTextBox.setRange(2, 4096)
        # Add to H stack
        self.siteBModulationHLayout.addWidget(self.siteBModulationLabel)
        self.siteBModulationHLayout.addWidget(self.siteBModulationTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBModulationHLayout)


    # Site B Bandwidth
    def siteBBandwidthUI(self):
        # Horizontal stack
        self.siteBBandwidthHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B bandwidth label
        self.siteBBandwidthLabel = QLabel(self)
        self.siteBBandwidthLabel.setText("Bandwidth (MHz):")
        self.siteBBandwidthLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBBandwidthLabel.setAlignment(Qt.AlignLeft)
        self.siteBBandwidthLabel.setFixedWidth(230)
        self.siteBBandwidthLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBBandwidthTextBox = QDoubleSpinBox(self)
        self.siteBBandwidthTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBBandwidthTextBox.setFixedWidth(170)
        self.siteBBandwidthTextBox.setFixedHeight(30)
        self.siteBBandwidthTextBox.setRange(1, 100)
        # Add to H stack
        self.siteBBandwidthHLayout.addWidget(self.siteBBandwidthLabel)
        self.siteBBandwidthHLayout.addWidget(self.siteBBandwidthTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBBandwidthHLayout)


    # Site B Data Rate
    def siteBDataRateUI(self):
        # Horizontal stack
        self.siteBDataRateHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B data rate label
        self.siteBDataRateLabel = QLabel(self)
        self.siteBDataRateLabel.setText("Data Rate (Mb/s):")
        self.siteBDataRateLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBDataRateLabel.setAlignment(Qt.AlignLeft)
        self.siteBDataRateLabel.setFixedWidth(230)
        self.siteBDataRateLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBDataRateTextBox = QDoubleSpinBox(self)
        self.siteBDataRateTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBDataRateTextBox.setFixedWidth(170)
        self.siteBDataRateTextBox.setFixedHeight(30)
        self.siteBDataRateTextBox.setRange(1, 4000)
        # Add to H stack
        self.siteBDataRateHLayout.addWidget(self.siteBDataRateLabel)
        self.siteBDataRateHLayout.addWidget(self.siteBDataRateTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBDataRateHLayout)


    # Site B Atmospheric Absorption
    def siteBAtmAbsUI(self):
        # Horizontal stack
        self.siteBAtmAbsHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B atmospheric absorption label
        self.siteBAtmAbsLabel = QLabel(self)
        self.siteBAtmAbsLabel.setText("Atmospheric Absorption:")
        self.siteBAtmAbsLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBAtmAbsLabel.setAlignment(Qt.AlignLeft)
        self.siteBAtmAbsLabel.setFixedWidth(230)
        self.siteBAtmAbsLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBAtmAbsTextBox = QDoubleSpinBox(self)
        self.siteBAtmAbsTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBAtmAbsTextBox.setFixedWidth(170)
        self.siteBAtmAbsTextBox.setFixedHeight(30)
        self.siteBAtmAbsTextBox.setRange(0, 4000)
        # Add to H stack
        self.siteBAtmAbsHLayout.addWidget(self.siteBAtmAbsLabel)
        self.siteBAtmAbsHLayout.addWidget(self.siteBAtmAbsTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBAtmAbsHLayout)


    # Site B Atmospheric Absorption
    def siteBRelativeDispersionFactorUI(self):
        # Horizontal stack
        self.siteBRelativeDispersionFactorHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site B atmospheric absorption label
        self.siteBRelativeDispersionFactorLabel = QLabel(self)
        self.siteBRelativeDispersionFactorLabel.setText("Relative Dispersion Factor:")
        self.siteBRelativeDispersionFactorLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.siteBRelativeDispersionFactorLabel.setAlignment(Qt.AlignLeft)
        self.siteBRelativeDispersionFactorLabel.setFixedWidth(230)
        self.siteBRelativeDispersionFactorLabel.setContentsMargins(10, 15, 10, 10) # margin
        self.siteBRelativeDispersionFactorTextBox = QDoubleSpinBox(self)
        self.siteBRelativeDispersionFactorTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.siteBRelativeDispersionFactorTextBox.setFixedWidth(170)
        self.siteBRelativeDispersionFactorTextBox.setFixedHeight(30)
        self.siteBRelativeDispersionFactorTextBox.setRange(0, 4000)
        # Add to H stack
        self.siteBRelativeDispersionFactorHLayout.addWidget(self.siteBRelativeDispersionFactorLabel)
        self.siteBRelativeDispersionFactorHLayout.addWidget(self.siteBRelativeDispersionFactorTextBox)
        # Add to V stack
        self.siteBVLayout.addLayout(self.siteBRelativeDispersionFactorHLayout)



    def button01Clicked(self, parent):
        print("btn 01 clicked..")

    # Open sub menu
    def button03Clicked(self, parent):
        print("Next button Clicked!")

    # Select Transmitter or Receiver (Site A)
    def dropDownAItemSelected(self, parent):
        item = self.siteARoleOptionList.currentText()
        str(item)
        print("Item selected!", item)
        if (item == "Transmitter"):
            # Hide RX Coupling Loss
            self.siteARXCouplingLossLabel.hide()
            self.siteARXCouplingLossTextBox.hide()
            # Hide RX Threshold
            self.siteARXThresholdLabel.hide()
            self.siteARXThresholdTextBox.hide()
            # Show transmit power
            self.siteATransmitPowerLabel.show()
            self.siteATransmitPowerTextBox.show()
            # Show TX coupling
            self.siteATXCouplingLossLabel.show()
            self.siteATXCouplingLossTextBox.show()
            # Show field margin
            self.siteAFieldMarginLabel.show()
            self.siteAFieldMarginTextBox.show()
            # Show Misc loss
            self.siteAMiscLossesLabel.show()
            self.siteAMiscLossesTextBox.show()
            # Show Frequency
            self.siteAFrequencyLabel.show()
            self.siteAFrequencyTextBox.show()
            # Show Polarization
            self.siteAPolarizationLabel.show()
            self.siteAPolarizationTextBox.show()
            # Show radio
            self.siteARadioTypeLabel.show()
            self.siteARadioTypeList.show()
            # Show modulation
            self.siteAModulationLabel.show()
            self.siteAModulationTextBox.show()
            # Show bandwidth
            self.siteABandwidthLabel.show()
            self.siteABandwidthTextBox.show()
            # Show data rate
            self.siteADataRateLabel.show()
            self.siteADataRateTextBox.show()
            # Show atm absorb
            self.siteAAtmAbsLabel.show()
            self.siteAAtmAbsTextBox.show()
        else:
            # Show RX Coupling Loss
            self.siteARXCouplingLossLabel.show()
            self.siteARXCouplingLossTextBox.show()
            # Show RX Threshold
            self.siteARXThresholdLabel.show()
            self.siteARXThresholdTextBox.show()
            # Hide transmit power
            self.siteATransmitPowerLabel.hide()
            self.siteATransmitPowerTextBox.hide()
            # Hide TX coupling
            self.siteATXCouplingLossLabel.hide()
            self.siteATXCouplingLossTextBox.hide()
            # Hide field margin
            self.siteAFieldMarginLabel.hide()
            self.siteAFieldMarginTextBox.hide()
            # Hide Misc loss
            self.siteAMiscLossesLabel.hide()
            self.siteAMiscLossesTextBox.hide()
            # Hide Frequency
            self.siteAFrequencyLabel.hide()
            self.siteAFrequencyTextBox.hide()
            # Hide Polarization
            self.siteAPolarizationLabel.hide()
            self.siteAPolarizationTextBox.hide()
            # Hide radio
            self.siteARadioTypeLabel.hide()
            self.siteARadioTypeList.hide()
            # Hide modulation
            self.siteAModulationLabel.hide()
            self.siteAModulationTextBox.hide()
            # Hide bandwidth
            self.siteABandwidthLabel.hide()
            self.siteABandwidthTextBox.hide()
            # Hide data rate
            self.siteADataRateLabel.hide()
            self.siteADataRateTextBox.hide()
            # Hide atm absorb
            self.siteAAtmAbsLabel.hide()
            self.siteAAtmAbsTextBox.hide()


    # Select Transmitter or Receiver (Site B)
    def dropDownBItemSelected(self, parent):
        item = self.siteBRoleOptionList.currentText()
        str(item)
        print("Item selected!", item)
        if (item == "Transmitter"):
            # Hide Site B RX Coupling Loss
            self.siteBRXCouplingLossLabel.hide()
            self.siteBRXCouplingLossTextBox.hide()
            # Hide Site B RX Threshold
            self.siteBRXThresholdLabel.hide()
            self.siteBRXThresholdTextBox.hide()
            # Show transmit power
            self.siteBTransmitPowerLabel.show()
            self.siteBTransmitPowerTextBox.show()
            # Show TX coupling
            self.siteBTXCouplingLossLabel.show()
            self.siteBTXCouplingLossTextBox.show()
            # Show field margin
            self.siteBFieldMarginLabel.show()
            self.siteBFieldMarginTextBox.show()
            # Show Misc loss
            self.siteBMiscLossesLabel.show()
            self.siteBMiscLossesTextBox.show()
            # Show Frequency
            self.siteBFrequencyLabel.show()
            self.siteBFrequencyTextBox.show()
            # Show Polarization
            self.siteBPolarizationLabel.show()
            self.siteBPolarizationTextBox.show()
            # Show radio
            self.siteBRadioTypeLabel.show()
            self.siteBRadioTypeList.show()
            # Show modulation
            self.siteBModulationLabel.show()
            self.siteBModulationTextBox.show()
            # Show bandwidth
            self.siteBBandwidthLabel.show()
            self.siteBBandwidthTextBox.show()
            # Show data rate
            self.siteBDataRateLabel.show()
            self.siteBDataRateTextBox.show()
            # Show atm absorb
            self.siteBAtmAbsLabel.show()
            self.siteBAtmAbsTextBox.show()
        else:
            # Show RX Coupling Loss
            self.siteBRXCouplingLossLabel.show()
            self.siteBRXCouplingLossTextBox.show()
            # Show RX Threshold
            self.siteBRXThresholdLabel.show()
            self.siteBRXThresholdTextBox.show()
            # Hide transmit power
            self.siteBTransmitPowerLabel.hide()
            self.siteBTransmitPowerTextBox.hide()
            # Hide TX coupling
            self.siteBTXCouplingLossLabel.hide()
            self.siteBTXCouplingLossTextBox.hide()
            # Hide field margin
            self.siteBFieldMarginLabel.hide()
            self.siteBFieldMarginTextBox.hide()
            # Hide Misc loss
            self.siteBMiscLossesLabel.hide()
            self.siteBMiscLossesTextBox.hide()
            # Hide Frequency
            self.siteBFrequencyLabel.hide()
            self.siteBFrequencyTextBox.hide()
            # Hide Polarization
            self.siteBPolarizationLabel.hide()
            self.siteBPolarizationTextBox.hide()
            # Hide radio
            self.siteBRadioTypeLabel.hide()
            self.siteBRadioTypeList.hide()
            # Hide modulation
            self.siteBModulationLabel.hide()
            self.siteBModulationTextBox.hide()
            # Hide bandwidth
            self.siteBBandwidthLabel.hide()
            self.siteBBandwidthTextBox.hide()
            # Hide data rate
            self.siteBDataRateLabel.hide()
            self.siteBDataRateTextBox.hide()
            # Hide atm absorb
            self.siteBAtmAbsLabel.hide()
            self.siteBAtmAbsTextBox.hide()
            # Hide Site B Relative Dispersive Factor
            self.siteBRelativeDispersionFactorLabel.hide()
            self.siteBRelativeDispersionFactorTextBox.hide()



    def moveToHomePage(self, parent):
        parent.central_widget.setCurrentIndex(2)

    def moveToPathDesignPage0(self, parent):
        parent.central_widget.setCurrentIndex(3)

    def moveToPathDesignPage1(self, parent):
        parent.central_widget.setCurrentIndex(4)

    def moveToPathDesignPage3(self, parent):
        parent.central_widget.setCurrentIndex(6)

    def showdialog(self):
        self.dialogWgt = QDialog()
        self.dialogWgt.setGeometry(600, 400, 400, 300)
        # site B path distance label
        self.errorMsgLabel = QLabel(self.dialogWgt)
        self.errorMsgLabel.setText("Invalid input. Check the entered values again.")
        self.errorMsgLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.errorMsgLabel.setAlignment(Qt.AlignCenter)
        self.errorMsgLabel.setGeometry(0, 100, 400, 30)
        # Close button
        self.closeBtn = QPushButton("ok",self.dialogWgt)
        self.closeBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color:blue;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        self.closeBtn.setGeometry(150, 250, 100, 40)
        self.closeBtn.clicked.connect(lambda: self.dialogWgt.close())
        self.dialogWgt.setWindowTitle("Invalid input")
        self.dialogWgt.setWindowModality(Qt.ApplicationModal)
        self.dialogWgt.exec_()


    # Trigger when "Next" button gets clicked
    def nextBtnClicked(self, parent):
        self.checkSelection(parent)

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    def checkSelection(self, parent):
        self.siteAOption = self.siteARoleOptionList.currentText()
        self.siteBOption = self.siteBRoleOptionList.currentText()
        if((self.siteAOption == "Transmitter") and (self.siteBOption == "Receiver")):
            print("Site A as `Transmitter` & Site B as `Receiver`")
            self.pathCalculationCase1(parent)
        elif((self.siteAOption == "Receiver") and (self.siteBOption == "Transmitter")):
            print("Site A as `Receiver` & Site B as `Transmitter`")
            self.pathCalculationCase2(parent)
        else:
            print("Please sleect option!!")
            self.showdialog()


    def pathCalculationCase1(self, parent):
        parent.pathCalc = PathProfileModules()
        # Get the user inputs
        # Site A
        self.siteALat = float(self.siteALatTextBox.text())
        self.siteALng = float(self.siteALngTextBox.text())
        self.antennaGain = float(self.siteAAntennaGainTextBox.text())
        self.transmitPower = float(self.siteATransmitPowerTextBox.text())
        self.TXCouplingLoss = float(self.siteATXCouplingLossTextBox.text())
        self.MiscLoss = float(self.siteAMiscLossesTextBox.text())
        self.freq = float(self.siteAFrequencyTextBox.text())
        self.txAntennaGain = float(self.siteAAntennaGainTextBox.text())
        self.siteATowerHeight = float(self.siteATHTextBox.text())
        self.siteAAntennaHeight = float(self.siteAAntennaHeightTextBox.text())
        self.freq = float(self.siteAFrequencyTextBox.text())
        # Site B
        self.siteBLat = float(self.siteBLatTextBox.text())
        self.siteBLng = float(self.siteBLngTextBox.text())
        self.rxAntennaGain = float(self.siteBAntennaGainTextBox.text())
        self.rxCouplingLoss = float(self.siteBRXCouplingLossTextBox.text())
        self.rxThresholdValue = float(self.siteBRXThresholdTextBox.text())
        self.siteBTowerHeight = float(self.siteBTHTextBox.text())
        self.siteBAntennaHeight = float(self.siteBAntennaHeightTextBox.text())

        # (1) EIRP
        self.EIRPResult = float(parent.pathCalc.EIRP(self.antennaGain, self.transmitPower, self.TXCouplingLoss, self.MiscLoss))
        parent.pathDesignWidget3.EIRPTextBox.setText(str(self.EIRPResult))
        # (2 - a) Path Distance km
        self.pathDistResultKm = float(parent.pathCalc.pathDistanceKm(self.siteALat, self.siteALng, self.siteBLat, self.siteBLng))
        # (2 - b) path distance miles
        self.pathDistResultMiles = float(parent.pathCalc.pathDistanceMiles(self.siteALat, self.siteALng, self.siteBLat, self.siteBLng))
        parent.pathDesignWidget3.pathDistanceTextBox.setText( str(round(self.pathDistResultMiles, 2)) )
        if(self.pathDistResultKm != 0):
            # Azimuth
            self.azimuth = float(parent.pathCalc.azimuth(self.siteALat, self.siteALng, self.siteBLat, self.siteBLng))
            parent.pathDesignWidget3.azimuthTextBox.setText( str( round(self.azimuth, 2) ) )
            # (3) Free Space Loss
            self.freeSpaceLossResult = float(parent.pathCalc.freeSpaceLoss(self.pathDistResultMiles, self.freq, self.txAntennaGain, self.rxAntennaGain))
            parent.pathDesignWidget3.freeSpaceLossTextBox.setText( str( round(self.freeSpaceLossResult, 2) ) )
            # (4) Received Signal Level
            self.receivedSignalLevelResult = float(parent.pathCalc.receivedSignalLevel(self.EIRPResult, self.rxAntennaGain, self.freeSpaceLossResult, self.rxCouplingLoss))
            parent.pathDesignWidget3.receivedSignalLevelTextBox.setText( str( round(self.receivedSignalLevelResult, 2) ))
            # (5) Flat Fade Margin
            self.flatFadeMarginResult = float(parent.pathCalc.flatFadeMargin(self.receivedSignalLevelResult, self.rxThresholdValue))
            parent.pathDesignWidget3.flatFadeMarginTextBox.setText( str( round(self.flatFadeMarginResult, 2) ))
            # (6) Cloud RF API
            if (self.siteAAntennaHeight != 0) and (self.siteBAntennaHeight != 0):
                parent.pathCalc.pathProfileAPI(parent, self.siteALat, self.siteALng, self.siteAAntennaHeight, 2.14, self.freq, self.siteBLat, self.siteBLng, self.siteBAntennaHeight, self.rxAntennaGain, 0, "v")
                # Move to next page
                parent.central_widget.setCurrentIndex(6)
            else:
                self.showdialog()
        else:
            self.showdialog()


    def pathCalculationCase2(self, parent):
        parent.pathCalc = PathProfileModules()
        # Get user inputs
        self.antennaGain = float(self.siteBAntennaGainTextBox.text())
        self.transmitPower = float(self.siteBTransmitPowerTextBox.text())
        self.TXCouplingLoss = float(self.siteBTXCouplingLossTextBox.text())
        self.MiscLoss = float(self.siteBMiscLossesTextBox.text())
        self.siteBLat = float(self.siteBLatTextBox.text())
        self.siteBLng = float(self.siteBLngTextBox.text())
        self.siteALat = float(self.siteALatTextBox.text())
        self.siteALng = float(self.siteALngTextBox.text())
        self.freq = float(self.siteBFrequencyTextBox.text())
        self.txAntennaGain = float(self.siteBAntennaGainTextBox.text())
        self.rxAntennaGain = float(self.siteAAntennaGainTextBox.text())
        self.rxCouplingLoss = float(self.siteARXCouplingLossTextBox.text())
        self.rxThresholdValue = float(self.siteARXThresholdTextBox.text())
        self.siteATowerHeight = float(self.siteATHTextBox.text())
        self.siteAAntennaHeight = float(self.siteAAntennaHeightTextBox.text())
        self.freq = float(self.siteBFrequencyTextBox.text())
        self.siteBTowerHeight = float(self.siteBTHTextBox.text())
        self.siteBAntennaHeight = float(self.siteBAntennaHeightTextBox.text())

        # (1) EIRP
        self.Eparentesult = float(parent.pathCalc.EIRP(self.antennaGain, self.transmitPower, self.TXCouplingLoss, self.MiscLoss))
        parent.pathDesignWidget3.EIRPTextBox.setText(str(self.EIRPResult))
        # (2 - a) Path Distance miles
        self.pathDistResultMiles = float(parent.pathCalc.pathDistanceMiles(self.siteALat, self.siteALng, self.siteBLat, self.siteBLng))
        # (2 - b) Path Distance km
        self.pathDistanceResultKm = float(parent.pathCalc.pathDistanceKm(self.siteBLat, self.siteBLng, self.siteALat, self.siteALng))
        parent.pathDesignWidget3.pathDistanceTextBox.setText(str(self.pathDistResultMiles))
        # Check if path distance is not zero. zero divide will return math error.
        if (self.pathDistResultKm != 0):
            # Azimuth
            self.azimuth = float(parent.pathCalc.azimuth(self.siteALat, self.siteALng, self.siteBLat, self.siteBLng))
            parent.pathDesignWidget3.azimuthTextBox.setText( str( round(self.azimuth, 2) ) )
            # Free Space Loss
            self.freeSpaceLossResult = float(parent.pathCalc.freeSpaceLoss(self.pathDistResultMiles, self.freq, self.txAntennaGain, self.rxAntennaGain))
            # Received Signal Level
            self.receivedSignalLevelResult = float(parent.pathCalc.receivedSignalLevel(self.EIRPResult, self.rxAntennaGain, self.freeSpaceLossResult, self.rxCouplingLoss))
            # Flat Fade Margin
            self.flatFadeMarginResult = float(parent.pathCalc.flatFadeMargin(self.receivedSignalLevelResult, self.rxThresholdValue))
            # Cloud RF API
            # (6) Cloud RF API
            if (self.siteAAntennaHeight != 0) and (self.siteBAntennaHeight != 0):
                parent.pathCalc.pathProfileAPI(parent, self.siteBLat, self.siteBLng, self.siteBAntennaHeight, 2.14, self.freq, self.siteALat, self.siteALng, self.siteAAntennaHeight, self.rxAntennaGain, 0, "v")
                # Move to next page
                parent.central_widget.setCurrentIndex(6)
            else:
                self.showdialog()
        else:
            self.showdialog()
