class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = [s for s in stones]
        n = len(stones)
        for i in range(1, n):
            prefix[i] += prefix[i-1]
        # @cache
        # def dfs(i):
        #     if i == n-1:
        #         return prefix[-1]
        #     return max(dfs(i+1), prefix[i] - dfs(i+1))
        # return dfs(1)
        dp = prefix[-1]
        for i in range(n-2, 0, -1):
            dp = max(dp, prefix[i] - dp)
        return dp
