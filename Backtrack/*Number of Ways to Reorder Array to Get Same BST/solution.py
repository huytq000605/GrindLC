class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def ways(nums):
            if len(nums) <= 1: return 1
            left = list(filter(lambda num: num < nums[0], nums))
            right = list(filter(lambda num: num > nums[0], nums))
            return ways(left) % MOD * ways(right) % MOD * math.comb(len(left) + len(right), len(left)) % MOD 
        return (ways(nums) - 1)
