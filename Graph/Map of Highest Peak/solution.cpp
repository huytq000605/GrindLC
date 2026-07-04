class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> result(m, vector<int>(n));
        deque<pair<int, int>> dq;
        for(int r{}; r < m; ++r) {
            for(int c{}; c < n; ++c) {
                if(grid[r][c]) {
                    grid[r][c] = -1;
                    dq.emplace_back(r, c);
                }
            }
        }
        vector<pair<int, int>> ds{{0,1}, {1,0}, {-1,0}, {0,-1}};
        int h{1};
        while(!dq.empty()) {
            int k = dq.size();
            while(k--) {
                auto [r, c] = dq.front();
                dq.pop_front();
                for(auto [dr, dc]: ds) {
                    int nr = r + dr, nc = c + dc;
                    if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                    if(grid[nr][nc] == -1) continue;
                    dq.emplace_back(nr, nc);
                    grid[nr][nc] = -1;
                    result[nr][nc] = h;
                }
            }
            ++h;
        }

        return result;
    }
};
