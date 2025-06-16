class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int result = -1;
        for(int i = 1, mn = nums.front(); i < nums.size(); ++i) {
            if(nums[i] > mn) result = max(result, nums[i] - mn);
            mn = min(mn, nums[i]);
        }
        return result;
    }
};
