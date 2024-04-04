class Solution {
public:
    int maxDepth(string s) {
        int stack = 0;
        int result = 0;
        for(char c: s) {
            if(c == '(') stack += 1;
            else if(c == ')') stack -= 1;
            result = max(result, stack);
        }
        return result;
    }
};
