class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        int m = grid.size(), n = grid[0].size();
        vector<int> vals(m*n);
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                vals[r*n+c] = grid[r][c];
            }
        }
        sort(vals.begin(), vals.end());
        int median = vals[m*n/2];
        int result = 0;
        for(int v: vals) {
            int d = abs(v - median);
            if(d % x) return -1;
            result += d/x;
        }
        return result;
    }
};
