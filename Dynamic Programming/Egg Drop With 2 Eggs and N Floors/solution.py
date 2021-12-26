class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [None for i in range(n)]

        def dfs(start, end):
            if dp[end - start] != None:
                return dp[end-start]
            if start > end:
                return 0 
            result = math.inf
            for egg in range(start, end + 1):
                egg_break = egg - start + 1
                egg_not_break = 1 + dfs(egg + 1, end)
                result = min(result, max(egg_break, egg_not_break))
            dp[end-start] = result
            return result
        
        return dfs(1, n)