class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        int n = words.size();
        vector<int> prefix(n);
        auto is_vowel = [](char c) -> bool {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        for(int i{}; i < n; ++i) {
            if(i) prefix[i] = prefix[i-1];
            prefix[i] += is_vowel(words[i].front()) && is_vowel(words[i].back());
        }
        vector<int> result{};
        for(auto &q: queries) {
            result.emplace_back(prefix[q[1]] - (q[0] ? prefix[q[0] - 1]: 0));
        }
        return result;
    }
};
