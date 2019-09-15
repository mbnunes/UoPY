from network.UOPacket import UOPacket
from network.packets.Packet_A0 import Packet_A0
from network.packets.Packet_80 import Packet_80
from network.packets.Packet_EF import Packet_EF
from network.packets.Packet_91 import Packet_91

from misc.WPAccount import WPAccount

class WPRx:


    def __init__(self, conn, transport):
        self.conn = conn
        self.transport = transport

    def verifyPacket(self):
        self.request = self.conn
        if self.request[0] == 239:
            pacote = Packet_EF(self.transport, self.request)
            pacote.receivePacket()
        elif self.request[0] == 128:
            pacote = Packet_80(self.transport, self.request)
            pacote.receivePacket()
        elif self.request[0] == 160:
            pacote = Packet_A0(self.transport, self.request)
            pacote.receivePacket()
        elif self.request[0] == 145:
            pacote = Packet_91(self.transport, self.request)
            pacote.receivePacket()


    # def package_0xEF(self):
    #     seed = UOPacket.getIPAddress(self.request,1)
    #     major = UOPacket.getInt32(self.request,5)
    #     minor = UOPacket.getInt32(self.request,9)
    #     revision = UOPacket.getInt32(self.request,13)
    #     build = UOPacket.getInt32(self.request,17)
    #
    # def package_0x80(self):
    #     login = UOPacket.getUTF8(self.request,1,30)
    #     password = UOPacket.getUTF8(self.request,31,30)
    #     account = WPAccount(self.transport)
    #     account.verifyAccount(login,password)
    #
    # def package_0xA0(self):
    #     account = WPAccount(self.transport)
    #     server = UOPacket.getInt16(self.request,1)
    #     connected = server - 1
    #     print("Account {} conecting on server.", "Teste")
    #     account.sendConnectionConfirmation(connected)