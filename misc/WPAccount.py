from network.packets.Packet_8C import Packet_8C
from network.packets.Packet_A8 import Packet_A8
from network.packets.Packet_B9 import Packet_B9
from config.wolfpack import WolfpackConfig

class WPAccount:

    def __init__(self,transport):
        self.client = transport
        self.featuresFlags = 0
        self.wpConfig = WolfpackConfig()

        self.updateFeaturesFlags()

    def verifyAccount(self, login, password):

        if login == "test" and password == "test":
            loginCheck = Packet_A8(self.client)
            loginCheck.sendPacket()
        else:
            print("Login Incorreto!")

    def sendConnectionConfirmation(self, server):

        packet = Packet_8C(self.client)
        packet.setIp(self.wpConfig.ReadServers()[server]['address'])
        packet.setPort(self.wpConfig.ReadServers()[server]['port'])
        packet.sendPacket()

    '''Enable locked client features'''
    def enableLockedFeatures(self, runInLot = False):
        packet = Packet_B9(self.client)
        packet.setFlags(self.featuresFlags)
        packet.send()


    def updateFeaturesFlags(self):
        self.featuresFlags = 0

        if self.wpConfig.FeaturesFlags('featuret2a') & 0x01:
            self.featuresFlags |= 0x00000004

        if self.wpConfig.FeaturesFlags('featuret2a') & 0x02:
            self.featuresFlags |= 0x00000001

        if self.wpConfig.FeaturesFlags('featurelbr') & 0x01:
            self.featuresFlags |= 0x00000008

        if self.wpConfig.FeaturesFlags('featurelbr') & 0x02:
            self.featuresFlags |= 0x00000002

        if self.wpConfig.FeaturesFlags('featureaos') & 0x01:
            self.featuresFlags |= (0x00000010 | 0x00008000)

        if self.wpConfig.FeaturesFlags('featurese') & 0x01:
            self.featuresFlags |= 0x00000040

        if self.wpConfig.FeaturesFlags('featureml') & 0x01:
            self.featuresFlags |= 0x00000080

        if self.wpConfig.FeaturesFlags('featuresa') & 0x01:
            self.featuresFlags |= 0x00010000

        if self.wpConfig.FeaturesFlags('featuretol') & 0x01:
            self.featuresFlags |= 0x00400000

        if self.wpConfig.FeaturesFlags('featureej') & 0x01:
            self.featuresFlags |= 0x00800000

        if self.wpConfig.AccountOptions('max_chars') > 6:
            self.featuresFlags |= 0x00001000

        if self.wpConfig.AccountOptions('max_chars') == 6:
            self.featuresFlags |= 0x00000020

        if self.wpConfig.FeaturesFlags('featureextra') & 0x01:
            self.featuresFlags |= 0x00000200

        if self.wpConfig.FeaturesFlags('featureextra') & 0x02:
            self.featuresFlags |= 0x00040000

        if self.wpConfig.FeaturesFlags('featureextra') & 0x04:
            self.featuresFlags |= 0x00080000

        if self.wpConfig.FeaturesFlags('featureextra') & 0x08:
            self.featuresFlags |= 0x00100000

        if self.wpConfig.FeaturesFlags('featureextra') & 0x10:
            self.featuresFlags |= 0x200000

        # Only for KR or Enhanced
        if self.wpConfig.FeaturesFlags('featureextra') & 0x20:
            self.featuresFlags |= 0x00002000
        