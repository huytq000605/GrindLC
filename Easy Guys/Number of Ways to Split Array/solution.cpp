class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        long long s = accumulate(nums.begin(), nums.end(), 0ll);
        long long result{}, left{};
        for(int i{}; i < nums.size() - 1; ++i) {
            left += nums[i];
            if(left >= s - left) ++result;
        }
        return result;
    }
};
