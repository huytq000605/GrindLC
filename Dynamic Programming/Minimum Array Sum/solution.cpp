class Solution {
public:
    int minArraySum(vector<int>& nums, int k, int op1, int op2) {
        vector<vector<int>> dp(op1+1, vector<int>(op2+1, INT_MAX));
        dp[0][0] = 0;
        for(int num: nums) {
            vector<vector<int>> ndp(op1+1, vector<int>(op2+1, INT_MAX));
            for(int i{}; i <= op1; ++i) {
                for(int j{}; j <= op2; ++j) {
                    if(dp[i][j] != INT_MAX) ndp[i][j] = dp[i][j] + num;
                    if(i && dp[i-1][j] != INT_MAX) ndp[i][j] = min(ndp[i][j], dp[i-1][j] + (num+1)/ 2);
                    if(j && num >= k && dp[i][j-1] != INT_MAX) ndp[i][j] = min(ndp[i][j], dp[i][j-1] + (num - k));
                    if(i && j && num >= k && dp[i-1][j-1] != INT_MAX) ndp[i][j] = min(ndp[i][j], dp[i-1][j-1] + ((num+1)/2 >= k ? (num+1)/2 - k : (num-k+1)/2) );
                }
            }
            swap(dp, ndp);
        }
        
        int result{INT_MAX};
        for(int i{}; i <= op1; ++i) {
            for(int j{}; j <= op2; ++j) {
                result = min(result, dp[i][j]);
            }
        }
        return result;
    }
};
