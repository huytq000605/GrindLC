class Solution {
public:
    string findValidPair(string s) {
        vector<int> counter(10);
        for(char c: s) {
            counter[c - '0']++;
        }
        for(int i{}; i < s.size()-1; ++i) {
            if(s[i] != s[i+1] && counter[s[i]-'0'] == s[i]-'0' && counter[s[i+1]-'0'] == s[i+1]-'0')
                return s.substr(i, 2);
        }
        return "";
    }
};
