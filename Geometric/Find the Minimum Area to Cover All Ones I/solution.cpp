class Solution {
public:
    int minimumArea(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int min_r = m, max_r = 0;
        int min_c = n, max_c = 0;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(grid[r][c]) {
                    min_r = min(min_r, r);
                    max_r = max(max_r, r);
                    min_c = min(min_c, c);
                    max_c = max(max_c, c);
                }
            }
        }
        return (max_r - min_r + 1) * (max_c - min_c + 1);
    }
};
