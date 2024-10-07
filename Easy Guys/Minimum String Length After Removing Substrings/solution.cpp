class Solution {
public:
    int minLength(string s) {
        stack<char> result;
        for(char c: s) {
            if(c == 'B' && result.size() && result.top() == 'A') result.pop();
            else if(c == 'D' && result.size() && result.top() == 'C') result.pop();
            else result.emplace(c);
        }
        return result.size();
    }
};
