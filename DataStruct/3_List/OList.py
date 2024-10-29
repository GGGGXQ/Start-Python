class ListNode:
    def __init__(self, item):
        self.data = item
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class OrderList:
    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = ListNode(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() is item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        if found:
            previous.set_next(current.get_next())

        if stop or current is None:
            raise ValueError("404 NOT FOUND")

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() is item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                current = current.get_next()
        return found

    def is_empty(self):
        return self.head is None

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def index(self, item):
        count = 0
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() is item:
                found = True
            elif current.get_data() > item:
                return -1
            else:
                current = current.get_next()
                count = count + 1
        return count

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
        found = False
        while current is not None and not found:
            if pos < 0 or pos > self.length():
                raise IndexError("out of range")
            elif count is pos:
                found = True
            else:
                previous = current
                current = current.get_next()
                count = count + 1
        previous.set_next(current.get_next())
        return current.get_data()
