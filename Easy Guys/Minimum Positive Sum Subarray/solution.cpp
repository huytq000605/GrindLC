class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int result{INT_MAX};
        for(int s{l}; s <= r; ++s) {
            int sum{};
            for(int i{}; i < nums.size(); ++i) {
                sum += nums[i];
                if(i+1 >= s) {
                    if(sum > 0) result = min(result, sum);
                    sum -= nums[i-s+1];
                }
            }
        }
        return result == INT_MAX ? -1 : result;
    }
};
