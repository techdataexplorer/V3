# This QThread class is for executing Gud Path Kizer Module

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class KizerModuleThread(QThread):

    def __init__(self, parent, kizerModule, moduleName):
        super(KizerModuleThread, self).__init__(parent)
        self.kizerModule = kizerModule
        self.moduleName = moduleName
        print("Thread " + self.moduleName + " is declared.")

    def run(self):
        print(self.moduleName + " thread running...")
        self.kizerModule.execute()

    def quit(self):
        print("Quit " + self.moduleName + " thread")
        self.kizerModule.endProgram()
        self.terminate()
