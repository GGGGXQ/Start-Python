class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] is key:
                self.data[hash_value] = data
            else:
                next_hash = self.rehash(hash_value, len(self.slots))
                while self.slots[next_hash] is not None and self.slots[next_hash] is not key:
                    next_hash = self.rehash(next_hash, len(self.slots))
                if self.slots[next_hash] is None:
                    self.slots[next_hash] = key
                    self.data[next_hash] = data
                else:
                    self.data[next_hash] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_hash = self.hash_function(key, len(self.slots))
        data = None
        found = False
        stop = False
        position = start_hash
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] is key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position is start_hash:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == '__main__':
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    print(H[17])
    print(H[20])
    H[20] = "duck"
    print(H[20])
    print(H.data)
    print(H[99])