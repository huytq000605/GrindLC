class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 1
        spaces = 2 * n
        # math.comb = n! / k! / (n-k)!
        # k is always 2
        # n * (n-1) / 2
        for i in range(n):
            # choose 2 spaces for pair of delivery & pickup
            result = (result * math.comb(spaces - 2 * i, 2)) % MOD
            # can be replace by this
            # result = (result * (spaces - 2 * i) * (spaces - 2 * i - 1) // 2) % MOD
        return result
