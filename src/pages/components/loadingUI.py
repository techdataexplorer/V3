#
# loading UI .py
# TDX Desktop
# Created by Che Blankenship on 12/17/2021
#
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class LoadingUI(QWidget):

    def __init__(self, page, width, height):
        # self.screenWidth = QDesktopWidget().screenGeometry(-1).width()
        # self.screenHeight = QDesktopWidget().screenGeometry(-1).height()
        # UI class attributes
        self.layer = QWidget(page)
        self.loadGifLabel = QLabel(page)
        self.cancelBtn = QPushButton(page)
        self.initUI(page, width, height)
        # self.hideLoadingUI(parent)

    # have a layer so user cannot click on other UI
    def initUI(self, page, width, height):
        # transparent black layer #
        self.layer.setAutoFillBackground(True)
        self.layer.setStyleSheet("""
            background-color: rgba(1, 1, 1, 0.5);
        """)
        self.layer.setGeometry(0, 0, width, height)
        # loading animation #
        gifWidth = width/10
        gifHeight = height/10
        self.loadGifLabel.setGeometry(int(width/2)-(gifWidth/2), int(height/2)-(gifWidth/2), gifWidth, gifWidth)
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
        self.cancelBtn.setGeometry(int(width/2)-75, int(height/2)+100, 150, 40)
        self.cancelBtn.clicked.connect(lambda: self.cancelThread())
        # self.showLoadingUI(page)
        self.hideLoadingUI()


    def hideLoadingUI(self):
        self.layer.hide()
        self.loadGifLabel.hide()
        self.cancelBtn.hide()


    def showLoadingUI(self):
        self.layer.show()
        self.loadGifLabel.show()
        self.cancelBtn.show()

    def cancelThread(self, threadObject):
        self.hideLoadingUI()
        threadObject.quit()


    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
