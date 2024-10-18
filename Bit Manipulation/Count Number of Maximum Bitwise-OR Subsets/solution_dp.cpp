class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        unordered_map<int, int> dp;
        int mx = 0;
        dp[0] = 1;
        for(int num: nums) {
            auto ndp = dp;
            for(auto [k, v]: dp) {
                ndp[k | num] += dp[k]; 
            }
            swap(dp, ndp);
            mx |= num;
        }
        return dp[mx];
    }
};
