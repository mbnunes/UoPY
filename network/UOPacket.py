

class UOPacket:

    @staticmethod
    def getInt32(packet, offset):
        return int.from_bytes(packet[offset:offset+4],"big")

    @staticmethod
    def getInt16(packet, offset):
        return int.from_bytes(packet[offset:offset+2],"big")

    @staticmethod
    def getInt8(packet, offset):
        return int.from_bytes(packet[offset],"big")

    @staticmethod
    def getIPAddress(packet, offset):
        return "{}.{}.{}.{}".format(packet[offset],packet[offset+1],packet[offset+2],packet[offset+3])

    @staticmethod
    def getUTF8(packet, offset, lenght):
        return packet[offset:offset+lenght].decode("utf-8")