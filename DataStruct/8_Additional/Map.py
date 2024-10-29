from random import randrange
from pythonds import Stack


def flip():
    return randrange(2)


class HeaderNode:
    def __init__(self):
        self.next = None
        self.down = None

    def get_map_next(self):
        return self.next

    def get_map_down(self):
        return self.down

    def set_map_next(self, new_next):
        self.next = new_next

    def set_map_down(self, new_down):
        self.down = new_down


class DataNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.next = None
        self.down = None

    def get_map_key(self):
        return self.key

    def get_map_value(self):
        return self.value

    def get_map_next(self):
        return self.next

    def get_map_down(self):
        return self.down

    def set_map_value(self, new_value):
        self.value = new_value

    def set_map_key(self, new_key):
        self.key = new_key

    def set_map_down(self, new_down):
        self.down = new_down

    def set_map_next(self, new_next):
        self.next = new_next


class SkipList:
    def __init__(self):
        self.head = None

# O(log n)
    def search(self, key):
        current = self.head
        found = False
        stop = False
        while not found and not stop:
            if current is None:
                stop = True
            else:
                if current.get_map_next().get_map_key() is key:
                    found = True
                else:
                    if key < current.get_map_next().get_map_key():
                        current = current.get_map_down()
                    else:
                        current = current.get_map_next()
        if found:
            return current.get_map_next().get_map_value()
        else:
            return None

# O(log n)
    def insert(self, key, value):
        if self.head is None:
            self.head = HeaderNode()
            temp = DataNode()
            temp.set_map_value(value)
            temp.set_map_key(key)
            self.head.set_map_next(temp)
            top = temp
            while flip() is 1:
                new_head = HeaderNode()
                temp = DataNode()
                temp.set_map_value(value)
                temp.set_map_key(key)
                temp.set_map_down(top)
                new_head.set_map_next(temp)
                new_head.set_map_down(self.head)
                self.head = new_head
                top = temp
        else:
            tower_stack = Stack()
            current = self.head
            stop = False
            while not stop:
                if current is None:
                    stop = True
                else:
                    if current.get_map_next() is None:
                        tower_stack.push(current)
                        current = current.get_map_down()
                    else:
                        if current.get_map_next().get_map_key() > key:
                            tower_stack.push(current)
                            current = current.get_map_down()
                        else:
                            current = current.get_map_next()
                lowest_level = tower_stack.pop()
                temp = DataNode()
                temp.set_map_value(value)
                temp.set_map_key(key)
                temp.set_map_next(lowest_level.get_map_next())
                lowest_level.set_map_next(temp)
                top = temp
                while flip() is 1:
                    if tower_stack.isEmpty():
                        new_head = HeaderNode()
                        temp = DataNode()
                        temp.set_map_value(value)
                        temp.set_map_key(key)
                        temp.set_map_down(top)
                        new_head.set_map_next(temp)
                        new_head.set_map_down(self.head)
                        top = temp
                    else:
                        next_level = tower_stack.pop()
                        temp = DataNode()
                        temp.set_map_value(value)
                        temp.set_map_key(key)
                        temp.set_map_down(top)
                        temp.set_map_next(next_level.get_map_next())
                        next_level.set_map_next(map)
                        top = temp


class Map:
    def __init__(self):
        self.collection = SkipList()

    def put(self, key, value):
        self.collection.insert(key, value)

    def get(self, key):
        return self.collection.search(key)