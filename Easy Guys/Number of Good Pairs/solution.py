class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        result = 0
        for num in nums:
            result += dp[num]
            dp[num] += 1
        return result
