class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        for(int i{}, j{}; i < str1.size(); ++i) {
            if(str1[i] == str2[j] || str1[i] + 1 == str2[j] || (str1[i] == 'z' && str2[j] == 'a')) ++j;
            if(j == str2.size()) return true;
        }
        return false;
    }
};
