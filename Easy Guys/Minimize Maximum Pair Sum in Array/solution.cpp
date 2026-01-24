class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(begin(nums), end(nums));
        int result = 0;
        for(int i = 0; i < nums.size() / 2; ++i) {
            result = max(result, nums[i] + nums[nums.size() - 1 - i]);
        }
        return result;
    }
};
