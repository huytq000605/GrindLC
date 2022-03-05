class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        keys = sorted(counter.keys())
        dp = [0 for i in range(len(keys))]
        dp[0] = counter[keys[0]] * keys[0]
        for i in range(1, len(keys)):
            if keys[i-1] == keys[i] - 1:
                prev = 0
                if i > 1:
                    prev = dp[i-2]
                dp[i] = max(dp[i-1], dp[i-2] + counter[keys[i]] * keys[i])
            else:
                dp[i] = dp[i-1] + counter[keys[i]] * keys[i]
        
        return dp[-1]