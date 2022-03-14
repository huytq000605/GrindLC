class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        @cache
        def dfs(idx1, idx2):
            if idx1 >= m or idx2 >= n:
                return 0
            result = dfs(idx1 + 1, idx2 + 1) + (nums1[idx1] * nums2[idx2])
            result = max(result, dfs(idx1 + 1, idx2))
            result = max(result, dfs(idx1, idx2 + 1))
            return result
        return dfs(0, 0)