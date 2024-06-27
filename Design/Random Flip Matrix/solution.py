class Solution:

    def __init__(self, m: int, n: int):
        self.r = m
        self.c = n
        self.n = m*n
        self.values = dict()

    def flip(self) -> List[int]:
        i = random.randint(0, self.n-1)
        ret = self.values.get(i, i)
        self.n -= 1
        
        self.values[i] = self.values.get(self.n, self.n)
        self.values[self.n] = ret
        
        return [ret // self.c, ret % self.c]


    def reset(self) -> None:
        self.n = self.r * self.c


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
