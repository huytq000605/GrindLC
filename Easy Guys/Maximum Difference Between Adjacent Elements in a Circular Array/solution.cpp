class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int result{nums[1] - nums[0]};
        for(int i{}; i < nums.size(); ++i) {
            result = max(result, abs(nums[i] - nums[(i+1)%(nums.size())]));
        }
        return result;
    }
};
