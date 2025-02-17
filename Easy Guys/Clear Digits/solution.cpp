class Solution {
public:
    string clearDigits(string s) {
        string result;
        for(int i{}; i < s.size(); ++i) {
            if(isdigit(s[i])) {
                if(!result.empty()) result.pop_back();
            } else {
                result += s[i];
            }
        }
        return result;
    }
};
