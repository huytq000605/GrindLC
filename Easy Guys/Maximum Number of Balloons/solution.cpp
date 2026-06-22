class Solution {
public:
    int maxNumberOfBalloons(string text) {
        vector<int> counter(26);
        for(char c: text) {
            counter[c - 'a']++;
        }
        int result = INT_MAX;
        for(auto [c, f]: vector<pair<char, int>>{{'b', 1}, {'a', 1}, {'l', 2}, {'o', 2}, {'n', 1}}) {
            result = min(result, counter[c - 'a'] / f);
        }
        return result;
    }
};
