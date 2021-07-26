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
import pyrebase
import dataclasses



@dataclasses.dataclass
class KMLGeneratorData:
    # Site 1
    pathColor: str
    dotColor: str
    header: bool
    nameVisibility: bool
    avoidSites: bool


    def __post_init__(self):
        pathColor = "Green"
        dotColor = "Red"
        header = True
        nameVisibility = True
        avoidSites = False


    def printKMLGeneratorData(self):
        print("---------------- KML Generator data ------------------")
        print("Path color               : ", str(self.pathColor))
        print("Dot color                : ", str(self.dotColor))
        print("CSV file header          : ", str(self.header))
        print("Site name visibility     : ", str(self.nameVisibility))
        print("Avoid sites altogether   : ", str(self.avoidSites))
        print("------------------------------------------------------")


    # Setter
    def setPathColor(self, color):
        self.pathColor = color

    def setDotColor(self, color):
        self.dotColor = color

    def setHeader(self, flag):
        self.header = flag

    def setNameVisibility(self, flag):
        self.nameVisibility = flag

    def setAvoidSites(self, flag):
        self.avoidSites = flag

    # Getter
    def getPathColor(self):
        return self.pathColor

    def getDotColor(self):
        return self.dotColor

    def getHeader(self):
        return self.header

    def getNameVisibility(self):
        return self.nameVisibility

    def getAvoidSites(self):
        return self.avoidSites
