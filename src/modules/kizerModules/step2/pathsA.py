#
# PathA.py
# Kizer Modules API
# Created by Che Blankenship on 11/08/2021
#

import sys
import json
import io
import os
import math
import requests
import pandas as pd
from geopy.distance import geodesic
# import urllib.request
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *


class PathA:
    # Directory and file paths
    downloadPath    = ""        # path where user wants to download the kml file
    inputFilePath   = ""        # csv file path (user input)
    output          = ""        # save result
    
    # Open folder on user's PC and get user's folder location.
    def getDownloadLocation(self, folderPrompt):
        folderName = QFileDialog.getExistingDirectory(self, folderPrompt)
        if folderName:
            return folderName

    
    # Get file name from path (i.e: ./dir-path/path1.csv will be "path1")
    def getFileNameFromPath(self, importedFilePath):
        splitedPath = os.path.basename(importedFilePath)
        fileName = splitedPath.split(".")
        return str(fileName[0])

    
# ### Test call the modules ###
# testkml = KML3DA()
# start_time = time.time()
# testkml.generateKML('/Users/cheblankenship/Downloads/', '/Users/cheblankenship/Downloads/Paths1.CSV', "Blue", "LtGreen")
# print("---New: %s seconds ---" % (time.time() - start_time))
