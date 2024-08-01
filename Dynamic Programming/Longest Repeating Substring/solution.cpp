class Solution {
public:
    int longestRepeatingSubstring(string s) {
        int n = s.size();
        int result = 0;
        // dp[i][j] = longest common substring ending at i and j
        vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                if(s[i] == s[j]) {
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1);
                    result = max(result, dp[i+1][j+1]);
                }
            }
        }
        return result;
    }
};
