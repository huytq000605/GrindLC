class Solution:
    def tribonacci(self, n: int) -> int:
        last = [0, 1, 1]
        if n < 3:
            return last[n]
        while n-2:
            new = sum(last)
            last[0], last[1], last[2] = last[1], last[2], new
            n -= 1
        return last[-1]
