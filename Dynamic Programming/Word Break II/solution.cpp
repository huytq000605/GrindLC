class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<string> result;
        unordered_set<string> words(wordDict.begin(), wordDict.end());
        unordered_map<int, vector<string>> dp;
        auto dfs = [&](int i, auto& dfs_ref) -> vector<string> {
            if(dp.find(i) != dp.end()) { return dp[i]; }
            if(i >= s.size()) return {""};
            int start_i = i;
            string cur;
            vector<string> result;
            while(i < s.size()) {
                cur += s[i];
                if(words.find(cur) != words.end()) {
                    auto suffixes = dfs_ref(i+1, dfs_ref);
                    for(auto suffix: suffixes) {
                        result.emplace_back(cur + (suffix != "" ? " ": "") + suffix);
                    }
                }
                i++;
            }
            dp[start_i] = result;
            return result;
        };
        

        return dfs(0, dfs);
    };
};
