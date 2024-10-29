from pythonds.graphs import Graph


# O(V+E)
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() is 'white':
                self.dfs_visit(aVertex)

    def dfs_visit(self, start_aVertex):
        start_aVertex.setColor('gray')
        self.time += 1
        start_aVertex.setDistance(self.time)
        for next_aVertex in start_aVertex.getConnections():
            if next_aVertex.getColor() is 'white':
                next_aVertex.setPred(start_aVertex)
                self.dfs_visit(next_aVertex)
        start_aVertex.setColor('black')
        self.time += 1
        start_aVertex.setFinish(self.time)
        