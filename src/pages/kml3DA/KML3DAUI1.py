#
# pathDesign_ui1.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import os
import csv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Data Model
# from constants.accountData import AccountData
# from constants.firebaseData import FirebaseData
# from constants.pathDesignData import PathDesignData
# from constants.siteData import SiteData

from pages.components.progressUI import ProgressUI
from pages.components.loadingUI import LoadingUI



# "1. Import / Select sites Page"
class KML3DAUI1(QWidget):

    def __init__(self, parent=None):
        super(KML3DAUI1, self).__init__(parent)
        self.screenWidth = QDesktopWidget().screenGeometry(-1).width()
        self.screenHeight = QDesktopWidget().screenGeometry(-1).height()
        self.progressUI = ProgressUI(self).setUp(parent, "KML 3DA", 5, True)
        self.initUI(parent)

    def initUI(self, parent):
        self.mapTableViewUI(parent)


    def mapTableViewUI(self, parent):
        # map/table view wrapper
        self.maptableContainer = QWidget(self)
        self.maptableContainer.setAutoFillBackground(True)
        self.maptableContainer.setStyleSheet("""
            background-color: white;
            border-radius: 5%;
        """)
        # self.maptableContainer.setGeometry(210, 70, 980, 720)
        self.maptableContainer.setGeometry(self.screenWidth*0.05, self.screenHeight*0.10, self.screenWidth*0.90, self.screenHeight*0.8)

        # Open file button
        self.importSitesBtn = QPushButton(self)
        self.importSitesBtn.setText("Click here to import site data")
        self.importSitesBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color:blue;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        self.importSitesBtn.setGeometry(220, 80, 250, 30)
        self.importSitesBtn.clicked.connect(lambda: self.openSheet(parent))

        # or skip and select sites from map view
        self.directionMsgLabel = QLabel(self)
        self.directionMsgLabel.setText("or enter site data manually into the table.")
        self.directionMsgLabel.setStyleSheet("""
            QLabel {
                color : gray;
                font-size: 15px;
            }"""
        )
        self.directionMsgLabel.setGeometry(410, 80, 400, 30)
        self.directionMsgLabel.setAlignment(Qt.AlignCenter)



        # Table view
        self.tablewidget = QTableWidget(self)
        self.tablewidget.setRowCount(10)
        self.tablewidget.setColumnCount(10)
        self.colHeaders = ["Index", "Site1", "Latitude1", "Longitude1", "Site2", "Latitude2", "Longitude2", "TowerHeight1", "TowerHeight2"]
        self.tablewidget.setHorizontalHeaderLabels(self.colHeaders)
        self.tablewidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tablewidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.directionMsgLabel.setStyleSheet("""
            QTableWidget {
                background-color: red;
                border: 3px solid blue;
            }"""
        )
        self.tablewidget.setGeometry(220, 120, 960, 600)


        # select specific sites button
        self.importSitesBtn = QPushButton(self)
        self.importSitesBtn.setText("Next")
        self.importSitesBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color:blue;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        self.importSitesBtn.setGeometry(self.screenWidth*0.8, self.screenHeight*0.83, 150, 40)
        self.importSitesBtn.clicked.connect(lambda: self.moveToKMLGeneratorPage2(parent)) # validate the rows



    def openSheet(self, parent):
        self.fileDialogWidget = QFileDialog(self)
        self.fileName = self.fileDialogWidget.getOpenFileName(self, 'Open file', os.path.expanduser('~') + '/', "Geo-data files (*.csv)")
        self.loadCSV(parent, self.fileName[0])


    # Load the csv file by path
    def loadCSV(self, parent, fileName):
        # Check if path is valid
        if fileName != '':
            parent.kmlGenerator.csvFilePath = fileName # set the file path for later use
            print('check; ', parent.kmlGenerator.csvFilePath)
            with open(fileName, newline='') as csv_file:
                self.tablewidget.setRowCount(0)
                self.tablewidget.setColumnCount(9)
                my_file = csv.reader(csv_file, delimiter=',', quotechar='|')
                for row_data in my_file:
                    row = self.tablewidget.rowCount()
                    self.tablewidget.insertRow(row)
                    if len(row_data) > 5:
                        self.tablewidget.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.tablewidget.setItem(row, column, item)
            self.tablewidget.update()
            # parent.pathDesignData.setFilePath(str(fileName)) # save file path & name
        else:
            print("Invalid file path")



    def moveToHomePage(self, parent):
        parent.central_widget.setCurrentIndex(2)


    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def moveToKMLGeneratorPage2(self, parent):
        # Change page
        parent.screenTransition.kml3daTwo(parent)
