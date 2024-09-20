class Solution {
public:
    int countKConstraintSubstrings(string s, int k) {
        int result = (s.size() + 1) * s.size() / 2;
        for(int i = 0, j = 0, ones = 0, zeros = 0; i < s.size(); i++) {
            ones += s[i] == '1';
            zeros += s[i] == '0';
            while(ones - (s[j] == '1') > k && zeros - (s[j] == '0') > k) {
                ones -= s[j] == '1';
                zeros -= s[j] == '0';
                j++;
            }
            if(ones > k && zeros > k) result -= j+1;
        }
        return result;
    }
};
