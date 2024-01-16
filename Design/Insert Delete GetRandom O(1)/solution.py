class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dict = dict()

    def insert(self, val: int) -> bool:
        if val in self.dict: return False
        self.dict[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict: return False
        idx = self.dict[val]
        self.dict[self.arr[-1]] = idx
        self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
        self.dict.pop(self.arr.pop())
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
