class Solution {
public:
    int countPartitions(vector<int>& nums) {
        int result{};
        int s = accumulate(nums.begin(), nums.end(), 0);
        for(int i{}, left{}; i < nums.size() - 1; ++i) {
            left += nums[i];
            int right = s - left;
            if(abs(right - left) % 2 == 0) ++result;
        }
        return result;
    }
};
