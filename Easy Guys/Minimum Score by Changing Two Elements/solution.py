class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return 0
        # can use pq to have O(nlog(3)) = O(n)
        nums.sort()
        high = min(nums[-3] - nums[0], nums[-2] - nums[1], nums[-1] - nums[2])
        return high
