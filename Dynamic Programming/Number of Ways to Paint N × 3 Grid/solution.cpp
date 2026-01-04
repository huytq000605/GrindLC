class Solution {
public:
    int numOfWays(int n) {
        vector<vector<int>> dp(5000, vector<int>(1 << 6, -1));
        int MOD = 1e9 + 7;
        auto dfs = [&](this auto&& dfs, int row, int mask) {
            if(row == n) {
                return 1;
            }
            if(dp[row][mask] != -1) return dp[row][mask];
            int result = 0;
            for(int nmask = 0; nmask < (1 << 6); nmask++) {
                bool valid = true;
                for(int col = 0, pbit = -1; col < 3; ++col) {
                    int bit = (mask >> (2 * col)) & 3;
                    int nbit = (nmask >> (2 * col)) & 3;
                    if(nbit == 3 || (pbit != -1 && pbit == nbit) || (row != 0 && bit == nbit)) {
                        valid = false;
                        break;
                    }
                    pbit = nbit;
                }
                if(!valid) continue;
                result = (result + dfs(row+1, nmask)) % MOD;
            }
            return dp[row][mask] = result;
        };

        return dfs(0, 0);
    }
};
