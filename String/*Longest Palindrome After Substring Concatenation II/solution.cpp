class Solution {
public:
    int longestPalindrome(string s, string t) {
        int n = s.size(), m = t.size();
        int result = 0;
        vector<vector<bool>> dpS(n, vector<bool>(n));
        // s_extend_right[i] = longest length of palindrome build from s start at i
        vector<int> s_extend_right(n, 1);
        for(int i = n-1; i >= 0; --i) {
            for(int j = i; j < n; ++j) {
                dpS[i][j] = s[i] == s[j] && (j-i<2 || dpS[i+1][j-1]);
                if(dpS[i][j]) s_extend_right[i] = max(s_extend_right[i], j-i+1);
                result = max(result, s_extend_right[i]);
            }
        }

        vector<vector<bool>> dpT(m, vector<bool>(m));
        // t_extend_left[i] = longest length of palindrome build from t end at i
        vector<int> t_extend_left(m, 1);
        for(int i = m-1; i >= 0; --i) {
            for(int j = i; j < m; ++j) {
                dpT[i][j] = t[i] == t[j] && (j-i<2 || dpT[i+1][j-1]);
                if(dpT[i][j]) t_extend_left[j] = max(t_extend_left[j], j-i+1);
                result = max(result, t_extend_left[j]);
            }
        }
        
        vector<vector<int>> dp(n, vector<int>(m));
        for(int i = 0; i < n; ++i) {
            for(int j = m-1; j >= 0; --j) {
                dp[i][j] = s[i] == t[j];
                if(dp[i][j] && i-1 >= 0 && j+1 < m) dp[i][j] += dp[i-1][j+1];
                if(dp[i][j]) {
                    int extra = max(i+1 < n ? s_extend_right[i+1]: 0, 
                        j-1 >= 0 ? t_extend_left[j-1]: 0);
                    result = max(result, dp[i][j] * 2 + extra);
                }
            }
        }
        return result;
    }
};
