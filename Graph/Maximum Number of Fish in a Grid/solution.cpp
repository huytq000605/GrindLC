class Solution {
public:
    int findMaxFish(vector<vector<int>>& grid) {
        array<pair<int, int>, 4> ds{{{1,0}, {0,1}, {-1,0}, {0,-1}}};
        int m = grid.size(), n = grid[0].size();
        function<int(int, int)> dfs = [&](int r, int c) -> int {
            int ret{grid[r][c]};
            grid[r][c] = 0;
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(!grid[nr][nc]) continue;
                ret += dfs(nr, nc);
            }
            return ret;
        };

        int result{};
        for(int r{}; r < m; ++r) {
            for(int c{}; c < n; ++c) {
                if(grid[r][c]) result = max(result, dfs(r, c));
            }
        }
        return result;
    }
};
