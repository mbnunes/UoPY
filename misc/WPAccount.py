
from network.WPTx import WRTx

class WPAccount:

    def __init__(self,transport):
        self.transport = transport

    def verifyAccount(self, login, password):

        if login == "test" and password == "test":
            print(WRTx.package_0x80())
            self.transport.write(WRTx.package_0x80())

        else:
            print("Login Incorreto!")
