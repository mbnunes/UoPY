from network.UOPacket import UOPacket
from misc.WPAccount import WPAccount

class Packet_91(UOPacket):

    def __init__(self, client=None, packet=None):
        self.setPacket(packet[0])
        self.packet = packet

        if client is not None:
            self.client = client

    def receivePacket(self):

        if self.client is None:
            return False

        auth_id = self.getInt32(self.packet, 1)
        login = self.getUTF8(self.packet, 5, 30)
        password = self.getUTF8(self.packet, 36, 30)

        account = WPAccount(self.client)
        account.enableLockedFeatures()


