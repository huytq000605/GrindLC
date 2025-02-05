class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        vector<int> diffs;
        for(int i{}; i < s1.size(); ++i) {
            if(s1[i] != s2[i]) {
                diffs.emplace_back(i);
                if(diffs.size() > 2) return false;
            }
        }

        if(diffs.empty()) return true;
        if(diffs.size() == 1) return false;
        int i1 = diffs[0], i2 = diffs[1];
        return s1[i1] == s2[i2] && s1[i2] == s2[i1];
    }
};
