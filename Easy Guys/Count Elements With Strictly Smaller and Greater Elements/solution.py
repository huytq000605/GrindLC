class Solution:
    def countElements(self, nums: List[int]) -> int:
        n_min = min(nums)
        n_max = max(nums)
        result = 0
        for num in nums:
            if num != n_min and num != n_max:
                result += 1
        return result