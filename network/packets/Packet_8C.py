from network.UOPacket import UOPacket

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