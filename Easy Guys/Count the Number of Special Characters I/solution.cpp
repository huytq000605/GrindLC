class Solution {
public:
    int numberOfSpecialChars(string word) {
        vector<bool> lower(26), upper(26);
        int result = 0;
        for(int c: word) {
            int i = c - 'A';
            if(0 <= i && i < 26) {
                if(lower[i] && !upper[i]) ++result;
                upper[i] = true;
            } else {
                i = c - 'a';
                if(upper[i] && !lower[i]) ++result;
                lower[i] = true;
            }
        }
        return result;
    }
};
