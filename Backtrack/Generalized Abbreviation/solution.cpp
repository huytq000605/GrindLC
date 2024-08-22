class Solution {
vector<string> result;
    void backtrack(string & word, int i, int abbr_count, string cur) {
        if(i >= word.size()) {
            result.emplace_back(cur + (abbr_count ? to_string(abbr_count): ""));
            return;
        }
        backtrack(word, i+1, abbr_count + 1, cur);
        if(abbr_count) backtrack(word, i+1, 0, cur + to_string(abbr_count) + word[i]);
        else backtrack(word, i+1, 0, cur + word[i]);
    };
public:
    vector<string> generateAbbreviations(string word) {
        backtrack(word, 0, 0, "");
        return result;
    }
};
