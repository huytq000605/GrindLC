class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        // dp[i] = length of suffix word2 that word1 starts from i can match
        vector<int> dp(m+1, 0);
        for(int i = m-1, j = n-1; i >= 0; --i) {
            dp[i] = dp[i+1];
            if(j >= 0 && word1[i] == word2[j]) {
                --j;
                ++dp[i];
            }
        }
        int skip = 1;
        vector<int> result;
        for(int i = 0, j = 0; i < m && j < n; ++i) {
            if(word1[i] == word2[j]) {
                result.emplace_back(i);
                ++j;
            } else if(skip && result.size() + skip + dp[i+skip] >= word2.size()) {
                ++j;
                --skip;
                result.emplace_back(i);
            }
        }
        return result.size() == word2.size() ? result : vector<int>();
    }
};
