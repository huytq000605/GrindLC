class Solution {
public:
    int maximumAmount(vector<vector<int>>& coins) {
        int m = coins.size(), n = coins[0].size();
        vector<vector<int>> dp(n, vector<int>(3));
        for(int r = 0; r < m; ++r) {
            vector<vector<int>> ndp(n, vector<int>(3, INT_MIN));
            for(int c = 0; c < n; ++c) {
                for(int u = 0; u < 3; ++u) {
                    if(r || c == 0) ndp[c][u] = dp[c][u] + coins[r][c];
                    if(c) ndp[c][u] = max(ndp[c][u], ndp[c-1][u] + coins[r][c]);
                    if(u) {
                        if(r || c == 0) ndp[c][u] = max(ndp[c][u], dp[c][u-1]);
                        if(c) ndp[c][u] = max(ndp[c][u], ndp[c-1][u-1]);
                    }
                }
            }
            dp = ndp;
        }
        return *max_element(begin(dp.back()), end(dp.back()));
    }
};
