class Solution {
public:
    int takeCharacters(string s, int k) {
        int n = s.size();
        int result{n};
        unordered_map<char, int> counter{};
        for(char c: s) ++counter[c];
        if(counter['a'] < k || counter['b'] < k || counter['c'] < k) return -1;
        for(int i{}, j{}; i < n; ++i) {
            --counter[s[i]];
            while(counter[s[i]] < k) {
                ++counter[s[j++]];
            }
            result = min(result, n - (i-j+1));
        }
        return result;
    }
};
