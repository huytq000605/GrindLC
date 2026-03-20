class Solution {
public:
    vector<vector<int>> minAbsDiff(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> result(m-k+1, vector<int>(n-k+1));
        if(k == 1) return result;
        for(int r = 0; r <= m-k; ++r) {
            for(int c = 0; c <= n-k; ++c) {
                vector<int> vs;
                for(int dr = 0; dr < k; ++dr) {
                    for(int dc = 0; dc < k; ++dc) {
                        vs.push_back(grid[r+dr][c+dc]);
                    }
                }
                int min_abs = INT_MAX;
                sort(begin(vs), end(vs));
                for(int i = 0; i < vs.size() - 1; ++i) {
                    if(vs[i+1] == vs[i]) continue;
                    min_abs = min(min_abs, abs(vs[i+1] - vs[i]));
                }
                result[r][c] = min_abs == INT_MAX ? 0: min_abs;
            }
        }
        return result;
    }
};
