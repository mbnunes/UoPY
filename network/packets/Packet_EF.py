from network.UOPacket import UOPacket

class Packet_EF(UOPacket):

    def __init__(self, client=None, packet=None):
        self.setPacket(packet[0])
        self.packet = packet

        if client is not None:
            self.client = client

    def receivePacket(self):

        if self.client is None:
            return False

        seed = self.getIPAddress(self.packet, 1)
        major = self.getInt32(self.packet, 5)
        minor = self.getInt32(self.packet, 9)
        revision = self.getInt32(self.packet, 13)
        build = self.getInt32(self.packet, 17)
