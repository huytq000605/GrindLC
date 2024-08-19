class Solution {
public:
    int minSteps(int n) {
        vector<int> dp(n+1, INT_MAX);
        dp[1] = 0;
        for(int i = 1; i + i <= n; i++) {
            int j = 1;
            while(i + i*j <= n) {
                dp[i + i*j] = min(dp[i + i*j], dp[i] + 1 + j);
                j++;
            }
        }
        return dp[n];
    }
};
