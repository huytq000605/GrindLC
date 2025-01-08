class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
        int result{};
        auto is_prefix_suffix = [](string_view w1, string_view w2) {
            if(w1.size() > w2.size()) return false;
            for(int i{}; i < w1.size(); ++i) {
                if(w1[i] != w2[i]) return false;
                if(w1[w1.size()-1-i] != w2[w2.size()-1-i]) return false;
            }
            return true;
        };
        int n = words.size();
        for(int i{}; i < n; ++i) {
            for(int j{i+1}; j < n; ++j) {
                result += is_prefix_suffix(words[i], words[j]);
            }
        }
        return result;
    }
};
