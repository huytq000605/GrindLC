class Solution {
public:
    vector<int> cheapestJump(vector<int>& coins, int maxJump) {
        int n = coins.size();
        vector<int> dp(n, INT_MAX), pos(n, -1), sz(n, 0);
        dp[0] = coins[0];
        sz[0] = 1;
        for(int i = 1; i < n; ++i) {
            if(coins[i] == -1) continue;
            for(int j = max(i - maxJump, 0); j < i; ++j) {
                if(dp[j] == INT_MAX) continue;
                if(dp[j] + coins[i] < dp[i] || (dp[j] + coins[i] == dp[i] && sz[j] + 1 > sz[i])) {
                    dp[i] = dp[j] + coins[i];
                    pos[i] = j;
                    sz[i] = sz[j] + 1;
                }
            }
        }
        if(dp.back() == INT_MAX) return {};
        vector<int> result;
        int p = n-1;
        while(p != -1) {
            result.push_back(p+1);
            p = pos[p];
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
