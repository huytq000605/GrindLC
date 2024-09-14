class Solution {
public:
    long long findMaximumScore(vector<int>& nums) {
        int i = 0;
        long long result = 0;
        for(int j = 0; j < nums.size(); ++j) {
            if(nums[j] > nums[i] || j == nums.size() - 1) {
                result += static_cast<long long>(j - i) * nums[i];
                i = j;
            }
        }
        return result;
    }
};
