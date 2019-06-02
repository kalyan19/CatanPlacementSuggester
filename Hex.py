class Hex:

    NUM_VERTICES = 6

    valueToScore = {0:0, 2:1, 3:2, 4:3, 5:4, 6:5, 8:5, 9:4, 10:3, 11:2, 12:1}

    def __init__(self, resource, value):
        self.resource = self.validate(resource.upper())
        self.vertices = []
        self.value = value

    def addVertex(self, vertex):
        self.vertices.append(vertex)
        if len(self.vertices) > self.NUM_VERTICES:
            raise Exception("This hex has too many vertices. {}".format(self.vertices))

    def getScore(self):
        return self.valueToScore[self.value]

    def validate(self, resourceName):
        if resourceName not in {"SHEEP", "HAY", "ORE", "WOOD", "BRICK", "DESERT"}:
            raise Exception("Resource {} is not a valid resource".format(resourceName))
        return resourceName
