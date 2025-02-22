class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int last_zero{-1};
        int result{};
        for(int i{}, j{}; i < nums.size(); ++i) {
            if(!nums[i]) {
                j = last_zero + 1;
                last_zero = i;
            }
            result = max(result, i - j + 1);
        }
        return result;
    }
};
