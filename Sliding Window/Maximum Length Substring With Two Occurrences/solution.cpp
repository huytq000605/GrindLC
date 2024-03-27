class Solution {
public:
    int maximumLengthSubstring(string s) {
        int counter[26] = {};
        int start = 0;
        int result = 0;
        for(int i = 0; i < s.size(); i++) {
            counter[s[i] - 'a'] += 1;
            while(counter[s[i] - 'a'] > 2) {
                counter[s[start] - 'a'] -= 1;
                start += 1;
            }
            result = std::max(result, i - start + 1);
        }
        return result;
    }
};
