class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        zeros = 0
        ones = 0
        have_zero = 0
        MOD = 10**9 + 7
        for l in binary:
            if l == "1":
                ones = ones + zeros + 1
                ones %= MOD
            else:
                have_zero = 1
                zeros = ones + zeros
                zeros %= MOD
        return (ones + zeros + have_zero) % MOD
