#
# pathA ui1.py
# TDX Desktop
# Created by Che Blankenship on 06/04/2021
#
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Import modules for this page
from modules.screenTransitionModules import ScreenTransitionModules
from pages.components.progressUI import ProgressUI


# "1. Import / Select sites Page"
class HomeUI(QWidget):

    def __init__(self, parent=None):
        super(HomeUI, self).__init__(parent)
        self.screenWidth = QDesktopWidget().screenGeometry(-1).width()
        self.screenHeight = QDesktopWidget().screenGeometry(-1).height()
        self.progressUI = ProgressUI(self).setUp(parent, "Home", 1, False)
        self.scrollVStack = QVBoxLayout()
        self.screenTransition = ScreenTransitionModules()
        # step 1 cards
        self.howFarCard = {
            "title": QLabel(self),
            "titleText": "How Far",
            "description": QLabel(self),
            "descriptionText": "It determines each paths fade margin and calculates expected two-way availability for various potential path lengths.",
            "btn": QPushButton(self)
        }
        self.step1Components = [self.howFarCard]
        # step 2 cards
        self.allPathACard = {
            "title": QLabel(self),
            "titleText": "All Path",
            "description": QLabel(self),
            "descriptionText": "Create 'Spider web' of possible paths.",
            "btn": QPushButton(self)
        }
        self.scriptACard = {
            "title": QLabel(self),
            "titleText": "Script A",
            "description": QLabel(self),
            "descriptionText": "Script A uses site data (csv file) to create GMS scripts for global mapper.",
            "btn": QPushButton(self)
        }
        self.pathACard = {
            "title": QLabel(self),
            "titleText": "Paths A",
            "description": QLabel(self),
            "descriptionText": "Process the path profiles.",
            "btn": QPushButton(self)
        }
        self.gudPathACard = {
            "title": QLabel(self),
            "titleText": "Good Path",
            "description": QLabel(self),
            "descriptionText": "Evaluate and optimize the paths.",
            "btn": QPushButton(self)
        }
        self.profilACard = {
            "title": QLabel(self),
            "titleText": "Profile A",
            "description": QLabel(self),
            "descriptionText": "Generate scripts used to create path profile pictures.",
            "btn": QPushButton(self)
        }
        self.kml3DACard = {
            "title": QLabel(self),
            "titleText": "KML 3DA",
            "description": QLabel(self),
            "descriptionText": "Generate KML file to represent the spider web on Google Earth.",
            "btn": QPushButton(self)
        }

        self.step2Components = [self.allPathACard, self.scriptACard, self.pathACard, self.gudPathACard, self.profilACard, self.kml3DACard]
        
        # step 3 cards
        self.profileScriptCard = {
            "title": QLabel(self),
            "titleText": "Profile Script",
            "description": QLabel(self),
            "descriptionText": "Create GMS script to generate terrain profiles for each path.",
            "btn": QPushButton(self)
        }
        self.roughnessCard = {
            "title": QLabel(self),
            "titleText": "Roughness",
            "description": QLabel(self),
            "descriptionText": "Analys the roughness.",
            "btn": QPushButton(self)
        }
        self.parameterCard = {
            "title": QLabel(self),
            "titleText": "Parameter",
            "description": QLabel(self),
            "descriptionText": "Perform the path availability calculations.",
            "btn": QPushButton(self)
        }
        self.pathDataPassCard = {
            "title": QLabel(self),
            "titleText": "Path Data Pass",
            "description": QLabel(self),
            "descriptionText": "Create basic template for the paths using text editor / excel.",
            "btn": QPushButton(self)
        }
        self.performanceCard = {
            "title": QLabel(self),
            "titleText": "Performance A",
            "description": QLabel(self),
            "descriptionText": "Perform path availability calculations using the various methologies.",
            "btn": QPushButton(self)
        }
        self.reportCard = {
            "title": QLabel(self),
            "titleText": "Report A",
            "description": QLabel(self),
            "descriptionText": "Generate final report.",
            "btn": QPushButton(self)
        }


        self.step3Components = [self.profileScriptCard, self.roughnessCard, self.parameterCard, self.pathDataPassCard, self.performanceCard, self.reportCard]


        self.initUI(parent)


    # This module will be executed, then load all the sub UIs
    def initUI(self, parent):
        self.scrollAreaUI(parent)
        self.defaultDesignStep1(parent, self.step1Components)
        self.defaultDesignStep2and3(parent, self.step2Components, "Step 2")
        self.defaultDesignStep2and3(parent, self.step3Components, "Step 3")
        self.setLambda(parent, self.step1Components, self.step2Components, self.step3Components)


    # Configure area to be scollable
    def scrollAreaUI(self, parent):
        # give a gray color background to the scroll container
        scrollBackground = QWidget(self)
        scrollBackground.setAutoFillBackground(True)
        scrollBackground.setStyleSheet("""
            QWidget {
                background-color: rgba(229, 229, 229, 1);
                border-radius: 5%;
            }"""
        )
        scrollBackground.setGeometry(self.screenWidth*0.05, self.screenHeight*0.1, self.screenWidth*0.9, self.screenHeight*0.8)
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
        scrollArea.setGeometry(self.screenWidth*0.05, self.screenHeight*0.1, self.screenWidth*0.9, self.screenHeight*0.8)
        # append the vertical stack view into a scroll view
        scrollBackground.setLayout(self.scrollVStack)

    
    def defaultDesignStep1(self, parent, components):
        # add section label
        sectionLabel = QLabel()
        sectionLabel.setText("Step 1")
        sectionLabel.setStyleSheet("""
                QLabel {
                    color : black;
                    font-size: 25px;
                }"""
        )
        sectionLabel.setAlignment(Qt.AlignCenter)
        sectionLabel.setFixedWidth(self.screenWidth*0.3)
        sectionLabel.setFixedWidth(self.screenWidth*0.2)
        sectionLabel.setContentsMargins(0, 80, 0, 80) # margin

        tempHLayout = QHBoxLayout()
        tempHLayout.addWidget(sectionLabel, alignment=Qt.AlignCenter)
        self.scrollVStack.addLayout(tempHLayout)

        # add all the cards
        # card component
        card = QWidget()
        card.setFixedWidth(self.screenWidth*0.25)
        card.setFixedHeight(self.screenWidth*0.2)
        card.setStyleSheet("""
            QWidget {
                color : black;
                background-color: white;
            }"""
        )
        # vertical stack for sub components (title, description, button)
        vBoxLayout = QVBoxLayout(card)
        # title
        components[0]["title"].setText(components[0]["titleText"])
        components[0]["title"].setStyleSheet("""
            QLabel {
                color : black;
                font-size: 25px;
                text-decoration: underline;
            }"""
        )
        components[0]["title"].setAlignment(Qt.AlignCenter)
        components[0]["title"].setFixedWidth(self.screenWidth*0.2)
        # description
        components[0]["description"].setText(components[0]["descriptionText"])
        components[0]["description"].setStyleSheet("""
            QLabel {
                color : black;
                font-size: 17px;
            }"""
        )
        components[0]["description"].setAlignment(Qt.AlignCenter)
        components[0]["description"].setFixedWidth(self.screenWidth*0.2)
        components[0]["description"].setFixedHeight(self.screenWidth*0.08)
        components[0]["description"].setWordWrap(True)
        
        # button
        components[0]["btn"].setText("Open")
        components[0]["btn"].setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 17px;
                background-color:blue;
                border: 3px solid blue;
                border-radius: 5%;
            }"""
        )
        components[0]["btn"].setFixedWidth(self.screenWidth*0.07)
        components[0]["btn"].setFixedHeight(self.screenWidth*0.04)
        # Add to V stack
        vBoxLayout.addWidget(components[0]["title"], alignment=Qt.AlignCenter)
        vBoxLayout.addWidget(components[0]["description"], alignment=Qt.AlignCenter)
        vBoxLayout.addWidget(components[0]["btn"], alignment=Qt.AlignCenter)
        # add to scroll v stack
        h = QHBoxLayout()
        h.addWidget(card, alignment=Qt.AlignCenter)
        self.scrollVStack.addLayout(h)

        

    # Template for {label, description, button} UI
    def defaultDesignStep2and3(self, parent, components, sectionTitle):
        # add section label
        sectionLabel = QLabel()
        sectionLabel.setText(sectionTitle)
        sectionLabel.setStyleSheet("""
                QLabel {
                    color : black;
                    font-size: 25px;
                }"""
            )
        sectionLabel.setAlignment(Qt.AlignCenter)
        sectionLabel.setFixedWidth(self.screenWidth*0.8)
        # sectionLabel.setFixedWidth(self.screenWidth*0.2)
        sectionLabel.setContentsMargins(0, 80, 0, 80) # margin
        tempHLayout = QHBoxLayout()
        tempHLayout.addWidget(sectionLabel, alignment=Qt.AlignCenter)
        self.scrollVStack.addLayout(tempHLayout)

        # add all the cards
        for i in range(0, len(components), 3):
            # make a pair
            threeComponents = [components[i], components[i+1], components[i+2]]
            # return back a horizontal card pair
            pairHBoxLayout = self.helper(threeComponents)
            # Add to V stack
            wrapVBoxLayout = QVBoxLayout()
            wrapVBoxLayout.addLayout(pairHBoxLayout)
            # add to scroll v stack
            self.scrollVStack.addLayout(wrapVBoxLayout)


    def helper(self, components):
        h = QHBoxLayout()
        for component in components:    
            # card component
            card = QWidget()
            card.setFixedWidth(self.screenWidth*0.25)
            card.setFixedHeight(self.screenWidth*0.2)
            card.setStyleSheet("""
                QWidget {
                    color : black;
                    background-color: white;
                }"""
            )
            # vertical stack for sub components (title, description, button)
            vBoxLayout = QVBoxLayout(card)
            # title
            component["title"].setText(component["titleText"])
            component["title"].setStyleSheet("""
                QLabel {
                    color : black;
                    font-size: 25px;
                    text-decoration: underline;
                }"""
            )
            component["title"].setAlignment(Qt.AlignCenter)
            component["title"].setFixedWidth(self.screenWidth*0.2)
            # description
            component["description"].setText(component["descriptionText"])
            component["description"].setStyleSheet("""
                QLabel {
                    color : black;
                    font-size: 17px;
                }"""
            )
            component["description"].setAlignment(Qt.AlignCenter)
            component["description"].setFixedWidth(self.screenWidth*0.2)
            component["description"].setFixedHeight(self.screenWidth*0.08)
            component["description"].setWordWrap(True)
            
            # button
            component["btn"].setText("Open")
            component["btn"].setStyleSheet("""
                QPushButton {
                    color: white;
                    font-size: 17px;
                    background-color:blue;
                    border: 3px solid blue;
                    border-radius: 5%;
                }"""
            )
            component["btn"].setFixedWidth(self.screenWidth*0.07)
            component["btn"].setFixedHeight(self.screenWidth*0.04)
            # Add to V stack
            vBoxLayout.addWidget(component["title"], alignment=Qt.AlignCenter)
            vBoxLayout.addWidget(component["description"], alignment=Qt.AlignCenter)
            vBoxLayout.addWidget(component["btn"], alignment=Qt.AlignCenter)
            # 
            h.addWidget(card, alignment=Qt.AlignCenter)

        return h


    def setLambda(self, parent, componentsOne, componentsTwo, componentsThree):
        # connect lambda for componentsOne (step 1 components)
        componentsOne[0]["btn"].clicked.connect(lambda: self.screenTransition.howFarOne(parent))
        # connect lambda for componentsTwo (step 2 components)
        # componentsTwo[0]["btn"].clicked.connect(lambda: self.screenTransition.pathsAOne(parent))
        componentsTwo[1]["btn"].clicked.connect(lambda: self.screenTransition.scriptAOne(parent))
        componentsTwo[2]["btn"].clicked.connect(lambda: self.screenTransition.pathsAOne(parent))
        componentsTwo[3]["btn"].clicked.connect(lambda: self.screenTransition.gudPathAOne(parent))
        componentsTwo[4]["btn"].clicked.connect(lambda: self.screenTransition.profileAOne(parent))
        componentsTwo[5]["btn"].clicked.connect(lambda: self.screenTransition.kml3daOne(parent))
