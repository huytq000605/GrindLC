class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return n
        result = 1
        while n:
            n >>= 1
            result <<= 1
        return result

