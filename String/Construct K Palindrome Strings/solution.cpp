class Solution {
public:
    bool canConstruct(string s, int k) {
        if(k > s.size()) return false;
        vector<int> counter(26);
        for(char c: s) counter[c-'a']++;
        for(int i{}, mn{}; i < 26; ++i) {
            mn += counter[i] & 1;
            if(k < mn) return false;
        }
        return true;
    }
};
