class Solution {
public:
    int numSub(string s) {
        int result = 0, cur = 0, MOD = 1e9 + 7;
        for(char c: s) {
            if(c == '1') {
                ++cur;
                result = (result + cur) % MOD;
            } else cur = 0;
        }
        return result;
    }
};
