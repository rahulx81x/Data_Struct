class HashTable:
    def __init__(self):
        self.arr = [[] for i in range(10)]

    def hash_func(self, key):
        hash_no = 0
        for char in key:
            hash_no += ord(char)
        hash_no = hash_no % 10
        return hash_no

    def add(self, key, value):
        index = self.hash_func(key)
        self.arr[index].append((key, value))

    def get(self, key):
        index = self.hash_func(key)
        for pair in self.arr[index]:
            if pair[0] == key:
                return pair[1]

    def delete(self, key):
        index = self.hash_func(key)
        for j in range(len(self.arr[index])):
            if self.arr[index][j][0] == key:
                self.arr[index].pop(j)

    def whole(self):
        for element in self.arr:

            print(element)
