from network.UOPacket import UOPacket
from config.uopy import UoPYConfig
from network.WPCompress import WPCompression


class Packet_8C(UOPacket):
    def __init__(self, client=None, packet=None):
        self.setPacket(b'\x8C')

        if client is not None:
            self.client = client


    def sendPacket(self):

        if self.client is None:
            return False

        self.setInt8(int(self.ip[0]))
        self.setInt8(int(self.ip[1]))
        self.setInt8(int(self.ip[2]))
        self.setInt8(int(self.ip[3]))
        self.setInt16(self.port)
        self.setInt8(0)
        self.setInt8(0)
        self.setInt8(0)
        self.setInt8(0)

        self.client.write(self.packetBytes)

    def setIp(self, ip):
        self.ip = ip.split(".")

    def setPort(self, port):
        self.port = port


class Packet_A8(UOPacket):


    def __init__(self, client=None, packet=None):
        self.UoPY = UoPYConfig()
        self.sizePackage = 0
        self.serverCount = len(self.UoPY.ReadServers())
        self.setPacket(b'\xa8')

        if client is not None:
            self.client = client


    def sendPacket(self):

        if self.client is None:
            return False

        self.setInt16(self.sizePackage)
        self.setInt8(0)
        self.setInt16(self.serverCount)

        for i in range(self.serverCount):
            self.setInt16(i)
            self.setUTF8(self.UoPY.ReadServers()[i]["name"], 32)
            self.setInt8(0)
            self.setSInt8(0)
            self.setInt32(0)

        tmpByte = len(self.packetBytes).to_bytes(2,"big")
        tmpList = list(self.packetBytes)

        tmpList[1] = tmpByte[0]
        tmpList[2] = tmpByte[1]

        self.client.write(bytes(tmpList))


class Packet_A9(UOPacket):

    def __init__(self, client=None, packet=None):
        self.UoPY = UoPYConfig()

        self.serverCount = len(self.UoPY.ReadServers())
        self.setPacket(b'\xa9')

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

        self.setInt16(0)
        self.setInt8(self.charCount)

        i = 0
        while i < self.charCount:
            if i < self.chars:
                self.setUTF8(self.chars[i]['name'], 30)
                self.setUTF8("", 30)
            else:
                self.setUTF8("", 60)
            i += 1

        self.setInt8(self.citiesCount)

        for i, cities in enumerate(self.cities):
            self.setInt8(i + 1)
            self.setUTF8(self.cities[i]["name"], 32)
            self.setUTF8(self.cities[i]["area"], 32)
            self.setInt32(self.cities[i]["position"]["x"])
            self.setInt32(self.cities[i]["position"]["y"])
            self.setInt32(self.cities[i]["position"]["z"])
            self.setInt32(self.cities[i]["position"]["map"])
            self.setInt32(self.cities[i]["cliloc"])
            self.setInt32(0)

        self.setInt32(self.flags)
        self.setInt16(self.lastCharLost)

        self.packetBytes = self.getSizePacket(self.packetBytes)

        compressed = WPCompression()
        testpacket = compressed.compress(self.packetBytes)

        self.client.write(testpacket)

    def getSizePacket(self, packet):
        originalPacket = len(packet)
        packetId = packet[0]
        packetCutted = packet[3:]
        newPacket = packetId.to_bytes(1, "big")
        newPacket += originalPacket.to_bytes(2, "big")
        newPacket += packetCutted

        return newPacket

    def setCharCount(self, charCount):
        self.charCount = charCount

    def setChars(self, chars):
        self.chars = chars

    def setCitiesCount(self, citiesCount):
        self.citiesCount = citiesCount

    def setCities(self, cities):
        self.cities = cities

    def setFlags(self, flags):
        self.flags = flags

    def setLastCharLost(self, lastCharLost):
        self.lastCharLost = lastCharLost

class Packet_B9(UOPacket):


    def __init__(self, client=None, packet=None):
        self.setPacket(b'\xB9')
        self.setLength(5)

        if client is not None:
            self.client = client


    def sendPacket(self):

        if self.client is None:
            return False

        self.setInt32(self.flags)
        compressed = WPCompression()
        packetCompressed = compressed.compress(self.packetBytes)
        self.client.write(packetCompressed)

    def setFlags(self, flags):
        self.flags = flags
