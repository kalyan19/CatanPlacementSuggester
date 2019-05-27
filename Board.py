from Hex import Hex
from Vertex import Vertex
from collections import deque

class Board:

    NUM_HEX = 19
    RESOURCES = ["SHEEP", "HAY", "ORE", "WOOD", "BRICK", "DESERT"]
    START_VERTEX_IDX = 1

    def __init__(self):
        self.HEX_TO_VERTICES = self.buildHexToVerticesTable()
        self.hexs, self.vertices = self.generateStaticBoard()

    def visualizeBoard(self):
        ABBRV_TABLE = {"SHEEP": "S", "HAY": "H", "ORE": "O", "WOOD": "W", "BRICK": "B", "DESERT": "D"}
        hexsAsList = [[""]*5 for i in range(5)]

        hexIdx = 1
        for i in range(0,3):
            hexsAsList[0][i] =  "{} ({})".format(ABBRV_TABLE[self.hexs[hexIdx].resource], self.hexs[hexIdx].value)
            hexIdx += 1
        for i in range(0,4):
            hexsAsList[1][i] = "{} ({})".format(ABBRV_TABLE[self.hexs[hexIdx].resource], self.hexs[hexIdx].value)
            hexIdx += 1
        for i in range(0,5):
            hexsAsList[2][i] = "{} ({})".format(ABBRV_TABLE[self.hexs[hexIdx].resource], self.hexs[hexIdx].value)
            hexIdx += 1
        for i in range(0,4):
            hexsAsList[3][i] =  "{} ({})".format(ABBRV_TABLE[self.hexs[hexIdx].resource], self.hexs[hexIdx].value)
            hexIdx += 1
        for i in range(0,3):
            hexsAsList[4][i] = "{} ({})".format(ABBRV_TABLE[self.hexs[hexIdx].resource], self.hexs[hexIdx].value)
            hexIdx += 1

        for line in hexsAsList:
            print('  '.join(line))

    # returns only vertices that are available
    def getLegalMoves(self):
        # traverse vertex graph via BFS
        verticesSeen = set()
        legalVertices = []
        q = deque()
        startVert = self.vertices[self.START_VERTEX_IDX]
        q.append(startVert)
        verticesSeen.add(startVert)
        while q:
            v = q.popleft()
            if v.available:
                legalVertices.append(v)
            for neigh in v.neighbors:
                if neigh not in verticesSeen:
                    verticesSeen.add(neigh)
                    q.append(neigh)

        return legalVertices

    def acceptMove(self, occupiedVertex):

        if not occupiedVertex.available:
            raise Exception("Illegal move. This vertex is unavailable.")

        # update this vertex and its neighbors
        occupiedVertex.available = False
        for neigh in occupiedVertex.neighbors:
            neigh.available = False

    # gives a mapping between a hex and all of its vertices
    # Note: hex and vertices start at index 1
    def buildHexToVerticesTable(self):

        table = {}

        table[1] = [1, 2, 3, 9, 10, 11]
        table[2] = [3, 4, 5, 11, 12, 13]
        table[3] = [5, 6, 7, 13, 14, 15]
        table[4] = [8, 9, 10, 18, 19, 20]
        table[5] = [10, 11, 12, 20, 21, 22]
        table[6] = [12, 13, 14, 22, 23, 24]
        table[7] = [14, 15, 16, 24, 25, 26]
        table[8] = [17, 18, 19, 28, 29, 30]
        table[9] = [19, 20, 21, 30, 31, 32]
        table[10] = [21, 22, 23, 32, 33, 34]
        table[11] = [23, 24, 25, 34, 35, 36]
        table[12] = [25, 26, 27, 36, 37, 38]
        table[13] = [29, 30, 31, 39, 40, 41]
        table[14] = [31, 32, 33, 41, 42, 43]
        table[15] = [33, 34, 35, 43, 44, 45]
        table[16] = [35, 36, 37, 45, 46, 47]
        table[17] = [40, 41, 42, 48, 49, 50]
        table[18] = [42, 43, 44, 50, 51, 52]
        table[19] = [44, 45, 46, 52, 53, 54]

        return table

    def generateStaticBoard(self):

        # top left to bottom right
        # Hexs and Vertices start at index 1
        hexs = [None]*(self.NUM_HEX+1)
        hexs[1] = Hex("WOOD", 6)
        hexs[2] = Hex("HAY", 5)
        hexs[3] = Hex("ORE", 9)
        hexs[4] = Hex("BRICK", 4)
        hexs[5] = Hex("SHEEP", 3)
        hexs[6] = Hex("BRICK", 8)
        hexs[7] = Hex("ORE", 10)
        hexs[8] = Hex("ORE", 6)
        hexs[9] = Hex("SHEEP", 5)
        hexs[10] = Hex("DESERT", 0)
        hexs[11] = Hex("HAY", 9)
        hexs[12] = Hex("SHEEP", 12)
        hexs[13] = Hex("BRICK", 3)
        hexs[14] = Hex("WOOD", 2)
        hexs[15] = Hex("HAY", 10)
        hexs[16] = Hex("WOOD", 11)
        hexs[17] = Hex("HAY", 11)
        hexs[18] = Hex("WOOD", 4)
        hexs[19] = Hex("SHEEP", 8)

        vertices = [None] + [Vertex() for i in range(54)]

        # add vertices for each hex
        for i in range(1,len(hexs)):
            hex = hexs[i]
            vertIndices = self.HEX_TO_VERTICES[i]
            hexVertices = [vertices[ind] for ind in vertIndices]
            self.addHexVertices(hex, hexVertices)

        # add neighbors for each vertex

        # for each row
        for i in range(1,7):
            vert1, vert2 = vertices[i], vertices[i+1]
            self.addEdge(vert1, vert2)

        for i in range(8,16):
            vert1, vert2 = vertices[i], vertices[i+1]
            self.addEdge(vert1, vert2)

        for i in range(17,27):
            vert1, vert2 = vertices[i], vertices[i+1]
            self.addEdge(vert1, vert2)

        for i in range(28,38):
            vert1, vert2 = vertices[i], vertices[i+1]
            self.addEdge(vert1, vert2)

        for i in range(39,47):
            vert1, vert2 = vertices[i], vertices[i + 1]
            self.addEdge(vert1, vert2)

        for i in range(48,54):
            vert1, vert2 = vertices[i], vertices[i + 1]
            self.addEdge(vert1, vert2)

        # for the columns
        OFFSET = 8 - 1 + 1 # +1 b/c the rows are increasing
        for i in range(1,8,2):
            vert1, vert2 = vertices[i], vertices[i + OFFSET]
            self.addEdge(vert1, vert2)

        OFFSET = 17 - 8 + 1 # +1 b/c the rows are increasing
        for i in range(8,17,2):
            vert1, vert2 = vertices[i], vertices[i + OFFSET]
            self.addEdge(vert1, vert2)

        OFFSET = 28 - 17 + 0 # +0 b/c this is the biggest row, so no change
        for i in range(17,28,2):
            vert1, vert2 = vertices[i], vertices[i + OFFSET]
            self.addEdge(vert1, vert2)

        OFFSET = 39 - 28 - 1 # -1 b/c the rows are decreasing
        for i in range(29,39,2):
            vert1, vert2 = vertices[i], vertices[i + OFFSET]
            self.addEdge(vert1, vert2)

        OFFSET = 48 - 39 - 1  # -1 b/c the rows are decreasing
        for i in range(40, 48, 2):
            vert1, vert2 = vertices[i], vertices[i + OFFSET]
            self.addEdge(vert1, vert2)

        return [hexs, vertices]


    def addHexVertices(self, hex, hexVertices):
        for vertex in hexVertices:
            self.addHexVertex(hex, vertex)

    def addHexVertex(self, hex, vertex):
        hex.addVertex(vertex)
        vertex.addHex(hex)

    def addEdge(self, vert1, vert2):
        vert1.addNeighbor(vert2)
        vert2.addNeighbor(vert1)




b = Board()
b.visualizeBoard()
l = b.getLegalMoves()
b.acceptMove(l[0])