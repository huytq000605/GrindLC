class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        int mx = 0;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] <= mx) return false;
            int b = __builtin_popcount(nums[i]);
            int nmx = nums[i];
            while(i+1 < nums.size() && __builtin_popcount(nums[i+1]) == b) {
                if(nums[i+1] <= mx) return false;
                nmx = max(nmx, nums[i+1]);
                ++i;
            }
            mx = nmx;
        }
        return true;
    }
};
