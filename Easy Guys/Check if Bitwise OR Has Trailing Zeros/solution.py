class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
        for num in nums:
            if num & 1 == 0:
                count += 1
            if count > 1:
                return True
        return False
