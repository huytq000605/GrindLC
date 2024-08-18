class Solution {
public:
    int nthUglyNumber(int n) {
        static constexpr array<int, 3> fs = {2, 3, 5};
        vector<int> dp(n, 0);
        dp[0] = 1;
        int t2 = 0, t3 = 0, t5 = 0;
        for(int i = 1; i < n; i++) {
            dp[i] = min(dp[t2] * 2, min(dp[t3] * 3, dp[t5] * 5));
            if(dp[t2] * 2 == dp[i]) t2++;
            if(dp[t3] * 3 == dp[i]) t3++;
            if(dp[t5] * 5 == dp[i]) t5++;
        }
        return dp[n-1];
    }
};
