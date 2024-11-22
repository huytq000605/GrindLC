class Solution {
public:
    vector<vector<int>> minScore(vector<vector<int>>& grid) {
        vector<pair<int, int>> rcs;
        for(int r{}; r < grid.size(); ++r) {
            for(int c{}; c < grid[0].size(); ++c) {
                rcs.emplace_back(r, c);
            }
        }
        function<bool(pair<int, int>, pair<int, int>)> cmp = [&grid](auto p1, auto p2) {
            return grid[p1.first][p1.second] < grid[p2.first][p2.second];
        };
        sort(rcs.begin(), rcs.end(), cmp);
        vector<int> rows(grid.size(), 0);
        vector<int> cols(grid[0].size(), 0);
        for(auto [r, c]: rcs) {
            int v = max(rows[r], cols[c]) + 1;
            rows[r] = v;
            cols[c] = v;
            grid[r][c] = v;
        }
        return grid;
    }
};
