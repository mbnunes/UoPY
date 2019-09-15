from network.UOPacket import UOPacket
from misc.WPAccount import WPAccount

class Packet_A0(UOPacket):

    def __init__(self, client=None, packet=None):
        self.setPacket(packet[0])
        self.packet = packet

        if client is not None:
            self.client = client

    def receivePacket(self):

        if self.client is None:
            return False

        account = WPAccount(self.client)
        server = self.getInt16(self.packet, 1)
        connected = server - 1
        account.sendConnectionConfirmation(connected)