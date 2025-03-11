class Solution {
public:
    bool hasSameDigits(string s) {
        while(s.size() > 2) {
            string ns{};
            for(int i{}; i < s.size() - 1; ++i) {
                int nd = (s[i]-'0' + s[i+1]-'0') % 10;
                ns += nd + '0';
            }
            s = ns;
        }
        
        return s[0] == s[1];
    }
};
