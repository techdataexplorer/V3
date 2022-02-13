#
# GudPath ui1.py
# TDX Desktop
# Created by Che Blankenship on 12/17/2021
#
import sys
import os
import csv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Import modules for this page
from pages.components.progressUI import ProgressUI
from pages.components.loadingUI import LoadingUI

# Import module & thread for gud path
from modules.kizerModules.step2.gudPathA import GudPath
from threads.kizerModuleThread import KizerModuleThread


# "1. Import / Select sites Page"
class GudPathUI1(QWidget):

    def __init__(self, parent=None):
        super(GudPathUI1, self).__init__(parent)
        # class attribute UI components (variables used globally in class)
        self.screenWidth = QDesktopWidget().screenGeometry(-1).width()
        self.screenHeight = QDesktopWidget().screenGeometry(-1).height()
        self.progressUI = ProgressUI(self).setUp(parent, "Gud Path", 0, True)
        self.gudPathModule = GudPath()
        self.thread = KizerModuleThread(self, self.gudPathModule, "Gud Path")
        self.scrollVStack = QVBoxLayout(self)
        # 1. Label, textField, button
        self.downloadComponent = {
            "label": QLabel(self),
            "labelText": "Select the location you want to download the results:",
            "textField": QLineEdit(self),
            "btn": QPushButton(self)
        }
        self.importDataComponent = {
            "label": QLabel(self),
            "labelText": "Select the input folder for Good path:",
            "textField": QLineEdit(self),
            "btn": QPushButton(self)
        }
        self.componentsOne = [self.downloadComponent, self.importDataComponent]
        # 2. Label, dropdown
        self.lulcComponent = {
            "label": QLabel(self),
            "labelText": "Does the profiles contain use & land cover data(Yes or No):",
            "dropDown": QComboBox(self),
            "options": ["Yes", "No"]
        }
        self.obstractionComponent = {
            "label": QLabel(self),
            "labelText": "Select obstraction option:",
            "dropDown": QComboBox(self),
            "options": ["Use path profile obstraction with heights for evals", "Use worst case obstraction height for EACH path sample point"]
        }
        self.optimizeComponent = {
            "label": QLabel(self),
            "labelText": "After evaluating the paths, optimize the good paths:",
            "dropDown": QComboBox(self),
            "options": ["Yes", "No"]
        }

        self.componentsTwo = [self.lulcComponent, self.obstractionComponent, self.optimizeComponent]

        # initialize UI components in specific order
        self.initUI(parent)




    # This module will be executed, then load all the sub UIs
    def initUI(self, parent):
        # progressUI(self, parent, "Gud Path", self.screenWidth, self.screenHeight)
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
        # next page btn
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
        componentsOne[0]["btn"].clicked.connect(lambda: self.setDownloadLocation(parent, componentsOne[0]["textField"]))
        componentsOne[1]["btn"].clicked.connect(lambda: self.getDataSetLocation(parent, componentsOne[1]["textField"]))
        # connect lambda for componentsTwo
        componentsTwo[0]["dropDown"].activated.connect(lambda: self.lulcSelected(parent, componentsTwo[0]["dropDown"]))
        componentsTwo[1]["dropDown"].activated.connect(lambda: self.obstractionSelected(parent, componentsTwo[1]["dropDown"]))
        componentsTwo[2]["dropDown"].activated.connect(lambda: self.optimizationSelected(parent, componentsTwo[2]["dropDown"]))




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
            component["label"].setFixedWidth(self.screenWidth*0.4)
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
            component["textField"].setFixedWidth(self.screenWidth*0.2)
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
            component["label"].setFixedWidth(self.screenWidth*0.4)
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
            component["dropDown"].setFixedWidth(self.screenWidth*0.25)
            # Add to H stack
            hBoxLayout.addWidget(component["label"])
            hBoxLayout.addWidget(component["dropDown"])
            # Add to V stack
            self.scrollVStack.addLayout(hBoxLayout)




    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    def setDownloadLocation(self, parent, textField):
        fileDialogWidget = QFileDialog(self)
        path = str(fileDialogWidget.getExistingDirectory(self, "Select location to save the results"))
        if path:
            textField.setText(path)
        # set the path to attribute
        textField = str(path)

    def getDataSetLocation(self, parent, textField):
        self.fileDialogWidget = QFileDialog(self)
        path = str(self.fileDialogWidget.getExistingDirectory(self, "Select the data for Gud Path"))
        if path:
            textField.setText(path)
            self.gudPathModule.setFolderPath(path)
            parent.gudPathUI2.savedLocationTextBox.setText(textField)
        textField = str(path)


    def lulcSelected(self, parent, option):
        choice = str(option.currentText())
        if choice == "Yes":
            self.gudPathModule.setLULC("Y")
        else:
            self.gudPathModule.setLULC("N")


    def obstractionSelected(self, parent, option):
        choice = str(option.currentIndex())
        if choice == 0:
            self.gudPathModule.setPathEval(1)
        else:
            self.gudPathModule.setPathEval(2)

    def optimizationSelected(self, parent, option):
        choice = str(option.currentIndex())
        if choice == 0:
            self.gudPathModule.setOptimizePathsOption("y")
        else:
            self.gudPathModule.setOptimizePathsOption("n")



    def moveToNextPage(self, parent):
        print("execute")
        self.loadingUI.showLoadingUI()
        self.thread.start()
        self.thread.finished.connect(lambda: parent.screenTransition.gudPathATwo(parent))
        # parent.KizerModuleThread.start()
        # parent.KizerModuleThread.finished.connect(lambda: parent.screenTransitionModules.moveToPathAPage2(parent))
        # parent.screenTransition.gudPathATwo(parent)









#
