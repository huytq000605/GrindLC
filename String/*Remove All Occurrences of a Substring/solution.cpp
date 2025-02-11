class Solution {
public:
    string removeOccurrences(string s, string p) {
        vector<int> lps(p.size());
        for(int i{1}, j{}; i < p.size(); ++i) {
            while(j && p[j] != p[i]) {
                j = lps[j-1];
            }
            if(p[i] == p[j]) ++j;
            lps[i] = j;
        }

        vector<int> lps2(s.size());
        string result;
        for(int i{}, j{}; i < s.size(); ++i) {
            result.push_back(s[i]);
            while(j && s[i] != p[j]) j = lps[j-1];
            if(s[i] == p[j]) ++j;
            if(j == p.size()) {
                int k = p.size();
                while(k--) result.pop_back();
                j = result.empty() ? 0: lps2[result.size()-1];
            } else {
                lps2[result.size()-1] = j;
            }
        }
        return result;
    }
};
