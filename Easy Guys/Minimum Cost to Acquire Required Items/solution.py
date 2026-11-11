class Solution:
    def minimumCost(self, c1: int, c2: int, cboth: int, need1: int, need2: int) -> int:
        n = min(need1, need2)
        return min(c1+c2, cboth) * n\
            + min(c1, cboth) * (need1-n)\
            + min(c2, cboth) * (need2-n)
