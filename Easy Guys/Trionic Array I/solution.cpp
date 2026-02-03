class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        if(nums[1] <= nums[0]) return false;
        int k = 0;
        for(int i = 2; i < nums.size(); ++i) {
            if(nums[i] == nums[i-1]) return false;
            if(k == 0 && nums[i] < nums[i-1]) {
                ++k;
            } else if(k == 1 && nums[i] > nums[i-1]) {
                ++k;
            } else if(k == 2 && nums[i] < nums[i-1]) return false;
        }   
        return k == 2;
    }
};
