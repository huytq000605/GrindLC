class Solution {
long long dp[50000][27][4];
public:
    long long dfs(int i, int p, int length, string &s) {
        if(i >= s.size()) {
            if(length == 3) return 0;
            return INT_MAX;
        }
        if(dp[i][p][length] != -1) return dp[i][p][length];
        long long result = INT_MAX;
        if(length == 3 || length == 0) {
            for(int nc{}; nc < 26; ++nc) {
                int ops = abs(nc - (s[i] - 'a'));
                int nlength = nc == p ? min(3, length + 1): 1;
                long long possible = dfs(i+1, nc, nlength, s);
                if(possible != INT_MAX) {
                    result = min(result, ops + possible);
                }
            }
        } else {
            long long possible = dfs(i+1, p, length + 1, s);
            if(possible != INT_MAX) result = abs(p - (s[i] - 'a')) + possible;
        }
        return dp[i][p][length] = result;
    };

    string minCostGoodCaption(string s) {
        memset(dp, -1, sizeof(dp));
        int n = s.size();
        if(n < 3) return "";
        long long min_ops = dfs(0, 26, 0, s);
        int ops{};
        int length{};
        string result(n, 'a');
        for(int i{}; i < n; ++i) {
            int p = i ? result[i-1] - 'a': 26;
            if(length == 3 || length == 0) {
                for(int c{}; c < 26; ++c) { 
                    int cost = abs(c - (s[i]-'a'));
                    int nlength = c == p ? min(3, length + 1): 1;
                    int possible = dfs(i+1, c, nlength, s);
                    if(possible != INT_MAX && ops + cost + possible == min_ops) {
                        result[i] = char(c + 'a');
                        ops += cost;
                        length = nlength;
                        break;
                    }
                }
            } else {
                ops += abs(result[i-1] - s[i]);
                length += 1;
                result[i] = result[i-1];
            }
        }
        return result;
    }
};
