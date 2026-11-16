class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd, even = 0, 0
        MOD = 10**9 + 7
        result = 0
        for num in arr:
            if num & 1:
                odd, even = even + 1, odd
            else:
                odd, even = odd, even+1
            result = (result + odd) % MOD
        return result
