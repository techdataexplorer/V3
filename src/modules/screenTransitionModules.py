#
# path_profile_modules.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import json
import io
import os
import csv
import math
# import sip
import folium
import urllib.request
import requests
from geopy.distance import geodesic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *



class ScreenTransitionModules:

    # Move to login page.
    def moveToLoginPage(self, parent):
        parent.central_widget.setCurrentIndex(0)

    # Move to signup page.
    def moveToLoginPage(self, parent):
        parent.central_widget.setCurrentIndex(1)

    # Move to home page.
    def moveToHomePage(self, parent):
        parent.central_widget.setCurrentIndex(2)

    # Move to path design page 0.
    def moveToPathDesignPage0(self, parent):
        parent.central_widget.setCurrentIndex(3)

    # Move to path design page 1.
    def moveToPathDesignPage1(self, parent):
        parent.central_widget.setCurrentIndex(4)

    # Move to path design page 2.
    def moveToPathDesignPage2(self, parent):
        parent.central_widget.setCurrentIndex(5)

    # Move to path design page 3.
    def moveToPathDesignPage3(self, parent):
        parent.central_widget.setCurrentIndex(6)
