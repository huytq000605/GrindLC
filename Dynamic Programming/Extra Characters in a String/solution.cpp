class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        unordered_set<string> dict(dictionary.begin(), dictionary.end());
        vector<int> dp(s.size() + 1, 0);
        for(int i = 0; i < s.size(); ++i) {
            dp[i+1] = dp[i] + 1;
            for(int j = 0; j <= i; ++j) {
                string ss = s.substr(j, i-j+1);
                if(dict.find(ss) != dict.end()) {
                    dp[i+1] = min(dp[i+1], dp[j]);
                }
            }
        }
        return dp[s.size()];
    }
};
