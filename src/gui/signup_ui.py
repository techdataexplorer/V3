#
# signup_ui.py
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

class SignUpWidget(QWidget):

    def __init__(self, parent=None):
        super(SignUpWidget, self).__init__(parent)
        self.initUI(parent)


    def initUI(self, parent):
        self.formUI(parent)


    # Left UI
    def formUI(self, parent):

        # Signup label
        self.appLabel = QLabel(self)
        self.appLabel.setText("Create New Account")
        self.appLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 25px;
            }"""
        )
        self.appLabel.setGeometry(300, 25, 600, 30)
        self.appLabel.setAlignment(Qt.AlignLeft)

        # Wrapper
        self.formContainer = QWidget(self)
        self.formContainer.setAutoFillBackground(True)
        self.formContainer.setStyleSheet("""
            background-color:white;
            border-radius: 5%;
        """)
        self.formContainer.setGeometry(300, 70, 600, 600)

        # Oragnization drop down
        # label
        self.appLabel = QLabel(self)
        self.appLabel.setText("Select Oragnization Name")
        self.appLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 15px;
            }"""
        )
        self.appLabel.setGeometry(400, 100, 400, 20)
        self.appLabel.setAlignment(Qt.AlignLeft)
        # drop down
        self.orgList = QComboBox(self)
        self.orgList.addItem("NTT Docomo")
        self.orgList.addItem("Au")
        self.orgList.addItem("Softbank")
        self.orgList.addItem("Mint")
        self.orgList.setGeometry(400, 120, 400, 50)

        # Full Name input text
        # label
        self.fullNameLabel = QLabel(self)
        self.fullNameLabel.setText("Full Name")
        self.fullNameLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 15px;

            }"""
        )
        self.fullNameLabel.setGeometry(400, 170, 450, 20)
        self.fullNameLabel.setAlignment(Qt.AlignLeft)
        # text field
        self.fullNameInput = QLineEdit(self)
        self.fullNameInput.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
            }"""
        )
        self.fullNameInput.setGeometry(400, 190, 400, 30)

        # Phone number input text
        # label
        self.phoneNumberLabel = QLabel(self)
        self.phoneNumberLabel.setText("Phone Number")
        self.phoneNumberLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 15px;

            }"""
        )
        self.phoneNumberLabel.setGeometry(400, 230, 450, 20)
        self.phoneNumberLabel.setAlignment(Qt.AlignLeft)
        # text field
        self.phoneNumberInput = QLineEdit(self)
        self.phoneNumberInput.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
            }"""
        )
        self.phoneNumberInput.setGeometry(400, 250, 400, 30)

        # Phone number input text
        # label
        self.addressLabel = QLabel(self)
        self.addressLabel.setText("Address")
        self.addressLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 15px;

            }"""
        )
        self.addressLabel.setGeometry(400, 290, 450, 20)
        self.addressLabel.setAlignment(Qt.AlignLeft)
        # text field
        self.addressInput = QLineEdit(self)
        self.addressInput.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
            }"""
        )
        self.addressInput.setGeometry(400, 310, 400, 30)

        # Phone number input text
        # label
        self.emailLabel = QLabel(self)
        self.emailLabel.setText("Email")
        self.emailLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 15px;

            }"""
        )
        self.emailLabel.setGeometry(400, 350, 450, 20)
        self.emailLabel.setAlignment(Qt.AlignLeft)
        # text field
        self.emailInput = QLineEdit(self)
        self.emailInput.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
            }"""
        )
        self.emailInput.setGeometry(400, 370, 400, 30)

        # Password input text
        # label
        self.passwordLabel = QLabel(self)
        self.passwordLabel.setText("Password")
        self.passwordLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 15px;

            }"""
        )
        self.passwordLabel.setGeometry(400, 410, 450, 20)
        self.passwordLabel.setAlignment(Qt.AlignLeft)
        # text field
        self.passwordInput = QLineEdit(self)
        self.passwordInput.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
            }"""
        )
        self.passwordInput.setGeometry(400, 430, 400, 30)

        # Confirm Password input text
        # label
        self.confirmPasswordLabel = QLabel(self)
        self.confirmPasswordLabel.setText("Confirm Password")
        self.confirmPasswordLabel.setStyleSheet("""
            QLabel {
                color : rgba(8, 44, 108, 1);
                font-size: 15px;

            }"""
        )
        self.confirmPasswordLabel.setGeometry(400, 470, 450, 20)
        self.confirmPasswordLabel.setAlignment(Qt.AlignLeft)
        # text field
        self.confirmPasswordInput = QLineEdit(self)
        self.confirmPasswordInput.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
            }"""
        )
        self.confirmPasswordInput.setGeometry(400, 490, 400, 30)

        # Signup Button
        self.signupBtn = QPushButton(self)
        self.signupBtn.setText("Create Account")
        self.signupBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 18px;
                border-radius: 5%;
                background-color: blue;
            }"""
        )
        self.signupBtn.setGeometry(400, 550, 150, 50)
        self.signupBtn.clicked.connect(lambda: self.moveToLogInPage(parent))

    def button01Clicked(self):
        print("Signup btn clicked!")

    def moveToLogInPage(self, parent):
        parent.central_widget.setCurrentIndex(0)
