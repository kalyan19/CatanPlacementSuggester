class Hex:

    NUM_VERTICES = 6

    def __init__(self, resource, value):
        self.resource = resource.upper()
        self.vertices = []
        self.value = value

    def addVertex(self, vertex):
        self.vertices.append(vertex)
        if len(self.vertices) > self.NUM_VERTICES:
            raise Exception("This hex has too many vertices")