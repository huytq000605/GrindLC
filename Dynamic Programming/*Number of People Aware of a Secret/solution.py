class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9+7
        # dp[i] is number of people receive secret at day i
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        # Number of peoples are sharing
        share = 0

        for day in range(2, n+1):
            # Peoples from day - delay are starting to share
            share += dp[day-delay]
            # Peoples from day - forget are stopping to share
            share -= dp[day-forget]
            dp[day] = share

        return sum(dp[n-forget+1:]) % MOD
