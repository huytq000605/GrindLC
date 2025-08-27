class Solution {
public:
    int dp[501][501][4][3][2];
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        memset(dp, 0, sizeof(dp));
        vector<pair<int,int>> ds{{-1, -1}, {-1, 1}, {1, 1}, {1, -1}};
        int m = grid.size(), n = grid[0].size();
        auto dfs = [&](this auto&& dfs, int r, int c, int d, int v, int turn) {
            if(dp[r][c][d][v][turn]) return dp[r][c][d][v][turn];
            int result = 0;
            auto [dr, dc] = ds[d];
            int nr = r + dr, nc = c + dc;
            if(nr >= 0 && nr < m && nc >= 0 && nc < n)
                result = grid[nr][nc] == v ? 1 + dfs(r + dr, c + dc, d, 2-v, turn): 0;
            if(turn) {
                int sd = (d+1) % 4;
                auto [dr, dc] = ds[sd];
                int nr = r + dr, nc = c + dc;
                if(nr >= 0 && nr < m && nc >= 0 && nc < n)
                    result = max(result, grid[nr][nc] == v ? 1 + dfs(r + dr, c + dc, sd, 2-v, turn-1): 0);
            }
            return dp[r][c][d][v][turn] = result;
        };
        int result = 0;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(grid[r][c] == 1) {
                    for(int d = 0; d < 4; ++d) {
                        result = max(result, 1 + dfs(r, c, d, 2, 1));
                    }
                }
            }
        }
        return result;
    }
};
