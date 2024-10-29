import sys
from pythonds.graphs import Graph, PriorityQueue, Vertex


def prim(g, start):
    pq = PriorityQueue()
    for v in g:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in g])
    while not pq.isEmpty():
        current_vert = pq.delMin()
        for next_vert in current_vert.getConnections():
            new_cost = current_vert.getWeight(next_vert) + current_vert.getDistance()
            if next_vert in pq and new_cost < next_vert.getDistance():
                next_vert.setDistance(new_cost)
                next_vert.setPred(current_vert)
                pq.decreaseKey(next_vert, new_cost)
