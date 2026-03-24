class Solution {
public:
    int maxProductPath(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<long long> dp(n, INT_MIN), dp2(n, INT_MAX);
        dp[0] = 1;
        dp2[0] = 1;
        for(int r = 0; r < m; ++r) {
            vector<long long> ndp(n, INT_MIN), ndp2(n, INT_MAX);
            for(int c = 0; c < n;++ c) {
                if(dp[c] != INT_MIN && dp[c] != INT_MAX) {
                    ndp[c] = max(dp[c] * grid[r][c], dp2[c] * grid[r][c]);
                    ndp2[c] = min(dp[c] * grid[r][c], dp2[c] * grid[r][c]);
                }
                if(c) {
                    ndp[c] = max(max(ndp2[c-1] * grid[r][c], ndp[c-1] * grid[r][c]), ndp[c]);
                    ndp2[c] = min(min(ndp2[c-1] * grid[r][c], ndp[c-1] * grid[r][c]), ndp2[c]);
                }
            }
            dp = ndp;
            dp2 = ndp2;
        }
        if(dp[n-1] < 0) return -1;
        return dp[n-1] % int(1e9+7);
    }
};
