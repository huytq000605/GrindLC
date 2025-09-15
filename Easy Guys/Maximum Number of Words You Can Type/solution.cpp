class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        bool can = true;
        int result = 0;
        vector<int> broken(26);
        for(char c: brokenLetters) {
            broken[c-'a'] = 1;
        }
        for(char c: text) {
            if(c == ' ') {
                result += can;
                can = true;
            } else {
                if(broken[c - 'a']) can = false;
            }
        }
        result += can;
        return result;
    }
};
