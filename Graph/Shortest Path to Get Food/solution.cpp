class Solution {
public:
    int getFood(vector<vector<char>>& grid) {
        deque<pair<int, int>> dq;
        int s{};
        int m = grid.size(), n = grid[0].size();
        for(int r{}; r < m; ++r) {
            for(int c{}; c < n; ++c) {
                if(grid[r][c] == '*') {
                    dq.emplace_back(r, c);
                    grid[r][c] = 'X';
                }
            }
        }
        vector<pair<int, int>> ds = {{0,1}, {1,0}, {-1,0}, {0,-1}};
        while(!dq.empty()) {
            int k = dq.size();
            for(int i{}; i < k; ++i) {
                auto [r, c] = dq.front();
                dq.pop_front();
                for(auto [dr, dc]: ds) {
                    int nr = r + dr;
                    int nc = c + dc;
                    if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                    if(grid[nr][nc] == 'X') continue;
                    if(grid[nr][nc] == '#') return s + 1;
                    dq.emplace_back(nr, nc);
                    grid[nr][nc] = 'X';
                }
            }
            ++s;
        }

        return -1;
    }
};
