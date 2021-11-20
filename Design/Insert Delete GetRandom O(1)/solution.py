class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        last, idx = self.arr[-1], self.map[self.arr[-1]]
        remove, idxRemove = val, self.map[val]
        self.arr[idxRemove] = last
        self.map[last] = idxRemove
        del self.map[remove]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        rand = randint(0, len(self.arr) - 1)
        return self.arr[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()