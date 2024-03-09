class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        odd_changes = 0
        s = 0
        min_diff = math.inf
        for num in nums:
            xor = num ^ k
            odd_changes ^= xor > num
            s += max(xor, num)
            min_diff = min(min_diff, abs(num - xor))
        if odd_changes:
            s -= min_diff
        return s
