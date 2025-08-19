class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long result = 0;
        for(int i = 0, cur = 0; i < nums.size(); ++i) {
            if(nums[i] != 0) cur = 0;
            else ++cur;
            result += cur;
        }
        return result;
    }
};
