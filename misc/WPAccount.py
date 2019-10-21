from network.packets.Packet_8C import Packet_8C
from network.packets.Packet_A8 import Packet_A8
from network.packets.Packet_A9 import Packet_A9
from network.packets.Packet_B9 import Packet_B9
from config.uopy import UoPYConfig

class WPAccount:

    def __init__(self,transport):
        self.client = transport
        self.featuresFlags = 0
        self.charListFlags = 0
        self.wpConfig = UoPYConfig()

        self.updateCharListFlags()
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
        packet.sendPacket()


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
            
    def updateCharListFlags(self):
        self.charListFlags = 0x00000000
        if self.wpConfig.FeaturesFlags('featureaos') & 0x02:
            self.charListFlags |= 0x00000020
        
        if self.wpConfig.FeaturesFlags('featureaos') & 0x04:
            self.charListFlags |= 0x00000008
        
        if self.wpConfig.FeaturesFlags('featurese') & 0x02:
            self.charListFlags |= 0x00000080
        
        if self.wpConfig.FeaturesFlags('featureml') & 0x01:
            self.charListFlags |= 0x00000100
        
        if self.wpConfig.FeaturesFlags('featurekr') & 0x01:
            self.charListFlags |= 0x00000200
        
        if self.wpConfig.FeaturesFlags('featuresa') & 0x02:
            self.charListFlags |= 0x00004000
        
        if self.wpConfig.FeaturesFlags('featureej') & 0x01:
            self.charListFlags |= 0x00008000
        
        if self.wpConfig.AccountOptions('max_chars') > 6:
            self.charListFlags |= 0x00001000
        elif self.wpConfig.AccountOptions('max_chars') == 6:
            self.charListFlags |= 0x00000040
        elif self.wpConfig.AccountOptions('max_chars') == 1:
            self.charListFlags |= (0x0000010 | 0x00000004)

        # Enable the "overwrite configuration file"
        #self.charListFlags |= 0x02
        self.tooltipEnabled = self.charListFlags & 0x00000020 and True or False
    


    def sendCharacterList(self):
        character = 0
        start_location = self.wpConfig.StartCitiesPositions()

        newPacket = Packet_A9(self.client)
        newPacket.setCharCount(7)
        newPacket.setChars(character)
        newPacket.setCitiesCount(len(start_location))
        newPacket.setCities(start_location)
        newPacket.setFlags(1408)
        newPacket.setLastCharLost(0)
        newPacket.sendPacket()
