import socket
import threading
from config.wolfpack import WolfpackConfig
from network.UOReceive import *

class Server:

    def __init__(self):
        self.wpconfig = WolfpackConfig()
        self.name = self.wpconfig.ReadServers()[0]["name"]
        self.address = self.wpconfig.ReadServers()[0]["address"]
        self.port = self.wpconfig.ReadServers()[0]["port"]
        self.status = True

    def initSocket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.address, self.port))
        self.server.listen()

    def client_socket(self, clientSocket):
        receiver = UOReceive(clientSocket)
        receiver.verifyPacket()


    def startServer(self):
        self.initSocket()
        while self.status:
            client, addr = self.server.accept()
            self.client_handler = threading.Thread(target=self.client_socket, args=(client,))
            self.client_handler.start()

    def stopServer(self):
        self.status = False
        self.server.close()

