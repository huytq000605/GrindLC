class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        prefix = 0
        min_avg_diff = math.inf
        result = 0
        for i in range(n):
            prefix += nums[i]
            suffix = s - prefix
            left_avg = prefix // (i+1)
            if i == n-1:
                right_avg = 0
            else:
                right_avg = suffix // (n-i-1)
            avg_diff = abs(left_avg - right_avg)
            if avg_diff < min_avg_diff:
                result = i
                min_avg_diff = avg_diff
        return result
