class Solution {
public:
    int trapRainWater(vector<vector<int>>& grid) {
        vector<pair<int, int>> ds{{0,1}, {1,0}, {-1,0}, {0,-1}};
        int m = grid.size(), n = grid[0].size();
        
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, decltype(
            [](auto &t1, auto &t2) -> bool {
                return get<0>(t1) > get<0>(t2);
            }
        )> pq;
        for(int r: {0, m-1}) {
            for(int c{}; c < n; ++c) {
                pq.emplace(grid[r][c], r, c);
                grid[r][c] = INT_MAX;
            }
        }

        for(int c: {0, n-1}) {
            for(int r{1}; r < m-1; ++r) {
                pq.emplace(grid[r][c], r, c);
                grid[r][c] = INT_MAX;
            }
        }

        int result{};
        while(!pq.empty()) {
            auto [h, r, c] = pq.top();
            pq.pop();
            for(auto &[dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(grid[nr][nc] == INT_MAX) continue;
                result += max(0, h - grid[nr][nc]);
                pq.emplace(max(grid[nr][nc], h), nr, nc);
                grid[nr][nc] = INT_MAX;
            }
        }
        return result;
    }
};
