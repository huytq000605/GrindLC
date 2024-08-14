class Solution {
public:
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        vector<int> dp(n);
        for(int i = 0; i < n; i++) dp[i] = i;
        vector<vector<int>> prev(n, vector<int>());
        vector<int> result;
        for(auto q: queries) {
            int u = q[0], v = q[1];
            prev[v].emplace_back(u);
            for(int i = 1; i < n; ++i) {
                dp[i] = min(dp[i], dp[i-1] + 1);
                for(auto p: prev[i]) {
                    dp[i] = min(dp[i], dp[p] + 1);
                }
            }     
            result.emplace_back(dp[n-1]);
        }
        return result;
        
    }
};
