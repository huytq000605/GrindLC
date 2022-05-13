class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.dict = dict()
        m = len(blacklist)
        self.n = n - 1 - m
        n -= 1
        blacklist = set(blacklist)
        for value in blacklist:
            if value <= self.n:
                while n in blacklist:
                    n -= 1
                self.dict[value] = n
                n -= 1

    def pick(self) -> int:
        r = random.randint(0, self.n)
        return self.dict.get(r, r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()