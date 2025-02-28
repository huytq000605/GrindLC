class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        int n = str1.size(), m = str2.size();
        vector<vector<int>> dp(n+1, vector<int>(m+1, m+n+1));
        for(int i = 0; i < n; ++i) dp[i][0] = i;
        for(int j = 0; j < m; ++j) dp[0][j] = j;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                dp[i+1][j+1] = min({dp[i+1][j+1], dp[i][j+1] + 1, dp[i+1][j] + 1, (str1[i] == str2[j]) ? (dp[i][j] + 1): m+n+1});
            }
        }
        string rresult{};
        int i = n-1, j = m-1;
        for(; i >= 0 && j >= 0;) {
            if(str1[i] == str2[j]) {
                rresult += str1[i];
                --i;
                --j;
            } else if(dp[i+1][j] + rresult.size() + 1 == dp[n][m]) {
                rresult += str2[j--];
            } else {
                rresult += str1[i--];
            }
        }
        while(i >= 0) rresult += str1[i--];
        while(j >= 0) rresult += str2[j--] ;
        return string(rresult.rbegin(), rresult.rend());
    }
};
