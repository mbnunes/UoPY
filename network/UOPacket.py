

class UOPacket:

    @staticmethod
    def getInt32(packet, offset):
        return int.from_bytes(packet[offset:offset+4],"big")

    @staticmethod
    def setInt32(number):
        return number.to_bytes(4, "big")

    @staticmethod
    def getInt16(packet, offset):
        return int.from_bytes(packet[offset:offset+2],"big")

    @staticmethod
    def setInt16(number):
        return number.to_bytes(2, "big")

    @staticmethod
    def getInt8(packet, offset):
        return int.from_bytes(packet[offset],"big")

    @staticmethod
    def setInt8(number):
        return number.to_bytes(1, "big")

    @staticmethod
    def setSInt8(number):
        return number.to_bytes(1, "little")

    @staticmethod
    def getIPAddress(packet, offset):
        return "{}.{}.{}.{}".format(packet[offset],packet[offset+1],packet[offset+2],packet[offset+3])

    @staticmethod
    def getUTF8(packet, offset, lenght):
        return str(packet[offset:offset+lenght],"utf-8").replace('\x00',"")

    @staticmethod
    def setUTF8(text, lenghtPacket):
        tmp = str.encode(text)

        for i in range(lenghtPacket):
            tmp += b""

        return tmp