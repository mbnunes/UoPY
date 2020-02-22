from network.packets.PyUO_Rx import *

from misc.WPAccount import WPAccount

class WPRx:


    def __init__(self, conn, transport):
        self.conn = conn
        self.transport = transport

    def verifyPacket(self):
        self.request = self.conn
        print("Received: %s\nSize: %d\nID: %d"%(self.request,len(self.request),self.request[0]))
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
        elif self.request[0] == 248:
            pacote = Packet_F8(self.transport, self.request)
            pacote.receivePacket()
