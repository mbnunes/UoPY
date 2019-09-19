
class WPCompression:

    def __init__(self):
        self.huffmanTable = [[b'\x00\x02', b'\x00\x00'], [b'\x00\x05', b'\x00\x1f'], [b'\x00\x06', b'\x00"'],
                [b'\x00\x07', b'\x004'], [b'\x00\x07', b'\x00u'], [b'\x00\x06', b'\x00['], [b'\x00\x06', b'\x00;'],
                [b'\x00\x07', b'\x002'], [b'\x00\x08', b'\x00\xe0'], [b'\x00\x08', b'\x00b'], [b'\x00\x07', b'\x00V'],
                [b'\x00\x08', b'\x00y'], [b'\x00\t', b'\x01\x9d'], [b'\x00\x08', b'\x00\x97'], [b'\x00\x06', b'\x00*'],
                [b'\x00\x07', b'\x00W'], [b'\x00\x08', b'\x00q'], [b'\x00\x08', b'\x00['], [b'\x00\t', b'\x01\xcc'],
                [b'\x00\x08', b'\x00\xa7'], [b'\x00\x07', b'\x00%'], [b'\x00\x07', b'\x00O'], [b'\x00\x08', b'\x00f'],
                [b'\x00\x08', b'\x00}'], [b'\x00\t', b'\x01\x91'], [b'\x00\t', b'\x01\xce'], [b'\x00\x07', b'\x00?'],
                [b'\x00\t', b'\x00\x90'], [b'\x00\x08', b'\x00Y'], [b'\x00\x08', b'\x00{'], [b'\x00\x08', b'\x00\x91'],
                [b'\x00\x08', b'\x00\xc6'], [b'\x00\x06', b'\x00-'], [b'\x00\t', b'\x01\x86'], [b'\x00\x08', b'\x00o'],
                [b'\x00\t', b'\x00\x93'], [b'\x00\n', b'\x01\xcc'], [b'\x00\x08', b'\x00Z'], [b'\x00\n', b'\x01\xae'],
                [b'\x00\n', b'\x01\xc0'], [b'\x00\t', b'\x01H'], [b'\x00\t', b'\x01J'], [b'\x00\t', b'\x00\x82'],
                [b'\x00\n', b'\x01\x9f'], [b'\x00\t', b'\x01q'], [b'\x00\t', b'\x01 '], [b'\x00\t', b'\x00\xe7'],
                [b'\x00\n', b'\x01\xf3'], [b'\x00\t', b'\x01K'], [b'\x00\t', b'\x01\x00'], [b'\x00\t', b'\x01\x90'],
                [b'\x00\x06', b'\x00\x13'], [b'\x00\t', b'\x01a'], [b'\x00\t', b'\x01%'], [b'\x00\t', b'\x013'],
                [b'\x00\t', b'\x01\x95'], [b'\x00\t', b'\x01s'], [b'\x00\t', b'\x01\xca'], [b'\x00\t', b'\x00\x86'],
                [b'\x00\t', b'\x01\xe9'], [b'\x00\t', b'\x00\xdb'], [b'\x00\t', b'\x01\xec'], [b'\x00\t', b'\x00\x8b'],
                [b'\x00\t', b'\x00\x85'], [b'\x00\x05', b'\x00\n'], [b'\x00\x08', b'\x00\x96'],
                [b'\x00\x08', b'\x00\x9c'], [b'\x00\t', b'\x01\xc3'], [b'\x00\t', b'\x01\x9c'],
                [b'\x00\t', b'\x00\x8f'], [b'\x00\t', b'\x01\x8f'], [b'\x00\t', b'\x00\x91'], [b'\x00\t', b'\x00\x87'],
                [b'\x00\t', b'\x00\xc6'], [b'\x00\t', b'\x01w'], [b'\x00\t', b'\x00\x89'], [b'\x00\t', b'\x00\xd6'],
                [b'\x00\t', b'\x00\x8c'], [b'\x00\t', b'\x01\xee'], [b'\x00\t', b'\x01\xeb'], [b'\x00\t', b'\x00\x84'],
                [b'\x00\t', b'\x01d'], [b'\x00\t', b'\x01u'], [b'\x00\t', b'\x01\xcd'], [b'\x00\x08', b'\x00^'],
                [b'\x00\t', b'\x00\x88'], [b'\x00\t', b'\x01+'], [b'\x00\t', b'\x01r'], [b'\x00\t', b'\x01\n'],
                [b'\x00\t', b'\x00\x8d'], [b'\x00\t', b'\x01:'], [b'\x00\t', b'\x01\x1c'], [b'\x00\n', b'\x01\xe1'],
                [b'\x00\n', b'\x01\xe0'], [b'\x00\t', b'\x01\x87'], [b'\x00\n', b'\x01\xdc'], [b'\x00\n', b'\x01\xdf'],
                [b'\x00\x07', b'\x00t'], [b'\x00\t', b'\x01\x9f'], [b'\x00\x08', b'\x00\x8d'],
                [b'\x00\x08', b'\x00\xe4'], [b'\x00\x07', b'\x00y'], [b'\x00\t', b'\x00\xea'], [b'\x00\t', b'\x00\xe1'],
                [b'\x00\x08', b'\x00@'], [b'\x00\x07', b'\x00A'], [b'\x00\t', b'\x01\x0b'], [b'\x00\t', b'\x00\xb0'],
                [b'\x00\x08', b'\x00j'], [b'\x00\x08', b'\x00\xc1'], [b'\x00\x07', b'\x00q'], [b'\x00\x07', b'\x00x'],
                [b'\x00\x08', b'\x00\xb1'], [b'\x00\t', b'\x01L'], [b'\x00\x07', b'\x00C'], [b'\x00\x08', b'\x00v'],
                [b'\x00\x07', b'\x00f'], [b'\x00\x07', b'\x00M'], [b'\x00\t', b'\x00\x8a'], [b'\x00\x06', b'\x00/'],
                [b'\x00\x08', b'\x00\xc9'], [b'\x00\t', b'\x00\xce'], [b'\x00\t', b'\x01I'], [b'\x00\t', b'\x01`'],
                [b'\x00\n', b'\x01\xba'], [b'\x00\n', b'\x01\x9e'], [b'\x00\n', b'\x03\x9f'], [b'\x00\t', b'\x00\xe5'],
                [b'\x00\t', b'\x01\x94'], [b'\x00\t', b'\x01\x84'], [b'\x00\t', b'\x01&'], [b'\x00\x07', b'\x000'],
                [b'\x00\x08', b'\x00l'], [b'\x00\t', b'\x01!'], [b'\x00\t', b'\x01\xe8'], [b'\x00\n', b'\x01\xc1'],
                [b'\x00\n', b'\x01\x1d'], [b'\x00\n', b'\x01c'], [b'\x00\n', b'\x03\x85'], [b'\x00\n', b'\x03\xdb'],
                [b'\x00\n', b'\x01}'], [b'\x00\n', b'\x01\x06'], [b'\x00\n', b'\x03\x97'], [b'\x00\n', b'\x02N'],
                [b'\x00\x07', b'\x00.'], [b'\x00\x08', b'\x00\x98'], [b'\x00\n', b'\x03<'], [b'\x00\n', b'\x03.'],
                [b'\x00\n', b'\x01\xe9'], [b'\x00\t', b'\x00\xbf'], [b'\x00\n', b'\x03\xdf'], [b'\x00\n', b'\x01\xdd'],
                [b'\x00\n', b'\x03-'], [b'\x00\n', b'\x02\xed'], [b'\x00\n', b'\x03\x0b'], [b'\x00\n', b'\x01\x07'],
                [b'\x00\n', b'\x02\xe8'], [b'\x00\n', b'\x03\xde'], [b'\x00\n', b'\x01%'], [b'\x00\n', b'\x01\xe8'],
                [b'\x00\t', b'\x00\xe9'], [b'\x00\n', b'\x01\xcd'], [b'\x00\n', b'\x01\xb5'], [b'\x00\t', b'\x01e'],
                [b'\x00\n', b'\x022'], [b'\x00\n', b'\x02\xe1'], [b'\x00\x0b', b'\x03\xae'], [b'\x00\x0b', b'\x03\xc6'],
                [b'\x00\x0b', b'\x03\xe2'], [b'\x00\n', b'\x02\x05'], [b'\x00\n', b'\x02\x9a'], [b'\x00\n', b'\x02H'],
                [b'\x00\n', b'\x02\xcd'], [b'\x00\n', b'\x02;'], [b'\x00\x0b', b'\x03\xc5'], [b'\x00\n', b'\x02Q'],
                [b'\x00\n', b'\x02\xe9'], [b'\x00\n', b'\x02R'], [b'\x00\t', b'\x01\xea'], [b'\x00\x0b', b'\x03\xa0'],
                [b'\x00\x0b', b'\x03\x91'], [b'\x00\n', b'\x02<'], [b'\x00\x0b', b'\x03\x92'],
                [b'\x00\x0b', b'\x03\xd5'], [b'\x00\n', b'\x023'], [b'\x00\n', b'\x02\xcc'], [b'\x00\x0b', b'\x03\x90'],
                [b'\x00\n', b'\x01\xbb'], [b'\x00\x0b', b'\x03\xa1'], [b'\x00\x0b', b'\x03\xc4'],
                [b'\x00\n', b'\x02\x11'], [b'\x00\n', b'\x02\x03'], [b'\x00\t', b'\x01*'], [b'\x00\n', b'\x021'],
                [b'\x00\x0b', b'\x03\xe0'], [b'\x00\n', b'\x02\x9b'], [b'\x00\x0b', b'\x03\xd7'],
                [b'\x00\n', b'\x02\x02'], [b'\x00\x0b', b'\x03\xad'], [b'\x00\n', b'\x02\x13'], [b'\x00\n', b'\x02S'],
                [b'\x00\n', b'\x03,'], [b'\x00\n', b'\x02='], [b'\x00\n', b'\x02?'], [b'\x00\n', b'\x03/'],
                [b'\x00\n', b'\x01\x1c'], [b'\x00\n', b'\x03\x84'], [b'\x00\n', b'\x03\x1c'], [b'\x00\n', b'\x01|'],
                [b'\x00\n', b'\x03\n'], [b'\x00\n', b'\x02\xe0'], [b'\x00\n', b'\x02v'], [b'\x00\n', b'\x02P'],
                [b'\x00\x0b', b'\x03\xe3'], [b'\x00\n', b'\x03\x96'], [b'\x00\n', b'\x01\x8f'],
                [b'\x00\n', b'\x02\x04'], [b'\x00\n', b'\x02\x06'], [b'\x00\n', b'\x020'], [b'\x00\n', b'\x02e'],
                [b'\x00\n', b'\x02\x12'], [b'\x00\n', b'\x02>'], [b'\x00\x0b', b'\x03\xac'], [b'\x00\x0b', b'\x03\x93'],
                [b'\x00\x0b', b'\x03\xe1'], [b'\x00\n', b'\x01\xde'], [b'\x00\x0b', b'\x03\xd6'],
                [b'\x00\n', b'\x03\x1d'], [b'\x00\x0b', b'\x03\xe5'], [b'\x00\x0b', b'\x03\xe4'],
                [b'\x00\n', b'\x02\x07'], [b'\x00\x0b', b'\x03\xc7'], [b'\x00\n', b'\x02w'], [b'\x00\x0b', b'\x03\xd4'],
                [b'\x00\x08', b'\x00\xc0'], [b'\x00\n', b'\x01b'], [b'\x00\n', b'\x03\xda'], [b'\x00\n', b'\x01$'],
                [b'\x00\n', b'\x01\xb4'], [b'\x00\n', b'\x02d'], [b'\x00\n', b'\x03='], [b'\x00\n', b'\x01\xd1'],
                [b'\x00\n', b'\x01\xaf'], [b'\x00\n', b'\x03\x9e'], [b'\x00\n', b'\x02O'], [b'\x00\x0b', b'\x03s'],
                [b'\x00\n', b'\x02I'], [b'\x00\x0b', b'\x03r'], [b'\x00\t', b'\x01g'], [b'\x00\n', b'\x02\x10'],
                [b'\x00\n', b'\x02:'], [b'\x00\n', b'\x01\xb8'], [b'\x00\x0b', b'\x03\xaf'], [b'\x00\n', b'\x01\x8e'],
                [b'\x00\n', b'\x02\xec'], [b'\x00\x07', b'\x00b'], [b'\x00\x04', b'\x00\r']]


    def compress(self, source):
        print("No Compress: ",source)
        size = len(source)
        print("Size no compress: ",size)
        retval = []
        current = val = cBits = 0
        packetReturn = b''

        m = 0
        while m < size:
            nrBits = int.from_bytes(self.huffmanTable[source[m]][0], "big") - 1
            val = int.from_bytes(self.huffmanTable[source[m]][1], "big")

            n = nrBits

            while n >= 0:
                x = (val >> n) % 2
                current = current << 1
                current += x
                cBits += 1
                if 8 == cBits:
                    retval.append(current)
                    cBits = 0
                n -= 1

            m += 1

        nrBits = int.from_bytes(self.huffmanTable[256][0], "big") - 1
        val = int.from_bytes(self.huffmanTable[256][0], "big")

        n = nrBits

        while n >= 0:
            x = (val >> n) % 2
            current <<= 1
            current += x
            cBits += 1
            if 8 == cBits:
                retval.append(current)
                cBits = 0
            n -= 1

        while 0 != cBits:
            current <<= 1
            cBits += 1

            if 8 == cBits:
                retval.append(current)
                current = 0
                cBits = 0

        packetReturn = retval[0].to_bytes(1, "big")
        for i in range(1,len(retval)):
            packetReturn += str.encode(chr(retval[i] & 255))

        print("Compressed: ", packetReturn)
        print("Compressed Size: ", len(packetReturn))
        return packetReturn

    def decompress(self,source):
        m_tree = self.createTree()

        retval = bytearray()
        current = val = 0
        size = len(source)
        currentNode = m_tree
        packetReturn = b''

        for i in range(0,size):
            current = source[i]

            n = 7
            while n >= 0:
                x = (current >> n) % 2
                if 0 == x:
                    currentNode = currentNode.right
                else:
                    currentNode = currentNode.left

                if True == currentNode.isLeaf:
                    val = currentNode.value
                    currentNode = m_tree

                if 256 == val:
                    for packet in retval:
                        packetReturn += packet

                    return packetReturn

                if len(retval) == 0 and val == 0:
                    continue

                retval.append(val)

                n -= 1

        for packet in retval:
            packetReturn += packet

        return packetReturn

    def createTree(self):
        mTree = TreeNode()

        nrBits = val = 0

        i = 0
        while i < 257:
            current = mTree

            nrBits = int.from_bytes(self.huffmanTable[i][0], "big") - 1
            val = int.from_bytes(self.huffmanTable[i][0], "big")

            n = nrBits
            while n >= 0:
                if ((val >> n) % 2) == 1:
                    if None == current.left:
                        current.left = TreeNode()
                    current = current.left
                else:
                    if None == current.right:
                        current.right = TreeNode()
                    current = current.right
                n -= 1

            current.isLeaf = True
            current.value = i

            i += 1

        return mTree

class TreeNode:
    isLeaf = False
    value = 0
    left = None
    right = None