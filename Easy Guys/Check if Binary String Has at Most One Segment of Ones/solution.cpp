class Solution {
public:
    bool checkOnesSegment(string s) {
        bool have_zero = false;
        for(char c: s) {
            if(c == '0') have_zero = true;
            else if(have_zero) return false;
        }
        return true;
    }
};
