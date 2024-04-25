class Solution {
public:
    int longestIdealString(string s, int k) {
        int dp[26] = {0};
        for(int i = 0; i < s.size(); i++) {
            int c = s[i] - 'a';
            dp[c] = *max_element(dp + max(0, c - k), dp + min(26, c + k + 1)) + 1;
        }
        return *max_element(dp, dp+26);
    }
};
