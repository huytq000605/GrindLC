class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> prefix_row(m, vector<int>(n+1, 0));
        vector<vector<int>> prefix_col(n, vector<int>(m+1, 0));
        unordered_map<int, vector<int>> prefix_dia1, prefix_dia2;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++ c) {
                prefix_row[r][c+1] = prefix_row[r][c] + grid[r][c];
                prefix_col[c][r+1] = prefix_col[c][r] + grid[r][c];
                if(prefix_dia1.find(r-c) == prefix_dia1.end())
                    prefix_dia1[r-c].resize(m+1);
                prefix_dia1[r-c][r+1] = prefix_dia1[r-c][r] + grid[r][c];
                if(prefix_dia2.find(r+c) == prefix_dia2.end())
                    prefix_dia2[r+c].resize(m+1);
                prefix_dia2[r+c][r+1] = prefix_dia2[r+c][r] + grid[r][c];
            }
        }
        int result = 0;
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                for(int sz = max(1, result); r + sz <= m && c + sz <= n; ++sz) {
                    int target = prefix_row[r][c+sz] - prefix_row[r][c];
                    bool valid = (prefix_dia1[r-c][r+sz] - prefix_dia1[r-c][r]) == target;
                    valid &= (prefix_dia2[r+c+sz-1][r+sz] - prefix_dia2[r+c+sz-1][r]) == target;
                    for(int i = 0; valid && i < sz; ++i) {
                        if(prefix_row[r+i][c+sz] - prefix_row[r+i][c] != target ||
                            prefix_col[c+i][r+sz] - prefix_col[c+i][r] != target) {
                            valid = false;
                        }
                    }
                    if(valid) result = max(result, sz);
                }
            }
        }
        return result;
    }
};
