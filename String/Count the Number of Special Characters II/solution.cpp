class Solution {
public:
    int numberOfSpecialChars(string word) {
        vector<int> l(26, INT_MAX), u(26, -1);
        for(int i = 0; i < word.size(); ++i) {
            char c = word[i];
            if(isupper(c)) {
                if(u[c-'A'] == -1) u[c-'A'] = i;
            } else {
                l[c-'a'] = i;
            }
        }
        int result = 0;
        for(int i = 0; i < 26; ++i) {
            result += l[i] < u[i];
        }
        return result;
    }
};
