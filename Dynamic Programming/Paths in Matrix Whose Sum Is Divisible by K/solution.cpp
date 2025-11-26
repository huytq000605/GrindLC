class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(k+1)));
        dp[0][0][grid[0][0] % k] = 1;
        int MOD = 1e9 + 7;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(r > 0) {
                    for(int mod = 0; mod < k; ++mod) {
                        dp[r][c][(mod + grid[r][c]) % k] += dp[r-1][c][mod];
                        dp[r][c][(mod + grid[r][c]) % k] %= MOD;
                    }
                }
                if(c > 0) {
                    for(int mod = 0; mod < k; ++mod) {
                        dp[r][c][(mod + grid[r][c]) % k] += dp[r][c-1][mod];
                        dp[r][c][(mod + grid[r][c]) % k] %= MOD;
                    }
                }
            }
        }
        return dp[m-1][n-1][0];
    }
};
