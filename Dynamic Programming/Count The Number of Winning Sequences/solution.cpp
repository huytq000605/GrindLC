class Solution {
static constexpr int MOD = 1000000007;
public:
    int countWinningSequences(string s) {
        // fwe
        vector<int> A;
        for(int i = 1; i < s.size(); ++i) {
            char c = s[i];
            if(c == 'F') A.emplace_back(0);
            else if(c == 'W') A.emplace_back(1);
            else if(c == 'E') A.emplace_back(2);
        }
        // dp[i][j] = number of ways for B end at i and diff points = j
        vector<vector<int>> dp(3, vector<int>(2001, 0));
        for(int b = 0; b < 3; ++b) {
            int a = s[0]=='F'? 0 : ((s[0] == 'W') ? 1 : 2); 
            int c = 0;
            if((a+1) % 3 == b) { // a < b
                c = -1;
            } else if((b+1) % 3 == a) { // b < a
                c = 1;
            }
            dp[b][1000-c] = 1;
        }

        for(int a: A) {
            vector<vector<int>> ndp(3, vector<int>(2001, 0));
            for(int b = 0; b < 3; ++b) {
                int c = 0;
                
                if((a+1) % 3 == b) { // a < b
                    c = -1;
                } else if((b+1) % 3 == a) { // b < a
                    c = 1;
                }
                for(int i = 1; i < 2000; ++i) {
                    for(int pb = 0; pb < 3; ++pb) {
                        if(pb == b) continue;
                        ndp[b][i] = (ndp[b][i] + dp[pb][i+c]) % MOD;
                    }
                }
            }
            swap(dp, ndp);
        }
        int result = 0;
        for(int b = 0; b < 3; ++b) {
            for(int d = 1001; d < 2001; ++d) result = (result + dp[b][d]) % MOD;
        }
        return result;
    }
};
