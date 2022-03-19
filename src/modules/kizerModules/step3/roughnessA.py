from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
import pandas as pd
import math

class RoughnessA(object):

    def __init__(self):
        self.FolderPath = ""
        self.NumberOfProfiles = float("inf")

    def setFolderPath(self, folderPath):
        self.FolderPath = str(folderPath)

    def setNumberOfProfiles(self, numOfProfiles):
        self.NumberOfProfiles = int(numOfProfiles)

    def execute(self):
        # Get local machine's path for Profiles folder
        self.FolderPath = self.FolderPath + "/Profiles"

        for counter in range(1, self.NumberOfProfiles+1):
            ProfileNumber = str(counter)

            if counter < 100000:
                ProfileNumber = "0" + ProfileNumber

            if counter < 10000:
                ProfileNumber = "0" + ProfileNumber

            if counter < 1000:
                ProfileNumber = "0" + ProfileNumber

            if counter < 100:
                ProfileNumber = "0" + ProfileNumber

            if counter < 10:
                ProfileNumber = "0" + ProfileNumber

            TheProfile = "/P" + ProfileNumber + ".CSV"
            TheRoughness = "/Roughness" + ProfileNumber + ".CSV"

            roughness_df = open(self.FolderPath  + TheRoughness, "w+")
            profile_df = pd.read_csv(self.FolderPath  + TheProfile, header=None)
            
            latitude = profile_df.iloc[:, 0].tolist()
            longitude = profile_df.iloc[:, 1].tolist()
            height = profile_df.iloc[:, 2].tolist()

            MaxLoopCounter = len(profile_df)
            LoopCounter = 0
            CumulativeSum = 0.0
            SqCumulativeSum = 0.0

            for h in height:
                LoopCounter += 1
                if 1 < LoopCounter < MaxLoopCounter:
                    CumulativeSum += h
                    SqCumulativeSum += (h*h)

            hlower = min(height[0], height[len(height)-1])

            Average = CumulativeSum / (MaxLoopCounter - 2)
            SqAverage = SqCumulativeSum / (MaxLoopCounter - 2)
            AverageSq = (Average * Average)
            Roughness = SqAverage - AverageSq
            Roughness = math.pow(Roughness, 0.5)
            # print(Roughness)

            if Roughness > 140:
                Roughness = 140
            if Roughness < 20:
                Roughness = 20

            print(str(Roughness) + "," + str(hlower))
            roughness_df.write(str(Roughness) + "," + str(hlower) + "\n")

        print("Program Completed")

#test = RoughnessA()
#test.setFolderPath("C:/Users/ecuth/Desktop/Spatial Datalyst/Kizer/Path Design 11 April 2021/Step 3 Path Availability/ExampleStep3")
#test.setNumberOfProfiles(6)
#test.execute()