class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unordered_set<char> s(allowed.begin(), allowed.end());
        int result = 0;
        for(auto w: words) {
            bool valid = true;
            for(char c: w) {
                if(s.find(c) == s.end()) {
                    valid = false;
                    break;
                }
            }
            result += valid;
        }
        return result;
    }
};
