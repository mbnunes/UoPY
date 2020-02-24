import json
import pprint
import os

class UoPYConfig:

    def __init__(self):
        self.pathFile = os.path.dirname(os.path.abspath(__file__))+"/uopy.json"
        with open(self.pathFile, "r") as wpconfig:
            self.data = json.load(wpconfig)

    def ReadServers(self):
        return self.data["servers"]

    def ConnectMongo(self):
        return self.data["mongodb"][0]

    def Debug(self):
        return self.data["settings"][0]['debug']

    def FeaturesFlags(self, feature):
        flags = self.data["features"][0][feature]
        featureFlag = 0

        for i in range(len(flags)):
            featureFlag |= flags[i]

        return featureFlag

    def AccountOptions(self, option):
        return self.data["accounts"][0][option]

    def StartCitiesPositions(self):
        return self.data["start_cities_locations"]

