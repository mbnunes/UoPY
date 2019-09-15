from network.UOPacket import UOPacket

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

        self.client.write(self.packetBytes)

    def setFlags(self, flags):
        self.flags = flags
