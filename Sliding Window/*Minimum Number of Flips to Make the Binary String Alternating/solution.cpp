class Solution {
public:
    int minFlips(string s) {
        int n = s.size();
        int res1 = 0, res2 = 0, result = INT_MAX;
        for(int i = 0; i < n*2; ++i) {
            if(i < n) s[i] -= '0';
            if((i&1) != s[i%n]) ++res1;
            if((i&1) == s[i%n]) ++res2;
            if(i >= n) {
                if(((i-n)&1) != s[i-n]) --res1;
                if(((i-n)&1) == s[i-n]) --res2;
            }
            if(i >= n-1) result = min(result, min(res1, res2));
        }
        return result;
    }
};
