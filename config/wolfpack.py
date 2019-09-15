import json
import pprint
import os

class WolfpackConfig:

    def __init__(self):
        self.pathFile = os.path.dirname(os.path.abspath(__file__))+"/wolfpack.json"
        with open(self.pathFile, "r") as wpconfig:
            self.data = json.load(wpconfig)

    def ReadServers(self):
        return self.data["servers"]

    def FeaturesFlags(self,feature):
        flags = self.data["features"][feature]

        for i in flags:
            feature |= flags[i]

        return feature

    def AccountOptions(self, option):
        return self.data["account"][option]

    def StartCitiesPositions(self):
        return self.data["start_cities_locations"]

