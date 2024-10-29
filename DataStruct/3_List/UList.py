class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def is_empty(self):
        return self.head is None

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def append(self, item):
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        temp = Node(item)
        current.set_next(temp)

    def index(self, item):
        count = 0
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                count = count + 1
        if count == 0:
            return -1
        else:
            return count

    def insert(self, pos, item):
        if self.length() < pos < 0:
            raise ValueError("Index out of range")
        count = 0
        current = self.head
        while current is not None and count is not pos:
            current = current.get_next()
            count = count + 1
        temp = Node(item)
        temp.set_next(current.get_next())
        current.set_next(temp)

    def pop(self):
        current = self.head
        previous = None
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        previous.set_next(None)
        return current.get_data()

    def pos_pop(self, pos):
        count = 0
        current = self.head
        previous = None
        if 0 > pos > self.length():
            raise ValueError("Index out of range")
        while current is not None and count is not pos:
            count = count + 1
            previous = current
            current = current.get_next()
        previous.set_next(current.get_next())
        return current.get_data()
