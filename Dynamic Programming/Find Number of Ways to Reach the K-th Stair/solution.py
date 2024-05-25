class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dfs(stair, prev_down, jump):
            if stair > k + 1: return 0
            result = stair == k
            result += dfs(stair + 2**jump, False, jump + 1)
            if stair and not prev_down:
                result += dfs(stair - 1, True, jump)
            return result
        
        return dfs(1, False, 0)
