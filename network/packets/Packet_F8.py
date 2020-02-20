from network.UOPacket import UOPacket

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
        self.ganderRacer = None
        self.str = None
        self.dex = None
        self.int = None
        self.skill1 = None
        self.skillAmount1 = None
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


    def receivePacket(self):

        if self.client is None:
            return False

        self.arg1 = self.getInt32(self.packet, 1)
        self.arg2 = self.getInt32(self.packet, 5)
        self.arg3 = self.getInt8(self.packet, 9)
        self.charName = self.getUTF8(self.packet, 10, 29)
        self.arg4 = self.getInt8(self.packet, 40)
        self.flags = self.getInt32(self.packet, 41)
        self.arg5 = self.getInt32(self.packet, 45)
        self.clientLoginCount = self.getInt32(self.packet, 49)
        self.profession = self.getInt8(self.packet, 53)
        self.arg6 = self.getUTF8(self.packet, 54, 15)
        self.ganderRacer = self.getInt8(self.packet, 69)
        self.str = self.getInt8(self.packet, 70)
        self.dex = self.getInt8(self.packet, 71)
        self.int = self.getInt8(self.packet, 72)
        self.skill1 = self.getInt8(self.packet, 73)
        self.skillAmount1 = self.getInt8(self.packet, 74)
        self.skill2 = self.getInt8(self.packet, 75)
        self.skillAmount2 = self.getInt8(self.packet, 76)
        self.skill3 = self.getInt8(self.packet, 77)
        self.skillAmount3 = self.getInt8(self.packet, 78)
        self.skill4 = self.getInt8(self.packet, 79)
        self.skillAmount4 = self.getInt8(self.packet, 80)
        self.skinColor = self.getInt16(self.packet, 81)
        self.hairStyle = self.getInt16(self.packet, 83)
        self.hairColor = self.getInt16(self.packet, 85)
        self.beardStyle = self.getInt16(self.packet, 87)
        self.beardColor = self.getInt16(self.packet, 89)
        self.shardIndex = self.getInt8(self.packet, 91)
        self.startingCity = self.getInt8(self.packet, 92)
        self.characterSlot = self.getInt32(self.packet, 93)
        self.clientIP = self.getIPAddress(self.packet, 97)
        self.shirtColor = self.getInt16(self.packet, 101)
        self.pantsColor = self.getInt16(self.packet, 103)

        self.createCharacter()

    def createCharacter(self):
        print(self.charName)
        print(self.flags)
        print(self.clientLoginCount)
        print(self.profession)
        print(self.ganderRacer)
        print(self.str)
        print(self.dex)
        print(self.int)
        print(self.skill1)
        print(self.skillAmount1)
        print(self.skill2)
        print(self.skillAmount2)
        print(self.skill3)
        print(self.skillAmount3)
        print(self.skill4)
        print(self.skillAmount4)
        print(self.skinColor)
        print(self.hairStyle)
        print(self.hairColor)
        print(self.beardStyle)
        print(self.beardColor)
        print(self.shardIndex)
        print(self.startingCity)
        print(self.characterSlot)
        print(self.clientIP)
        print(self.shirtColor)
        print(self.pantsColor)