class Solution {
public:
    long long minCost(int n, vector<vector<int>>& costs) {
        vector<vector<long long>> dp(3, vector<long long>(3));
        for(int i{}; i < n/2; ++i) {
            vector<vector<long long>> ndp(3, vector<long long>(3, LLONG_MAX));
            for(int pl{}; pl < 3; ++pl) {
                for(int pr{}; pr < 3; ++pr) {
                    if(pl == pr) continue;
                    for(int l{}; l < 3; ++l) {
                        if(l == pl) continue;
                        for(int r{}; r < 3; ++r) {
                            if(l == r || r == pr) continue;
                            ndp[l][r] = min(ndp[l][r], dp[pl][pr] + costs[i][l] + costs[n-1-i][r]);
                        }
                    }
                }
            }
            dp = ndp;
        }
        long long result{LLONG_MAX};
        for(int pl{}; pl < 3; ++pl) {
            for(int pr{}; pr < 3; ++pr) {
                result = min(result, dp[pl][pr]);
            }
        }
        return result;
    }
};
