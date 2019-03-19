

class UOReceive:


    def __init__(self, conn):
        self.conn = conn

    def verifyPacket(self):
        self.request = self.conn.recv(4096)

        if self.request[0] == 239:
            for i in self.request:
                print(i)


    def package_0xEF(self):
        pass