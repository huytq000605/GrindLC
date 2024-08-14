class Solution {
public:
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        vector<int> dp(n, 0);
        for(int i = 0; i < n-1; i++) dp[i] = i + 1;
        int res = n-1;
        vector<int> result;
        for(auto q: queries) {
            int u = q[0], v = q[1];
            // remove from [u, v-1]
            // set dp[i] = v for i in [u, v-1]
            // there will be no partial overlap intervals 
            // but thinking about the case [0, 3], [1, 3] require us to set dp[i] for all i in [u, v-1]
            while(dp[u] < v) {
                res--;
                int nu = dp[u];
                dp[u] = v;
                u = nu;
            }
            dp[u] = v;
            result.emplace_back(res);
        }
        return result;
    }
};
