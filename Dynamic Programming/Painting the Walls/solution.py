class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @cache
        def dfs(i, busy):
            if i >= n:
                if busy < 0: return math.inf
                return 0
            return min(dfs(i+1, busy-1), cost[i] + dfs(i+1, min(n, busy + time[i])))
        return dfs(0, 0)
            
        
