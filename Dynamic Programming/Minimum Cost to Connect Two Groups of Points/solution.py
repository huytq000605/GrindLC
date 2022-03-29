class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        min_connect_second = [math.inf for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                min_connect_second[j] = min(min_connect_second[j], cost[i][j])
        
        @cache
        def dfs(i, mask):
            if i >= m:
                result = 0
                for j in range(n):
                    if (mask >> j) & 1 == 1:
                        result += min_connect_second[j]
                return result
                
            result = math.inf
            for j in range(n):
                result = min(result, dfs(i + 1, mask & ~(1<<j)) + cost[i][j])
            
            return result
        
        return dfs(0, (1 << n) - 1)