class Solution {
public:
    int minScoreTriangulation(vector<int>& values) {
        int n = values.size();
        vector<vector<int>> dp(n, vector<int>(n));
        auto dfs = [&](this auto&& dfs, int i, int j) {
            if(j - i + 1 < 3) return 0;
            if(dp[i][j]) return dp[i][j];
            int result = INT_MAX;
            for(int k = i+1; k < j; ++k) {
                result = min(result, dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j]);
            }
            return dp[i][j] = result;
        };
        return dfs(0, n-1);
    }
};
