class Solution:
    def maxTotalReward(self, rewards: List[int]) -> int:
        rewards.sort()
        dp = [[-1 for i in range(4001)] for j in range(len(rewards))]
        
        def dfs(i, s):
            if i >= len(rewards):
                return 0
            if dp[i][s] != -1: return dp[i][s]
            result = dfs(i+1, s)
            if rewards[i] > s:
                if s + rewards[i] > 4000:
                    result = max(result, 1)
                else:
                    result = max(result, rewards[i] + dfs(i+1, rewards[i] + s))
            dp[i][s] = result
            return result
        return dfs(0, 0)
