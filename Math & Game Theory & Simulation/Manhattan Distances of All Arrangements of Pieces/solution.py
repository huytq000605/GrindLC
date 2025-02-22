class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        # considering 2 specific positions, it will appears C(m*n-2, k-2) times
        MOD = 10**9 + 7
        mul = comb(m*n-2, k-2) % MOD
        result = 0
        for dc in range(1, n):
            # for each dc, there are (n-d) combinations
            # and the value for (ci, cy)
            # ci has m values
            # cy has m values
            result += dc * (n-dc) * m * m
        for dr in range(1, m):
            result += dr * (m-dr) * n * n
        return result * mul % MOD
