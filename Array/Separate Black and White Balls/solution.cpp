class Solution {
public:
    long long minimumSteps(string s) {
        int i = 0, j = s.size() - 1;
        long long result = 0;
        while(i < j) {
            while(i < s.size() && s[i] == '0') ++i;
            while(j >= 0 && s[j] == '1') --j;
            if(i < j) result += (j--) - (i++);
        }
        return result;
    }
};
