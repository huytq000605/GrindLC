class Solution {
public:
    int longestSubsequence(string s, int k) {
        long long num = 0, p = 1;
        int result = 0;
        for(int i = s.size()-1; i >= 0; --i) {
            if(s[i] == '0') ++result;
            else if(s[i] == '1' && num + p <= k) {
                num += p;
                ++result;
            }
            if(p <= k) p <<= 1;
        }
        return result;
    }
};
