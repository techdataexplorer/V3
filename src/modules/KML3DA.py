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
import requests
import pandas as pd
import urllib.request
from geopy.distance import geodesic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngineWidgets import *


# Folder path from Cloud
folderPath = "" # root file



def openFolderNameDialog(self, folderPrompt):
    folderName = QFileDialog.getExistingDirectory(self, folderPrompt)
    if folderName:
        return folderName

def checkPathColor(arg):
    pass

def checkDotColor(arg):
    pass



def generateKML(arg):
    pass
