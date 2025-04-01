class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        vector<long long> dp(n+1);
        for(int i = n-1; i >= 0; --i) {
            auto& q = questions[i];
            int p = q[0], b = q[1];
            dp[i] = max(dp[i+1], dp[min(i+b+1, n)] + p);
        }
        return dp[0];
    }
};
