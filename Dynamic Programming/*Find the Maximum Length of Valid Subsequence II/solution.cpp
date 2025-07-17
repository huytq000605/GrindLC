class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        int n = nums.size();
        int result = 0;
        for(int mod = 0; mod < k; ++mod) {
            vector<int> dp(k);
            for(int i = 0; i < n; ++i) {
                dp[nums[i] % k] = dp[((mod % k - nums[i] % k) + k) % k] + 1;
                result = max(result, dp[nums[i] % k]);
            }
        }
        return result;
        
    }
};
