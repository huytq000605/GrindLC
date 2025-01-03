class Solution {
public:
    int minimumOperations(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int result{};
        for(int c{}; c < n; ++c) {
            int prev{-1};
            for(int r{}; r < m; ++r) {
                if(prev >= grid[r][c]) {
                    result += ++prev - grid[r][c];
                } else {
                    prev = grid[r][c];
                }
            }
        }
        return result;
    }
};
