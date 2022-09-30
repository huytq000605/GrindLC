class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2): 
            return self.findLength(nums2, nums1)
        m, n = len(nums1), len(nums2)
        dp, prevDP = [0] * (n+1), [0] * (n+1)
        ans = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[j+1] = prevDP[j] + 1
                else:
                    dp[j+1] = 0
                ans = max(ans, dp[j+1])
            dp, prevDP = prevDP, dp
        return ans
