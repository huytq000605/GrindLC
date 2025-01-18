class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        vector<pair<int, int>> ds{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, m*n));
        deque<pair<int, int>> dq;
        dp[0][0] = 0;
        dq.emplace_back(0, 0);
        while(!dq.empty()) {
            auto [r, c] = dq.front();
            if(r == m-1 && c == n-1) return dp[r][c];
            dq.pop_front();
            {
                auto [dr, dc] = ds[grid[r][c] - 1];
                int nr = r + dr;
                int nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    ;
                } else if(dp[nr][nc] > dp[r][c]) {
                    dp[nr][nc] = dp[r][c];
                    dq.emplace_front(nr, nc);
                } 
            }
            
            for(auto &[dr, dc]: ds) {
                if(make_pair(dr, dc) == ds[grid[r][c]-1]) continue;
                int nr = r + dr;
                int nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(dp[nr][nc] > dp[r][c] + 1) {
                    dp[nr][nc] = dp[r][c] + 1;
                    dq.emplace_back(nr, nc);
                }
            }
        }

        return -1;
    }
};
