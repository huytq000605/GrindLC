class Solution {
public:
    int numWays(vector<string>& words, string target) {
        int MOD = 1e9 + 7;
        int m = words[0].size();
        vector<vector<int>> counter(m, vector<int>(26));
        for(int i{}; i < m; ++i) {
            for(auto &word: words) {
                ++counter[i][word[i] - 'a'];
            }
        }

        vector<long long> dp(m + 1, 0);
        dp[0] = 1;
        for(int i{}; i < target.size(); ++i) {
            vector<long long> ndp(m+1, 0);
            long long prefix{};
            for(int j{}; j < m; ++j) {
                prefix = (prefix + dp[j]) % MOD; 
                ndp[j+1] = (counter[j][target[i] - 'a'] * prefix) % MOD;
            }
            swap(dp, ndp);
        }
        return accumulate(dp.begin(), dp.end(), 0ll) % MOD;
    }
};
