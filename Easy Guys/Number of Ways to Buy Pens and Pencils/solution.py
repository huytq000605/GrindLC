class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        i = 0
        result = 0
        while i * cost1 <= total:
            pencils = (total - i * cost1) // cost2
            result += pencils + 1
            i += 1
        return result