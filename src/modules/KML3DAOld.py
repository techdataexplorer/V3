#
# KML3DAOld.py
# Slow version
# Kizer Modules API
# Created by Che Blankenship on 07/28/2021
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
import time


class KML3DAModules:
    # Public varables for KML3DAModules
    downloadPath= ""    # path where user wants to download the kml file
    csvFilePath = ""    # csv file path (user input)
    dotColor    = '<color>'+'7f000000'+'</color>'    # default as black
    pathColor   = '<color>'+'7f0000ff'+'</color>'    # default as red
    headerYN    = "Yes"
    siteTitleYN = "Yes"
    pathsOnlyYN = "No"
    DISTANCE    = ""
    FREQ        = ""
    INDEX       = None
    # Site 1 data
    site1Data   = {
        "name": None,
        "lat": None,
        "lon": None,
        "height": None
    }
    # Site 2 data
    site2Data   = {
        "name": None,
        "lat": None,
        "lon": None,
        "height": None
    }
    # csv row data
    ROW         = None
    # hardcoded data
    RANGE       = "3000"
    ALTITUDE    = "300"
    AZIMUTH     = "0"
    TILT        = "45"

    # Open folder on user's PC and get user's folder location.
    def getDownloadLocation(self, folderPrompt):
        folderName = QFileDialog.getExistingDirectory(self, folderPrompt)
        if folderName:
            return folderName

    # convert path and dot color string to hex
    def convertColorToHex(self, color):
        # [Black, Red, Green, Blue, Yellow, Brown, Orange, LtGreen]
        colors = ['7f000000', '7f0000ff', '7f00ff00', '7fff0000', '7f00ffff', '7f000040', '7f0080ff', '7f00ff80']
        if color == "Black":
            return '<color>'+str(colors[0])+'</color>'
        if color == "Red":
            return '<color>'+str(colors[1])+'</color>'
        if color == "Green":
            return '<color>'+str(colors[2])+'</color>'
        if color == "Blue":
            return '<color>'+str(colors[3])+'</color>'
        if color == "Yellow":
            return '<color>'+str(colors[4])+'</color>'
        if color == "Brown":
            return '<color>'+str(colors[5])+'</color>'
        if color == "Orange":
            return '<color>'+str(colors[6])+'</color>'
        if color == "LtGreen":
            return '<color>'+str(colors[7])+'</color>'
        else:
            return '<color>'+str(colors[0])+'</color>'


    # Get file name from path
    def getFileNameFromPath(self, importedFilePath):
        # get the file name from path
        splitedPath = os.path.basename(importedFilePath)
        # remove file extension from file name string
        fileName = splitedPath.split(".")
        return str(fileName[0])


    # Generate KML file
    # Inputs
    # csvFilePath       : user's imported file path
    # selectedDotColor  : selected dot color by user
    # selectedPathColor : selected path color by user
    def generateKML(self, downloadLocation, csvFilePath, selectedDotColor, selectedPathColor):
        tempFile    = downloadLocation + "/" + "tempFile.csv"    # temporary file used for kml generation
        outPutFile  = downloadLocation + "/" + "result.kml"      # KML file to save results
        # read the csv file using pandas
        primary_df = pd.read_csv(csvFilePath)
        output = open(outPutFile, "w")
        temp = open(tempFile, "w")
        temp.close()                    # create an empty file
        # update path and dot colors
        self.dotColor = self.convertColorToHex(selectedDotColor)
        self.pathColor = self.convertColorToHex(selectedPathColor)
        # check if header exist
        if self.headerYN == 'Yes':
            headers = list(primary_df.columns)

        ### start creating KML file ###
        # Write the header content
        inputFileName = self.getFileNameFromPath(csvFilePath)
        output.write("<?xml version=" + chr(34) + "1.0" + chr(34) + " encoding=" + chr(34) + "UTF-8" + chr(34) + "?>")
        output.write("\n<kml xmlns=" + chr(34) + "http://www.opengis.net/kml/2.2" + chr(34) + ">")
        output.write("\n<Document>")
        output.write("\n<name>" + inputFileName + " System Map</name>")
        output.write("\n<description>Microwave Paths</description>")
        output.write("\n")

        # iterate through the input csv file
        for index, row in primary_df.iterrows():
            self.INDEX = int(row[0])
            self.site1Data["name"]      = str(row[1])
            self.site1Data["lat"]       = float(row[2])
            self.site1Data["lon"]       = float(row[3])
            self.site1Data["height"]    = float(row[7])
            self.site2Data["name"]      = str(row[4])
            self.site2Data["lat"]       = float(row[5])
            self.site2Data["lon"]       = float(row[6])
            self.site2Data["height"]    = float(row[8])
            #Convert heights in feet to heights in meters
            self.site1Data["height"]    = self.site1Data["height"] / 3.28084
            self.site2Data["height"]    = self.site2Data["height"] / 3.28084
            # Generate string for kml (e.g: Site 1 - Site 2 )
            thePath = self.site1Data["name"] + " - " + self.site2Data["name"]
            pathInfo = thePath + self.DISTANCE + self.FREQ
            # Suppress multiple site names
            FlagS1 = 0
            FlagS2 = 0
            try:
                temp_df = pd.read_csv(tempFile, header=None)
                for index, row in temp_df.iterrows():
                    ASITE = row[0]
                    # Site 1
                    if (self.site1Data["name"] == ASITE): #this site name has been used previously
                        FlagS1 = 1
                        self.site1Data["name"] = ""
                    # Site 2
                    if (self.site2Data["name"] == ASITE): #this site name has been used previously
                        FlagS2 = 1
                        self.site2Data["name"] = ""


            except pd.errors.EmptyDataError:
                pass
            self.writeToKML(output, temp, tempFile, pathInfo, thePath, FlagS1, FlagS2)

        # write the footer
        output.write("\n</Document>")
        output.write("\n</kml>\n")
        # Delete file
        del primary_df
        output.close()
        os.remove(tempFile)
        print("\nProgram Completed")


    def writeToKML(self, output, temp, tempFile, pathInfo, thePath, FlagS1, FlagS2):
        temp.close()
        temp = open(tempFile, "a")
        # Write site 1 or site 2 based on the falg statement.
        if (FlagS1 == 0):
            temp.write(self.site1Data["name"])
            temp.write("\n")
        if (FlagS2 == 0):
            temp.write(self.site2Data["name"])
            temp.write("\n")
        temp.close()
        # Write data into output KML file
        output.write("\n<Style id=" + chr(34) + "blackLineGreenPoly" + chr(34) + ">")
        output.write("\n<LineStyle>\n")
        output.write(self.pathColor)
        output.write("\n<width>4</width>")
        output.write("\n</LineStyle>")
        output.write("\n<PolyStyle>\n")
        output.write(self.dotColor)
        output.write("\n</PolyStyle>")
        output.write("\n</Style>")
        output.write("\n<Placemark>")
        output.write("\n<name>" + pathInfo + "</name>")
        output.write("\n<description>Path Between " + thePath + "</description>")
        output.write("\n<LookAt>")
        output.write("\n<longitude>{}</longitude>".format(self.site1Data["lon"]))
        output.write("\n<latitude>{}</latitude>".format(self.site1Data["lat"]))
        output.write("\n<altitude>{}</altitude>".format(self.ALTITUDE))
        output.write("\n<range>{}</range>".format(self.RANGE))
        output.write("\n<tilt>{}</tilt>".format(self.TILT))
        output.write("\n<heading>{}</heading>".format(self.AZIMUTH))
        output.write("\n<altitudeMode>relativeToGround</altitudeMode>")
        output.write("\n</LookAt>")
        output.write("\n<styleUrl>#blackLineGreenPoly</styleUrl>")
        output.write("\n<LineString>")
        output.write("\n<extrude>1</extrude>")
        output.write("\n<tessellate>1</tessellate>")
        output.write("\n<altitudeMode>relativeToGround</altitudeMode>")
        output.write("\n<coordinates>{},{},{}".format(self.site1Data["lon"], self.site1Data["lat"], self.site1Data["height"])) #height in feet
        output.write("\n{},{},{}".format(self.site2Data["lon"], self.site2Data["lat"], self.site2Data["height"]))
        output.write("\n</coordinates>")
        output.write("\n</LineString>")
        output.write("\n</Placemark>")
        output.write("\n")

        #Sites
        if(self.pathsOnlyYN=="Yes"):
            self.writeToKML(output, temp, tempFile, pathInfo, thePath, FlagS1, FlagS2)

        output.write("\n<Placemark>")
        output.write("\n<description>Microwave Site</description>")
        output.write("\n<name>{}</name>".format(self.site1Data["name"]))
        if(self.siteTitleYN=="Yes"):
            output.write("\n<visibility>1</visibility>")
        if(self.siteTitleYN != "Yes"):
            output.write("\n<visibility>0</visibility>")
        output.write("\n<Style>")
        output.write("\n<IconStyle>")
        output.write("\n<color>ff0000ff</color>")
        output.write("\n<scale>0.7</scale>")
        output.write("\n<Icon>")
        output.write("\n<href>http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png</href>")
        output.write("\n</Icon>")
        output.write("\n</IconStyle>")
        output.write("\n<LabelStyle>")
        output.write("\n<scale>0.9</scale>")
        output.write("\n</LabelStyle>")
        output.write("\n</Style>")
        output.write("\n<Point>")
        output.write("\n<IconAltitude>1</IconAltitude>")
        output.write("\n<extrude>1</extrude>")
        output.write("\n<altitudeMode>relativeToGround</altitudeMode>")
        output.write("\n<coordinates>{},{},0</coordinates>".format(self.site1Data["lon"], self.site1Data["lat"]))
        output.write("\n</Point>")
        output.write("\n</Placemark>")
        output.write("\n<Placemark>")
        output.write("\n<description>Microwave Site</description>")
        output.write("\n<name>{}</name>".format(self.site2Data["name"]))
        if(self.siteTitleYN=="Yes"):
            output.write("\n<visibility>1</visibility>")
        if(self.siteTitleYN!="Yes"):
            output.write("\n<visibility>0</visibility>")
        output.write("\n<Style>")
        output.write("\n<IconStyle>")
        output.write("\n<color>ff0000ff</color>")
        output.write("\n<scale>0.7</scale>")
        output.write("\n<Icon>")
        output.write("\n<href>http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png</href>")
        output.write("\n</Icon>")
        output.write("\n</IconStyle>")
        output.write("\n<LabelStyle>")
        output.write("\n<scale>0.9</scale>")
        output.write("\n</LabelStyle>")
        output.write("\n</Style>")
        output.write("\n<Point>")
        output.write("\n<IconAltitude>1</IconAltitude>")
        output.write("\n<extrude>1</extrude>")
        output.write("\n<altitudeMode>relativeToGround</altitudeMode>")
        output.write("\n<coordinates>{},{},0</coordinates>".format(self.site2Data["lon"], self.site2Data["lat"]))
        output.write("\n</Point>")
        output.write("\n</Placemark>")
        output.write("\n")


# ### Test call the modules ###
# testkml = KML3DAModules()
# start_time = time.time()
# testkml.generateKML('/Users/cheblankenship/Downloads/', '/Users/cheblankenship/Downloads/Paths1.CSV', "Blue", "LtGreen")
# print("---Old: %s seconds ---" % (time.time() - start_time))
