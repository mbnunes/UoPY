from config.UoPY import UoPYConfig
from network.UOPacket import UOPacket


class WRTx:

    @staticmethod
    def package_0xA8():
        UoPY = UoPYConfig()
        sizePackage = 0

        tmp = b'\xa8'
        tmp += sizePackage.to_bytes(2,"big")
        tmp += b"\x00"

        serverCount = len(UoPY.ReadServers())
        tmp += serverCount.to_bytes(2,"big")

        for i in range(serverCount):
            tmp += i.to_bytes(2,"big")
            tmp += UOPacket.setUTF8(UoPY.ReadServers()[i]["name"], 32)
            tmp += UOPacket.setInt8(0)
            tmp += UOPacket.setSInt8(0)
            tmp += b"\x00\x00\x00\x00"

        tmpByte = len(tmp).to_bytes(2,"big")
        tmpList = list(tmp)

        tmpList[1] = tmpByte[0]
        tmpList[2] = tmpByte[1]

        return bytes(tmpList)