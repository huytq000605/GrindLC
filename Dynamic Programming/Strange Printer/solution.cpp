class Solution {
public:
    int strangePrinter(string s) {
        string ss;
        for(char c: s) {
            if(!ss.empty() && ss[ss.size() - 1] == c) continue;
            ss += c;
        }
        int n = ss.size();
        // dp[i][j] = number of turns to print ss[i:j+1] 
        vector<vector<int>> dp(n, vector<int>(n, n+1));
        for(int i = 0; i < n; ++i) dp[i][i] = 1;
        // length of string
        for(int l = 2; l <= n; ++l) {
            for(int i = 0; i+l-1 < n; ++i) {
                // number of chars on the left
                for(int k = 1; k < l; ++k) {
                    dp[i][i+l-1] = min(dp[i][i+l-1], dp[i][i+k-1] + dp[i+k][i+l-1] - (ss[i] == ss[i+l-1]));
                }
            }
        }
        return dp[0][n-1];
    }
};
