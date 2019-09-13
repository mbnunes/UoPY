from network.UOPacket import UOPacket
from misc.WPAccount import WPAccount

class WPRx:


    def __init__(self, conn, transport):
        self.conn = conn
        self.transport = transport

    def verifyPacket(self):
        self.request = self.conn
        print(self.request)
        if self.request[0] == 239:
            self.package_0xEF()
        elif self.request[0] == 128:
            self.package_0x80()
        elif self.request[0] == 160:
            self.package_0xA0()


    def package_0xEF(self):
        seed = UOPacket.getIPAddress(self.request,1)
        major = UOPacket.getInt32(self.request,5)
        minor = UOPacket.getInt32(self.request,9)
        revision = UOPacket.getInt32(self.request,13)
        build = UOPacket.getInt32(self.request,17)

    def package_0x80(self):
        login = UOPacket.getUTF8(self.request,1,30)
        password = UOPacket.getUTF8(self.request,31,30)
        account = WPAccount(self.transport)
        account.verifyAccount(login,password)

    def package_0xA0(self):
        server = UOPacket.getInt16(self.request,1)
        connected = server - 1
        print("Account {} conecting on server.", "Teste")
        WPAccount.sendConnectionConfirmation(connected)