
class UOCompression:

    def __init__(self):
        self.huffmanTable = [(2,0),(5,31),(6,34),(7,52),(7,117),(6,40),(6,59),(7,50),(8,224),(8,98),(7,86),(8,121),
                            (9,413),(8,151),(6,42),(7,87),(8,113),(8,91),(9,460),(8,167),(7,37),(7,79),(8,102),
                            (8,125),(9,401),(9,462),(7,63),(9,144),(8,89),(8,123),(8,145),(8,198),(6,45),(9,390),
                            (8,111),(9,147),(10,460),(8,90),(10,430),(10,448),(9,328),(9,330),(9,130),(10,415),
                            (9,369),(9,288),(9,231),(10,499),(9,331),(9,256),(9,400),(6,19),(9,353),(9,293),(9,307),
                            (9,405),(9,371),(9,458),(9,134),(9,489),(9,219),(9,492),(9,139),(9,133),(5,10),(8,150),
                            (8,156),(9,451),(9,412),(9,143),(9,399),(9,145),(9,135),(9,198),(9,375),(9,137),(9,214),
                            (9,140),(9,494),(9,491),(9,132),(9,356),(9,373),(9,461),(8,94),(9,136),(9,299),(9,370),
                            (9,266),(9,141),(9,314),(9,284),(10,481),(10,480),(9,391),(10,476),(10,479),(7,116),
                            (9,415),(8,141),(8,228),(7,121),(9,234),(9,225),(8,64),(7,65),(9,267),(9,176),(8,106),
                            (8,193),(7,113),(7,120),(8,177),(9,332),(7,67),(8,118),(7,102),(7,77),(9,138),(6,47),
                            (8,201),(9,206),(9,329),(9,352),(10,442),(10,414),(10,927),(9,229),(9,404),(9,388),
                            (9,294),(7,48),(8,108),(9,289),(9,488),(10,449),(10,285),(10,355),(10,901),(10,987),
                            (10,381),(10,262),(10,919),(10,590),(7,46),(8,152),(10,828),(10,814),(10,489),(9,191),
                            (10,991),(10,477),(10,813),(10,749),(10,779),(10,263),(10,744),(10,990),(10,293),
                            (10,488),(9,233),(10,461),(10,437),(9,357),(10,562),(10,737),(11,942),(11,966),(11,994),
                            (10,517),(10,666),(10,584),(10,717),(10,571),(11,965),(10,593),(10,745),(10,594),(9,490),
                            (11,928),(11,913),(10,572),(11,914),(11,981),(10,563),(10,716),(11,912),(10,443),
                            (11,929),(11,964),(10,529),(10,515),(9,298),(10,561),(11,992),(10,667),(11,983),(10,514),
                            (11,941),(10,531),(10,595),(10,812),(10,573),(10,575),(10,815),(10,284),(10,900),
                            (10,796),(10,380),(10,778),(10,736),(10,630),(10,592),(11,995),(10,918),(10,399),
                            (10,516),(10,518),(10,560),(10,613),(10,530),(10,574),(11,940),(11,915),(11,993),
                            (10,478),(11,982),(10,797),(11,997),(11,996),(10,519),(11,967),(10,631),(11,980),
                            (8,192),(10,354),(10,986),(10,292),(10,436),(10,612),(10,829),(10,465),(10,431),
                            (10,926),(10,591),(11,883),(10,585),(11,882),(9,359),(10,528),(10,570),(10,440),
                            (11,943),(10,398),(10,748),(7,98),(4,13)]

    def compress(self, source):
        size = len(source)
        retval = []
        current = cBits = 0

        m = 0
        while m < size:
            nrBits = self.huffmanTable[source[m]][0] - 1
            val = self.huffmanTable[source[m]][1]

            n = nrBits
            while n >= 0:
                x = (val >> n) % 2
                current <<= 1
                current += x
                cBits += 1
                if 8 == cBits:
                    retval.append(current & 0xFF)
                    cBits = 0
                n -= 1
            m += 1

        nrBits = self.huffmanTable[256][0] - 1
        val = self.huffmanTable[256][1]

        w = nrBits

        while w >= 0:
            x = (val >> w) % 2
            current <<= 1
            current += x
            cBits += 1
            if 8 == cBits:
                retval.append(current & 0xFF)
                cBits = 0
            w -= 1

        while 0 != cBits:
            current <<= 1
            cBits += 1

            if 8 == cBits:
                retval.append(current & 0xFF)
                current = 0
                cBits = 0

        packetReturn = b''

        for i in range(len(retval)):
            packetReturn += retval[i].to_bytes(1, "big")

        return packetReturn

    def decompress(self,source):

        m_tree = self.createTree()

        retval = []
        current = val = 0
        size = len(source)
        currentNode = m_tree
        packetReturn = b''

        i = 0
        while i < size:
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
                        packetReturn += packet.to_bytes(1, "big")

                    return packetReturn

                if len(retval) == 0 and val == 0:
                    continue

                retval.append(val)

                n -= 1
            i += 1

        for packet in retval:
            packetReturn += packet.to_bytes(1, "big")


        print(packetReturn)

        return packetReturn

    def createTree(self):
        mTree = TreeNode()

        nrBits = val = 0

        i = 0
        while i < 257:
            current = mTree

            nrBits = self.huffmanTable[i][0] - 1
            val = self.huffmanTable[i][1]

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