from network.UOPacket import UOPacket
from misc.WPAccount import WPAccount
from misc.db import PyUODB
import globals

class Packet_80(UOPacket):

    def __init__(self, client=None, packet=None):

        if packet[0] != 128:
            print("Pacote ID inválido")
            return False

        self.packet = packet

        if client is not None:
            self.client = client

    def receivePacket(self):

        if self.client is None:
            return False

        login = self.getUTF8(self.packet, 1, 30)
        password = self.getUTF8(self.packet, 31, 30)
        account = WPAccount(self.client)
        account.verifyAccount(login,password)

class Packet_91(UOPacket):

    def __init__(self, client=None, packet=None):
        self.setPacket(packet[0])
        self.packet = packet

        if client is not None:
            self.client = client

        globals.clientList[self.client] = {}

    def receivePacket(self):

        if self.client is None:
            return False

        auth_id = self.getInt32(self.packet, 1)
        login = self.getUTF8(self.packet, 5, 30)
        password = self.getUTF8(self.packet, 36, 30)

        account = WPAccount(self.client)
        account.enableLockedFeatures()
        account.sendCharacterList()
        globals.clientList[self.client].update({"account": account})

class Packet_A0(UOPacket):

    def __init__(self, client=None, packet=None):
        self.setPacket(packet[0])
        self.packet = packet

        if client is not None:
            self.client = client

    def receivePacket(self):

        if self.client is None:
            return False

        account = WPAccount(self.client)
        server = self.getInt16(self.packet, 1)
        connected = server - 1
        account.sendConnectionConfirmation(connected)

class Packet_EF(UOPacket):

    def __init__(self, client=None, packet=None):
        self.setPacket(packet[0])
        self.packet = packet

        if client is not None:
            self.client = client

    def receivePacket(self):

        if self.client is None:
            return False

        seed = self.getIPAddress(self.packet, 1)
        major = self.getInt32(self.packet, 5)
        minor = self.getInt32(self.packet, 9)
        revision = self.getInt32(self.packet, 13)
        build = self.getInt32(self.packet, 17)

class Packet_F8(UOPacket):

    def __init__(self, client=None, packet=None):
        if client is not None:
            self.client = client
        self.setPacket(packet[0])
        self.packet = packet
        self.arg1 = None
        self.arg2 = None
        self.arg3 = None
        self.charName = None
        self.arg4 = None
        self.flags = None
        self.arg5 = None
        self.clientLoginCount = None
        self.profession = None
        self.arg6 = None # array 15 bytes
        self.genderRace = None
        self.str = None
        self.dex = None
        self.int = None
        self.skill1 = None
        self.skill2 = None
        self.skillAmount2 = None
        self.skill3 = None
        self.skillAmount3 = None
        self.skill4 = None
        self.skillAmount4 = None
        self.skinColor = None
        self.hairStyle = None
        self.hairColor = None
        self.beardStyle = None
        self.beardColor = None
        self.shardIndex = None
        self.startingCity = None
        self.characterSlot = None
        self.clientIP = None
        self.shirtColor = None
        self.pantsColor = None
        self.condb = PyUODB()
        self.colPlayers = self.condb.db["players"]


    def receivePacket(self):

        if self.client is None:
            return False

        self.arg1 = self.getInt32(self.packet, 1)
        self.arg2 = self.getInt32(self.packet, 5)
        self.arg3 = self.getInt8(self.packet, 9)
        self.charName = self.getUTF8(self.packet, 10, 30)
        self.arg4 = self.getInt16(self.packet, 40)
        self.flags = self.getInt32(self.packet, 42)
        self.arg5 = self.getInt32(self.packet, 46)
        self.clientLoginCount = self.getInt32(self.packet, 50)
        self.profession = self.getInt8(self.packet, 54)
        self.arg6 = self.getUTF8(self.packet, 55, 15)
        self.genderRace = self.getInt8(self.packet, 70)
        self.str = self.getInt8(self.packet, 71)
        self.dex = self.getInt8(self.packet, 72)
        self.int = self.getInt8(self.packet, 73)
        self.skill1 = self.getInt8(self.packet, 74)
        self.skillAmount1 = self.getInt8(self.packet, 75)
        self.skill2 = self.getInt8(self.packet, 76)
        self.skillAmount2 = self.getInt8(self.packet, 77)
        self.skill3 = self.getInt8(self.packet, 78)
        self.skillAmount3 = self.getInt8(self.packet, 79)
        self.skill4 = self.getInt8(self.packet, 80)
        self.skillAmount4 = self.getInt8(self.packet, 81)
        self.skinColor = self.getInt16(self.packet, 82)
        self.hairStyle = self.getInt16(self.packet, 84)
        self.hairColor = self.getInt16(self.packet, 86)
        self.beardStyle = self.getInt16(self.packet, 88)
        self.beardColor = self.getInt16(self.packet, 90)
        self.shardIndex = self.getInt8(self.packet, 92)
        self.startingCity = self.getInt8(self.packet, 93)
        self.characterSlot = self.getInt32(self.packet, 94)
        self.clientIP = self.getIPAddress(self.packet, 98)
        self.shirtColor = self.getInt16(self.packet, 102)
        self.pantsColor = self.getInt16(self.packet, 104)

        self.createCharacter()

    def createCharacter(self):

        if not self.colAcc.find_one({"charName": self.charName})['charName']:
            createCharJson = {"charName": self.charName, "flags": self.flags, \
                            "clientLoginCount": self.clientLoginCount, "profession": self.profession, \
                            "genderRace": self.genderRace, "str": self.str, \
                            "dex": self.dex, "int": self.int, \
                            "skill1": self.skill1, "skillAmount1": self.skillAmount1, \
                            "skill2": self.skill2, "skillAmount2": self.skillAmount2, \
                            "skill3": self.skill3, "skillAmount3": self.skillAmount3, \
                            "skill4": self.skill4, "skillAmount4": self.skillAmount4, \
                            "skinColor": self.skinColor, "hairStyle": self.hairStyle, \
                            "hairColor": self.hairColor, "beardStyle": self.beardStyle, \
                            "beardColor": self.beardColor, "shardIndex": self.shardIndex, \
                            "startCity": self.startingCity, "characterSlot": self.characterSlot, \
                            "clientIP": self.clientIP, "shirtColor": self.shirtColor, \
                            "pantsColor": self.pantsColor, 'account_id': globals.clientList[self.client]['account_id']    }
            try:
                self.colPlayers.insert_one(createCharJson)
            except:
                print("O Cliente: %s - Erro ao tentar criar o char no MongoDB", self.client)
        
        else:
            print("Nome já escolhido")