class Solution {
public:
    int countSubarrays(vector<int>& nums) {
        int result{};
        for(int i{2}; i < nums.size(); ++i) {
            if((nums[i-2] + nums[i]) * 2 == nums[i-1]) ++result;
        }
        return result;
    }
};
