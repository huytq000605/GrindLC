class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        minAbs = math.inf
        total = 0
        for i, num in enumerate(nums):
            if num < 0 and k > 0:
                nums[i] = -num
                k -= 1
            minAbs = min(minAbs, abs(num))
            total += nums[i]
        if k % 2 == 1:
            total -= 2 * minAbs
        return total