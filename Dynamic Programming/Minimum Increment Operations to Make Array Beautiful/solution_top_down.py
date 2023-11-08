class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        @cache
        def dfs(i, m):
            if m < 0:
                return math.inf
            if i >= n:
                return 0
            if nums[i] > k:
                return dfs(i+1, 2)
            return min(dfs(i+1, m-1), dfs(i+1, 2) + k - nums[i])
        
        return dfs(0, 2)
