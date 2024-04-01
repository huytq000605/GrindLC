class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1;
        int result = 0;
        while(s[i] == ' ') i--;
        while(i >= 0 && s[i--] != ' ') result += 1;
        return result;
    }
};
