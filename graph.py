class Graph(object):

    def __init__(self):
        # make a dict of vertices
        self.vertices = {}

    def add_edge(self, value, source, destination):
        e = Edge(value, source, self.vertices[destination])
        if e in self.vertices[source].edges:
            self.vertices[source].edges[e] += 1
        else:
            self.vertices[source].edges[e] = 1

    def add_vertex(self, value):
        if value not in self.vertices:
            vert = Vertex(value)
            self.vertices[value] = vert


class Vertex(object):

    def __init__(self, value):
        # make a dict of adjacent edges with scratch as val
        self.edges = {}
        self.value = value

    def get_total_scratch(self):
        """ total scratch of all the edges for probability """
        return sum(e for e in self.edges.values())


class Edge(object):

    def __init__(self, value, source, destination):
        self.source = source
        self.destination = destination
        self.value = value
