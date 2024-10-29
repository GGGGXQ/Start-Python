class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
def hotPotato(namelist, num):
    simpleQueue = Queue()
    for name in namelist:
        simpleQueue.enqueue(name)
    while simpleQueue.size() > 1:
        for _ in range(num):
            simpleQueue.enqueue(simpleQueue.dequeue())
        simpleQueue.dequeue()
    return simpleQueue.dequeue()
if __name__ == '__main__':
    test1 = hotPotato(["Mike", "Tom", "Bill", "David", "Kent"], 10)
    print(test1)