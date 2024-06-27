class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        nums = [1 for _ in range(n)]
        for _ in range(k):
            s = 0
            for i in range(n):
                next_s = s + nums[i]
                nums[i] += s
                s = next_s % MOD
                nums[i] %= MOD
        return nums[-1]
