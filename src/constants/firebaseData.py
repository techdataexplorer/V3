#
# firebaseData.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import json
import io
import os
import csv
import sip
# import folium
import pyrebase
import dataclasses


@dataclasses.dataclass
class FirebaseData:

    def __post_init__(self, apiKey=None, authDomain=None, databaseURL=None, storageBucket=None, messagingSenderId=None):
        self.config = {
            "apiKey": "AIzaSyDZlk_X5tfG4_J4BKwzdFULomGQt6r_QwM",
            "authDomain": "tdx-desktop-e2280.firebaseapp.com",
            "databaseURL": "https://tdx-desktop-e2280.firebaseio.com",
            "projectId": "tdx-desktop-e2280",
            "storageBucket": "tdx-desktop-e2280.appspot.com",
            "messagingSenderId": "889911816542",
            "appId": "1:889911816542:web:542868e4fc540851525fcf",
            "measurementId": "G-GXYN1EEXNM"
        }
        self.apiKey = self.config["apiKey"]
        self.authDomain = self.config["authDomain"]
        self.databaseURL = self.config["databaseURL"]
        self.storageBucket = self.config["storageBucket"]
        self.messagingSenderId = self.config["messagingSenderId"]
        self.appId = self.config["appId"]
        self.measurementId = self.config["measurementId"]
        # Connect to DB
        self.firebase = pyrebase.initialize_app(self.config)
        # Get a reference to the auth service
        self.auth = self.firebase.auth()
        # DB access
        # self.db =


    def printFirebaseData(self):
        print("-- Firebase data --")
        print("apiKey       : ", self.apiKey)
        print("authDomain   : ", self.authDomain)
        print("databaseURL  : ", self.databaseURL)
        print("storageBucket: ", self.storageBucket)
