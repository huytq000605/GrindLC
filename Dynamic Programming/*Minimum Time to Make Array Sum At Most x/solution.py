class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        # If we're gonna do k operations
        # We want to do the last operation with biggest nums2[i] value
        nums = sorted((-nums2[i], nums1[i]) for i in range(n))
        
        # dfs[i][j] = max value can remove if start from index i and have j operation 
        # @cache
        # def dfs(i, j):
        #     if j < 0:
        #         return -math.inf
        #     if i >= n:
        #         return 0
        #     # dp[i][j] = max(dp[i+1][j-1] + nums[i][1] - nums[i][0] * j, dp[i+1][j])
        #     return max(-nums[i][0] * j + nums[i][1] + dfs(i+1, j-1), dfs(i+1, j))

        # Optimize to bottom up, otherwise MLE
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for j in range(1, n+1):
            for i in reversed(range(n)):
                dp[i][j] = max(dp[i+1][j-1] + nums[i][1] - nums[i][0] * j, dp[i+1][j])
            
        s1, s2 = sum(nums1), sum(nums2)
        for k in range(n+1):
            if s1 + s2 * k - dp[0][k] <= x:
                return k
        return -1
            
            
