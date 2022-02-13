#
# patha ui2.py
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


# Modules
from pages.components.progressUI import ProgressUI

# "2. Path Calculation Page"
class GudPathUI2(QWidget):

    def __init__(self, parent=None):
        super(GudPathUI2, self).__init__(parent)
        self.screenWidth = QDesktopWidget().screenGeometry(-1).width()
        self.screenHeight = QDesktopWidget().screenGeometry(-1).height()
        self.progressUI = ProgressUI(self).setUp(parent, "Gud Path", 0, True)

        self.initUI(parent)
        self.update()

    def initUI(self, parent):
        self.parametersUI(parent)
        self.configUI(parent)


    def parametersUI(self, parent):
        # parameters view wrapper
        self.paramsContainer = QWidget(self)
        self.paramsContainer.setAutoFillBackground(True)
        self.paramsContainer.setStyleSheet("""
            background-color: white;
            border-radius: 5%;
        """)
        self.paramsContainer.setGeometry(self.screenWidth*0.05, self.screenHeight*0.10, self.screenWidth*0.90, self.screenHeight*0.8)

        # Message label
        self.directionMsgLabel2 = QLabel(self)
        self.directionMsgLabel2.setText("Paths are generated")
        self.directionMsgLabel2.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 20px;
            }"""
        )
        self.directionMsgLabel2.setGeometry(self.screenWidth*0.15, self.screenHeight*0.12, 500, 30)
        self.directionMsgLabel2.setAlignment(Qt.AlignLeft)


        # go to kml generator btn
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
        self.nextPageBtn.setGeometry(self.screenWidth*0.8, self.screenHeight*0.83, 150, 40)
        self.nextPageBtn.clicked.connect(lambda: parent.screenTransition.backToHome(parent))



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
        self.siteAContainer.setGeometry(self.screenWidth*0.15, self.screenHeight*0.2, self.screenWidth*0.7, self.screenHeight*0.6)

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
        self.siteAScroll.setGeometry(self.screenWidth*0.15, self.screenHeight*0.2, self.screenWidth*0.7, self.screenHeight*0.6)
        # define each UI field and append them to the vertical stack view
        self.savedLocationUI(parent)
        # append the vertical stack view into a container view
        self.siteAContainer.setLayout(self.configVLayout)



    # Each horizontal layout UI
    # Define result file download location
    def savedLocationUI(self, parent):
        # Horizontal stack
        self.savedLocationHLayout = QHBoxLayout() # remove 'self' due to err msg
        # savedLocation label
        self.savedLocationLabel = QLabel(self)
        self.savedLocationLabel.setText("Location where csv files are saved:")
        self.savedLocationLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.savedLocationLabel.setAlignment(Qt.AlignLeft)
        self.savedLocationLabel.setFixedWidth(500)
        self.savedLocationLabel.setContentsMargins(10, 15, 10, 10) # margin
        # savedLocation result (read only)
        self.savedLocationTextBox = QLineEdit(self)
        self.savedLocationTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.savedLocationTextBox.setText("-- Path not defined --")
        self.savedLocationTextBox.setAlignment(Qt.AlignLeft)
        self.savedLocationTextBox.setFixedWidth(320)
        self.savedLocationTextBox.setReadOnly(True)
        # Add to H stack
        self.savedLocationHLayout.addWidget(self.savedLocationLabel)
        self.savedLocationHLayout.addWidget(self.savedLocationTextBox)
        # Add to V stack
        self.configVLayout.addLayout(self.savedLocationHLayout)



    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    def nextBtnClicked(self, parent):
        parent.screenTransitionModules.moveToPathAPage1(parent)
