class Solution {
public:
    int minOperations(vector<int>& nums) {
        int ones = count(nums.begin(), nums.end(), 1);
        if(ones) return nums.size() - ones;
        int result = INT_MAX;
        for(int i = 0; i < nums.size(); ++i) {
            int g = nums[i];
            for(int j = i+1; j < nums.size(); ++j) {
                g = gcd(g, nums[j]);
                if(g == 1) {
                    result = min(result, j - i - 1 + static_cast<int>(nums.size()));
                }
            }
        }
        return result == INT_MAX ? -1: result;
    }
};
