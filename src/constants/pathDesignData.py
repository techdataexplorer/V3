#
# pathDesignData.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import json
import io
import os
import csv
#import sip
import folium
import pyrebase
import dataclasses


# from constants.siteData import SiteData


@dataclasses.dataclass
class PathDesignData:
    selectedFilePath: str
    fileType: str
    site1Name: str              # Site 1
    site1Latitude: float
    site1Longitude: float
    site1TowerHeight: float
    site1AntennaHeight: float
    site2Name: str              # Site 2
    site2Latitude: float
    site2Longitude: float
    site2TowerHeight: float
    site2AntennaHeight: float

    def __post_init__(self):
        self.site1Name = "Site 1"        # Site 1
        self.site1Latitude = 0
        self.site1Longitude = 0
        self.site1TowerHeight = 0
        self.site1AntennaHeight = 0
        self.site2Name = "Site 2"              # Site 2
        self.site2Latitude = 0
        self.site2Longitude = 0
        self.site2TowerHeight = 0
        self.site2AntennaHeight = 0


    def printPathDesignData(self):
        print("---------------- Path design data ------------------")
        print("Selected File Path   : ", str(self.selectedFilePath))
        print("File Type            : ", str(self.fileType))
        print("--------------------- Site 1 -----------------------")
        print("Site 1 name          : ", str(self.site1Name))
        print("Site 1 lat           : ", str(self.site1Latitude))
        print("Site 1 lng           : ", str(self.site1Longitude))
        print("Site 1 tower height  : ", str(self.site1TowerHeight))
        print("Site 1 antenna height: ", str(self.site1AntennaHeight))
        print("--------------------- Site 2 -----------------------")
        print("Selected File Path   : ", str(self.selectedFilePath))
        print("File Type            : ", str(self.fileType))
        print("Site 2 name          : ", str(self.site2Name))
        print("Site 2 lat           : ", str(self.site2Latitude))
        print("Site 2 lng           : ", str(self.site2Longitude))
        print("Site 2 tower height  : ", str(self.site2TowerHeight))
        print("Site 2 antenna height: ", str(self.site2AntennaHeight))
        print("--------------------------------------------------")


    def setFilePath(self, path):
        self.selectedFilePath = path

    def setFileType(self, fileExtension):
        self.fileType = fileExtension

    def getFilePath(self):
        return self.selectedFilePath

    def getFileType(self):
        return self.fileType

    ### Site 1 ###
    def setSite1Name(self, data):
        if(data != None):
            self.site1Name = str(data)
        else:
            self.site1Name = "Site 1"

    def setSite1Lat(self, data):
        print("CHECK DATA >>> ", data)
        if(data != None):
            print("Update value....")
            self.site1Latitude = float(data)
        else:
            self.site1Latitude = float(0)

    def setSite1Lng(self, data):
        if(data != None):
            print("Update value....")
            self.site1Longitude = float(data)
        else:
            self.site1Latitude = float(0)

    def setSite1TH(self, data):
        if(data != None):
            print("Update value....")
            self.site1TowerHeight = float(data)
        else:
            self.site1Latitude = float(0)

    def setSite1AH(self, data):
        if(data != None):
            print("Update value....")
            self.site1AntennaHeight = float(data)
        else:
            self.site1Latitude = float(0)

    def getSite1Name(self):
        return self.site1Name

    def getSite1Lat(self):
        return float(self.site1Latitude)

    def getSite1Lng(self):
        return float(self.site1Longitude)

    def getSite1TH(self):
        return float(self.site1TowerHeight)

    def getSite1AH(self):
        return float(self.site1AntennaHeight)


    ### Site 2 ###
    def setSite2Name(self, data):
        if(data != None):
            print("Update value....")
            self.site2Name = str(data)
        else:
            self.site1Latitude = "Site 2"

    def setSite2Lat(self, data):
        print("CHECK DATA >>> ", data)
        if(data != None):
            print("Update value....")
            self.site2Latitude = float(data)
        else:
            self.site1Latitude = float(0)

    def setSite2Lng(self, data):
        if(data != None):
            print("Update value....")
            self.site2Longitude = float(data)
        else:
            self.site1Latitude = float(0)

    def setSite2TH(self, data):
        if(data != None):
            print("Update value....")
            self.site2TowerHeight = float(data)
        else:
            self.site1Latitude = float(0)

    def setSite2AH(self, data):
        if(data != None):
            print("Update value....")
            self.site2AntennaHeight = float(data)
        else:
            self.site1Latitude = float(0)

    def getSite2Name(self):
        return str(self.site1Name)

    def getSite2Lat(self):
        return float(self.site2Latitude)

    def getSite2Lng(self):
        return float(self.site2Longitude)

    def getSite2TH(self):
        return float(self.site2TowerHeight)

    def getSite2AH(self):
        return float(self.site2AntennaHeight)
