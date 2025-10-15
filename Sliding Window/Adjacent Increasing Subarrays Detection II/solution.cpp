class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int prev = 0, up = 0;
        int result = 0;
        for(int i = 0; i < nums.size(); ++i) {
            if(!i || nums[i] > nums[i-1]) up++;
            else {
                prev = up;
                up = 1;
            }
            result = max(result, max(up / 2, min(prev, up)));
        }
        return result;
    }
};
