class Solution {
public:
    long long maxScore(vector<int>& a, vector<int>& b) {
        int n = b.size();
        vector<long long> dp(n, 0);
        for(int i = 0; i < n; ++i) dp[i] = static_cast<long long>(a[0]) * b[i];
        
        for(int i = 1; i < 4; ++i) {
            vector<long long> ndp(n, LLONG_MIN);
            long long mx = dp[i-1];
            for(int j = i; j < n; ++j) {
                ndp[j] = mx + static_cast<long long>(a[i]) * b[j];
                mx = max(mx, dp[j]);
            }
            swap(dp, ndp);
        }

        return *max_element(dp.begin(), dp.end());
        
    }
};
