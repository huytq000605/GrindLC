class Solution {
public:
    int maxSumAfterOperation(vector<int>& nums) {
        int dp1{}, dp2{};
        int result{};
        for(int num: nums) {
            dp2 = max(dp2 + num, dp1 + num * num);
            dp1 = max(0, dp1 + num);
            result = max(result, dp2);
        }
        return result;
    }
};
