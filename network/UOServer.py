from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol
from network.UOPacketRx import *
from config.uopy import UoPYConfig
import globals

uoConfig = UoPYConfig()

class UOServerProtocol(protocol.Protocol):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numConnections += 1
        if globals.DEBUG:
            print("Connections: {}".format(self.factory.numConnections))

    def dataReceived(self, data):
        request = UOPacketRx(data, self.transport)
        request.verifyPacket()

    def connectionLost(self, reason=None):
        self.factory.numConnections -= 1
        if globals.DEBUG:
            print("Connections: {}".format(self.factory.numConnections))

class UOServerFactory(Factory):
    numConnections = 0

    def __init__(self):
        print("UoPY Emu v0.0.1a")
        print("PORT: {}".format(uoConfig.ReadServers()[0]["port"]))

    def buildProtocol(self, addr):
        return UOServerProtocol(self)


def runserver():
    reactor.listenTCP(uoConfig.ReadServers()[0]["port"], UOServerFactory())
    reactor.run()
