class Solution {
public:
    long long numberOfRightTriangles(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        long long result = 0;
        vector<int> counter_row(m, 0);
        vector<int> counter_col(n, 0);
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                if(grid[r][c] != 1) continue;
                counter_row[r] += 1;
                counter_col[c] += 1;
            }
        }
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                if(grid[r][c] != 1) continue;
                result += (counter_row[r]-1) * (counter_col[c]-1);
            }
        }
        
        return result;
    }
};
