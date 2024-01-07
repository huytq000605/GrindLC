class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        result = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j][diff]
                dp[i][diff] += count + 1
                # arithmetic subsequences can only be formed with at least 3 numbers
                if count >= 1:
                    result += count
        return result
