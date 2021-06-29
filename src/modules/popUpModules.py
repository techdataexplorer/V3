#
# main.py
# TDX Desktop
# Created by Che Blankenship on 06/22/2021
#
import sys
import json
import io
import os
import csv
import math
import folium
import pyrebase
import dataclasses
from geopy.distance import geodesic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class PopUpModules:

    def upCommingFunctionality(self):
        self.dialogWgt = QDialog()
        self.dialogWgt.setGeometry(600, 400, 400, 300)
        # site B path distance label
        self.errorMsgLabel = QLabel(self.dialogWgt)
        self.errorMsgLabel.setText("This functionality is coming soon....")
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
        self.dialogWgt.setWindowTitle("Message")
        self.dialogWgt.setWindowModality(Qt.ApplicationModal)
        self.dialogWgt.exec_()
