#
# home_ui.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import json
import io
import os
import csv
import sip
import folium
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


# Data Model
from constants.accountData import AccountData
from constants.firebaseData import FirebaseData
from constants.pathDesignData import PathDesignData

class HomeWidget(QWidget):

    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)
        self.initUI(parent)

    def initUI(self, parent):
        self.sideMenuUI(parent)
        self.accountUI(parent)
        self.projectUI(parent)




    def sideMenuUI(self, parent):
        # side menu wrapper
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
                color: rgba(8, 44, 108, 1);
                font-size: 15px;
                background-color: white;
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
                color: white;
                font-size: 15px;
                background-color: rgba(8, 44, 108, 1);
                border: 0px solid white;
            }"""
        )
        self.nwcfBtn.setGeometry(0, 400, 1200/6, 50)
        self.nwcfBtn.clicked.connect(lambda: self.moveToPathDesignPage0(parent))

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
        self.usersEmailLabel.setText("test@email.com")
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



    def projectUI(self, parent):
        # Open new project button
        self.newProjectBtn = QPushButton(self)
        self.newProjectBtn.setText("Create new project")
        self.newProjectBtn.setIcon(QIcon("./img/plus-icon.png"))
        self.newProjectBtn.setIconSize(QSize(36,36))
        self.newProjectBtn.setStyleSheet("""
            QPushButton {
                color: blue;
                font-size: 30px;
                border: 3px solid blue;
                border-radius: 5%;
                background-color: white;
            }"""
        )
        self.newProjectBtn.setGeometry(450, 350, 400, 60)
        self.newProjectBtn.clicked.connect(lambda: parent.popUp.upCommingFunctionality())

        # Open existing project button
        self.openProjectBtn = QPushButton(self)
        self.openProjectBtn.setText("Open existing project")
        self.openProjectBtn.setIcon(QIcon("./img/folder-icon.png"))
        self.openProjectBtn.setIconSize(QSize(36,36))
        self.openProjectBtn.setStyleSheet("""
            QPushButton {
                color: blue;
                font-size: 30px;
                border: 3px solid blue;
                border-radius: 5%;
                background-color: white;
            }"""
        )
        self.openProjectBtn.setGeometry(450, 450, 400, 60)
        self.openProjectBtn.clicked.connect(lambda: parent.popUp.upCommingFunctionality())
        # self.newProjectBtn.setEnabled(False)


    def button01Clicked(self):
        print("clicked!")

    # Open sub menu
    def button03Clicked(self):
        print("Network Config Clicked!")

    #
    def moveToHomePage(self, parent):
        parent.central_widget.setCurrentIndex(2)

    def moveToPathDesignPage0(self, parent):
        parent.central_widget.setCurrentIndex(3)
