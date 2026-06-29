class Solution {
public:
    bool kmp(string& s, string& p) {
        vector<int> lps(p.size());
        for(int i = 1, j = 0; i < p.size(); ++i) {
            while(j && p[i] != p[j]) {
                j = lps[j-1];
            }
            if(p[i] == p[j]) ++j;
            lps[i] = j;
        }

        for(int i = 0, j = 0; i < s.size(); ++i) {
            while(j && s[i] != p[j]) {
                j = lps[j-1];
            }
            if(s[i] == p[j]) ++j;
            if(j == p.size()) return true;
        }
        return false;
    }
    int numOfStrings(vector<string>& patterns, string word) {
        int result = 0;
        for(auto& p: patterns) {
            result += kmp(word, p);
        }
        return result;
    }
};
