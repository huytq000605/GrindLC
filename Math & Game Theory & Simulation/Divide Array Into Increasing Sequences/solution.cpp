class Solution {
public:
    bool canDivideIntoSubsequences(vector<int>& nums, int k) {
        int n = nums.size();
        int max_freq = 0;
        for(int i = 0, freq = 0; i < nums.size(); ++i) {
            freq = (i == 0 || nums[i] == nums[i-1]) ? freq + 1: 1;
            max_freq = max(max_freq, freq);
        }
        return max_freq * k <= n;
    }
};
