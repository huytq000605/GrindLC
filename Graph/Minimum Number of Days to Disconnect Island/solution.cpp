class Solution {
public:
    int minDays(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();

        auto count_island = [&](int rr, int rc) -> int {
            bool reset = false;
            if(rr >= 0 && rr < m && rc >= 0 && rc < n) {
                grid[rr][rc] = 0;
                reset = true;
            }

            auto dfs = [&](int r, int c, auto dfs_ref) -> void {
                for(auto [dr, dc]: ds) {
                    int nr = r + dr, nc = c + dc;
                    if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                    if(grid[nr][nc] != 1) continue;
                    grid[nr][nc] = 2;
                    dfs_ref(nr, nc, dfs_ref);
                }
            };
            int islands = 0;
            for(int r = 0; r < m; r++) {
                for(int c =0 ; c < n; c++) {
                    if(grid[r][c] == 1) {
                        islands++;
                        grid[r][c] = 2;
                        dfs(r, c, dfs);
                    }
                }
            }

            for(int r = 0; r < m; r++) {
                for(int c = 0; c < n; c++) {
                    if(grid[r][c] == 2) grid[r][c] = 1;
                }
            }
            if(reset) grid[rr][rc] = 1;
            return islands;
        };

        if(count_island(-1, -1) != 1) return 0;
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                if(grid[r][c] == 1 && count_island(r, c) != 1) return 1; 
            }
        }
        return 2;
    }
private:
    static constexpr array<pair<int, int>, 4> ds{{ {0, 1}, {1, 0}, {-1, 0}, {0, -1} }};
};
