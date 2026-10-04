class Solution {
public:
    bool checkValidString(string s) {
        int max_diff = 0, min_diff = 0;
        for(char & c: s) {
            if(c == '(') {
                max_diff += 1;
                min_diff += 1;
            } else if(c == ')') {
                max_diff -= 1;
                min_diff -= 1;
            } else {
                min_diff -= 1;
                max_diff += 1;
            }
            if(max_diff < 0) return false;
            min_diff = max(min_diff, 0);
        }
        return min_diff == 0;
    }
};
