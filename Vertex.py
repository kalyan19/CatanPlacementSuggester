class Vertex:

    MAX_EDGES = 3

    def __init__(self):
        self.available = True
        self.neighbors = []
        self.hexs = []

    def addNeighbor(self, vertexNeigh):
        self.neighbors.append(vertexNeigh)
        if len(self.neighbors) > self.MAX_EDGES:
            raise Exception("This vertex has too many neighbors")

    def addHex(self, hex):
        self.hexs.append(hex)
        if len(self.hexs) > self.MAX_EDGES:
            raise Exception("This vertex has too many hexs")
