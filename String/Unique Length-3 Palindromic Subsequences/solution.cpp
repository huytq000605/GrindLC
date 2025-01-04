class Solution {
public:
    int countPalindromicSubsequence(string s) {
        vector<int> left(26), right(26);
        for(char c: s) {
            right[c - 'a']++;
        }
        int result{};
        vector<vector<int>> counter(26, vector<int>(26));
        for(char c: s) {
            right[c - 'a']--;
            for(char ch{}; ch < 26; ++ch) {
                if(left[ch] && right[ch]) {
                    result += counter[c-'a'][ch] == 0;
                    counter[c-'a'][ch] = 1;
                };
            }
            left[c - 'a']++;
        }
        return result;
    }
};
