class Solution {
static constexpr array<pair<int, int>, 4> ds = {{ {0,1}, {1,0}, {0, -1}, {-1, 0} }};
public:
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int m = grid2.size(), n = grid2[0].size();
        int i1 = 0, i2 = 0, result = 0;
        auto dfs = [&](int r, int c, auto dfs_ref) -> void {
            grid2[r][c] = 0;
            ++i2;
            i1 += grid1[r][c] == 1;
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(!grid2[nr][nc]) continue;
                dfs_ref(nr, nc, dfs_ref);
            }
        };
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                if(grid2[r][c]) {
                    dfs(r, c, dfs);
                    if(i1 == i2) ++result;
                    i1 = i2 = 0;
                }
            }
        }
        return result;
    }
};
