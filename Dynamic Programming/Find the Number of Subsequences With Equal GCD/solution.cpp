class Solution {
static constexpr int MOD = 1000000007;
public:
    int subsequencePairCount(vector<int>& nums) {
        int mx = *max_element(nums.begin(), nums.end());
        // dp[i][j] = number of pairs where seq1 has gcd = i, seq2 has gcd = j
        vector<vector<int>> dp(mx+1, vector<int>(mx+1));
        dp[0][0] = 1;
        for(int num: nums) {
            vector<vector<int>> ndp(mx+1, vector<int>(mx+1));
            for(int i = 0; i <= mx; ++i) {
                for(int j = 0; j <= mx; ++j) {
                    ndp[i][j] = (ndp[i][j] + dp[i][j]) % MOD;
                    ndp[gcd(i, num)][j] = (ndp[gcd(i, num)][j] + dp[i][j]) % MOD;
                    ndp[i][gcd(j, num)] = (ndp[i][gcd(j, num)] + dp[i][j]) % MOD;
                }
            }
            dp = move(ndp);
        }
        int result = 0;
        for(int i = 1; i <= mx; ++i) result = (result + dp[i][i]) % MOD;
        return result;
    }
};
