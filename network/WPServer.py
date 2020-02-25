from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol
from network.WPRx import *
from config.uopy import UoPYConfig
import globals

wpConfig = UoPYConfig()

class WPServerProtocol(protocol.Protocol):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numConnections += 1
        if globals.DEBUG:
            print("Connections: {}".format(self.factory.numConnections))

    def dataReceived(self, data):
        request = WPRx(data, self.transport)
        request.verifyPacket()

    def connectionLost(self, reason=None):
        self.factory.numConnections -= 1
        if globals.DEBUG:
            print("Connections: {}".format(self.factory.numConnections))

class WPServerFactory(Factory):
    numConnections = 0

    def __init__(self):
        print("UoPY Emu v0.0.1a")
        print("PORT: {}".format(wpConfig.ReadServers()[0]["port"]))

    def buildProtocol(self, addr):
        return WPServerProtocol(self)


def runserver():
    reactor.listenTCP(wpConfig.ReadServers()[0]["port"], WPServerFactory())
    reactor.run()
