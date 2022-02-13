#
# pathA ui1.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Import modules for this page
from pages.components.progressUI import ProgressUI
from pages.components.loadingUI import LoadingUI

from threads.kizerModuleThread import KizerModuleThread
from modules.kizerModules.step2.pathsA import PathsA


# "1. Import / Select sites Page"
class PathsAUI1(QWidget):

    def __init__(self, parent=None):
        super(PathsAUI1, self).__init__(parent)
        self.screenWidth = QDesktopWidget().screenGeometry(-1).width()
        self.screenHeight = QDesktopWidget().screenGeometry(-1).height()
        self.progressUI = ProgressUI(self).setUp(parent, "Paths A", 1, True)
        self.pathsAModule = PathsA()
        self.thread = KizerModuleThread(self, self.pathsAModule, "Path A")
        self.initUI(parent)


    # This module will be executed, then load all the sub UIs
    def initUI(self, parent):
        # progressUI(self, parent, "Paths A", self.screenWidth, self.screenHeight)
        self.parametersUI(parent)
        self.configUI(parent)
        self.loadingUI = LoadingUI(self, self.screenWidth, self.screenHeight)


    def parametersUI(self, parent):
        # parameters view wrapper
        self.paramsContainer = QWidget(self)
        self.paramsContainer.setAutoFillBackground(True)
        self.paramsContainer.setStyleSheet("""
            background-color: white;
            border-radius: 5%;
        """)
        self.paramsContainer.setGeometry(self.screenWidth*0.05, self.screenHeight*0.10, self.screenWidth*0.90, self.screenHeight*0.8)
        # Message label
        self.directionMsgLabel2 = QLabel(self)
        self.directionMsgLabel2.setText("Configurate the input settings.")
        self.directionMsgLabel2.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 20px;
            }"""
        )
        self.directionMsgLabel2.setGeometry(self.screenWidth*0.15, self.screenHeight*0.12, 500, 30)
        self.directionMsgLabel2.setAlignment(Qt.AlignLeft)
        # go to next page btn
        self.nextPageBtn = QPushButton(self)
        self.nextPageBtn.setText("Next")
        self.nextPageBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color:blue;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        self.nextPageBtn.setGeometry(self.screenWidth*0.8, self.screenHeight*0.83, 150, 40)
        self.nextPageBtn.clicked.connect(lambda: self.moveToNextPage(parent))



    def configUI(self, parent):
        ### Config UI wrapper ###
        self.siteAContainer = QWidget(self)
        self.siteAContainer.setAutoFillBackground(True)
        self.siteAContainer.setStyleSheet("""
            QWidget {
                background-color: rgba(229, 229, 229, 1);
                border-radius: 5%;
            }"""
        )
        self.siteAContainer.setGeometry(self.screenWidth*0.15, self.screenHeight*0.2, self.screenWidth*0.7, self.screenHeight*0.6)
        # Site A vertical stack
        self.configVLayout = QVBoxLayout(self)
        self.configVLayout.setSpacing(10)
        # Scroll area
        self.siteAScroll = QScrollArea(self)
        self.siteAScroll.setAutoFillBackground(True)
        self.siteAScroll.setStyleSheet("""
            QScrollArea {
                background-color: rgba(225, 225, 225, 0);
                border-radius: 5%;
            }"""
        )
        # add widgets to scroll view
        self.siteAScroll.setWidget(self.siteAContainer)
        self.siteAScroll.setWidgetResizable(True)
        self.siteAScroll.setGeometry(self.screenWidth*0.15, self.screenHeight*0.2, self.screenWidth*0.7, self.screenHeight*0.6)
        # define each UI field and append them to the vertical stack view
        self.downloadLocationUI(parent)
        self.importDataSetUI(parent)
        self.lulcUI(parent)                       #
        self.compressionUI(parent)
        self.distanceFractionUI(parent)
        self.maxDataPointsUI(parent)
        # append the vertical stack view into a container view
        self.siteAContainer.setLayout(self.configVLayout)



    # Define result file download location
    def downloadLocationUI(self, parent):
        # Horizontal stack
        self.downloadLocationHLayout = QHBoxLayout() # remove 'self' due to err msg
        # downloadLocation label
        self.downloadLocationLabel = QLabel(self)
        self.downloadLocationLabel.setText("Select the location you want to download the results:")
        self.downloadLocationLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.downloadLocationLabel.setAlignment(Qt.AlignLeft)
        self.downloadLocationLabel.setFixedWidth(self.screenWidth*0.4)
        self.downloadLocationLabel.setContentsMargins(10, 15, 10, 10) # margin
        # downloadLocation result (read only)
        self.downloadLocationTextBox = QLineEdit(self)
        self.downloadLocationTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.downloadLocationTextBox.setText("-- Path not defined --")
        self.downloadLocationTextBox.setAlignment(Qt.AlignLeft)
        self.downloadLocationTextBox.setFixedWidth(self.screenWidth*0.2)
        self.downloadLocationTextBox.setReadOnly(True)
        # Open finder and select location for download
        self.downloadLocationBtn = QPushButton(self)
        self.downloadLocationBtn.setText("...")
        self.downloadLocationBtn.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 15px;
                background-color:lightgray;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        self.downloadLocationBtn.setFixedWidth(self.screenWidth*0.025)
        self.downloadLocationBtn.setFixedHeight(self.screenWidth*0.025)
        self.downloadLocationBtn.clicked.connect(lambda: self.setDownloadLocation(parent))
        # Add to H stack
        self.downloadLocationHLayout.addWidget(self.downloadLocationLabel)
        self.downloadLocationHLayout.addWidget(self.downloadLocationTextBox)
        self.downloadLocationHLayout.addWidget(self.downloadLocationBtn)
        # Add to V stack
        self.configVLayout.addLayout(self.downloadLocationHLayout)


    # Define result file download location
    def importDataSetUI(self, parent):
        # Horizontal stack
        self.importDataSetHLayout = QHBoxLayout() # remove 'self' due to err msg
        # importDataSet label
        self.importDataSetLabel = QLabel(self)
        self.importDataSetLabel.setText("Import the data set folder:")
        self.importDataSetLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.importDataSetLabel.setAlignment(Qt.AlignLeft)
        self.importDataSetLabel.setFixedWidth(self.screenWidth*0.4)
        self.importDataSetLabel.setContentsMargins(10, 15, 10, 10) # margin
        # importDataSet result (read only)
        self.importDataSetTextBox = QLineEdit(self)
        self.importDataSetTextBox.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.importDataSetTextBox.setText("-- No data set selected --")
        self.importDataSetTextBox.setAlignment(Qt.AlignLeft)
        self.importDataSetTextBox.setFixedWidth(self.screenWidth*0.2)
        self.importDataSetTextBox.setReadOnly(True)
        # Open finder and select location for download
        self.importDataSetBtn = QPushButton(self)
        self.importDataSetBtn.setText("...")
        self.importDataSetBtn.setStyleSheet("""
            QPushButton {
                color: black;
                font-size: 15px;
                background-color:lightgray;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        self.importDataSetBtn.setFixedWidth(self.screenWidth*0.025)
        self.importDataSetBtn.setFixedHeight(self.screenWidth*0.025)
        self.importDataSetBtn.clicked.connect(lambda: self.getDataSetLocation(parent))
        # Add to H stack
        self.importDataSetHLayout.addWidget(self.importDataSetLabel)
        self.importDataSetHLayout.addWidget(self.importDataSetTextBox)
        self.importDataSetHLayout.addWidget(self.importDataSetBtn)
        # Add to V stack
        self.configVLayout.addLayout(self.importDataSetHLayout)


    def lulcUI(self, parent):
        # Horizontal stack
        self.lulcHLayout = QHBoxLayout() # remove 'self' due to err msg
        self.lulcLabel = QLabel(self)
        self.lulcLabel.setText("Does the profiles contain use & land cover data(Yes or No):")
        self.lulcLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.lulcLabel.setAlignment(Qt.AlignLeft)
        self.lulcLabel.setFixedWidth(self.screenWidth*0.4)
        self.lulcLabel.setContentsMargins(10, 15, 10, 10) # margin
        # drop down
        self.lulcOptionList = QComboBox(self)
        self.lulcOptionList.addItems(["Yes", "No"])
        self.lulcOptionList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.lulcOptionList.activated.connect(lambda: self.lulcSelected(parent))
        # self.lulcOptionList.setGeometry(530, 140, 150, 30)
        self.lulcOptionList.setFixedWidth(self.screenWidth*0.25)
        # Add to H stack
        self.lulcHLayout.addWidget(self.lulcLabel)
        self.lulcHLayout.addWidget(self.lulcOptionList)
        # Add to V stack
        self.configVLayout.addLayout(self.lulcHLayout)


    def compressionUI(self, parent):
        # Horizontal stack
        self.compressionHLayout = QHBoxLayout() # remove 'self' due to err msg
        self.compressionLabel = QLabel(self)
        self.compressionLabel.setText("Select compression choices:")
        self.compressionLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.compressionLabel.setAlignment(Qt.AlignLeft)
        self.compressionLabel.setFixedWidth(self.screenWidth*0.4)
        self.compressionLabel.setContentsMargins(10, 15, 10, 10) # margin
        # drop down
        self.compressionOptionList = QComboBox(self)
        self.compressionOptions = [
            "No compression",
            "Compress each path to a normal incremental distance",
            "Compress each path to a normal number of samples"
        ]
        self.compressionOptionList.addItems(self.compressionOptions)
        self.compressionOptionList.setStyleSheet("""
            QComboBox {
                color: black;
                font-size: 13px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        self.compressionOptionList.activated.connect(lambda: self.compressionSelected(parent))
        self.compressionOptionList.setFixedWidth(self.screenWidth*0.25)
        # Add to H stack
        self.compressionHLayout.addWidget(self.compressionLabel)
        self.compressionHLayout.addWidget(self.compressionOptionList)
        # Add to V stack
        self.configVLayout.addLayout(self.compressionHLayout)

    # Enter approximate fraction of a mile or kilometer for path increments
    def distanceFractionUI(self, parent):
        # Horizontal stack
        self.distanceFractionHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A lng label
        self.distanceFractionLabel = QLabel(self)
        self.distanceFractionLabel.setText("Enter approximate fraction of a mile or kilometer for path increments:")
        self.distanceFractionLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.distanceFractionLabel.setAlignment(Qt.AlignLeft)
        self.distanceFractionLabel.setFixedWidth(self.screenWidth*0.5)
        self.distanceFractionLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B latitude text input
        self.distanceFractionTextBox = QDoubleSpinBox(self)
        self.distanceFractionTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        # self.distanceFractionTextBox.setGeometry(530, 140, 200, 30)
        self.distanceFractionTextBox.setFixedWidth(self.screenWidth*0.15)
        self.distanceFractionTextBox.setRange(1, 100)
        self.distanceFractionTextBox.setDecimals(1)
        # Add to H stack
        self.distanceFractionHLayout.addWidget(self.distanceFractionLabel)
        self.distanceFractionHLayout.addWidget(self.distanceFractionTextBox)
        # Add to V stack
        self.configVLayout.addLayout(self.distanceFractionHLayout)
        # hide
        self.distanceFractionLabel.setVisible(False)
        self.distanceFractionTextBox.setVisible(False)


    # The final profile number of points will be between N and 2N
    def maxDataPointsUI(self, parent):
        # Horizontal stack
        self.maxDataPointsHLayout = QHBoxLayout() # remove 'self' due to err msg
        # Site A lng label
        self.maxDataPointsLabel = QLabel(self)
        self.maxDataPointsLabel.setText("Enter approximate maximum number of path profile data points (N). \n The final profile number of points will be between N and 2N:")
        self.maxDataPointsLabel.setWordWrap(True)
        self.maxDataPointsLabel.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        self.maxDataPointsLabel.setAlignment(Qt.AlignLeft)
        self.maxDataPointsLabel.setFixedWidth(self.screenWidth*0.5)
        self.maxDataPointsLabel.setContentsMargins(10, 15, 10, 10) # margin
        # site B latitude text input
        self.maxDataPointsTextBox = QDoubleSpinBox(self)
        self.maxDataPointsTextBox.setStyleSheet("""
            QDoubleSpinBox {
                font-size: 15px;
                border-radius: 5%;
                border: 3px solid lightgray;
                background-color: white;
            }"""
        )
        # self.maxDataPointsTextBox.setGeometry(530, 140, 200, 30)
        self.maxDataPointsTextBox.setFixedWidth(self.screenWidth*0.15)
        self.maxDataPointsTextBox.setRange(1, 100)
        self.maxDataPointsTextBox.setDecimals(1)
        # Add to H stack
        self.maxDataPointsHLayout.addWidget(self.maxDataPointsLabel)
        self.maxDataPointsHLayout.addWidget(self.maxDataPointsTextBox)
        # Add to V stack
        self.configVLayout.addLayout(self.maxDataPointsHLayout)
        # hide
        self.maxDataPointsLabel.setVisible(False)
        self.maxDataPointsTextBox.setVisible(False)


    # have a layer so user cannot click on other UI
    # def loadingUI(self, parent):
    #     # transparent black layer #
    #     self.layer = QWidget(self)
    #     self.layer.setAutoFillBackground(True)
    #     self.layer.setStyleSheet("""
    #         background-color: rgba(1, 1, 1, 0.5);
    #     """)
    #     self.layer.setGeometry(0, 0, self.screenWidth, self.screenHeight)
    #     # loading animation #
    #     self.loadGifLabel = QLabel(self)
    #     self.loadGifLabel.setGeometry(int(self.screenWidth/2)-100, int(self.screenWidth/2)-100, 200, 200)
    #     # self.loadGif = QMovie("./img/loading.gif")
    #     self.loadGif = QMovie(self.resource_path("loading.gif"))
    #     self.loadGifLabel.setMovie(self.loadGif)
    #     self.loadGif.start()
    #     # cancel button #
    #     self.cancelBtn = QPushButton(self)
    #     self.cancelBtn.setText("Cancel")
    #     self.cancelBtn.setStyleSheet("""
    #         QPushButton {
    #             color: white;
    #             font-size: 15px;
    #             text-decoration: underline;
    #             background-color: rgba(0, 0, 0, 0)
    #         }"""
    #     )
    #     self.cancelBtn.setGeometry(int(self.screenWidth/2)-75, int(self.screenHeight/2)+100, 150, 40)
    #     self.cancelBtn.clicked.connect(lambda: self.cancelPathA(parent))

    # def hideLoadingUI(self, parent):
    #     self.layer.hide()
    #     self.loadGifLabel.hide()
    #     self.cancelBtn.hide()

    # def showLoadingUI(self, parent):
    #     self.layer.show()
    #     self.loadGifLabel.show()
    #     self.cancelBtn.show()


    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    def setDownloadLocation(self, parent):
        fileDialogWidget = QFileDialog(self)
        path = str(fileDialogWidget.getExistingDirectory(self, "Select location to save the results"))
        if path:
            self.downloadLocationTextBox.setText(path)
            parent.pathsAUI2.savedLocationTextBox.setText(path)
        # set the path to attribute
        # parent.kmlGenerator.downloadPath = path

    def getDataSetLocation(self, parent):
        self.fileDialogWidget = QFileDialog(self)
        path = str(self.fileDialogWidget.getExistingDirectory(self, "Select the data set for Paths A"))
        if path:
            self.importDataSetTextBox.setText(path)
            self.pathsAModule.FolderPath = str(path)
            print("Check data set path >> ", path)
        self.pathsAModule.setFolderPath(str(path))
        # self.pathsAModule.FolderPath = str(path)


    def lulcSelected(self, parent):
        choice = str(self.lulcOptionList.currentText())
        if choice == "Yes":
            self.pathsAModule.setLULC("Y")
            # self.pathsAModule.LandUse = "Y"
        else:
            self.pathsAModule.setLULC("N")
            # self.pathsAModule.LandUse = "N"

    def compressionSelected(self, parent):
        choice = int(self.compressionOptionList.currentIndex())
        if choice == 0:
            self.pathsAModule.setCompressionOption(1)
            # self.pathsAModule.CompChoice = 1
            # hide additional option and reset
            self.maxDataPointsLabel.setVisible(False)
            self.maxDataPointsTextBox.setVisible(False)
            self.maxDataPointsTextBox.setValue(1)
            self.distanceFractionLabel.setVisible(False)
            self.distanceFractionTextBox.setVisible(False)
        if choice == 1:
            self.pathsAModule.setCompressionOption(2)
            # self.pathsAModule.CompChoice = 2
            # show additional option
            self.distanceFractionLabel.setVisible(True)
            self.distanceFractionTextBox.setVisible(True)
            # hide additional option and reset
            self.maxDataPointsLabel.setVisible(False)
            self.maxDataPointsTextBox.setVisible(False)
            self.maxDataPointsTextBox.setValue(1)
        if choice == 2:
            self.pathsAModule.setCompressionOption(3)
            # self.pathsAModule.CompChoice = 3
            # show additional option
            self.maxDataPointsLabel.setVisible(True)
            self.maxDataPointsTextBox.setVisible(True)
            self.distanceFractionLabel.setVisible(False)
            self.distanceFractionTextBox.setVisible(False)
        print("compression option selected >> ", str(self.pathsAModule.CompChoice))

    # def cancelPathA(self, parent):
    #     print("Cancel program")
    #     parent.pathsAThread.quit()

    def moveToNextPage(self, parent):
        print("execute")
        self.loadingUI.showLoadingUI()
        self.pathsAModule.setMaxDataPoints(int(float(self.maxDataPointsTextBox.text())))
        self.pathsAModule.setDistanceFraction(int(float(self.distanceFractionTextBox.text())))
        self.thread.start()
        self.thread.finished.connect(lambda: parent.screenTransition.pathsATwo(parent))
        # self.showLoadingUI(parent)
        # # set the additional attribute values
        # self.pathsAModule.setMaxDataPoints(int(float(self.maxDataPointsTextBox.text())))
        # # self.pathsAModule.MaxDataPointsN = int(float(self.maxDataPointsTextBox.text()))
        # self.pathsAModule.setDistanceFraction(int(float(self.distanceFractionTextBox.text())))
        # # self.pathsAModule.DistanceFraction = int(float(self.distanceFractionTextBox.text()))
        # parent.pathsAThread.start()
        # parent.pathsAThread.finished.connect(lambda: parent.screenTransitionModules.moveToPathAPage2(parent))
        # parent.screenTransition.pathsATwo(parent)
