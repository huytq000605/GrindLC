class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # k indices arr[i-1] == arr[i] => n-k distinct integers
        # for the first number, we have m ways to choose = m
        # for the n-k-1 numbers, we have (m-1) ways to choose (as long as it's different than the previous) = pow(m-1, n-k-1)
        # after this, we've built an array of n-k elements, but we have n elements
        # we can think of it as stars and bars, split the array of n elements into n-k groups by placing bars
        # we need to put (n-k-1) bars where we have n-1 gaps => (n-1 choose n-k-1) = (n-1 choose k) = comb(n-1, k)
        MOD = 10**9+7
        return m * pow(m-1, n-k-1, MOD) * math.comb(n-1, k) % MOD
