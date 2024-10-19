class Solution {
private:
    static constexpr int MOD = 1000000007;
    static inline long long dp[1001][1001] = {}, comb[1001][1001] = {};
    void init() {
        dp[0][0] = comb[0][0] = 1;
        for(int i = 1; i <= 1000; ++i) {
            comb[i][0] = 1;
            for(int j = 1; j <= i; ++j) {
                dp[i][j] = (j * dp[i-1][j-1] % MOD) + (j * dp[i-1][j] % MOD);
                dp[i][j] %= MOD;
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD;
            }
        }
    }
    
public:
    int numberOfWays(int n, int x, int y) {
        if(dp[0][0] == 0) init();
        long long pow = 1;
        long long result = 0;
        for(int m = 1; m <= min(n, x); ++m) {
            // stage selection
            long long res = comb[x][m];
            // putting n people to m stages
            res = (res * dp[n][m]) % MOD;
            // award for each stage
            pow = (pow * y) % MOD;
            res = (res * pow) % MOD;
            result = (result + res) % MOD;
        }
        return result;
        
    }
};
