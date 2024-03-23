class Solution {
public:
    bool isSubstringPresent(string s) {
        std::unordered_set<string> set;
        for(int i = 0; i < s.size() - 1; i++) {
            set.emplace(s.substr(i, 2));
        }
        for(int i = s.size() - 1; i > 0; i--) {
            string ss = s.substr(i-1, 2);
            std::reverse(ss.begin(), ss.end());
            if(set.find(ss) != set.end()) {
                return true;
            }
        }
        return false;
    }
};
