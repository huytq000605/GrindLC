class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for i in range(n)]
        result = 0
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[j] - nums[i]
                count = 0
                if diff in dp[i]:
                    count = dp[i][diff]
                    result += count
                dp[j][diff] += count + 1
        return result
                
