class Solution {
public:
    bool checkStrings(string s1, string s2) {
        int n = s1.size();
        string s1e, s1o, s2e, s2o;
        for(int i = 0; i < n; ++i) {
            if(i & 1) {
                s1o += s1[i];
                s2o += s2[i];
            } else {
                s1e += s1[i];
                s2e += s2[i];
            }
        }
        for(auto* s: {&s1e, &s1o, &s2e, &s2o}) sort(s->begin(), s->end());
        for(int i = 0; i < s1e.size(); ++i) if(s1e[i] != s2e[i]) return false;
        for(int i = 0; i < s1o.size(); ++i) if(s1o[i] != s2o[i]) return false;
        return true;
    }
};
