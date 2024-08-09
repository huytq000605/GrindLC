class Solution {
public:
    int minFlips(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        
        int all_rows = 0;
        for(int r = 0; r < m; r++) {
            int i = 0, j = n-1;
            while(i < j) {
                if(grid[r][i++] != grid[r][j--]) all_rows++;
            }
        }
        
        int all_cols = 0;
        for(int c = 0; c < n; c++) {
            int i = 0, j = m-1;
            while(i < j) if(grid[i++][c] != grid[j--][c]) all_cols++;
        }
        
        return min(all_rows, all_cols);
    }
};
