#
# path_profile_modules.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class ScreenTransitionModules:

    def backToHome(self, parent):
        parent.centralWidget.setCurrentIndex(0)
    
    def scriptAOne(self, parent):
        parent.centralWidget.setCurrentIndex(1)

    def scriptATwo(self, parent):
        parent.centralWidget.setCurrentIndex(2)

    def pathsAOne(self, parent):
        parent.centralWidget.setCurrentIndex(3)

    def pathsATwo(self, parent):
        parent.centralWidget.setCurrentIndex(4)
    
    def gudPathAOne(self, parent):
        parent.centralWidget.setCurrentIndex(5)

    def gudPathATwo(self, parent):
        parent.centralWidget.setCurrentIndex(6)
    
    def profileAOne(self, parent):
        parent.centralWidget.setCurrentIndex(7)
    
    def profileATwo(self, parent):
        parent.centralWidget.setCurrentIndex(8)
    
    def kml3daOne(self, parent):
        parent.centralWidget.setCurrentIndex(9)
    
    def kml3daTwo(self, parent):
        parent.centralWidget.setCurrentIndex(10)
    
    def kml3daThree(self, parent):
        parent.centralWidget.setCurrentIndex(11)
    
    def howFarOne(self, parent):
        parent.centralWidget.setCurrentIndex(12)
    
    def howFarTwo(self, parent):
        parent.centralWidget.setCurrentIndex(13)