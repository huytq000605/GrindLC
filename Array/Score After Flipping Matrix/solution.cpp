class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int result = (1 << (n-1)) * m;
        for(int c = 1; c < n; c++) {
            int ones = 0;
            for(int r = 0; r < m; r++) {
                ones += grid[r][c] == grid[r][0];
            }
            result += (1 << (n-c-1)) * max(ones, m - ones);
        }
        return result;
    }
};
