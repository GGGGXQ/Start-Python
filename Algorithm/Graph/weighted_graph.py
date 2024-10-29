from typing import TypeVar, Generic, List, Tuple
from graph import Graph
from weighted_edge import WeightedEdge

V = TypeVar('V')


class WeightedGraph(Generic[V], Graph[V]):
    def __init__(self, vertices: List[V] = None, directed=False) -> None:
        super().__init__(vertices, directed)
        if vertices is None:
            vertices = []
        self._vertices: List[V] = vertices
        self._edges: List[List[WeightedEdge]] = [[] for _ in vertices]
        self.directed = directed

    def add_edge_by_indices(self, u: int, v: int, weight: float = None) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first: V, second: V, weight: float = None) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    def weighted_edges_for_index(self, index: int) -> List[WeightedEdge]:
        return self._edges[index]

    def neighbors_for_index_with_weights(self, index: int) -> List[Tuple[V, float]]:
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.weighted_edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples

    def remove_vertex_by_index(self, index: int) -> None:
        edges = self.weighted_edges_for_index(index)
        if not self.directed:
            for edge in edges:
                self._edges[edge.v].remove(edge.reversed())
        self._vertices.pop(index)
        self._edges.pop(index)
        for i in range(len(self._edges)):
            self._edges[i] = [WeightedEdge(e.u if e.u < index else e.u - 1,
                                           e.v if e.v < index else e.v - 1, e.weight) for e in self._edges[i]]

    def remove_vertex_by_vertex(self, vertex: V) -> None:
        index = self.index_of(vertex)
        self.remove_vertex_by_index(index)

    def remove_edge(self, edge: WeightedEdge) -> None:
        if edge.u < self.vertex_count and edge.v < self.vertex_count:
            self._edges[edge.u].remove(edge)
            if not self.directed:
                self._edges[edge.v].remove(edge.reversed())

    def remove_edge_by_indices(self, u: int, v: int, weight=None) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.remove_edge(edge)

    def remove_edge_by_vertices(self, first: V, second: V, weight=None) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.remove_edge(WeightedEdge(u, v, weight))

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
        return desc


if __name__ == '__main__':
    city_graph2 = WeightedGraph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston",
                                 "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia",
                                 "Washington"])
    city_graph2.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph2.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph2.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph2.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph2.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph2.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph2.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph2.add_edge_by_vertices("Phoenix", "Chicago", 887)
    city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 1015)
    city_graph2.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph2.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph2.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph2.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph2.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph2.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph2.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph2.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph2.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph2.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph2.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph2.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph2.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph2.add_edge_by_vertices("Boston", "New York", 190)
    city_graph2.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph2.add_edge_by_vertices("Philadelphia", "Washington", 123)

    print(city_graph2)
    city_graph2.remove_vertex_by_vertex("Philadelphia")
    print("")
    print(city_graph2)
    print("")
    city_graph2.remove_edge_by_vertices("Washington", "Detroit", 396)
    print(city_graph2)
