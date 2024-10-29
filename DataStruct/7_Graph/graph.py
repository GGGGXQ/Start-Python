class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = { }

    def add_neighbor(self, nbr, weight):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

    def get_id(self):
        return self.id

    def get_connected_to(self):
        return self.connected_to

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vert_list = { }
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vert_list:
            nv = self.add_vertex(from_vert)
        if to_vert not in self.vert_list:
            nv = self.add_vertex(to_vert)
        self.vert_list[from_vert].add_neighbor(self.vert_list[to_vert], weight)

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def __contains__(self, n):
        return n in self.vert_list


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.vert_list)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g:
        for w in v.get_connected_to():
            print("( %s , %s ) " % (v.get_id(), w.get_id()))