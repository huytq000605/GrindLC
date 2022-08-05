class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(target):
            if target == 0:
                return 1
            result = 0
            for num in nums:
                if target - num >= 0:
                    result += dfs(target-num)
            return result
        return dfs(target)
