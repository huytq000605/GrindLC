class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int start = 0;
        int result = 0;
        for(int end = 0; end < nums.size(); end++) {
            if(nums[end] == 0) k--;
            while(k < 0) {
                k += nums[start++] == 0;
            }
            result = max(result, end - start + 1);
        }
        return result;
    }
};
