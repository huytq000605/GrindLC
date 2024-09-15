class Solution {
    static constexpr array<char, 5> vowels = {'a', 'e', 'i', 'o', 'u'};
public:
    int findTheLongestSubstring(string s) {
        int result = 0;
        int mask = 0;
        map<int, int> seen;
        seen[0] = -1;
        for(int i = 0; i < s.size(); ++i) {
            for(int j = 0; j < vowels.size(); ++j) {
                if(s[i] == vowels[j]) {
                    mask ^= (1 << j);
                    break;
                }
            }
            if(seen.find(mask) == seen.end()) seen[mask] = i;
            result = max(result, i - seen[mask]);
        }
        return result;
    }
};
