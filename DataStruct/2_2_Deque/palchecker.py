class Deque:
    def __init__(self):
        self.items = []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
def palchecker(astring):
    chardeque = Deque()
    for ch in astring:
        chardeque.addRear(ch)
    stillEuqal = True
    while chardeque.size() > 1 and stillEuqal:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEuqal = False

    return stillEuqal
if __name__ == '__main__':
    print(palchecker('hello'))
    print(palchecker('toot'))
    print(palchecker('abcba'))