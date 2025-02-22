class Solution {
public:
    int maximumAmount(vector<vector<int>>& coins) {
        int m = coins.size(), n = coins[0].size();
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(3, INT_MIN)));
        dp[0][0][0] = coins[0][0];
        if(coins[0][0] < 0) dp[0][0][1] = 0;
        for(int r{}; r < m; ++r) {
            for(int c{}; c < n; ++c) {
                if(r == 0 && c == 0) continue;
                for(int used{}; used < 3; ++used) {
                    if(r) {
                        if(dp[r-1][c][used] != INT_MIN) dp[r][c][used] = max(dp[r][c][used], dp[r-1][c][used] + coins[r][c]);
                        if(used && coins[r][c] < 0 && dp[r][c][used-1] != INT_MIN) dp[r][c][used] = max(dp[r][c][used], dp[r-1][c][used-1]);
                    }
                    
                    if(c) {
                        if(dp[r][c-1][used] != INT_MIN) dp[r][c][used] = max(dp[r][c][used], dp[r][c-1][used] + coins[r][c]);
                        if(used && coins[r][c] < 0 && dp[r][c][used-1] != INT_MIN) dp[r][c][used] = max(dp[r][c][used], dp[r][c-1][used-1]);
                    }
                }
            }
        }
        
        return *max_element(dp[m-1][n-1].begin(), dp[m-1][n-1].end());
    }
};
