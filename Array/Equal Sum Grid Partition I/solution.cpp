class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        long long s = 0;
        for(int r = 0; r < m; ++r) 
            for(int c = 0; c < n; ++c) s += grid[r][c];
        if(s&1) return false;
        vector<long long> dp(n, 0);
        for(int r = 0; r < m; ++r) {
            vector<long long> ndp(n, 0);
            for(int c = 0; c < n; ++c) {
                ndp[c] = dp[c] + (c-1 >= 0 ? ndp[c-1]: 0) - (c-1 >= 0 ? dp[c-1]: 0) + grid[r][c];
                if(r == m -1 && ndp[c] * 2 == s) return true;
            }
            if(ndp.back() * 2 == s) return true;
            dp = ndp;
        }
        return false;
    }
};
