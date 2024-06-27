class Solution {
public:
    bool satisfiesConditions(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                if(r + 1 < m && grid[r][c] != grid[r+1][c]) return false;
                if(c+1<n && grid[r][c] == grid[r][c+1]) return false;
            }
        }
        return true;
    }
};
