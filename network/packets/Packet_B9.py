from network.UOPacket import UOPacket
from network.WPCompress import WPCompression

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
        print("Send: ", self.packetBytes)
        print("Size: ", len(self.packetBytes))
        compressed = WPCompression()
        packetCompressed = compressed.compress(self.packetBytes)
        self.client.write(packetCompressed)

    def setFlags(self, flags):
        self.flags = flags
