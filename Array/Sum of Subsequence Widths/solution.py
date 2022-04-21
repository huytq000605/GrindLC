class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        max_num = 0
        min_num = 0
        MOD = 10**9 + 7
        n = len(nums)
        for i, num in enumerate(nums):
            max_num += num * pow(2, i, MOD)
            min_num += num * pow(2, n-i-1, MOD)
        return (max_num - min_num)%MOD