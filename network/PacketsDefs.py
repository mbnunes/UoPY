

class PacketsDefs:

    @staticmethod
    def getLenght(self, packet_id):
        LENGTH = { b'\x00' : 104, b'\x01' : 5, b'\x02' : 7, b'\x03' : False, b'\x04' : 2, b'\x05' : 5, b'\x06' : 5,
            b'\x07' : 7, b'\x08' : 15, b'\x09' : 5, b'\x0A' : 11, b'\x0B' : 266, b'\x0C' : False, b'\x0D' : 3,
            b'\x0E' : False, b'\x0F' : 61, b'\x10' : 215, b'\x11' : False, b'\x12' : False, b'\x13' : 10, b'\x14' : 6,
            b'\x15' : 9, b'\x16' : 1, b'\x17' : False, b'\x18' : False, b'\x19' : False, b'\x1A' : False, b'\x1B' : 37,
            b'\x1C' : False, b'\x1D' : 5, b'\x1E' : 4, b'\x1F' : 8, b'\x20' : 19, b'\x21' : 8, b'\x22' : 3,
            b'\x23' : 26, b'\x24' : 7, b'\x25' : 21, b'\x26' : 5, b'\x27' : 2, b'\x28' : 5, b'\x29' : 1,
            b'\x2A' : 5, b'\x2B' : 2, b'\x2C' : 2, b'\x2D' : 17, b'\x2E' : 15, b'\x2F' : 10, b'\x30' : 5,
            b'\x31' : 1, b'\x32' : 2, b'\x33' : 2, b'\x34' : 10, b'\x35' : 653, b'\x36' : False, b'\x37' : 8,
            b'\x38' : 7, b'\x39' : 9, b'\x3A' : False, b'\x3B' : False, b'\x3C' : False, b'\x3D' : 2, b'\x3E' : 37,
            b'\x3F' : False, b'\x40' : 201, b'\x41' : False, b'\x42' : False, b'\x43' : 553, b'\x44' : 713, b'\x45' : 5,
            b'\x46' : False, b'\x47' : 11, b'\x48' : 73, b'\x49' : 93, b'\x4A' : 5, b'\x4B' : 9, b'\x4C' : False,
            b'\x4D' : False, b'\x4E' : 6, b'\x4F' : 2, b'\x50' : False, b'\x51' : False, b'\x52' : False, b'\x53' : 2,
            b'\x54' : 12, b'\x55' : 1, b'\x56' : 11, b'\x57' : 110, b'\x58' : 106, b'\x59' : False, b'\x5A' : False,
            b'\x5B' : 4, b'\x5C' : 2, b'\x5D' : 73, b'\x5E' : False, b'\x5F' : 49, b'\x60' : 5, b'\x61' : 9,
            b'\x62' : 15, b'\x63' : 13, b'\x64' : 1, b'\x65' : 4, b'\x66' : False, b'\x67' : 21, b'\x68' : False,
            b'\x69' : False, b'\x6A' : 3, b'\x6B' : 9, b'\x6C' : 19, b'\x6D' : 3, b'\x6E' : 14, b'\x6F' : False,
            b'\x70' : 28, b'\x71' : False, b'\x72' : 5, b'\x73' : 2, b'\x74' : False, b'\x75' : 35, b'\x76' : 16,
            b'\x77' : 17, b'\x78' : False, b'\x79' : 9, b'\x7A' : False, b'\x7B' : 2, b'\x7C' : False, b'\x7D' : 13,
            b'\x7E' : 2, b'\x7F' : False, b'\x80' : 62, b'\x81' : False, b'\x82' : 2, b'\x83' : 39, b'\x84' : 69,
            b'\x85' : 2, b'\x86' : False, b'\x87' : False, b'\x88' : 66, b'\x89' : False, b'\x8A' : False, b'\x8B' : False,
            b'\x8C' : 11, b'\x8D' : False, b'\x8E' : False, b'\x8F' : False, b'\x90' : 19, b'\x91' : 65, b'\x92' : False,
            b'\x93' : 99, b'\x94' : False, b'\x95' : 9, b'\x96' : False, b'\x97' : 2, b'\x98' : -1, b'\x99' : 26,
            b'\x9A' : False, b'\x9B' : 258, b'\x9C' : 309, b'\x9D' : 51, b'\x9E' : False, b'\x9F' : False, b'\xA0' : 3,
            b'\xA1' : 9, b'\xA2' : 9, b'\xA3' : 9, b'\xA4' : 149, b'\xA5' : False, b'\xA6' : False, b'\xA7' : 4,
            b'\xA8' : False, b'\xA9' : False, b'\xAA' : 5, b'\xAB' : False, b'\xAC' : False, b'\xAD' : False, b'\xAE' : False,
            b'\xAF' : 13, b'\xB0' : False, b'\xB1' : False, b'\xB2' : False, b'\xB3' : False, b'\xB4' : False, b'\xB5' : 64,
            b'\xB6' : 9, b'\xB7' : False, b'\xB8' : False, b'\xB9' : 3, b'\xBA' : 6, b'\xBB' : 9, b'\xBC' : 3,
            b'\xBD' : -1, b'\xBE' : False, b'\xBF' : -1, b'\xC0' : 36, b'\xC1' : False, b'\xC2' : False, b'\xC3' : False,
            b'\xC4' : 6, b'\xC5' : 203, b'\xC6' : 1, b'\xC7' : 49, b'\xC8' : 2, b'\xC9' : 6, b'\xCA' : 6,
            b'\xCB' : 7, b'\xCC' : False, b'\xCD' : 1, b'\xCE' : False, b'\xCF' : 78, b'\xD0' : False, b'\xD1' : 2,
            b'\xD2' : 25, b'\xD3' : False, b'\xD4' : False, b'\xD5' : False, b'\xD6' : False, b'\xD7' : False, b'\xD8' : False,
            b'\xD9' : 268, b'\xDA' : False, b'\xDB' : False, b'\xDC' : 9, b'\xDD' : 65535, b'\xDE' : 1, b'\xDF' : 1,
            b'\xE0' : 1, b'\xE1' : 9, b'\xE2' : 10, b'\xE3' : 77, b'\xEC' : 1, b'\xED' : 1, b'\xEF' : 21,
            b'\xF0' : -1, b'\xF1' : False, b'\xF3' : 24, b'\xF5' : 21, b'\xF8' : 106 }

        return LENGTH[packet_id]