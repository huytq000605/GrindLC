class Solution {
public:
    int maxScore(string s) {
        int ones = count(s.begin(), s.end(), '1');
        int zeros{};
        int result{};
        for(int i{}; i < s.size() - 1; ++i) {
            if(s[i] == '0') ++zeros;
            else --ones;
            result = max(result, zeros + ones); 
        }
        return result;
    }
};
