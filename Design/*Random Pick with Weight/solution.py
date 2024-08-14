class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] = w[i-1] + w[i]
        self.w = w

    def pickIndex(self) -> int:
        v = randint(1, self.w[-1])
        start = 0
        end = len(self.w) - 1
        while start < end:
            mid = start + (end - start) // 2
            if self.w[mid] < v:
                start = mid + 1
            else:
                end = mid
        return start


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
