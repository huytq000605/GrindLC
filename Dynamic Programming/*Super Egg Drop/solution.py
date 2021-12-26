class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[None for j in range(k + 1)] for i in range(n + 1)]
        
        def dfs(n, k):
            if n <= 1:
                return 1
            if k == 1:
                return n
            if dp[n][k] != None:
                return dp[n][k]
            start = 1
            end = n
            result = math.inf
            while start < end:
                mid = start + (end - start) // 2
                left = dfs(mid - 1, k - 1)
                right = dfs(n - mid, k)
                if left < right:
                    start = mid + 1
                else:
                    end = mid
                result = min(result, max(left, right) + 1)
            
            dp[n][k] = result
            return result
        
        return dfs(n, k)