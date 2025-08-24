class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int result = 0;
        for(int i = 0, j = 0, k = 0; i < nums.size(); ++i) {
            if(nums[i] == 0) ++k;
            while(k > 1) {
                k -= nums[j++] == 0;
            }
            result = max(result, i - j);
        }
        return result;
    }
};
