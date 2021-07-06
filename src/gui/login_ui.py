#
# login_ui.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import json
import io
import os
import csv
# import sip
import folium
import requests
import pyrebase
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# Gui
from gui.signup_ui import SignUpWidget

# Data Model
from constants.accountData import AccountData
from constants.firebaseData import FirebaseData
from constants.pathDesignData import PathDesignData

# Modules
# from modules.sideMenuModules import SideMenuModules



class LogInWidget(QWidget):

    def __init__(self, parent=None):
        super(LogInWidget, self).__init__(parent)
        self.initUI(parent)


    def initUI(self, parent):
        self.leftUI()
        self.rightUI(parent)


    # Left UI
    def leftUI(self):
        # left wrapper
        self.leftContainer = QWidget(self)
        self.leftContainer.setAutoFillBackground(True)
        self.leftContainer.setStyleSheet("""
            background-color:rgba(8, 44, 108, 1);
        """)
        self.leftContainer.setGeometry(0, 0, (1200/3), 800)

        # Image
        self.logoLabel = QLabel(self)
        path = os.path.dirname(os.path.abspath(__file__))
        self.logoLabel.setPixmap(QPixmap(os.path.join(path, "../img/SD_logo.png"))) # path starts from main.py
        self.logoLabel.setGeometry(0, 100, 400, 80)
        self.logoLabel.setAlignment(Qt.AlignCenter)

        # TDX desktop label
        self.appLabel = QLabel(self)
        self.appLabel.setText("Telecom Data Explorer Desktop")
        self.appLabel.setStyleSheet("""
            QLabel {
                color : rgba(239, 240, 242, 1);
                font-size: 25px;
            }"""
        )
        self.appLabel.setGeometry(0, 250, 400, 30)
        self.appLabel.setAlignment(Qt.AlignCenter)

        # contact label
        self.contactLabel = QLabel(self)
        self.contactLabel.setText('<a href="https://www.spatialdatalyst.com/service-options">Contact us</a>')
        self.contactLabel.setStyleSheet("""
            QLabel {
                color : white;
                font-size: 15px;

            }"""
        )
        self.contactLabel.setGeometry(0, 600, 400, 20)
        self.contactLabel.setAlignment(Qt.AlignCenter)

        # version label
        self.versionLabel = QLabel(self)
        self.versionLabel.setText("Version 1.0.6")
        self.versionLabel.setStyleSheet("""
            QLabel {
                color: rgba(239, 240, 242, 1);
                font-size: 15px;
            }"""
        )
        self.versionLabel.setGeometry(0, 700, 400, 20)
        self.versionLabel.setAlignment(Qt.AlignCenter)


    # Right UI
    def rightUI(self, parent):
        # message label 1
        self.msgLabel1 = QLabel(self)
        self.msgLabel1.setText("Welcome to TDX Desktop ")
        self.msgLabel1.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 20px;
            }"""
        )
        self.msgLabel1.setGeometry(550, 100, 750, 30)
        self.msgLabel1.setAlignment(Qt.AlignLeft)

        # message label
        self.msgLabel2 = QLabel(self)
        self.msgLabel2.setText("Sign into your account")
        self.msgLabel2.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 30px;
            }"""
        )
        self.msgLabel2.setGeometry(550, 130, 750, 40)
        self.msgLabel2.setAlignment(Qt.AlignLeft)

        # form wrapper
        self.formContainer = QWidget(self)
        self.formContainer.setAutoFillBackground(True)
        self.formContainer.setStyleSheet("""
            background-color: white;
            border-radius: 5%;
        """)
        self.formContainer.setGeometry(550, 200, 500, 400)


        # Email label
        self.emailLabel = QLabel(self)
        self.emailLabel.setText("Email")
        self.emailLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 15px;
            }"""
        )
        self.emailLabel.setGeometry(650, 270, 750, 30)
        self.emailLabel.setAlignment(Qt.AlignLeft)

        # Email text input
        self.emailInput = QLineEdit(self)
        self.emailInput.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
            }"""
        )
        self.emailInput.setGeometry(650, 300, 300, 30)

        # password
        self.passwordLabel = QLabel(self)
        self.passwordLabel.setText("Password")
        self.passwordLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 15px;
            }"""
        )
        self.passwordLabel.setGeometry(650, 350, 750, 30)
        self.passwordLabel.setAlignment(Qt.AlignLeft)

        # password text input
        self.passwordInput = QLineEdit(self)
        self.passwordInput.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
            }"""
        )
        self.passwordInput.setEchoMode(self.passwordInput.Password)
        self.passwordInput.setGeometry(650, 380, 300, 30)

        # Login Button
        self.btn1 = QPushButton(self)
        self.btn1.setText("Sign in")
        self.btn1.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 20px;
                border-radius: 5%;
                background-color: blue;
            }"""
        )
        self.btn1.setGeometry(650, 450, 100, 50)
        self.btn1.clicked.connect(lambda: self.checkLogIn(parent))

        # Create account label
        # Email label
        self.newAccountLabel = QLabel(self)
        self.newAccountLabel.setText("Don’t have an account?")
        self.newAccountLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 15px;
            }"""
        )
        self.newAccountLabel.setGeometry(550, 650, 750, 30)
        self.newAccountLabel.setAlignment(Qt.AlignLeft)

        # Sign in Button
        self.btn2 = QPushButton(self)
        self.btn2.setText("Create New Account")
        self.btn2.setStyleSheet("""
            QPushButton {
                color: blue;
                font-size: 15px;
                border: 3px solid blue;
                border-radius: 5%;
                background-color: white;
            }"""
        )
        self.btn2.setGeometry(550, 680, 170, 50)
        self.btn2.clicked.connect(lambda: parent.popUp.upCommingFunctionality())


    def checkLogIn(self, parent):
        self.emailStr = str(self.emailInput.text())
        self.passwdStr = str(self.passwordInput.text())
        try:
            if (self.emailInput.text() != "") and (self.passwordInput.text() != ""):
                self.emailUserInput = str(self.emailInput.text());
                self.passwdUserInput = str(self.passwordInput.text());
                print("Check log in called email    : ", self.emailUserInput)
                print("Check log in called passwd   : ", self.passwdUserInput)
                try:
                    self.user = parent.firebaseData.auth.sign_in_with_email_and_password(self.emailUserInput, self.passwdUserInput)
                    print("check results >> ", self.user)
                    parent.accountData.setEmail(self.emailUserInput)
                    parent.accountData.setPasswd(self.passwdUserInput)
                    self.moveToHomePage(parent)
                except Exception as e:
                    try:
                        print("Login Error: ", e)
                    except Exception as e:
                        print("Login error. Try again..")
            else:
                print("Input field needs valid input")

        except Exception as e:
            print("Error: invalid input")



    def moveToSingupPage(self, parent):
        parent.sideMenuModules.moveToSingupPage(parent)



    def moveToHomePage(self, parent):
        # Update the email on the side menu
        parent.homeWidget.usersEmailLabel.setText(parent.accountData.getEmail())
        parent.pathDesignWidget0.usersEmailLabel.setText(parent.accountData.getEmail())
        parent.pathDesignWidget1.usersEmailLabel.setText(parent.accountData.getEmail())
        parent.pathDesignWidget2.usersEmailLabel.setText(parent.accountData.getEmail())
        parent.pathDesignWidget3.usersEmailLabel.setText(parent.accountData.getEmail())
        parent.screenTransitionModules.moveToHomePage(parent)
