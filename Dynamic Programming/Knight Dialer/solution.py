class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        dialect = {
            1:[8, 6],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [0, 7, 1],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        dp = [1 for _ in range(10)]
        for i in range(n-1):
            next_dp = [0 for _ in range(10)]
            for num in range(10):
                for prev_num in dialect[num]:
                    next_dp[num] = (next_dp[num] + dp[prev_num]) % MOD
            dp = next_dp
        return sum(dp) % MOD
