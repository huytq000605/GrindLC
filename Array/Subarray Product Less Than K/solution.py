class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        start = 0
        result = 0
        for i, num in enumerate(nums):
            product *= num
            while start <= i and product >= k:
                product //= nums[start]
                start += 1
            result += (i - start + 1)
        return result
                
