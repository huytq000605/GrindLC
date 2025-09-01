class Solution {
int dp[11][(1 << 11) - 1];
public:
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        memset(dp, 0, sizeof(dp));
        auto dfs = [&](this auto&& dfs, int w, int mask) {
            if(dp[w][mask]) return dp[w][mask];
            if(w >= workers.size()) {
                return 0;
            }
            int result = INT_MAX;
            for(int b = 0; b < bikes.size(); ++b) {
                if(mask & (1 << b)) continue;
                result = min(result, abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1]) + dfs(w+1, mask | (1 << b)));
            }
            return dp[w][mask] = result;
        };
        return dfs(0, 0);
    }
};
