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


# "1. Import / Select sites Page"
class ProfileAUI1(QWidget):

    def __init__(self, parent=None):
        super(ProfileAUI1, self).__init__(parent)
        # class attribute UI components (variables used globally in class)
        self.screenWidth = QDesktopWidget().screenGeometry(-1).width()
        self.screenHeight = QDesktopWidget().screenGeometry(-1).height()
        self.progressUI = ProgressUI(self).setUp(parent, "Profile A", 4, True)
        self.scrollVStack = QVBoxLayout(self)
        # 1. Label, textField, button
        self.importDataComponent = {
            "label": QLabel(self),
            "labelText": "Select the input folder for Profile A:",
            "textField": QLineEdit(self),
            "btn": QPushButton(self),
            "labelRatio": 0.4,
            "textFieldRatio": 0.2
        }
        self.componentsOne = [self.importDataComponent]
        #
        self.initUI(parent)
        # loading UI
        self.loadingUI(parent)
        self.hideLoadingUI(parent)


    # This module will be executed, then load all the sub UIs
    def initUI(self, parent):
        self.wrapperUI(parent)
        self.configUI(parent)


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
        # connect lambdas to the UI components
        self.setLambda(parent, self.componentsOne)
        # append the vertical stack view into a scroll view
        scrollBackground.setLayout(self.scrollVStack)


    def setLambda(self, parent, componentsOne):
        # connect lambda for componentsOne
        componentsOne[0]["btn"].clicked.connect(lambda: self.getDataSetLocation(parent, componentsOne[0]["textField"]))


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


    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    def getDataSetLocation(self, parent, textField):
        folderDialogWidget = QFileDialog(self)
        path = str(folderDialogWidget.getExistingDirectory(self, "Select the data for profileA"))
        if path:
            textField.setText(path)
            parent.profileAGenerator.setFolderPath(path)
        textField = str(path)


    # have a layer so user cannot click on other UI
    def loadingUI(self, parent):
        # transparent black layer #
        self.layer = QWidget(self)
        self.layer.setAutoFillBackground(True)
        self.layer.setStyleSheet("""
            background-color: rgba(1, 1, 1, 0.5);
        """)
        self.layer.setGeometry(0, 0, self.screenWidth, self.screenHeight)
        # loading animation #
        self.loadGifLabel = QLabel(self)
        self.loadGifLabel.setGeometry(int(self.screenWidth/2)-100, int(self.screenWidth/2)-100, 200, 200)
        # self.loadGif = QMovie("./img/loading.gif")
        self.loadGif = QMovie(self.resource_path("loading.gif"))
        self.loadGifLabel.setMovie(self.loadGif)
        self.loadGif.start()
        # cancel button #
        self.cancelBtn = QPushButton(self)
        self.cancelBtn.setText("Cancel")
        self.cancelBtn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 15px;
                text-decoration: underline;
                background-color: rgba(0, 0, 0, 0)
            }"""
        )
        self.cancelBtn.setGeometry(int(self.screenWidth/2)-75, int(self.screenHeight/2)+100, 150, 40)
        self.cancelBtn.clicked.connect(lambda: self.cancelPathA(parent))


    def hideLoadingUI(self, parent):
        self.layer.hide()
        self.loadGifLabel.hide()
        self.cancelBtn.hide()

    def showLoadingUI(self, parent):
        self.layer.show()
        self.loadGifLabel.show()
        self.cancelBtn.show()

    def cancelPathA(self, parent):
        print("Cancel program")
        parent.profileAThread.quit()


    def moveToNextPage(self, parent):
        print("execute")
        # self.showLoadingUI(parent)
        # parent.profileAThread.start()
        # parent.profileAThread.finished.connect(lambda: parent.screenTransitionModules.moveToPathAPage2(parent))
        parent.screenTransition.profileATwo(parent)









#
