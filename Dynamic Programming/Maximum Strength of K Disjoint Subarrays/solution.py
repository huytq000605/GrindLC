class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[[None for k in range(2)] for j in range(k+1)] for i in range(n)]
        def dfs(i, k, picked):
            if k <= 0:
                return -math.inf if k & 1 else math.inf
            if i >= n:
                if k > 1 or not picked: return -math.inf if k & 1 else math.inf
                return 0
            if dp[i][k][picked] != None:
                return dp[i][k][picked]
            if k & 1:
                result = dfs(i+1, k, True) + nums[i] * k
                if picked:
                    result = max(result, -dfs(i, k-1, False))
                else:
                    result = max(result, dfs(i+1, k, False))
                # special case where we can stop
                if k == 1 and picked:
                    result = max(result, 0)
            else:
                result = dfs(i+1, k, True) + nums[i] * k
                if picked:
                    result = min(result, -dfs(i, k-1, False))
                else:
                    result = min(result, dfs(i+1, k, False))
            dp[i][k][picked] = result
            return result
        return dfs(0, k, False)
