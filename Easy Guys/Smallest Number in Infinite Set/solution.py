class SmallestInfiniteSet:

    def __init__(self):
        self.s = set()

    def popSmallest(self) -> int:
        res = 0
        for i in range(1, 1001):
            if i not in self.s:
                self.s.add(i)
                res = i
                break
        return res

    def addBack(self, num: int) -> None:
        self.s.discard(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
