class Solution {
public:
    bool canPermutePalindrome(string s) {
        vector<int> can(26);
        for(char c: s) {
            can[c - 'a'] ^= 1;
        }
        return accumulate(can.begin(), can.end(), 0) <= 1;  
    }
};
