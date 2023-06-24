class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)

        @cache
        def dfs(i, diff):
            if i >= n:
                if diff == 0: return 0
                return -math.inf
            a = rods[i] + dfs(i+1, diff + rods[i])
            b = dfs(i+1, diff - rods[i])
            c = dfs(i+1, diff)
            return max(a,b,c)
        
        result = dfs(0, 0)
        if result == -math.inf:
            return 0
        return result
