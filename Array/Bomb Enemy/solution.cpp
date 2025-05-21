class Solution {
public:
    int maxKilledEnemies(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> t(m, vector<int>(n));
        vector<vector<int>> b(m, vector<int>(n));
        vector<vector<int>> l(m, vector<int>(n));
        vector<vector<int>> rm(m, vector<int>(n));
        for(int c = 0; c < n; ++c) {
            int p = 0;
            for(int r = 0; r < m; ++r) {
                if(grid[r][c] == 'W') p = 0;
                else p += grid[r][c] == 'E';
                t[r][c] = p;
            }

            p = 0;
            for(int r = m-1; r >= 0; --r) {
                if(grid[r][c] == 'W') p = 0;
                else p += grid[r][c] == 'E';
                b[r][c] = p;
            }
        }

        for(int r = 0; r < m; ++r) {
            int p = 0;
            for(int c = 0; c < n; ++c) {
                if(grid[r][c] == 'W') p = 0;
                else p += grid[r][c] == 'E';
                l[r][c] = p;
            }

            p = 0;
            for(int c = n-1; c >= 0; --c) {
                if(grid[r][c] == 'W') p = 0;
                else p += grid[r][c] == 'E';
                rm[r][c] = p;
            }
        }
        int result = 0;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(grid[r][c] == '0') result = max(result, t[r][c] + b[r][c] + l[r][c] + rm[r][c]);
            }
        }
        return result;
    }
};
