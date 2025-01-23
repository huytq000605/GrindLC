class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int result{};
        vector<int> rows(m), cols(n);
        for(int r{}; r < m; ++r) {
            for(int c{}; c < n; ++c) {
                if(grid[r][c]) {
                    rows[r]++;
                    cols[c]++;
                    ++result;
                }
            }
        }
        for(int r{}; r < m; ++r) {
            for(int c{}; c < n; ++c) {
                if(grid[r][c] && rows[r] == 1 && cols[c] == 1) --result;
            }
        }
        return result;
    }
};
