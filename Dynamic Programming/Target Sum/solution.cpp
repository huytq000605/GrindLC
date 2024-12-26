class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        unordered_map<int, int> dp;
        dp[0] = 1;
        for(int num: nums) {
            unordered_map<int, int> ndp;
            for(auto [prev, ways]: dp) {
                ndp[prev - num] += ways;
                ndp[prev + num] += ways;
            }
            swap(dp, ndp);
        }
        return dp[target];
    }
};
