class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int result{};
        vector<vector<int>> dp(301, vector<int>(301));
        // dp[i][j] = length of longest subsequence ending at nums[i] and 
        // diff is at least j
        for(int num: nums) {
            for(int prev{1}; prev <= 300; ++prev) {
                int diff = abs(prev - num);
                dp[num][diff] = max(dp[num][diff], dp[prev][diff] + 1);
            }
            // dp[num][diff] is valid then dp[num][diff-1] must be at least dp[num][diff]
            for(int diff{299}; diff >= 0; --diff) {
                dp[num][diff] = max(dp[num][diff], dp[num][diff+1]);
                result = max(result, dp[num][diff]);
            }
        }
        
        return result;
    }
};
