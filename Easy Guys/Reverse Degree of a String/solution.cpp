class Solution {
public:
    int reverseDegree(string s) {
        int result = 0;
        for(int i = 0; i < s.size(); ++i) {
            result += (i+1) * (26 - (s[i] - 'a'));
        }
        return result;
    }
};
