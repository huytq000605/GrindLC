class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int close = 0;
        for(char c: s) {
            if(c == ')') close += 1;
        }
        int open = 0;
        string result;
        for(char c: s) {
            if(c == '(') {
                if(open + 1 > close) continue;
                open += 1;
            } else if(c == ')') {
                close -= 1;
                if(!open) continue;
                open -= 1;
            }
            result.push_back(c);
        }
        return result;
    }
};
