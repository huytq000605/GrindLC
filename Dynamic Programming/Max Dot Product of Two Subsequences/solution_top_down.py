class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        mn1, mx1 = min(nums1), max(nums1)
        mn2, mx2 = min(nums2), max(nums2)
        
        if mn1 > 0 and mx2 < 0:
            return mn1 * mx2
        
        if mn2 > 0 and mx1 < 0:
            return mn2 * mx1
        
        @cache
        def dfs(i1, i2):
            if i1 >= m or i2 >= n:
                return 0
            
            # dp[i1][i2] = max(nums1[i1] * nums2[i2] + dp[i1 + 1][i2 + 1],
            #                  dp[i1+1, i2],
            #                  dp[i1, i2 +1])
            return max(nums1[i1] * nums2[i2] + dfs(i1 + 1, i2 + 1),
                      dfs(i1+1, i2),
                      dfs(i1, i2+1)
                      )
        
         return dfs(0, 0)
    
# Bottom up
#        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
#        for i in reversed(range(m)):
#            for j in reversed(range(n)):
#                dp[i][j] = max(nums1[i] * nums2[j] + dp[i+1][j+1],
#                              dp[i+1][j],
#                              dp[i][j+1])
#        return dp[0][0]
