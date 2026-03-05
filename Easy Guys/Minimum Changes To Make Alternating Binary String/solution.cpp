class Solution {
public:
    int minOperations(string s) {
        int r1 = 0, r2 = 0;
        for(int i = 0; i < s.size(); ++i) {
            if(i & 1) {
                r1 += s[i] == '0';
                r2 += s[i] == '1';
            } else {
                r1 += s[i] == '1';
                r2 += s[i] == '0';
            }
        }
        return min(r1, r2);
    }
};
