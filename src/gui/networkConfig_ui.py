#
# pathDesign_ui0.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import json
import io
import os
import csv
# import sip
# import folium
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
# from modules.KML3DA import

# "Network Config Page"
class NetworkConfigWidget(QWidget):

    def __init__(self, parent=None):
        super(NetworkConfigWidget, self).__init__(parent)
        self.initUI(parent)

    def initUI(self, parent):
        self.sideMenuUI(parent)
        self.accountUI()
        self.rightMsgUI(parent)
        self.subMenuUI(parent)

    # Sub menu UI when "Network Config" is clicked
    def subMenuUI(self, parent):
        # side menu wrapper
        self.subMenuContainer = QWidget(self)
        self.subMenuContainer.setAutoFillBackground(True)
        self.subMenuContainer.setStyleSheet("""
            background-color: white;
        """)
        self.subMenuContainer.setGeometry(200, 400, 200, 250)
        self.subMenuContainer.setVisible(False)

        # Path desgin link
        self.pathDesignLink = QPushButton(self)
        self.pathDesignLink.setText("Path design")
        self.pathDesignLink.setStyleSheet("""
            QPushButton {
                color: rgba(8, 44, 108, 1);
                font-size: 15px;
                background-color: white;
                border: 0px solid white;
                text-decoration: underline;
            }"""
        )
        self.pathDesignLink.setGeometry(200, 410, 200, 50)
        self.pathDesignLink.setVisible(False)
        self.pathDesignLink.clicked.connect(lambda: parent.screenTransitionModules.moveToPathDesignPage1(parent))

        # Network design link
        self.nwkDesignLink = QPushButton(self)
        self.nwkDesignLink.setText("Network design")
        self.nwkDesignLink.setStyleSheet("""
            QPushButton {
                color: rgba(8, 44, 108, 1);
                font-size: 15px;
                background-color: white;
                border: 0px solid white;
                text-decoration: underline;
            }"""
        )
        self.nwkDesignLink.setGeometry(200, 470, 200, 50)
        self.nwkDesignLink.setVisible(False)
        self.nwkDesignLink.clicked.connect(lambda: parent.popUp.upCommingFunctionality())

        # Coverage map link
        self.coverageMapLink = QPushButton(self)
        self.coverageMapLink.setText("Converage map")
        self.coverageMapLink.setStyleSheet("""
            QPushButton {
                color: rgba(8, 44, 108, 1);
                font-size: 15px;
                background-color: white;
                border: 0px solid white;
                text-decoration: underline;
            }"""
        )
        self.coverageMapLink.setGeometry(200, 530, 200, 50)
        self.coverageMapLink.setVisible(False)
        self.coverageMapLink.clicked.connect(lambda: parent.popUp.upCommingFunctionality())
        # History

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
        self.nwcfBtn.clicked.connect(lambda: self.openSubMenuUI(parent))

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


    def rightMsgUI(self, parent):
        # show option cards
        self.pathDesignBtn(parent)
        self.networkDesignBtn(parent)
        self.kmlGeneratorBtn(parent)


    # Path desgin button
    def pathDesignBtn(self, parent):
        # wrapper
        self.pathDesignBtnWrapper = QWidget(self)
        self.pathDesignBtnWrapper.setStyleSheet("""
            QWidget {
                color: blue;
                font-size: 30px;
                border: 3px solid white;
                border-radius: 5%;
                background-color: white;
            }"""
        )
        self.pathDesignBtnWrapper.setGeometry(250, 50, 400, 250)
        # Button label
        self.pathDesignBtnLabel = QLabel(self)
        self.pathDesignBtnLabel.setText('Path Desgin')
        self.pathDesignBtnLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 30px;
            }"""
        )
        self.pathDesignBtnLabel.setGeometry(250, 70, 400, 60)
        self.pathDesignBtnLabel.setAlignment(Qt.AlignCenter)
        # discription
        self.pathDesignBtnDescriptionLabel = QLabel(self)
        self.pathDesignBtnDescriptionLabel.setText('Generate a point to point path profile. Visualize & analyze by importing your own site data.')
        self.pathDesignBtnDescriptionLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 15px;
            }"""
        )
        self.pathDesignBtnDescriptionLabel.setGeometry(260, 120, 380, 60)
        self.pathDesignBtnDescriptionLabel.setWordWrap(True)
        self.pathDesignBtnDescriptionLabel.setAlignment(Qt.AlignCenter)
        # "Try" button
        self.pathDesignTryBtn = QPushButton(self)
        self.pathDesignTryBtn.setText("Open")
        self.pathDesignTryBtn.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 20px;
                background-color: orange;
                border: 0px solid orange;
                border-radius: 5%;
            }"""
        )
        self.pathDesignTryBtn.setGeometry(400, 220, 100, 40)
        self.pathDesignTryBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToPathDesignPage1(parent))


    # Network desgin button
    def networkDesignBtn(self, parent):
        # wrapper
        self.networkDesignBtnWrapper = QWidget(self)
        self.networkDesignBtnWrapper.setStyleSheet("""
            QWidget {
                color: blue;
                font-size: 30px;
                border: 3px solid white;
                border-radius: 5%;
                background-color: white;
            }"""
        )
        self.networkDesignBtnWrapper.setGeometry(700, 50, 400, 250)
        # Button label
        self.networkDesignBtnLabel = QLabel(self)
        self.networkDesignBtnLabel.setText('Network Desgin')
        self.networkDesignBtnLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 30px;
            }"""
        )
        self.networkDesignBtnLabel.setGeometry(700, 70, 400, 60)
        self.networkDesignBtnLabel.setAlignment(Qt.AlignCenter)
        # discription
        self.networkDesignBtnDescriptionLabel = QLabel(self)
        self.networkDesignBtnDescriptionLabel.setText('Design your own network. Visualize & analyze by selecting specific sites.')
        self.networkDesignBtnDescriptionLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 15px;
            }"""
        )
        self.networkDesignBtnDescriptionLabel.setGeometry(710, 120, 380, 60)
        self.networkDesignBtnDescriptionLabel.setWordWrap(True)
        self.networkDesignBtnDescriptionLabel.setAlignment(Qt.AlignCenter)
        # "Try" button
        self.networkDesignTryBtn = QPushButton(self)
        self.networkDesignTryBtn.setText("Open")
        self.networkDesignTryBtn.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 20px;
                background-color: orange;
                border: 0px solid orange;
                border-radius: 5%;
            }"""
        )
        self.networkDesignTryBtn.setGeometry(850, 220, 100, 40)
        self.networkDesignTryBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToPathDesignPage1(parent))


    # KML Generator button
    def kmlGeneratorBtn(self, parent):
        # wrapper
        self.kmlGeneratorBtnWrapper = QWidget(self)
        self.kmlGeneratorBtnWrapper.setStyleSheet("""
            QWidget {
                color: blue;
                font-size: 30px;
                border: 3px solid white;
                border-radius: 5%;
                background-color: white;
            }"""
        )
        self.kmlGeneratorBtnWrapper.setGeometry(250, 350, 400, 250)
        # Button label
        self.kmlGeneratorBtnLabel = QLabel(self)
        self.kmlGeneratorBtnLabel.setText('KML Generator')
        self.kmlGeneratorBtnLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 30px;
            }"""
        )
        self.kmlGeneratorBtnLabel.setGeometry(250, 370, 400, 60)
        self.kmlGeneratorBtnLabel.setAlignment(Qt.AlignCenter)
        # discription
        self.kmlGeneratorBtnDescriptionLabel = QLabel(self)
        self.kmlGeneratorBtnDescriptionLabel.setText('Generate a KML file. You can upload to Google Earth to visualize the network.')
        self.kmlGeneratorBtnDescriptionLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 15px;
            }"""
        )
        self.kmlGeneratorBtnDescriptionLabel.setGeometry(260, 420, 380, 60)
        self.kmlGeneratorBtnDescriptionLabel.setWordWrap(True)
        self.kmlGeneratorBtnDescriptionLabel.setAlignment(Qt.AlignCenter)
        # "Try" button
        self.kmlGeneratorTryBtn = QPushButton(self)
        self.kmlGeneratorTryBtn.setText("Open")
        self.kmlGeneratorTryBtn.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 20px;
                background-color: orange;
                border: 0px solid orange;
                border-radius: 5%;
            }"""
        )
        self.kmlGeneratorTryBtn.setGeometry(400, 520, 100, 40)
        self.kmlGeneratorTryBtn.clicked.connect(lambda: parent.screenTransitionModules.moveToKMLGeneratorPage1(parent))


    # Open sub menu
    def openSubMenuUI(self, parent):
        if self.subMenuContainer.isVisible():
            self.subMenuContainer.setVisible(False)
            self.pathDesignLink.setVisible(False)
            self.nwkDesignLink.setVisible(False)
            self.coverageMapLink.setVisible(False)
        else:
            self.subMenuContainer.setVisible(True)
            self.pathDesignLink.setVisible(True)
            self.nwkDesignLink.setVisible(True)
            self.coverageMapLink.setVisible(True)

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
