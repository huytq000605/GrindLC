class RandomizedCollection:

    def __init__(self):
        self.idxs = defaultdict(set)
        self.arr = []

    def insert(self, val: int) -> bool:
        ret = val not in self.idxs
        self.idxs[val].add(len(self.arr))
        self.arr.append(val)
        return ret

    def remove(self, val: int) -> bool:
        if val not in self.idxs: return False
        # get the index we need to pop
        idx = self.idxs[val].pop()
        # if there is no more indexes of this value, remove
        if len(self.idxs[val]) == 0:
            self.idxs.pop(val)
        # if the index is the last index, just pop the arr
        if idx == len(self.arr) - 1:
            self.arr.pop()
            return True
        # otherwise, need to swap places
        self.arr[idx] = self.arr[-1]
        self.idxs[self.arr[-1]].remove(len(self.arr) - 1)
        self.idxs[self.arr[-1]].add(idx)
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
