class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        value = math.inf
        curr = 0
        for num in nums:
            curr += num
            value = min(value, curr)
        return abs(min(value, 0)) +1