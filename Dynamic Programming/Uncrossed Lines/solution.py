class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx1, idx2):
            if idx1 >= len(nums1) or idx2 >= len(nums2):
                return 0
            if nums1[idx1] == nums2[idx2]:
                return 1 + dfs(idx1 + 1, idx2 + 1)
            else:
                result = max(dfs(idx1 + 1, idx2), dfs(idx1, idx2 + 1))
                return result
        return dfs(0, 0)