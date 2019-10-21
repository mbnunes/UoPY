from network.UOPacket import UOPacket
from config.uopy import UoPYConfig

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
