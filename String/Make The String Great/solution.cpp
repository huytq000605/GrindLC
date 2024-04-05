class Solution {
public:
    string makeGood(string s) {
        stack<char> result;
        for(char c: s) {
            if(result.size() > 0 &&
                tolower(result.top()) == tolower(c) &&
                result.top() != c
            ) {
                result.pop();
                continue;
            }
            result.push(c);
        }
        string ret;
        while(result.size() > 0) {
            ret.push_back(result.top());
            result.pop();
        }
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
