class Solution {
static constexpr int MOD = 1000000007;
public:
    int countOfPairs(vector<int>& nums) {
        // dp[i][a1] = number of pairs that has i nums and last num1 is a1
        // dp[0][0] = 1
        // dp[i][na1] = sum(dp[i-1][a1]) where a1 in a range [0, X]
        // na2 = nums[i-1] - na1
        // a2 = nums[i-2] - a1
        // a2 >= na2 
        // => nums[i-2] - a1 >= nums[i-1] - na1
        // nums[i-2] - nums[i-1] + na1 >= a1
        // a1 <= nums[i-2] - nums[i-1] + na1
        // X = nums[i-2] - nums[i-1] + na1
        // X = min(X, nums[i])
        int n = nums.size();
        int m = *max_element(nums.begin(), nums.end());
        vector<int> dp(m + 1, 0);
        dp[0] = 1;
        for(int i = 1; i <= n; i++) {
            vector<int> ndp(m + 1, 0);
            int j = 0;
            int prefix = 0;
            for(int na1 = 0; na1 <= nums[i-1]; na1++) {
                int na2 = nums[i-1] - na1;
                // a2 >= na2
                // nums[i-2] - a1 >= na2
                // a1 <= nums[i-2] - na2
                int max_a1 = (i-2 >= 0 ? nums[i-2]: m+1) - na2;
                // a1 <= na1
                max_a1 = min(max_a1, na1);
                while(j <= m && j <= max_a1) {
                    prefix = (prefix + dp[j++]) % MOD;
                    prefix %= MOD;
                }
                ndp[na1] = prefix;
            }
            swap(ndp, dp);
        }
        int result = 0;
        for(auto d: dp) result = (result + d) % MOD;
        return result;
    }
};
