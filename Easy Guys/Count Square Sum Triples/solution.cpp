class Solution {
public:
    int countTriples(int n) {
        int result = 0;
        for(int c = 1; c <= n; ++c) {
            for(int a = 1, b = floor(c); a < b;) {
                if(a*a+ b*b == c*c) {
                    result += 2;
                    ++a;
                }
                else if(a*a + b*b < c*c) ++a;
                else --b;
            }
        }
        return result;
    }
};
