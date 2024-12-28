class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        vector<int> prefix(nums.size() + 1, 0);
        for(int i{}; i < nums.size(); ++i) {
            prefix[i+1] = prefix[i] + nums[i];
        }
        // dp[i][j] = maximum sum with (i+1) subarrays using nums[:j]
        vector<vector<int>> dp(3, vector<int>(nums.size() + 1, 0));
        for(int i{}; i < 3; ++i) {
            for(int j{(i+1)*k}; j <= nums.size(); ++j) {
                dp[i][j] = (i ? dp[i-1][j-k]: 0) + prefix[j] - prefix[j-k];
                dp[i][j] = max(dp[i][j], dp[i][j-1]);
            }
        }
        int target = *max_element(dp[2].begin(), dp[2].end());
        vector<int> result(3, 0);
        for(int i{2}; i >= 0; --i) {
            int ntarget{};
            int chosen_j{-1};
            for(int j{(i+1)*k}; j <= nums.size(); ++j) {
                if(dp[i][j] == target) {
                    ntarget = i ? dp[i-1][j-k]: 0;
                    chosen_j = j;
                    break;
                }
            }
            target = ntarget;
            result[i] = chosen_j - k;
        }
        return result;
    }
};
