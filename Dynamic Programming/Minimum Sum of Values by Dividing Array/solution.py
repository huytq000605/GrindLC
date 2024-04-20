class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        m, n = len(nums), len(andValues)
        @cache
        def dfs(i, j, mask):
            if i == m and j == n: return 0
            if i == m or j == n: return math.inf
            mask &= nums[i]
            if mask < andValues[j]: return math.inf
            result = dfs(i+1, j, mask)
            if mask == andValues[j]: result = min(result, nums[i] + dfs(i+1, j+1, (1 << 17) - 1))
            return result
        result = dfs(0, 0, (1 << 17) - 1)
        if result == math.inf: return -1
        return result
            
