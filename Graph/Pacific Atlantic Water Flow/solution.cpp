class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<pair<int, int>> ds{{0,1}, {1,0}, {-1,0}, {0,-1}};
        vector<vector<int>> dp1(m, vector<int>(n));
        vector<vector<int>> dp2(m, vector<int>(n));
        auto dfs = [&](this auto&& dfs, bool to_pacific, int r, int c) -> void{
            vector<vector<int>>& dp = to_pacific ? dp1: dp2;
            if(dp[r][c]) return;
            dp[r][c] = 1;
            for(auto [dr, dc]: ds) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n || heights[nr][nc] < heights[r][c]) continue;
                dfs(to_pacific, nr, nc);
            }
        };

        for(int c = 0; c < n; ++c) {
            dfs(true, 0, c);
            dfs(false, m-1, c);
        }
        for(int r = 0; r < m; ++r) {
            dfs(true, r, 0);
            dfs(false, r, n-1);
        }

        vector<vector<int>> result;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(dp1[r][c] && dp2[r][c]) {
                    result.push_back({r, c});
                }
            }
        }
        return result;
    }
};
