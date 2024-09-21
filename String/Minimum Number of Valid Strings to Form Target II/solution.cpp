class Solution {
public:
    int minValidStrings(vector<string>& words, string target) {
        vector<vector<int>> kmps;
        for(auto &word: words) {
            kmps.emplace_back(kmp(word + "#" + target));
        }

        int l = target.size();
        int result = 0;
        while(l) {
            int match = 0;
            for(int i = 0; i < words.size(); ++i) {
                match = max(match, kmps[i][words[i].size() + l]);
            }
            if(match == 0) return -1;
            ++result;
            l -= match;
        }
        return result;
    }

    vector<int> kmp(string s) {
        vector<int> result(s.size(), 0);
        for(int i = 1; i < s.size(); ++i) {
            int j = result[i-1];
            while(j && s[i] != s[j]) j = result[j-1];
            if(s[i] == s[j]) ++j;
            result[i] = j;
        }
        return result;
    }
};
