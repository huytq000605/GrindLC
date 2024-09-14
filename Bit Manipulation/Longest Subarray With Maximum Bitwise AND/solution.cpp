class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int mx = *max_element(nums.begin(), nums.end());
        int result = 1;
        int streak = 0;
        for(int num: nums) {
            if(num == mx) ++streak;
            else streak = 0;
            result = max(result, streak);
        }
        return result;
    }
};
