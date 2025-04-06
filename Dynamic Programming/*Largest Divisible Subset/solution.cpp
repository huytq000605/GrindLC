class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> dp(nums.size(), 1);
        for(int i = 0; i < nums.size(); ++i) {
            for(int j = 0; j < i; ++j) {
                if(nums[i] % nums[j] == 0) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        int size = *max_element(dp.begin(), dp.end());
        vector<int> result;
        for(int i = nums.size() - 1; i >= 0; --i) {
            if(dp[i] == size && (result.empty() || result.back() % nums[i] == 0)) {
                result.emplace_back(nums[i]);
                --size;
            }
        }
        return result;
    }
};
