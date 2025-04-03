class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long result = 0;
        long long mx = nums[0], mx_diff = 0;
        for(int i = 1; i < nums.size(); ++i) {
            result = max(result, mx_diff * nums[i]);
            mx_diff = max(mx_diff, mx - nums[i]);
            mx = max(mx, static_cast<long long>(nums[i]));
        }
        return result;
    }
};
