class Solution {
public:
    int numSteps(string s) {
        int result = 0, carry = 0;
        for(int i = s.size() - 1; i > 0; --i) {
            int v = s[i] - '0' + carry;
            if(v == 1) carry = 1;
            result += v == 1 ? 2: 1;
        }
        return result + carry;
    }
};
