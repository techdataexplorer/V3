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
import sip
# import folium
import pyrebase
import dataclasses



@dataclasses.dataclass
class SiteData:
    # Site data
    siteName: str
    latitude: int
    longitude: int
    towerHeight: int
    antennaHeight: int

    def setSiteName(self, data):
        self.siteName = str(data)
