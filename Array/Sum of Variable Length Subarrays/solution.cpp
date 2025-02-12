class Solution {
public:
    int subarraySum(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix(n+1);
        for(int i{}; i < n; ++i) prefix[i+1] = prefix[i] + nums[i];
        int result{};
        for(int i{}; i < n; ++i) {
            int start = max(0, i - nums[i]);
            result += prefix[i+1] - prefix[start];
        }
        return result;
    }
};
