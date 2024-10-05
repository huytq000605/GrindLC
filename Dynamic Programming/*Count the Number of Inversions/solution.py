class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7
        reqs = {e+1:c for e, c in requirements}
        max_pairs = max(reqs.values())
        dp = [0 for _ in range(max_pairs + 1)]
        dp[0] = 1
        # dp[n][k] = dp[n-1][k] + dp[n-1][k-1] + ... + dp[n-1][k-(n-1)]
        # dp[n][k] = number of array with size n and k inverse pairs
        for sz in range(1, n+1):
            next_dp = [0 for _ in range(max_pairs + 1)]
            if sz in reqs:
                pairs = reqs[sz]
                for p in range(max(0, pairs - (sz - 1)), pairs + 1):
                    next_dp[pairs] += dp[p]
            else:
                prefix_dp = [0 for _ in range(max_pairs + 1)]
                for p in range(max_pairs + 1):
                    if p: prefix_dp[p] = prefix_dp[p-1]
                    prefix_dp[p] += dp[p]
                for p in range(max_pairs + 1):
                    next_dp[p] = prefix_dp[p]
                    if p - (sz - 1) - 1 >= 0:
                        next_dp[p] -= prefix_dp[p - (sz - 1) - 1]
            dp = next_dp
        
        return sum(dp) % MOD
