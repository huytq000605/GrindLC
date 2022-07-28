class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cur, result = 0, 0
        for num in nums:
            if num == 0:
                cur += 1
            else:
                cur = 0
            result += cur
        return result
