class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        sort(words.begin(), words.end(), [](auto &w1, auto &w2) -> bool {
            return w1.size() < w2.size();
        }); 

        auto is_substring = [](string_view s, string_view p) {
            vector<int> lps(p.size());
            for(int i{1}, j{}; i < p.size(); i++) {
                while(j && p[i] != p[j]) {
                    j = lps[j-1];
                }
                if(p[i] == p[j]) {
                    ++j;
                }
                lps[i] = j;
            };

            for(int i{}, j{}; i < s.size(); ++i) {
                while(j && s[i] != p[j]) {
                    j = lps[j-1];
                }
                if(s[i] == p[j]) ++j;
                if(j == p.size()) return true;
            }
            return false;
        };

        unordered_set<string> result;
        for(int i{}; i < words.size(); ++i) {
            for(int j{}; j < i; ++j) {
                if(is_substring(words[i], words[j])) {
                    result.emplace(words[j]);
                }
            }
        }
        return vector<string>(result.begin(), result.end());

    }
};
