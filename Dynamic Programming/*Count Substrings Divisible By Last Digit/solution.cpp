class Solution {
public:
    long long countSubstrings(string s) {
        long long result{};
        for(int t = 1; t < 10; ++t) {
            vector<long long> dp(t);
            for(int i = 0; i < s.size(); ++i) {
                vector<long long> ndp(t);
                int d = s[i] - '0';
                for(int prev = 0; prev < t; ++prev) {
                    ndp[(prev*10 + d) % t] += dp[prev];
                }
                ndp[d%t] += 1;
                dp = ndp;
                if(d == t) result += dp[0];
            }
        }
        return result;
    }
};
