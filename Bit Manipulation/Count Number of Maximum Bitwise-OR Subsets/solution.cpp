class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int target = 0;
        for(int num: nums) target |= num;
        int result = 0;
        for(int mask = 0; mask < (1 << nums.size()); ++mask) {
            int v = 0;
            for(int i = 0; i < nums.size(); ++i) {
                if(mask & (1 << i)) v |= nums[i]; 
            }
            result += v == target;
        }
        return result;
    }
};
