from pythonds.graphs import PriorityQueue, Graph, Vertex


# O((V+E)logV)
def dijkstra(a_graph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in a_graph])
    while not pq.isEmpty():
        current_vert = pq.delMin()
        for next_vert in current_vert.getConnections():
            new_dist = current_vert.getDistance() + current_vert.getWeight(next_vert)
            if new_dist < next_vert.getDistance():
                next_vert.setDistance(new_dist)
                next_vert.setPred(current_vert)
                pq.decreaseKey(next_vert, new_dist)
