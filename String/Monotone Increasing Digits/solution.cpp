class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        string s = to_string(n);
        int i = 0;
        for(i; i < s.size() - 1; i++) {
            if(s[i] > s[i+1]) break;
        }
        if(i == s.size() - 1) return n;
        while(i > 0 && s[i] == s[i-1]) i--;
        return stoi(s.substr(0, i) + to_string(s[i] - '1') + string(s.size() - i - 1, '9'));
    }
};
