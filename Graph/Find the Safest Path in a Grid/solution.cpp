class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        vector<pair<int, int>> ds = {{0,1}, {1,0}, {-1,0}, {0,-1}};
        int n = grid.size();
        queue<pair<int, int>> thiefs;
        for(int r = 0; r < n; r++) {
            for(int c = 0; c < n; c++) {
                if(grid[r][c]) thiefs.emplace(r, c);
            }
        }

        while(thiefs.size()) {
            auto [r, c] = thiefs.front();
            thiefs.pop();
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                if(grid[nr][nc]) continue;
                grid[nr][nc] = grid[r][c] + 1;
                thiefs.emplace(nr, nc);
            }
        }

        priority_queue<
            pair<int, pair<int, int>>, 
            vector<pair<int, pair<int, int>>>,
            decltype([](auto a, auto b) -> bool {
                return a.first < b.first;
            })> pq;
        vector<vector<int>> distances(n, vector<int>(n, -1));
        pq.push({grid[0][0], {0, 0}});
        distances[0][0] = grid[0][0];
        while(pq.size()) {
            auto [d, rc] = pq.top();
            auto [r, c] = rc;
            if(r == n-1 && c == n-1) return d-1;
            pq.pop();
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                if(min(grid[nr][nc], d) > distances[nr][nc]) {
                    distances[nr][nc] = min(grid[nr][nc], d);
                    pq.push({distances[nr][nc], {nr, nc}});
                }
            }
        }
        return -1;
    }
};
