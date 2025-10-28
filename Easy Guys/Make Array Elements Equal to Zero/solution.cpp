class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        int s = accumulate(nums.begin(), nums.end(), 0);
        int result = 0;
        for(int i = 0, left = 0; i < nums.size(); ++i) {
            left += nums[i];
            if(!nums[i]) {
                int d = abs(left - (s-left));
                result += d == 0 ? 2: d == 1 ? 1: 0;
            }
        }
        return result;
    }
};
