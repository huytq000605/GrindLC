class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        need = sorted([capacity[i] - rocks[i] for i in range(n)])
        result = 0
        rocks = additionalRocks
        for n in need:
            if rocks >= n:
                rocks -= n
                result += 1
            else:
                break
        return result
        
