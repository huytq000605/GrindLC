class Solution {
public:
    int sumOfGoodNumbers(vector<int>& nums, int k) {
        int n = nums.size();
        int result{};
        for(int i = 0; i < n; ++i) {
            if((i-k < 0 || nums[i] > nums[i-k]) && (i+k >= n || nums[i] > nums[i+k])) result += nums[i];
        }
        return result;
    }
};
