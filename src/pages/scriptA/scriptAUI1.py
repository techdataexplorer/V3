#
# GudPath ui1.py
# TDX Desktop
# Created by Che Blankenship on 12/17/2021
#
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Import modules for this page
from pages.components.progressUI import ProgressUI
from pages.components.loadingUI import LoadingUI

from modules.kizerModules.step2.scriptA import ScriptA
from threads.kizerModuleThread import KizerModuleThread


# "1. Import / Select sites Page"
class ScriptAUI1(QWidget):

    def __init__(self, parent=None):
        super(ScriptAUI1, self).__init__(parent)
        # class attribute UI components (variables used globally in class)
        self.screenWidth = QDesktopWidget().screenGeometry(-1).width()
        self.screenHeight = QDesktopWidget().screenGeometry(-1).height()
        self.scrollVStack = QVBoxLayout(self)
        self.progressUI = ProgressUI(self).setUp(parent, "Script A", 3, True)
        self.scriptAModule = ScriptA()
        self.thread = KizerModuleThread(self, self.scriptAModule, "Script A")
        # 1. Label, textField, button
        self.importDataComponent = {
            "label": QLabel(self),
            "labelText": "Select the input folder for ScriptA:",
            "textField": QLineEdit(self),
            "btn": QPushButton(self),
            "labelRatio": 0.4,
            "textFieldRatio": 0.2
        }
        self.terrainDataComponent = {
            "label": QLabel(self),
            "labelText": "Find terrain folder:",
            "textField": QLineEdit(self),
            "btn": QPushButton(self),
            "labelRatio": 0.4,
            "textFieldRatio": 0.2
        }
        self.componentsOne = [self.importDataComponent, self.terrainDataComponent]
        # 2. Label, dropdown
        self.lulcComponent = {
            "label": QLabel(self),
            "labelText": "Want to add land use & land cover (LULC) data to path profile data?",
            "dropDown": QComboBox(self),
            "options": ["Yes", "No"],
            "labelRatio": 0.4,
            "dropDownRatio": 0.25
        }
        self.terrainOptionComponent = {
            "label": QLabel(self),
            "labelText": "Select terrain database option:",
            "dropDown": QComboBox(self),
            "options": [
                "USGS NATIONAL ELEVATION DATABASE FOR THE US (10 METER NED) [includes Hawaii]",
                "USGS NATIONAL ELEVATION DATABASE FOR THE US (30 METER NED) [Hawaii and Alasaka]",
                "USGS PUERTO RICO AND THE US VIRGIN ISLANDS (30 METER DEM)",
                "SHUTTLE TERRAIN DATA FOR THE US (30 METER SRTM)",
                "SHUTTLE TERRAIN DATA FOR THE WORLD (90 METER SRTM)",
                "USGS GTOPO30 TERRAIN DATABASE FOR THE WORLD (1 KM GRID)",
                "CANADA CDED 1: 50,000 SCALE TERRAIN DATA FILES (10 - 20 METER)",
                "CANADA CDED 1:250,000 SCALE TERRAIN DATA FILES (30 - 90 METER)"
            ],
            "labelRatio": 0.25,
            "dropDownRatio": 0.4
        }
        self.retainOptionComponent = {
            "label": QLabel(self),
            "labelText": "If your input file has an index, do you want to retain it?",
            "dropDown": QComboBox(self),
            "options": ["Yes", "No"],
            "labelRatio": 0.4,
            "dropDownRatio": 0.25
        }

        self.componentsTwo = [self.lulcComponent, self.terrainOptionComponent, self.retainOptionComponent]
        self.initUI(parent)



    # This module will be executed, then load all the sub UIs
    def initUI(self, parent):
        # progressUI(self, parent, "Script A", self.screenWidth, self.screenHeight)
        self.wrapperUI(parent)
        self.configUI(parent)
        self.loadingUI = LoadingUI(self, self.screenWidth, self.screenHeight)



    def wrapperUI(self, parent):
        # parameters view wrapper
        paramsContainer = QWidget(self)
        paramsContainer.setAutoFillBackground(True)
        paramsContainer.setStyleSheet("""
            background-color: white;
            border-radius: 5%;
        """)
        paramsContainer.setGeometry(self.screenWidth*0.05, self.screenHeight*0.10, self.screenWidth*0.90, self.screenHeight*0.8)
        # Message label
        label = QLabel(self)
        label.setText("Configurate the input settings.")
        label.setStyleSheet("""
            QLabel {
                color : black;
                font-size: 20px;
            }"""
        )
        label.setGeometry(self.screenWidth*0.15, self.screenHeight*0.12, 500, 30)
        label.setAlignment(Qt.AlignLeft)
        # go to kml generator btn
        btn = QPushButton(self)
        btn.setText("Next")
        btn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                background-color:blue;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        btn.setGeometry(self.screenWidth*0.8, self.screenHeight*0.83, 150, 40)
        btn.clicked.connect(lambda: self.moveToNextPage(parent))


    # All the configuration UI components get call here
    def configUI(self, parent):
        ### Config UI wrapper ###
        # give a gray color background to the scroll container
        scrollBackground = QWidget(self)
        scrollBackground.setAutoFillBackground(True)
        scrollBackground.setStyleSheet("""
            QWidget {
                background-color: rgba(229, 229, 229, 1);
                border-radius: 5%;
            }"""
        )
        scrollBackground.setGeometry(self.screenWidth*0.15, self.screenHeight*0.2, self.screenWidth*0.7, self.screenHeight*0.6)
        self.scrollVStack.setSpacing(10)
        # Scroll area
        scrollArea = QScrollArea(self)
        scrollArea.setAutoFillBackground(True)
        scrollArea.setStyleSheet("""
            QScrollArea {
                background-color: rgba(225, 225, 225, 0);
                border-radius: 5%;
            }"""
        )
        # add widgets to scroll view
        scrollArea.setWidget(scrollBackground)
        scrollArea.setWidgetResizable(True)
        scrollArea.setGeometry(self.screenWidth*0.15, self.screenHeight*0.2, self.screenWidth*0.7, self.screenHeight*0.6)
        # define UI components
        self.defaultDesignOne(parent, self.componentsOne)
        self.defaultDesignTwo(parent, self.componentsTwo)
        # connect lambdas to the UI components
        self.setLambda(parent, self.componentsOne, self.componentsTwo)
        # append the vertical stack view into a scroll view
        scrollBackground.setLayout(self.scrollVStack)


    def setLambda(self, parent, componentsOne, componentsTwo):
        # connect lambda for componentsOne
        componentsOne[0]["btn"].clicked.connect(lambda: self.getDataSetLocation(parent, componentsOne[0]["textField"]))
        componentsOne[1]["btn"].clicked.connect(lambda: self.setTerrainDataLocation(parent, componentsOne[1]["textField"]))
        # connect lambda for componentsTwo
        componentsTwo[0]["dropDown"].activated.connect(lambda: self.lulcSelected(parent, componentsTwo[0]["dropDown"]))
        componentsTwo[1]["dropDown"].activated.connect(lambda: self.terrainOptionSelected(parent, componentsTwo[1]["dropDown"]))
        componentsTwo[2]["dropDown"].activated.connect(lambda: self.indexRetainSelected(parent, componentsTwo[2]["dropDown"]))




    # Template for {label, textfield, button} UI
    def defaultDesignOne(self, parent, components):
        for component in components:
            # Horizontal stack
            hBoxLayout = QHBoxLayout()
            # label
            component["label"].setText(component["labelText"])
            component["label"].setStyleSheet("""
                QLabel {
                    color : black;
                    font-size: 17px;
                }"""
            )
            component["label"].setAlignment(Qt.AlignLeft)
            component["label"].setFixedWidth(self.screenWidth * component["labelRatio"])
            component["label"].setContentsMargins(10, 15, 10, 10)
            # text field
            component["textField"].setStyleSheet("""
                QLineEdit {
                    font-size: 15px;
                    border-radius: 5%;
                    border: 3px solid lightgray;
                    background-color: white;
                }"""
            )
            component["textField"].setText("-- Path not defined --")
            component["textField"].setAlignment(Qt.AlignLeft)
            component["textField"].setFixedWidth(self.screenWidth * component["textFieldRatio"])
            component["textField"].setReadOnly(True)
            # button
            component["btn"].setText("...")
            component["btn"].setStyleSheet("""
                QPushButton {
                    color: black;
                    font-size: 15px;
                    background-color:lightgray;
                    border: 3px solid blue;
                    border-radius: 5%;
                }"""
            )
            component["btn"].setFixedWidth(self.screenWidth*0.025)
            component["btn"].setFixedHeight(self.screenWidth*0.025)
            # Add to H stack
            hBoxLayout.addWidget(component["label"])
            hBoxLayout.addWidget(component["textField"])
            hBoxLayout.addWidget(component["btn"])
            # Add to V stack
            self.scrollVStack.addLayout(hBoxLayout)


    # Template for {label, drop down} UI
    def defaultDesignTwo(self, parent, components):
        for component in components:
            # Horizontal stack
            hBoxLayout = QHBoxLayout() # remove 'self' due to err
            # label
            component["label"] = QLabel(self)
            component["label"].setText(component["labelText"])
            component["label"].setStyleSheet("""
                QLabel {
                    color : black;
                    font-size: 17px;
                }"""
            )
            component["label"].setAlignment(Qt.AlignLeft)
            component["label"].setFixedWidth(self.screenWidth * component["labelRatio"])
            component["label"].setContentsMargins(10, 15, 10, 10)
            # drop down
            component["dropDown"].addItems(component["options"])
            component["dropDown"].setStyleSheet("""
                QComboBox {
                    color: black;
                    font-size: 13px;
                    border-radius: 5%;
                    border: 3px solid lightgray;
                    background-color: white;
                }"""
            )
            component["dropDown"].setFixedWidth(self.screenWidth * component["dropDownRatio"])
            # Add to H stack
            hBoxLayout.addWidget(component["label"])
            hBoxLayout.addWidget(component["dropDown"])
            # Add to V stack
            self.scrollVStack.addLayout(hBoxLayout)




    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    def getDataSetLocation(self, parent, textField):
        folderDialogWidget = QFileDialog(self)
        path = str(folderDialogWidget.getExistingDirectory(self, "Select the data for ScriptA"))
        if path:
            textField.setText(path)
            self.scriptAModule.setFolderPath(path)
        textField = str(path)
        parent.scriptAUI2.savedLocationTextBox.setText(textField)


    def setTerrainDataLocation(self, parent, textField):
        folderDialogWidget = QFileDialog(self)
        path = str(folderDialogWidget.getExistingDirectory(self, "Select terrain data location"))
        if path:
            textField.setText(path)
            self.scriptAModule.setTerrainDataPath(path)
        # set the path to attribute
        textField = str(path)

    def lulcSelected(self, parent, option):
        choice = str(option.currentText())
        if choice == "Yes":
            self.scriptAModule.setLULC("Y")
        else:
            self.scriptAModule.setLULC("N")


    def terrainOptionSelected(self, parent, option):
        choice = str(option.currentIndex())
        if choice == 0:
            self.scriptAModule.setTerrainOption(1)
        if choice == 1:
            self.scriptAModule.setTerrainOption(2)
        if choice == 2:
            self.scriptAModule.setTerrainOption(3)
        if choice == 3:
            self.scriptAModule.setTerrainOption(4)
        if choice == 4:
            self.scriptAModule.setTerrainOption(5)
        if choice == 5:
            self.scriptAModule.setTerrainOption(6)
        if choice == 6:
            self.scriptAModule.setTerrainOption(7)
        if choice == 7:
            self.scriptAModule.setTerrainOption(8)
        else:
            self.scriptAModule.setTerrainOption(1)


    def indexRetainSelected(self, parent, option):
        choice = str(option.currentIndex())
        if choice == 0:
            self.scriptAModule.setRetainIndex("Y")
        else:
            self.scriptAModule.setRetainIndex("N")



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

    # def cancelPathA(self, parent):
    #     print("Cancel program")
    #     self.thread.quit()


    def moveToNextPage(self, parent):
        print("execute")
        # self.showLoadingUI(parent)
        self.thread.start()
        self.thread.finished.connect(lambda: parent.screenTransition.scriptATwo(parent))
        parent.screenTransition.scriptATwo(parent)









#
