class Solution {
public:
    bool containsCycle(vector<vector<char>>& grid) {
        vector<pair<int, int>> ds{{0,1},{1,0},{0,-1},{-1,0}};
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        auto dfs = [&](this auto& dfs, int r, int c, int pr, int pc) -> bool {
            if(visited[r][c]) return true;
            visited[r][c] = true;
            for(auto [dr, dc]: ds) {
                if(r + dr < 0 || r + dr >= m || c + dc < 0 || c + dc >= n) continue;
                if(r + dr == pr && c + dc == pc) continue;
                if(grid[r+dr][c+dc] != grid[pr][pc]) continue;
                if(dfs(r + dr, c + dc, r, c)) return true;
            }
            return false;
        };
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(!visited[r][c] && dfs(r, c, r, c)) return true;
            }
        }
        return false;
    }
};
