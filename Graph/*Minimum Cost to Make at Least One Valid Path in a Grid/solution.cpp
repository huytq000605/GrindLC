class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        vector<pair<int, int>> ds{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, m*n));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, decltype([](auto &t1, auto &t2) -> bool {
            return get<0>(t1) > get<0>(t2);
        })> pq;
        dp[0][0] = 0;
        pq.emplace(0, 0, 0);
        while(!pq.empty()) {
            auto [s, r, c] = pq.top();
            if(r == m-1 && c == n-1) return s;
            pq.pop();
            for(auto &[dr, dc]: ds) {
                int nr = r + dr;
                int nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                int cost = !(make_pair(dr, dc) == ds[grid[r][c] - 1]);
                if(dp[nr][nc] > s + cost) {
                    dp[nr][nc] = s + cost;
                    pq.emplace(s+cost, nr, nc);
                }
            }
        }

        return -1;
    }
};
