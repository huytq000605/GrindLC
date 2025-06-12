class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int n = nums.size();
        int result = abs(nums.front() - nums.back());
        for(int i = 0; i < n-1; ++i) {
            result = max(result, abs(nums[i] - nums[i+1]));
        }
        return result;
    }
};
