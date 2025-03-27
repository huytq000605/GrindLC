class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        int majority = nums[0], count = 1;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] == majority) ++count;
            else --count;
            if(!count) {
                majority = nums[i];
                count = 1;
            }
        }
        count = 0;
        for(int num: nums) count += num == majority;

        for(int i = 0, left = 0, right = count; i < nums.size()-1; ++i) {
            left += nums[i] == majority;
            right -= nums[i] == majority;
            if(left*2 > i+1 && right*2 > (nums.size()-1-i)) return i;
        }
        return -1;
    }
};
