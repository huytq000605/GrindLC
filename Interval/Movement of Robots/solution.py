class Solution:
    def sumDistance(self, nums: List[int], s: str, seconds: int) -> int:
        # Even if there is collision, there is no changes to their distance.
        MOD = 10**9 + 7
        n = len(nums)
        result = 0
        for i in range(n):
            if s[i] == "L":
                nums[i] -= seconds
            else:
                nums[i] += seconds
        nums.sort()
        pref = 0
        for i in range(n):
            result = (result + (i * nums[i]) % MOD - pref + MOD) % MOD
            pref = (pref + nums[i]) % MOD
        return result
