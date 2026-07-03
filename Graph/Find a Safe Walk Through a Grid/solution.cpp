class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m = grid.size(), n = grid[0].size();
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, decltype([](auto &t1, auto &t2) -> bool {
            return get<0>(t1) > get<0>(t2);
        })> pq;
        vector<pair<int, int>> ds{{0,1}, {1,0}, {-1,0}, {0,-1}};
        pq.emplace(grid[0][0], 0, 0);
        vector<vector<int>> healths(m, vector<int>(n, health));
        healths[0][0] = grid[0][0];
        while(!pq.empty()) {
            auto [v, r, c] = pq.top(); pq.pop();
            if(r == m-1 && c == n-1) return true;
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(v + grid[nr][nc] < healths[nr][nc]) {
                    healths[nr][nc] = v + grid[nr][nc];
                    pq.emplace(healths[nr][nc], nr, nc);
                }
            }
        }
        return false;
    }
};
