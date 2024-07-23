class Solution {
public:
    int maxOperations(string s) {
        int prefix = 0;
        int n = s.size();
        int result = 0;
        for(int i = 0; i < n-1; i++) {
            if(s[i] == '1') prefix += 1;
            if(s[i] == '1' && s[i+1] == '0') {
                result += prefix;
            }
        }
        return result;
    }
};
