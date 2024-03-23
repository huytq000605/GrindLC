class Solution {
public:
    long long countSubstrings(string s, char c) {
        long long result = 0;
        long long existing = 0;
        for(auto &cc: s) {
            if(cc == c) {
                result += existing;
                existing += 1;
                result += 1;
            }
        }
        return result;
    }
};
