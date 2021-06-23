#
# accountData.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import json
import io
import os
import csv
import sip
import folium
import dataclasses


@dataclasses.dataclass
class AccountData:
    orgName: str
    fullName: str
    email: str
    passwd: str
    address: str


    def printAccountData(self):
        print("Org name : ", str(self.orgName))
        print("full name: ", str(self.fullName))
        print("email    : ", str(self.email))
        print("passwd   : ", str(self.passwd))
        print("address  : ", str(self.address))

    def setOrgName(self, data):
        self.orgName = str(data)
        print

    def setFullName(self, data):
        self.fullName = str(data)

    def setEmail(self, data):
        self.email = str(data)

    def setPasswd(self, data):
        self.passwd = str(data)

    def setAddress(self, data):
        self.address = str(data)

    def updateOrgName(self, data):
        if str(self.orgName) != str(data):
            self.orgName = str(data)
        else:
            print("Already set to the org name you tried to update.")

    def updateFullName(self, data):
        if str(self.orgName) != str(data):
            self.orgName = str(data)
        else:
            print("Already set to the full name you tried to update.")

    def updateEmail(self, data):
        if str(self.orgName) != str(data):
            self.orgName = str(data)
        else:
            print("Already set to the email you tried to update.")

    def updatePasswd(self, data):
        if str(self.orgName) != str(data):
            self.orgName = str(data)
        else:
            print("Already set to the passwd you tried to update.")

    def updateAddress(self, data):
        if str(self.orgName) != str(data):
            self.orgName = str(data)
        else:
            print("Already set to the address you tried to update.")

    def getOrgName(self):
        return str(self.orgName)

    def getFullName(self):
        return str(self.fullName)

    def getEmail(self):
        return str(self.email)

    def getAddress(self):
        return str(self.address)

    def getPasswd(self):
        return str(self.passwd)
