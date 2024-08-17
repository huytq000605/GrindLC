class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        int m = points.size(), n = points[0].size();
        vector<long long> dp(points[0].begin(), points[0].end());
        for(long long r = 1; r < m; r++) {
            vector<long long> ndp(n, 0);
            for(long long c = 0, mx = 0; c < n; c++) {
                mx = max(mx-1, dp[c]);
                ndp[c] = points[r][c] + mx;
            }
            for(long long c = n-1, mx = 0; c >= 0; c--) {
                mx = max(mx-1, dp[c]);
                ndp[c] = max(ndp[c], points[r][c] + mx);
            }
            swap(dp, ndp);
        }
        return *max_element(dp.begin(), dp.end());
    }
};
