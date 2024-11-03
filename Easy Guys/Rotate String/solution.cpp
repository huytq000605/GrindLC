class Solution {
public:
    bool rotateString(string s, string goal) {
        int n = s.size();
        if(n != goal.size()) return false;
        for(size_t i{0}; i < n; ++i) {
            bool valid = true;
            for(size_t j{0}; j < n; ++j) {
                if(s[j] != goal[(i+j)%n]) {
                    valid = false;
                    break;
                };
            }
            if(valid) return true;
        }
        return false;
    }
};
