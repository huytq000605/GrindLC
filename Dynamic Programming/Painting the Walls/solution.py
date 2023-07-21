class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @cache
        def dfs(i, remaining):
            if remaining <= 0: return 0
            if i >= n: return math.inf
            return min(cost[i] + dfs(i+1, remaining - time[i] - 1), dfs(i+1, remaining))
        return dfs(0, n)
            
            
        
