class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        vector<vector<pair<int, int>>> ds{
            {{0,1}, {0,-1}},
            {{1,0}, {-1, 0}},
            {{0,-1}, {1,0}},
            {{0, 1}, {1, 0}},
            {{-1,0}, {0,-1}},
            {{-1,0}, {0, 1}}
        };
        int m = grid.size(), n = grid[0].size();
        deque<pair<int, int>> dq{{0, 0}};
        vector<vector<int>> visited(m, vector<int>(n));
        while(!dq.empty()) {
            auto [r, c] = dq.front(); dq.pop_front();
            if(r == m-1 && c == n-1) return true;
            for(auto [dr, dc]: ds[grid[r][c] - 1]) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(visited[nr][nc]) continue;
                for(auto [ddr, ddc]: ds[grid[nr][nc] - 1]) {
                    if(nr + ddr == r && nc + ddc == c) {
                        visited[nr][nc] = 1;
                        dq.emplace_back(nr, nc);
                    }
                }
            }
        }
        return false;
    }
};
