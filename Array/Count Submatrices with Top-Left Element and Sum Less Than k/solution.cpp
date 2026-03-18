class Solution {
public:
    int countSubmatrices(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        int result = 0;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                grid[r][c] += (r-1 >= 0 ? grid[r-1][c]: 0) + (c-1 >= 0 ? grid[r][c-1]: 0) - (r-1>=0 && c-1>=0 ? grid[r-1][c-1]: 0);
                if(grid[r][c] <= k) ++result;
                else break;
            }
        }
        return result;
    }
};
