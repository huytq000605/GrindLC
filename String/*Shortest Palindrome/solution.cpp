class Solution {
public:
    string shortestPalindrome(string s) {
        // find longest palindrome starts from 0
        // use kmp with s + # + rev_s to find longest rev_s matches with s
        // => longest palindrome from start = kmp[rev_s[-1]]
        string rs(s.rbegin(), s.rend());
        string merged = s + "#" + rs;
        vector<int> kmp(merged.size(), 0);
        int j = 0;
        for(int i = 1; i < merged.size(); ++i) {
            while(j && merged[i] != merged[j]) {
                j = kmp[j-1];
            }
            if(merged[i] == merged[j]) ++j;
            kmp[i] = j;
        }
        return rs.substr(0, s.size() - kmp[merged.size() - 1]) + s;
    }
};
