#
# progress ui.py
# TDX Desktop
# Created by Che Blankenship on 11/15/2021
#
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from modules.screenTransitionModules import ScreenTransitionModules


# progress bar UI
class ProgressUI(QWidget):
    def __init__(self, parent=None):
        super(ProgressUI, self).__init__(parent)
        self.screenWidth = QDesktopWidget().screenGeometry(-1).width()
        self.screenHeight = QDesktopWidget().screenGeometry(-1).height()
        self.screenTransition = ScreenTransitionModules()
        # components
        self.projectNameTag = QPushButton(self)
        self.backHomeButton = QPushButton(self)
        self.navHome = QPushButton(self)
        self.navNetworkConfig = QPushButton(self)
        self.navAccount = QPushButton(self)
        self.networkConfigList = QWidget(self)

    
    def setUp(self, parent, moduleName, index, backBtn):
        # Back to home button
        if backBtn:
            # Tag 
            self.projectNameTag.setText(moduleName)
            self.projectNameTag.setGeometry(self.screenWidth*0.1, 10, self.screenWidth*0.09, 50)
            self.projectNameTag.setEnabled(False)
            colors = [
                """
                QPushButton {
                    color: black;
                    border-radius: 5%;
                    font-size: 17px;
                    background-color: red;
                }
                """,
                """
                QPushButton {
                    color: white;
                    border-radius: 5%;
                    font-size: 17px;
                    background-color: rgba(22, 58, 39, 1);
                }""",
                """
                QPushButton {
                    color: white;
                    border-radius: 5%;
                    font-size: 17px;
                    background-color: rgba(20, 91, 24, 1);
                }""",
                """
                QPushButton {
                    color: white;
                    border-radius: 5%;
                    font-size: 17px;
                    background-color: rgba(91, 20, 53, 1);
                }""",
                """
                QPushButton {
                    color: white;
                    border-radius: 5%;
                    font-size: 17px;
                    background-color: rgba(20, 53, 91, 1);
                }""",
                """
                QPushButton {
                    color: white;
                    border-radius: 5%;
                    font-size: 17px;
                    background-color: rgba(91, 59, 20, 1);
                }"""
            ]
            self.projectNameTag.setStyleSheet(colors[index])

            # Back to home button
            self.backHomeButton.setText(" <- ")
            self.backHomeButton.setGeometry(self.screenWidth*0.05, 10, 50, 50)
            self.backHomeButton.setStyleSheet("""
                QPushButton {
                    color: white;
                    border-radius: 25%;
                    font-size: 17px;
                    background-color: gray;
                }
                """
            )
            self.backHomeButton.clicked.connect(lambda: self.screenTransition.backToHome(parent))
        else:
            self.backHomeButton.hide()
            self.projectNameTag.hide()


        # Nav bar components
        # Account
        self.navAccount.setText("Account")
        self.navAccount.setGeometry(self.screenWidth*0.85, 10, self.screenWidth*0.09, 50)
        self.navAccount.setStyleSheet("""
            QPushButton {
                color: white;
                border-top-right-radius: 5%;
                border-bottom-right-radius: 5%;
                font-size: 17px;
                background-color: black;
            }"""
        )
        
        # Home
        self.navHome.setText("Home")
        self.navHome.setGeometry(self.screenWidth*0.76, 10, self.screenWidth*0.09, 50)
        self.navHome.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 17px;
                background-color: black;
            }"""
        )
        self.navHome.clicked.connect(lambda: self.screenTransition.backToHome(parent))

        # Network config
        self.navNetworkConfig.setText("Network Configuration")
        self.navNetworkConfig.setGeometry(self.screenWidth*0.62, 10, self.screenWidth*0.14, 50)
        self.navNetworkConfig.setStyleSheet("""
            QPushButton {
                color: white;
                border-top-left-radius: 5%;
                border-bottom-left-radius: 5%;
                font-size: 17px;
                background-color: black;
            }"""
        )
