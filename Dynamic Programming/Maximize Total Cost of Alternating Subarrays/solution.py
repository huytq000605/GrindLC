class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        pos, neg = -math.inf, 0
        for num in nums:
            npos = max(pos + num, neg + num)
            neg = pos - num
            pos = npos
        return max(pos, neg)
