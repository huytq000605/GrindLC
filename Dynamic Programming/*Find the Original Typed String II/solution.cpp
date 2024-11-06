class Solution {
static constexpr int MOD = 1000000007;
public:
    int possibleStringCount(string word, int k) {
        vector<int> segments;
        long long total = 1;
        for(int i{0}; i < word.size(); ++i) {
            int cnt = 1;
            while(i+1 < word.size() && word[i] == word[i+1]) {
                cnt = (cnt+1) % MOD;
                ++i;
            }
            total = (total * cnt) % MOD;
            segments.emplace_back(cnt);
        }
        if(segments.size() >= k) return total;
        // dp[i][j] = number of ways that type j characters with i segments
        // dp[i][j] = dp[i-1][j-1] + dp[i-1][j-2] + ... + dp[i-2][j-segments[i]]
        // => dp[i][j] = prefix[i-1][j-1] - prefix[i][j-segments[i]-1]
        vector<int> dp(k, 0);
        dp[0] = 1;
        for(int i{0}; i < segments.size(); ++i) {
            vector<int> prefix(k, 0);
            for(int j = 0; j < k; ++j) {
                if(j) prefix[j] = prefix[j-1];
                prefix[j] = (prefix[j] + dp[j]) % MOD;
            }
            vector<int> ndp(k, 0);
            for(int j = i+1; j < k; ++j) {
                ndp[j] = prefix[j-1] - (j-segments[i]-1 >= 0 ? prefix[j - segments[i]-1]: 0);
                ndp[j] %= MOD;
            }
            dp = move(ndp);
        }
        
        int less_than_k = 0;
        for(int i{0}; i < dp.size(); ++i) less_than_k = (less_than_k + dp[i]) % MOD;
        return (total - less_than_k + MOD) % MOD;
    }
};
