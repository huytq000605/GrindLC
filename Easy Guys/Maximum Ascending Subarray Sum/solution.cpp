class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int result{nums[0]};
        for(int i{1}, s{nums[0]}; i < nums.size(); ++i) {
            if(nums[i] > nums[i-1]) {
                s += nums[i];
            } else {
                s = nums[i];
            }
            result = max(result, s);
        }
        return result;
    }
};
