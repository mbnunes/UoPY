from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol
from network.WPRx import *
from config.wolfpack import WolfpackConfig

wpConfig = WolfpackConfig()

class WPServerProtocol(protocol.Protocol):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numConnections += 1
        print("Connections: {}".format(self.factory.numConnections))

    def dataReceived(self, data):
        request = WPRx(data, self.transport)
        request.verifyPacket()

    def connectionLost(self, reason=None):
        self.factory.numConnections -= 1
        print("Connections: {}".format(self.factory.numConnections))

class WPServerFactory(Factory):
    numConnections = 0

    def __init__(self):
        print("Wolfpack Emu v0.0.1a")
        print("PORT: {}".format(wpConfig.ReadServers()[0]["port"]))

    def buildProtocol(self, addr):
        return WPServerProtocol(self)


def runserver():
    reactor.listenTCP(wpConfig.ReadServers()[0]["port"], WPServerFactory())
    reactor.run()
