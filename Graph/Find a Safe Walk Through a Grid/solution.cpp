class Solution {
private:
    static constexpr array<pair<int, int>, 4> ds = {{ {0,1}, {1,0}, {-1,0}, {0,-1} }};
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, decltype([](auto t1, auto t2) -> bool {
            return get<0>(t1) < get<0>(t2);
        })> pq;
        dp[0][0] = health - grid[0][0];
        pq.emplace(health - grid[0][0], 0, 0);
        while(!pq.empty()) {
            auto [h, r, c] = pq.top();
            if(r == m-1 && c == n-1) return true;
            pq.pop();
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(h - grid[nr][nc] > dp[nr][nc]) {
                    dp[nr][nc] = h - grid[nr][nc];
                    pq.emplace(h - grid[nr][nc], nr, nc);
                }
            }
        }
        return false;
        
    }
};
