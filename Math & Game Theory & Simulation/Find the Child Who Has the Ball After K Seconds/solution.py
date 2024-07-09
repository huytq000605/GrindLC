class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cycle = (n-1) * 2
        k %= cycle
        if k > n-1:
            return n-1-(k-n+1)
        return k
