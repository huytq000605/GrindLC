class Solution {
public:
    long long gridGame(vector<vector<int>>& grid) {
        int n = grid[0].size();
        long long result{LLONG_MAX};
        long long bot = accumulate(grid[1].begin(), grid[1].end(), 0ll);
        long long top = accumulate(grid[0].begin(), grid[0].end(), 0ll);
        long long r2_top{}, r2_bot{bot};
        for(int c{}; c < n; ++c) {
            r2_top += grid[0][c];
            long long robot1 = max(top - r2_top, bot - r2_bot);
            result = min(result, robot1);
            r2_bot -= grid[1][c];
        }
        return result;
    }
};
