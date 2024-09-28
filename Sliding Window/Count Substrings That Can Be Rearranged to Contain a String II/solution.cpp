class Solution {
public:
    long long validSubstringCount(string word1, string word2) {
        vector<int> counter(26, 0);
        for(auto c: word2) {
            counter[c - 'a'] += 1;
        }
        auto is_valid = [&]() -> bool {
            for(auto v: counter) {
                if(v > 0) return false;
            }
            return true;
        };
        int i = 0;
        long long result = 0;
        for(auto c: word1) {
            counter[c - 'a'] -= 1;
            while(is_valid()) {
                counter[word1[i++] - 'a'] += 1;
            }
            result += i;
        }
        return result;
    }
};
