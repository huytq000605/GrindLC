class Solution {
public:
    int numberOfSubstrings(string s) {
        // a = number of ones
        // b = number of zeros
        // a + b = n
        // b * b <= a <= n 
        // b <= sqrt(n)
        int sq = sqrt(s.size());
        int result = 0;
        for(int b = 0; b <= sq; b++) {
            int i = 0, j = 0;
            int zeros = 0;
            int ones_i = 0, ones_j = 0;
            for(int idx = 0; idx < s.size(); idx++) {
                char c = s[idx];
                if(c == '0') zeros++;
                else {
                    ones_i++;
                    ones_j++;
                }
                while(zeros > b) {
                    if(s[i] == '0') zeros--;
                    else ones_i--;
                    i++;
                }
                while(j < i || 
                (zeros == b && 
                j + 1 <= idx && // Guarantee in case when b = 0, j can make ones_j to become 0
                s[j] == '1' && ones_j > zeros * zeros)) {
                    if(s[j] == '1') ones_j--;
                    j++;
                }
                
                if(zeros == b && i <= idx && ones_j >= zeros * zeros) {
                    result += j - i + 1;
                }
            }
        }
        return result;
    }
};
