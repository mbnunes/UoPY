from network.UOPacket import UOPacket
from misc.WPAccount import WPAccount

class Packet_80(UOPacket):

    def __init__(self, client=None, packet=None):

        if packet[0] != 128:
            print("Pacote ID inválido")
            return False

        self.packet = packet

        if client is not None:
            self.client = client

    def receivePacket(self):

        if self.client is None:
            return False

        login = self.getUTF8(self.packet, 1, 30)
        password = self.getUTF8(self.packet, 31, 30)
        account = WPAccount(self.client)
        account.verifyAccount(login,password)