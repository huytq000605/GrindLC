class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = set(nums[i])
        result = nums[0]
        for i in range(n):
            result = result.intersection(nums[i])
        return sorted(result)