class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int result = 0;
        int min_col_has_x = n;
        vector<int> row(n, 0);
        for(int r = 0; r < m ; ++r) {
            vector<int> nrow(n, 0);
            for(int c = 0; c < n; ++c) {
                if(grid[r][c] == 'X') min_col_has_x = min(min_col_has_x, c);
                nrow[c] = (grid[r][c] == 'X' ? 1: grid[r][c] == 'Y' ? -1: 0) + row[c] + (c-1 >= 0 ? nrow[c-1]: 0) - (c-1 >= 0 ? row[c-1]: 0);
                if(!nrow[c] && min_col_has_x <= c) ++result;
            }
            row = nrow;
        }
        return result;
    }
};
