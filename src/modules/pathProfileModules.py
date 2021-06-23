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
#import sip
import folium
import urllib.request
import requests
from geopy.distance import geodesic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *




class PathProfileModules:

    # Effective Isotropic Radiated Power (dBm)
    # [Input]
    # (1)
    # (2)
    # (3)
    # (4)
    def EIRP(self, antennaGain, transmitPower, TXCouplingLoss, MiscLoss):
        result = float(antennaGain + transmitPower - TXCouplingLoss - MiscLoss)
        print("EIRP: ", result)
        return result


    #
    def azimuth(self):
        print("Azimuth: not implemented yet...")


    # Distance in Km
    # Input: site1 & site2 lat/lng
    # Output: Distance in km
    def pathDistanceKm(self, site1Lat, site1Lng, site2Lat, site2Lng):
        coordinate1 = (site1Lat, site1Lng)
        coordinate2 = (site2Lat, site2Lng)
        print("Path distance: ", geodesic(coordinate1, coordinate2).km, " km.")
        return geodesic(coordinate1, coordinate2).km

    # Distance in Miles
    # Input: site1 & site2 lat/lng
    # Output: Distance in Miles
    def pathDistanceMiles(self, site1Lat, site1Lng, site2Lat, site2Lng):
        coordinate1 = (site1Lat, site1Lng)
        coordinate2 = (site2Lat, site2Lng)
        print("Path distance: ", geodesic(coordinate1, coordinate2).miles, " miles.")
        return geodesic(coordinate1, coordinate2).miles


    # Free Space Loss (dB)
    # https://www.everythingrf.com/rf-calculators/free-space-path-loss-calculator
    # [Input]
    # (1) Path distance (km)
    # (2) Frequency (MHz)
    # (3) Transmitting Antenna Gain - Tx (dB)
    # (4) Receiving Antenna Gain - Rx (dB)
    # Output: Free space path loss in dB
    def freeSpaceLoss(self, pathDistance, frequency, transmitAntennaGain, receiveAntennaGain):
        # FSPL(dB) = 20Log(d) + 20log(f) + 92.45
        result = float((20 * math.log(pathDistance, 10)) + (20 * math.log((frequency/1000), 10)) + 92.45)
        return result


    # Received Signal Level
    # [Input]
    # (1) EIRP (dBm)
    # (2)
    # (3)
    # (4)
    def receivedSignalLevel(self, eirp, receiveAntennaGain, freeSpaceLoss, rxCouplingLoss):
        # EIRP+rcv antenna gain – Free space loss - rx coupling loss
        result = float(eirp + receiveAntennaGain - freeSpaceLoss - rxCouplingLoss)
        print("Received Signal Level: ", result)
        return result


    # Flat Fade Margin
    # Input
    # Output
    def flatFadeMargin(self, receivedSignalLevel, rxThreshold):
        # receive signal level - Rx Threshold
        result = float(receivedSignalLevel - rxThreshold)
        print("Flat Fade Margin: ", result)
        return result


    def pathProfileAPI(self, parent, lat=0, lon=0, txh=8, txg=2.14, frq=11000, rlat=0, rlon=0, rxh=2, rxg=2.14, azi=0, pol="v"):
        baseURL = "https://cloudrf.com/API/path"
        parameters = {
            "uid": 32004,
            "key": "50498b81f98ccecde3d98234bb345711e815a8d3",
            "lat": 50.355108,
            "lon": -4.152938,
            "txh": 8,
            "frq": 11000,
            "rxh": 2,
            "dis": "f",
            "txw": 0.1,
            "txg": 2.14,
            "rxg": 2.14,
            "pm": 1,
            "pe": 1,
            "res": 30,
            "rad": 10,
            "out": 2,
            "rxs": -95,
            "ant": 38,
            "azi": 0,
            "bwi": 0.1,
            "ber": 0,
            "clm": 0,
            "cli": 5,
            "cll": 2,
            "fbr": 0,
            "hbw": 0,
            "ked": 0,
            "mod": 3,
            "nam": "TEST",
            "net": "DEVON",
            "out": 2,
            "pol": "v",
            "ter": 4,
            "tlt": 0,
            "vbw": 0,
            "rel": 90,
            "rlat": 50.355108,
            "rlon": -4.12,
            "nf": -101,
            "mat": 0,
            "file": "kmz"
        }
        # update the param values
        parameters["lat"]   = lat
        parameters["lon"]   = lon
        parameters["txh"]   = txh
        parameters["frq"]   = frq
        parameters["rxh"]   = rxh
        parameters["rlat"]  = rlat
        parameters["rlon"]  = rlon
        parameters["txg"]   = txg
        parameters["rxg"]   = rxg
        parameters["azi"]   = azi
        parameters["pol"]   = pol
        ## Default ##
        parameters["dis"]   = "f"
        parameters["txw"]   = 0.1
        parameters["rad"]   = 10
        parameters["pm"]    = 1
        parameters["pe"]    = 1
        parameters["res"]   = 30
        parameters["out"]   = 2
        parameters["rxs"]   = -95
        parameters["ant"]   = 38
        parameters["bwi"]   = 0.1
        parameters["ber"]   = 0
        parameters["clm"]   = 0
        parameters["cli"]   = 5
        parameters["cll"]   = 2
        parameters["fbr"]   = 0
        parameters["hbw"]   = 0
        parameters["ked"]   = 0
        parameters["mod"]   = 3
        parameters["nam"]   = "DRAKES_ISLAND"
        parameters["net"]   = "DEVON"
        parameters["ter"]   = 4
        parameters["tlt"]   = 0
        parameters["vbw"]   = 0
        parameters["rel"]   = 90
        parameters["nf"]    = -101
        parameters["mat"]   = 0
        parameters["file"]  = "kmz"


        response = requests.post("https://cloudrf.com/API/path", params=parameters)
        self.jprint(response.json())

        url = str(response.json()["Chart image"])
        data = urllib.request.urlopen(url).read()
        image = QImage()
        image.loadFromData(data)
        parent.pathDesignWidget3.pathProfileLabel.setPixmap(QPixmap(image))


    def jprint(self, obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)



# Test
# test = PathProfileModules()
# test.EIRP(10, 5, 1, 1)
# test.pathDistanceKm(52.2296756, 21.0122287, 52.406374, 16.9251681)
# test.pathDistanceMiles(52.2296756, 21.0122287, 52.406374, 16.9251681)
# test.freeSpaceLoss(test.pathDistanceKm(52.2296756, 21.0122287, 52.406374, 16.9251681), 25, )
# test.pathProfileAPI(parent, 32.99, -96.74, 328, 2.14, 11000, 32.99, -96.71, 320, 2.14, 0, "v")
