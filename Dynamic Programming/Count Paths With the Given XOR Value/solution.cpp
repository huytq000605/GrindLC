class Solution {
public:
    int countPathsWithXorValue(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        const int MOD = 1e9 + 7;
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(16, -1)));
        auto dfs = [&](int r, int c, int v, auto dfs) -> int {
            if(r == m-1 && c == n-1) return v == k ? 1: 0;
            if(dp[r][c][v] != -1) return dp[r][c][v];
            dp[r][c][v] = (r+1 < m ? dfs(r+1, c, v ^ grid[r+1][c], dfs) % MOD: 0) + (c+1 < n ? dfs(r, c+1, v ^ grid[r][c+1], dfs) % MOD: 0);
            dp[r][c][v] %= MOD;
            return dp[r][c][v];
        };
        return dfs(0, 0, grid[0][0], dfs);
    }
};
