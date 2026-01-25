class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        sort(begin(nums), end(nums));
        int result = INT_MAX;
        for(int i = 0; i + k - 1< nums.size(); ++i) {
            result = min(result, nums[i+k-1] - nums[i]);
        }
        return result;
    }
};
