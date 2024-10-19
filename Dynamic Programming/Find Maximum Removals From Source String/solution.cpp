class Solution {
public:
    int maxRemovals(string source, string pattern, vector<int>& targetIndices) {
        // dp[i][j] = dp[i+1][j] + i in targets
        // if s[i] == p[j]: dp[i][j] = max(dp[i][j], dp[i+1][j+1])
        vector<int> targets(source.size(), 0);
        for(auto i: targetIndices) targets[i] = 1;
        // dp[i][j] = max operations that match s[i:] and p[j:] 
        // could be optimized to 1d
        vector<vector<int>> dp(source.size()+1, vector<int>(pattern.size()+1, INT_MIN));
        dp[source.size()][pattern.size()] = 0;
        for(int i = source.size() - 1; i >= 0; --i) {
            for(int j = 0; j <= pattern.size(); ++j) {
                dp[i][j] = dp[i+1][j] + targets[i];
                if(j < pattern.size() && source[i] == pattern[j]) dp[i][j] = max(dp[i][j], dp[i+1][j+1]);
            }
        }
        return dp[0][0];
    }
};
