class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        last_flip = -1
        result = 0
        cur = 0
        for i, num in enumerate(nums):
            if num == 0:
                cur = i - last_flip
                last_flip = i
            else:
                cur += 1
            result = max(result, cur)
        return result
