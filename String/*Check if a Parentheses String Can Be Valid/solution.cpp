class Solution {
public:
    bool canBeValid(string s, string locked) {
        if(s.size() % 2 == 1) return false;
        int minDiff = 0, maxDiff = 0;
        for(int i = 0; i < s.size(); i++) {
            if(locked[i] == '0') {
                minDiff -= 1;
                maxDiff += 1;
            } else {
                if(s[i] == '(') {
                minDiff += 1;
                maxDiff += 1;
                } else {
                    minDiff -= 1;
                    maxDiff -= 1;
                }
            }
            if(maxDiff < 0) return false;
            minDiff = max(minDiff,  0);
        }
        return minDiff == 0;
    }
};
