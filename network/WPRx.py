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
        print(self.request)
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
