class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        vector<pair<int, int>> ds = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        set<pair<int, int>> seen;
        int m = grid.size(), n = grid[0].size();
        auto dfs = [&](int r, int c) -> int {
            auto dfs_ref = [&](int r, int c, auto dfs_ref) -> int {
                seen.emplace(r, c);
                int mx = 0;
                for(auto [dr, dc]: ds) {
                    int nr = r + dr, nc = c + dc;
                    if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                    if(grid[nr][nc] == 0 || seen.find({nr, nc}) != seen.end()) continue;
                    mx = max(mx, dfs_ref(nr, nc, dfs_ref));
                }
                seen.erase({r, c});
                return grid[r][c] + mx;
            };
            return dfs_ref(r, c, dfs_ref);
        };
        int result = 0;
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                if(grid[r][c]) result = max(result, dfs(r, c));
            }
        }
        return result;
    }
};
