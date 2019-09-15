from network.PacketsDefs import PacketsDefs

class UOPacket:

    def __init__(self):
        self.client = None
        self.length = None
        self.packet = None
        self.packetBytes = b''

    def setPacket(self, packet_id=None):
        if packet_id is None:
            return False

        if isinstance(packet_id, bytes):
            packet_id = int.from_bytes(packet_id, "big")

        self.packet = packet_id
        self.setLength(PacketsDefs.getLenght(packet_id))
        self.packetBytes = packet_id.to_bytes(1, "big")

    def setLength(self, packet_lenght):
        self.length = packet_lenght

    def getPacket(self):
        return self.packet

    def getInt32(self, packet, offset):
        return int.from_bytes(packet[offset:offset+4],"big")

    def setInt32(self, number):
        self.packetBytes += number.to_bytes(4, "big")

    def getInt16(self, packet, offset):
        return int.from_bytes(packet[offset:offset+2],"big")

    def setInt16(self, number):
        self.packetBytes += number.to_bytes(2, "big")

    def getInt8(self, packet, offset):
        return int.from_bytes(packet[offset],"big")

    def setInt8(self, number):
        self.packetBytes += number.to_bytes(1, "big")

    def setSInt8(self, number):
        self.packetBytes += number.to_bytes(1, "little")

    def getIPAddress(self, packet, offset):
        return "{}.{}.{}.{}".format(packet[offset],packet[offset+1],packet[offset+2],packet[offset+3])

    def getUTF8(self, packet, offset, lenght):
        return str(packet[offset:offset+lenght],"utf-8").replace('\x00',"")

    def setUTF8(self, text, lenghtPacket):
        tmp = str.encode(text)

        for i in range(lenghtPacket):
            tmp += b""

        self.packetBytes += tmp