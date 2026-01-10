class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int n = s1.size(), m = s2.size();
        vector<vector<int>> dp(n+1, vector<int>(m+1, INT_MAX));
        dp[0][0] = 0;
        for(int i = 0; i < n; ++i) {
            dp[i+1][0] = dp[i][0] + s1[i];
        }
        for(int i = 0; i < m; ++i) {
            dp[0][i+1] = dp[0][i] + s2[i];
        }
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                if(s1[i] == s2[j]) dp[i+1][j+1] = dp[i][j];
                else dp[i+1][j+1] = min(dp[i][j+1] + s1[i], dp[i+1][j] + s2[j]);
            }
        }
        return dp.back().back();
    }
};
