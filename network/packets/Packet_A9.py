from network.UOPacket import UOPacket
from config.wolfpack import WolfpackConfig

class Packet_A8(UOPacket):


    def __init__(self, client=None, packet=None):
        self.wolfpack = WolfpackConfig()

        self.serverCount = len(self.wolfpack.ReadServers())
        self.setPacket(b'\xa8')

        self.sizePacket = 0
        self.charCount = 0
        self.chars = None
        self.citiesCount = 0
        self.cities = None
        self.flags = None
        self.lastCharLost = None

        if client is not None:
            self.client = client


    def sendPacket(self):

        if self.client is None:
            return False

        self.setInt8(self.charCount)

        for i in range(self.charCount):
            if i < len(self.chars):
                self.setUTF8(self.chars[i]['name'], 30)
                self.setUTF8("", 30)
            else:
                self.setUTF8("", 60)

        self.setInt8(self.citiesCount)

        for i, cities in enumerate(self.cities):
            self.setInt8(i+1)
            self.setUTF8(self.cities[i]["name"], 32)
            self.setUTF8(self.cities[i]["area"], 32)
            self.setInt32(self.cities[i]["position"]["x"])
            self.setInt32(self.cities[i]["position"]["y"])
            self.setInt32(self.cities[i]["position"]["z"])
            self.setInt32(self.cities[i]["position"]["map"])
            self.setInt32(0)

        self.setInt32(self.flags)
        self.setInt16(self.lastCharLost)

        self.client.write(self.packetBytes)

    def setSizePacket(self, sizePacket):
        self.sizePacket = sizePacket
    
    def setCharCount(self, charCount):
        self.charCount = charCount

    def setChars(self, chars):
        self.chars = self, chars

    def setCitiesCount(self, citiesCount):
        self.citiesCount = citiesCount

    def setCities(self, cities):
        self.cities = cities

    def setFlags(self, flags):
        self.flags = flags

    def setLastCharLost(self, lastCharLost):
        self.lastCharLost = lastCharLost
