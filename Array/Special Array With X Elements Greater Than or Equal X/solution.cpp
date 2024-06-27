class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.rbegin(), nums.rend());
        int i = 0;
        while(i < nums.size() && nums[i] >= i+1) {
            i++;
        }
        // There are i nums >= i;
        // If nums[i] >= i => (i+1) nums >= i, not satisfy
        if(i < nums.size() && nums[i] >= i) return -1;
        return i;
    }
};
