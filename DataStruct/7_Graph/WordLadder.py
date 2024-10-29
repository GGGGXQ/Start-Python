from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def build_graph(word_file):
    d = {}
    g = Graph()
    w_file = open(word_file, 'r')
    # 创建词桶
    for line in w_file:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # 为同一个桶中的单词添加顶点和边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 is not word2:
                    g.addEdge(word1, word2)
    return g


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vert_queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        current_vert = vert_queue.dequeue()
        for nbr in current_vert.getConnections():
            if nbr.getColor() is 'white':
                nbr.setColor('gray')
                nbr.setDistance(current_vert.getDistance() + 1)
                nbr.setPred(current_vert)
                vert_queue.enqueue(nbr)
        current_vert.setColor('black')
    traverse(g.getVertex('sage'))


def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())