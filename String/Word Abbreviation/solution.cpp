class Solution {
public:
    vector<string> wordsAbbreviation(vector<string>& words) {
        unordered_map<string, vector<int>> m;
        vector<string> result(words.size());
        for(int i = 0; i < words.size(); ++i) {
            if(words[i].size() <= 3) {
                result[i] = words[i];
                continue;
            }
            string s = words[i][0] + to_string(words[i].size()-2) + words[i].back();
            result[i] = s;
            m[s].push_back(i);
        }
        auto diff = [](string& s1, string& s2) -> int {
            for(int i = 0; i < s1.size(); ++i) {
                if(s1[i] != s2[i]) return i;
            }
            return static_cast<int>(s1.size());
        };
        for(auto &[abb, idxs]: m) {
            if(idxs.size() == 1) continue;
            vector<int> dp(idxs.size());
            for(int i = 0; i < idxs.size(); ++i) {
                for(int j = i+1; j < idxs.size(); ++j) {
                    int d = diff(words[idxs[i]], words[idxs[j]]);
                    dp[i] = max(dp[i], d);
                    dp[j] = max(dp[j], d);
                }
                int idx = idxs[i];
                int n = words[idx].size();
                if(dp[i] < n-3) {
                    result[idx] = words[idx].substr(0, dp[i]+1) + to_string(n-2-dp[i]) + words[idx].back();
                } else {
                    result[idx] = words[idx];
                }
            }
        }
        return result;
    }
};
