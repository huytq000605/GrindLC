class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int result{};
        for(auto &word: words) {
            if(word.size() < pref.size()) continue;
            bool is_prefix{true};
            for(int i{}; i < pref.size(); ++i) if(word[i] != pref[i]) {
                is_prefix = false;
                break;
            }
            if(is_prefix) ++result;
        }
        return result;
    }
};
