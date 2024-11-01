from typing import TypeVar, Generic, List
from edge import Edge
from Algorithm.Searching.generic_search import bfs, Node, node_to_path

V = TypeVar('V')


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = None, directed: bool = False) -> None:
        if vertices is None:
            vertices = []
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]
        self.directed = directed

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))

    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        if not self.directed:
            self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    def remove_vertex_by_index(self, index: int) -> None:
        edges = self.edges_for_index(index)
        if not self.directed:
            for edge in edges:
                self._edges[edge.v].remove(edge.reversed())
        self._vertices.pop(index)
        self._edges.pop(index)
        for i in range(len(self._edges)):
            self._edges[i] = [Edge(e.u if e.u < index else e.u - 1,
                                   e.v if e.v < index else e.v - 1) for e in self._edges[i]]

    def remove_vertex_by_vertex(self, vertex: V) -> None:
        index = self.index_of(vertex)
        self.remove_vertex_by_index(index)

    def remove_edge(self, edge: Edge) -> None:
        if edge.u < self.vertex_count and edge.v < self.vertex_count:
            self._edges[edge.u].remove(edge)
            if not self.directed:
                self._edges[edge.v].remove(edge.reversed())

    def remove_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.remove_edge(edge)

    def remove_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.remove_edge(Edge(u, v))

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc


# if __name__ == "__main__":
#     city_graph = Graph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston",
#                         "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])
#     city_graph.add_edge_by_vertices("Seattle", "Chicago")
#     city_graph.add_edge_by_vertices("Seattle", "San Francisco")
#     city_graph.add_edge_by_vertices("San Francisco", "Riverside")
#     city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
#     city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
#     city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
#     city_graph.add_edge_by_vertices("Riverside", "Phoenix")
#     city_graph.add_edge_by_vertices("Phoenix", "Chicago")
#     city_graph.add_edge_by_vertices("Phoenix", "Dallas")
#     city_graph.add_edge_by_vertices("Dallas", "Atlanta")
#     city_graph.add_edge_by_vertices("Dallas", "Chicago")
#     city_graph.add_edge_by_vertices("Dallas", "Houston")
#     city_graph.add_edge_by_vertices("Houston", "Atlanta")
#     city_graph.add_edge_by_vertices("Houston", "Miami")
#     city_graph.add_edge_by_vertices("Atlanta", "Chicago")
#     city_graph.add_edge_by_vertices("Atlanta", "Washington")
#     city_graph.add_edge_by_vertices("Atlanta", "Miami")
#     city_graph.add_edge_by_vertices("Miami", "Washington")
#     city_graph.add_edge_by_vertices("Chicago", "Detroit")
#     city_graph.add_edge_by_vertices("Detroit", "Boston")
#     city_graph.add_edge_by_vertices("Detroit", "Washington")
#     city_graph.add_edge_by_vertices("Detroit", "New York")
#     city_graph.add_edge_by_vertices("Boston", "New York")
#     city_graph.add_edge_by_vertices("New York", "Philadelphia")
#     city_graph.add_edge_by_vertices("Philadelphia", "Washington")
#     bfs_result = bfs("Boston", lambda x: x == "Miami", city_graph.neighbors_for_vertex)
#     if bfs_result is None:
#         print("No path found")
#     else:
#         path = node_to_path(bfs_result)
#         print("Path from Boston to Miami")
#         print(path)


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D']
    graph = Graph(vertices, directed=False)
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('A', 'D'),
        ('B', 'C'),
        ('B', 'D'),
        ('C', 'D'),
        ('A', 'B'),
    ]
    for first, second in edges:
        graph.add_edge_by_vertices(first, second)
    print(graph)

    # 判断每个顶点的度数
    degree_count = {vertex: 0 for vertex in vertices}
    for i in range(graph.vertex_count):
        degree_count[graph.vertex_at(i)] = len(graph.edges_for_index(i))

    # 计算奇数度数的顶点数量
    odd_degree_vertices = sum(1 for count in degree_count.values() if count % 2 == 1)

    # 判断欧拉路径的条件
    if odd_degree_vertices <= 2:
        print("存在一条经过每座桥一次且仅一次的路径。")
    else:
        print("不存在这样的路径。")
