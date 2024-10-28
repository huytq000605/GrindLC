class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        map<long long, int> dp;
        int result = -1;
        for(int i = 0; i < nums.size(); ++i) {
            if(i && nums[i] == nums[i-1]) continue;
            long long num = nums[i];
            dp[num] += 1;
            dp[num*num] = dp[num];
            if(dp[num] > 1) result = max(result, dp[num]);
        }
        return result;
    }
};
