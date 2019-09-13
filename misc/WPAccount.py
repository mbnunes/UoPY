
from network.WPTx import WRTx
from network.packets.packet_8C import *
from config.wolfpack import WolfpackConfig

class WPAccount:

    def __init__(self,transport):
        self.client = transport

    def verifyAccount(self, login, password):

        if login == "test" and password == "test":
            print(WRTx.package_0x80())
            self.client.write(WRTx.package_0x80())

        else:
            print("Login Incorreto!")

    def sendConnectionConfirmation(self,server):
        wpConfig = WolfpackConfig()

        packet = Packet_8C(self.client)
        packet.setIp(wpConfig.ReadServers()[server]['address'])
        packet.setPort(wpConfig.ReadServers()[server]['port'])
        packet.sendPacket()