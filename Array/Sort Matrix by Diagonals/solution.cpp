class Solution {
public:
    vector<vector<int>> sortMatrix(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        unordered_map<int, vector<int>> um;
        for(int r{}; r < m; ++r) {
            for(int c{}; c < n; ++c) {
                um[r-c].emplace_back(grid[r][c]);
            }
        }
        for(auto &[k, vals]: um) {
            if(k < 0) {
                sort(vals.rbegin(), vals.rend());
            } else {
                sort(vals.begin(), vals.end());
            }
            
        }
        for(int r{}; r < m; ++r) {
            for(int c{}; c < n; ++c) {
                grid[r][c] = um[r-c].back();
                um[r-c].pop_back();
            }
        }
        return grid;
    }
};
