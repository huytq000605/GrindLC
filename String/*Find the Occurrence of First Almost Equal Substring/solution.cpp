class Solution {
public:
    int minStartingIndex(string s, string p) {
        auto z = [](string s) -> vector<int> {
            vector<int> z(s.size(), 0);
            int l = 0, r = 0;
            for(int i = 1; i < s.size(); ++i) {
                if(i < r) {
                    z[i] = min(z[i-l], r-i);
                } 
                while(s[z[i]] == s[i + z[i]]) {
                    ++z[i];
                }
                if(i + z[i] > r) {
                    l = i;
                    r = i + z[i];
                }
            }
            return z;
        };
        
        int m = s.size(), n = p.size();
        int skip = 1;
        auto matched = z(p + s);
        auto rmatched = z(string(p.rbegin(), p.rend()) + string(s.rbegin(), s.rend()));
        reverse(rmatched.begin(), rmatched.end());
        // for each substring length = n
        // check longest prefix and suffix, if prefix + suffix + skip >= m then it's matched
        // we cannot use KMP because from prefix, we couldn't know where to match suffix
        // even when we found prefix, suffix, there's no efficient way to tell where
        // does the substring start
        // for example: 
        // 1. s = "efeff", p = "fe", ans = 1
        // 2. s = "ffggf", p = "gg", ans = 1
        for(int i = 0; i < m-n+1; ++i) {
            int prefix = matched[n+i]; // + n due to first n are p
            int suffix = rmatched[i+n-1]; // last idx of substr starts at i is i+n-1
            if(prefix + 1 + suffix >= p.size()) return i;
        }
        return -1;
    }
};
