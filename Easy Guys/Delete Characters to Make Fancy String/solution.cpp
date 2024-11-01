class Solution {
public:
    string makeFancyString(string s) {
        int j = min(static_cast<int>(s.size()), 2);
        for(int i = 2; i < s.size(); ++i) {
            if(s[j-2] == s[j-1] && s[j-1] == s[i]) {
                continue;
            }
            swap(s[j++], s[i]);
        }
        s.resize(j);
        return s;
    }
};
