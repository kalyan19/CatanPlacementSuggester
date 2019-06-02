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

    def getScore(self):
        return sum([hex.getScore() for hex in self.hexs])

    def getResources(self):
        return [hex.resource for hex in self.hexs]

    def getValues(self):
        return [hex.value for hex in self.hexs]

    def __str__(self):
        return "hexs = {} with score = {}".format([hex.resource for hex in self.hexs], self.getScore())

    def __repr__(self):
        return self.__str__()