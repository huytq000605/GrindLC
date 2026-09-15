class Solution {
public:
    int maxPalindromes(string s, int k) {
        int n = s.size();
        vector<int> dp(n, 0);
        vector<vector<bool>> is_palindrome(n, vector<bool>(n));
        for(int j = 0; j < n; ++j) {
            is_palindrome[j][j] = true;
            for(int i = j-1, k = j+1; i >= 0 && k < n; --i, ++k) {
                if(s[i] != s[k]) break;
                is_palindrome[i][k] = true;
            }

            for(int i = j-1, k = j; i >= 0 && k < n; --i, ++k) {
                if(s[i] != s[k]) break;
                is_palindrome[i][k] = true;
            }
        }
        for(int i = 0; i < n; ++i) {
            if(i) dp[i] = dp[i-1];
            for(int j = i-k+1; j >= 0; --j) {
                if(is_palindrome[j][i]) {
                    dp[i] = max(dp[i], 1 + (j ? dp[j-1]: 0));
                }
            }
        }
        return dp.back();
    }
};
