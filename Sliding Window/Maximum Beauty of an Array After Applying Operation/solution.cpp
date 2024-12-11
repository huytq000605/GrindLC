class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int result{};
        for(int i{}, j{}; i < nums.size(); ++i) {
            while(nums[i] - nums[j] > 2 * k) ++j;
            result = max(result, i - j + 1);
        }
        return result;
    }
};
