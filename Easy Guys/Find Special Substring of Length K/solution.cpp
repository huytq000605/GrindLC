class Solution {
public:
    bool hasSpecialSubstring(string s, int k) {
        char cur = ' ';
        int count = 0;
        for(char c: s) {
            if(c == cur) {
                ++count;
            } else {
                if(count == k) return true;
                cur = c;
                count = 1;
            }
        }
        return count == k;
    }
};
