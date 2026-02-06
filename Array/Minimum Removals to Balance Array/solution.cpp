class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        sort(begin(nums), end(nums));
        int result = nums.size() - 1;
        for(int i = 0, j = 0; i < nums.size() && j < nums.size(); ++i) {
            while(j < nums.size() && 1LL * nums[i] * k >= nums[j]) ++j;
            result = min(result, i + static_cast<int>(nums.size()) - j);
        }
        return result;
    } 
};
