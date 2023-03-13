class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time %= ((n-1) * 2)
        idx = 1 + time
        if idx > n:
            idx = n - (idx - n)
        return idx
        
