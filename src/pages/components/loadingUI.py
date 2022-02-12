#
# loading UI .py
# TDX Desktop
# Created by Che Blankenship on 12/17/2021
#
import sys
import json
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class LoadingUI(QWidget):

    def __init__(self, parent=None):
        super(LoadingUI, self).__init__(parent)
        self.screenWidth = QDesktopWidget().screenGeometry(-1).width()
        self.screenHeight = QDesktopWidget().screenGeometry(-1).height()
        # UI class attributes
        self.layer = QWidget(self)
        self.loadGifLabel = QLabel(self)
        self.cancelBtn = QPushButton(self)
        self.initUI(parent)
        # self.hideLoadingUI(parent)

    # have a layer so user cannot click on other UI
    def initUI(self, parent):
        # transparent black layer #
        self.layer.setAutoFillBackground(True)
        self.layer.setStyleSheet("""
            background-color: rgba(1, 1, 1, 0.5);
        """)
        self.layer.setGeometry(0, 0, self.screenWidth, self.screenHeight)
        # loading animation #
        self.loadGifLabel.setGeometry(int(self.screenWidth/2)-100, int(self.screenWidth/2)-100, 200, 200)
        gifAnimation = QMovie(self.resource_path("loading.gif"))
        self.loadGifLabel.setMovie(gifAnimation)
        gifAnimation.start()
        # cancel button #
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
        self.cancelBtn.clicked.connect(lambda: self.cancelThread(parent))
        self.showLoadingUI(parent)
        self.hideLoadingUI(parent)


    def hideLoadingUI(self, parent):
        self.layer.hide()
        self.loadGifLabel.hide()
        self.cancelBtn.hide()


    def showLoadingUI(self, parent):
        self.layer.show()
        self.loadGifLabel.show()
        self.cancelBtn.show()

    def cancelThread(self, parent):
        self.hideLoadingUI(parent)
        parent.parent.gudPathThread.quit()


    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
