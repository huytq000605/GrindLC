dp = [0 for _ in range(801)]
for num in range(2, 801):
    dp[num] = dp[num.bit_count()] + 1

class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        result = 0
        set_bit = 0
        for i in range(n):
            if s[i] == '0':
                continue
            for sb in range(n - i):
                if set_bit + sb > 0 and 1 + dp[set_bit + sb] <= k:
                    result = (result + math.comb(n-i-1, sb)) % MOD
            set_bit += 1
        return result
