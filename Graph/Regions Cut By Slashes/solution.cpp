class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
        vector<vector<char>> upscale(n*3, vector<char>(n*3, ' '));
        for(int r = 0; r < n; r++) {
            for(int c = 0; c < n; c++) {
                if(grid[r][c] == '/') {
                    upscale[r*3][c*3+2] = '.';
                    upscale[r*3+1][c*3+1] = '.';
                    upscale[r*3+2][c*3] = '.';
                } else if(grid[r][c] == '\\') {
                    upscale[r*3][c*3] = '.';
                    upscale[r*3+1][c*3+1] = '.';
                    upscale[r*3+2][c*3+2] = '.';
                }
            }
        }
        set<pair<int, int>> seen;
        auto dfs = [&](int r, int c, auto dfs_ref) -> void {
            for(auto d: ds) {
                int nr = r + d.first, nc = c + d.second;
                if(nr < 0 || nr >= n*3 || nc < 0 || nc >= n*3) continue;
                if(upscale[nr][nc] != ' ' || seen.find({nr, nc}) != seen.end()) continue;
                seen.emplace(nr, nc);
                dfs_ref(nr, nc, dfs_ref);
            }
        };
        int result = 0;
        for(int r = 0; r < n*3; r++) {
            for(int c = 0; c < n*3; c++) {
                if(upscale[r][c] == ' ' && seen.find({r, c}) == seen.end()) {
                    seen.emplace(r, c);
                    dfs(r, c, dfs);
                    result++;
                }
            }
        }
        return result;
    }
private:
    static constexpr array<pair<int, int>, 4> ds{{ {0, 1}, {1, 0}, {0, -1}, {-1, 0} }};
};
