class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(n+1, vector<int>(m+1, INT_MIN));
        dp[0][0] = 0;
        int result = 0;
        for(auto& str: strs) {
            int o = 0, z = 0;
            for(char c: str) {
                z += c == '0';
                o += c == '1';
            }
            for(int i = n-o; i >= 0; --i) {
                for(int j = m-z; j >= 0; --j) {
                    if(dp[i][j] == INT_MIN) continue;
                    dp[i+o][j+z] = max(dp[i+o][j+z], dp[i][j] + 1);
                    result = max(dp[i+o][j+z], result);
                }
            }
        }
        return result;
    }
};
