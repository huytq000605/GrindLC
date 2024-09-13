class Solution {
public:
    int maxScore(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        // select by values, state is selected row
        vector<pair<int, int>> values;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                values.emplace_back(r, grid[r][c]);
            }
        }
        sort(values.begin(), values.end(), [](auto p1, auto p2) {
            return p1.second > p2.second;
        });
        // group same values into group to make sure not using the same values
        vector<vector<pair<int, int>>> group_values;
        for(auto [r, v]: values) {
            if(group_values.empty() || group_values.back()[0].second != v) {
                group_values.push_back({});
            }
            group_values.back().emplace_back(r, v);
        }
        // knapsack with row_mask as bit mask of selected rows
        vector<unordered_map<int, int>> dp(group_values.size());
        auto dfs = [&](int i, int row_mask, auto dfs_ref) -> int {
            if(row_mask == (1 << m) - 1 || i >= group_values.size()) return 0;
            if(dp[i].find(row_mask) != dp[i].end()) return dp[i][row_mask];
 
            int result = dfs_ref(i+1, row_mask, dfs_ref);
            for(auto [r, v]: group_values[i]) {
                if((row_mask >> r) & 1) continue;
                
                result = max(result, v + dfs_ref(i+1, row_mask | (1 << r), dfs_ref));
            }
            return dp[i][row_mask] = result;
        };

        return dfs(0, 0, dfs);
    }
};
