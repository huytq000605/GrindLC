class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        sort(events.begin(), events.end());
        vector<vector<int>> dp(events.size(), vector<int>(k+1, -1));
        auto dfs = [&](this auto&& dfs, int e, int k) -> int {
            if(e >= events.size()) return 0;
            if(dp[e][k] != -1) return dp[e][k];
            int result = dfs(e + 1, k);
            if(!k) return dp[e][k] = result;
            int lo = e+1, hi = events.size();
            while(lo < hi) {
                int mi = lo + (hi - lo) / 2;
                if(events[mi][0] <= events[e][1]) {
                    lo = mi + 1;
                } else {
                    hi = mi;
                }
            }
            result = max(result, events[e][2] + dfs(lo, k-1));
            return dp[e][k] = result;
        };
        return dfs(0, k);
    }
};
